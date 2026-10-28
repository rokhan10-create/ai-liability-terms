"""Replace a grouped log row (several firms on one line) with individual firm rows.

Usage: python split_grouped.py <naics4> "<grouped rank as logged>" new_rows.json
Every replacement is recorded in rank-changes.csv.
"""
import csv, datetime, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'screening-log.csv')
CHANGES = os.path.join(HERE, 'rank-changes.csv')
naics, grouped_rank, path = sys.argv[1:4]

rows = list(csv.DictReader(open(LOG, encoding='utf8')))
cols = list(rows[0].keys())
hits = [r for r in rows if r['naics4'] == naics and r['rank'] == grouped_rank]
if len(hits) != 1:
    sys.exit(f'expected 1 grouped row, found {len(hits)}')
old = hits[0]
new = json.load(open(path, encoding='utf8'))
for r in new:
    r['candidate_id'] = old['candidate_id']
    r['naics4'] = naics
rows = [r for r in rows if r is not old] + [{c: r.get(c, '') for c in cols} for r in new]
w = csv.DictWriter(open(LOG, 'w', newline='', encoding='utf8'), fieldnames=cols)
w.writeheader()
w.writerows(rows)
with open(CHANGES, 'a', newline='', encoding='utf8') as f:
    csv.writer(f).writerow([datetime.date.today().isoformat(), naics, old['firm'], grouped_rank,
                            '; '.join(f"{r['rank']}:{r['firm']}" for r in new), 'grouped row split into individual firms'])
print(f'replaced grouped row {grouped_rank} with {len(new)} rows')
