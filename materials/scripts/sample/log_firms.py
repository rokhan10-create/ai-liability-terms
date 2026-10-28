"""Append screened firms to screening-log.csv.

Usage: python log_firms.py batch.json
batch.json = list of objects keyed by the screening-log columns (missing keys are left blank).
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'screening-log.csv')
TEMPLATE = os.path.join(HERE, 'screening-log-TEMPLATE.csv')

cols = next(csv.reader(open(TEMPLATE, encoding='utf8')))
rows = json.load(open(sys.argv[1], encoding='utf8'))
# candidate_id is always derived from naics4 (a hand-typed ID once misfiled three industries).
CAND = os.path.join(HERE, 'candidate-industries.csv')
code2id = {r['naics4']: r['candidate_id'] for r in csv.DictReader(open(CAND, encoding='utf8'))}
for r in rows:
    if r.get('naics4') not in code2id:
        sys.exit(f"unknown naics4 {r.get('naics4')!r} for {r.get('firm')}")
    r['candidate_id'] = code2id[r['naics4']]
new = not os.path.exists(LOG)
with open(LOG, 'a', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=cols)
    if new:
        w.writeheader()
    for r in rows:
        unknown = set(r) - set(cols)
        if unknown:
            sys.exit(f'unknown columns: {unknown}')
        w.writerow(r)
print(f'logged {len(rows)} rows -> {LOG}')
