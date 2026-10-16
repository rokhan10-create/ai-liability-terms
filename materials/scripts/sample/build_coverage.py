"""Rebuild coverage-table.csv (one row per eligible industry) from candidate-industries.csv.

Run build_sample.py first: it writes the per-industry k/n results this script reads.
Original-set columns (firms from the 59-firm coded corpus) are static and are carried
over from the existing coverage-table.csv.

companies = slot depth under protocol v3 (10 in the top-20 industries, else 5)
checked   = eligible firms identified and screened (< companies when fewer firms of scale exist)
pct_ai    = ai / checked, NA when nothing was checked
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.join(HERE, 'candidate-industries.csv')
RANKING = os.path.join(HERE, 'industry-household-revenue-ranking.csv')
OUT = os.path.join(HERE, 'coverage-table.csv')

old = {r['naics4']: r for r in csv.DictReader(open(OUT, encoding='utf8'))}
rank = {r['naics4']: r for r in csv.DictReader(open(RANKING, encoding='utf8'))}
cand = [r for r in csv.DictReader(open(CAND, encoding='utf8')) if r['screen_result'] != 'excluded-scope']

rows = []
for c in cand:
    code = c['naics4']
    rk = rank.get(code, {}).get('rank', '')
    main = rk != '' and int(rk) <= 20
    m = re.match(r'(\d+)/(\d+)(?: \(\+(\d+) unclear\))?', c['screen_result'])
    if m:
        ai, checked, unclear = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
        pct = str(round(100 * ai / checked)) if checked else 'NA'
    else:  # industry whose firms were all skipped (no consumer-facing firm of scale)
        ai, checked, unclear, pct = 0, 0, 0, 'NA'
    o = old.get(code, {})
    rows.append({
        'hh_rank': rk or 'NA', 'naics4': code, 'industry': c['naics4_title'],
        'group': 'main' if main else 'supplementary',
        'companies': 10 if main else 5, 'checked': checked, 'ai': ai, 'unclear': unclear,
        'pct_ai': pct, 'original_us': o.get('original_us', '0'),
        'original_firms': o.get('original_firms', ''), 'original_nonus': o.get('original_nonus', ''),
    })

rows.sort(key=lambda r: int(r['hh_rank']) if r['hh_rank'] != 'NA' else 999)
with open(OUT, 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f'{len(rows)} industries -> {OUT}')
