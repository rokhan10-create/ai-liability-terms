"""Derive the sample from screening-log.csv under protocol v2 (top 5 eligible firms per industry).

Writes:
  sample.csv          - top-5 firms with consumer_ai=yes and by_cutoff=yes (main sample)
  sample-unclear.csv  - top-5 firms with consumer_ai=unclear (robustness set)
  and updates candidate-industries.csv with k/5 adoption per industry.
Prints industries whose top-5 roster is incomplete or covered by grouped rows.
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'screening-log.csv')
CAND = os.path.join(HERE, 'candidate-industries.csv')

# Firms that cannot be deployers do not occupy a top-5 slot (protocol v2 §2).
SKIP = ('model-developer', 'no-consumer-channel', 'nonprofit-public', 'non-us',
        'other: no consumer-facing channel')


def is_skip(r):
    reason = r['exclusion_reason'].strip().lower()
    return r['decision'] == 'skip' or any(reason.startswith(s) for s in SKIP)


def rank_key(r):
    m = re.match(r'\d+', r['rank'])
    return int(m.group()) if m else 999


rows = list(csv.DictReader(open(LOG, encoding='utf8')))
# Key on the NAICS code, not the logged ID, so a mistyped candidate_id cannot misfile a firm.
code2id = {r['naics4']: r['candidate_id'] for r in csv.DictReader(open(CAND, encoding='utf8'))}
# Main sample (protocol v3): top 20 industries by household spending.
RANKING = os.path.join(HERE, 'industry-household-revenue-ranking.csv')
MAIN = {code2id[r['naics4']] for r in csv.DictReader(open(RANKING, encoding='utf8')) if int(r['rank']) <= 20}
cols = list(rows[0].keys())
by_ind = {}
for r in rows:
    by_ind.setdefault(code2id[r['naics4']], []).append(r)

sample, unclear, summary, problems = [], [], {}, []
for cid, rs in by_ind.items():
    eligible = [r for r in sorted(rs, key=rank_key) if not is_skip(r)]
    depth = 10 if cid in MAIN else 5          # protocol v3: top 10 in main-sample industries
    top5 = eligible[:depth]
    grouped = [r['firm'] for r in top5 if not re.fullmatch(r'\d+', r['rank'])]
    if len(top5) < depth:
        problems.append(f'{cid}: only {len(top5)} eligible firms logged')
    if grouped:
        problems.append(f'{cid}: grouped row inside top 5 -> {grouped}')
    k = 0
    for r in top5:
        if r['consumer_ai'] == 'yes' and r['by_cutoff'] == 'yes':
            sample.append(r)
            k += 1
        elif r['consumer_ai'] == 'unclear':
            unclear.append(r)
    summary[cid] = (len(top5), k, sum(r['consumer_ai'] == 'unclear' for r in top5))

main_sample = [r for r in sample if code2id[r['naics4']] in MAIN]
supp_sample = [r for r in sample if code2id[r['naics4']] not in MAIN]
for name, data in (('sample.csv', main_sample), ('sample-supplementary.csv', supp_sample), ('sample-unclear.csv', unclear)):
    with open(os.path.join(HERE, name), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(data)

cand = list(csv.reader(open(CAND, encoding='utf8')))
h = cand[0]
for row in cand[1:]:
    if row[0] in summary and row[h.index('screen_result')] != 'excluded-scope':
        n, k, u = summary[row[0]]
        row[h.index('firms_checked')] = str(n)
        row[h.index('firms_consumer_ai')] = str(k)
        row[h.index('screen_result')] = f'{k}/{n}' + (f' (+{u} unclear)' if u else '')
csv.writer(open(CAND, 'w', newline='', encoding='utf8')).writerows(cand)

print(f'main sample: {len(main_sample)} firms | supplementary: {len(supp_sample)} | unclear: {len(unclear)} | industries screened: {len(summary)}')
for cid, (n, k, u) in sorted(summary.items()):
    print(f'  {cid}: {k}/{n}' + (f' (+{u} unclear)' if u else ''))
for p in problems:
    print('  PROBLEM', p)
