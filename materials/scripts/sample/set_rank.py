"""Correct a logged firm's rank (roster corrections only; every change is appended to rank-changes.csv).

Usage: python set_rank.py <naics4> "<firm name as logged>" <new_rank> "<reason>"
"""
import csv, datetime, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'screening-log.csv')
CHANGES = os.path.join(HERE, 'rank-changes.csv')

naics, firm, new_rank, reason = sys.argv[1:5]
rows = list(csv.DictReader(open(LOG, encoding='utf8')))
cols = list(rows[0].keys())
hits = [r for r in rows if r['naics4'] == naics and r['firm'] == firm]
if len(hits) != 1:
    sys.exit(f'expected 1 match, found {len(hits)}')
old = hits[0]['rank']
hits[0]['rank'] = new_rank
w = csv.DictWriter(open(LOG, 'w', newline='', encoding='utf8'), fieldnames=cols)
w.writeheader()
w.writerows(rows)
new = not os.path.exists(CHANGES)
with open(CHANGES, 'a', newline='', encoding='utf8') as f:
    cw = csv.writer(f)
    if new:
        cw.writerow(['date', 'naics4', 'firm', 'old_rank', 'new_rank', 'reason'])
    cw.writerow([datetime.date.today().isoformat(), naics, firm, old, new_rank, reason])
print(f'{firm}: {old} -> {new_rank}')
