"""Map the 59-firm pilot corpus (documents.csv) onto the v2 industry roster.

Writes recollection/pilot-corpus-crosswalk.csv (one row per pilot firm) and appends four
v2 columns to documents.csv: naics4_v2, industry_v2, sample_group_v2, status_v2.
Run from the project root. Re-running is safe (columns are overwritten, not duplicated).

status_v2 values
  carry-over                firm is on the v2 roster and passed the screen; keep docs, re-verify hash
  merged-into-roster-firm   brand/subsidiary of a roster firm; docs count toward that firm
  conflict-screen-excluded  v2 screen excluded the firm although the pilot coded an AI feature
  out-below-slots           in a v2 industry but below the top-N slots
  out-not-on-roster         subsidiary whose parent is classified elsewhere / not listed
  out-model-developer       excluded by the model-developer rule
  out-nonprofit             excluded by the commercial-firm rule
  out-non-us                non-US firm; EU/UK firms are comparison-set candidates
"""
import csv
from collections import Counter

C = 'carry-over'
RV = 're-verify hash in window'

# company: (naics4, status, roster_firm, roster_rank, action, note)
M = {
    'Walmart': ('4552', C, 'Walmart', '2', RV, ''),
    'Target': ('4552', C, 'Target', '4', RV, ''),
    'Amazon': ('4552', 'out-model-developer', 'Amazon', '1', 'supplementary only',
               'Excluded: develops its own foundation models (Nova).'),
    'Home Depot': ('4441', C, 'The Home Depot', '1', RV, ''),
    "Lowe's": ('4441', C, "Lowe's", '2', RV, ''),
    'Verizon': ('5171', C, 'Verizon', '1', RV, ''),
    'Comcast': ('5171', C, 'Comcast', '3', RV, ''),
    'Wells Fargo': ('5221', C, 'Wells Fargo', '4', RV, ''),
    'Marriott': ('7211', C, 'Marriott International', '1', RV, ''),
    'Hilton': ('7211', C, 'Hilton Worldwide', '4', RV, ''),
    'Delta': ('4811', C, 'Delta Air Lines', '1', RV, ''),
    'United': ('4811', C, 'United Airlines Holdings', '2', RV, ''),
    'American': ('4811', C, 'American Airlines Group', '3', RV, ''),
    'Alaska (+ Hawaiian)': ('4811', C, 'Alaska Air Group', '5', RV,
                            'Screening log marks Alaska "stop" (v1 legacy label); sample.csv includes it. Hawaiian is part of Alaska Air Group.'),
    'Frontier': ('4811', C, 'Frontier Group (Frontier Airlines)', '7', RV, ''),
    'Hims & Hers': ('6211', C, 'Hims & Hers Health', '4', RV, ''),
    'Capital One': ('5222', C, 'Capital One Financial', '2', RV, ''),
    'Chime': ('5223', C, 'Chime Financial', '4', RV, ''),
    'Booking.com': ('5615', C, 'Booking Holdings', '1', RV + '; code with Priceline/Kayak as one firm',
                    'Firm = Booking Holdings; Booking.com, Priceline and Kayak are its brands.'),
    'Priceline': ('5615', 'merged-into-roster-firm', 'Booking Holdings', '1', 'code as a Booking Holdings brand',
                  'Brand of Booking Holdings; counted once at firm level.'),
    'Kayak': ('5615', 'merged-into-roster-firm', 'Booking Holdings', '1', 'code as a Booking Holdings brand',
              'Brand of Booking Holdings; counted once at firm level.'),
    'Expedia': ('5615', C, 'Expedia Group', '2', RV, ''),
    'Airbnb': ('5615', C, 'Airbnb', '3', RV, ''),
    'Tripadvisor': ('5615', C, 'Tripadvisor', '4', RV, ''),
    'Chegg': ('6117', C, 'Chegg', '2', RV, ''),
    'Uber Eats': ('4853', C, 'Uber Technologies', '1', RV + '; confirm docs reach the feature the screen used',
                  'Firm = Uber Technologies (4853). Screen qualified it on NL search; pilot docs cover Uber Eats.'),
    'DoorDash': ('4922', C, 'DoorDash', '1', RV, ''),
    'Instacart': ('4922', C, 'Maplebear (Instacart)', '2', RV, ''),
    'Zillow': ('5312', C, 'Zillow Group', '4', RV, ''),
    'Redfin': ('5222', 'merged-into-roster-firm', 'Rocket Companies', '5',
               'DECIDE: use Redfin docs for Rocket, or collect Rocket fresh',
               'Redfin owned by Rocket since 2025; Rocket is a 5222 roster firm (rank 5).'),
    'Teladoc': ('6211', 'conflict-screen-excluded', 'Teladoc Health', '3', 'DECIDE: re-screen or drop',
                'v2 screen: internal-only (human care navigators, "not chatbots"). Pilot coded a Teladoc AI feature.'),
    'GEICO': ('5241', 'out-not-on-roster', '', '', 'supplementary only',
              'Berkshire Hathaway subsidiary; not on 5241 roster. FLAG: confirm the subsidiary rule excludes it.'),
    'Lemonade': ('5241', 'out-below-slots', '', '', 'supplementary only', 'Below top 10 in 5241.'),
    'Gopuff': ('4451', 'out-below-slots', '', '', 'supplementary only', 'Private; below top 10 in 4451.'),
    'K Health': ('6211', 'out-below-slots', '', '', 'supplementary only', 'Private; below top 10 in 6211.'),
    'Dave': ('5222', 'out-below-slots', '', '', 'supplementary only', 'Below top 10 in 5222.'),
    'Coinbase': ('5231', 'out-below-slots', '', '', 'supplementary only',
                 '5231 top 5 = Goldman, Fidelity, Schwab, Edward Jones, Raymond James.'),
    'Robinhood': ('5231', 'out-below-slots', '', '', 'supplementary only', 'Below top 5 in 5231.'),
    'Public': ('5231', 'out-below-slots', '', '', 'supplementary only', 'Private; below top 5 in 5231.'),
    'Duolingo': ('5132', 'out-below-slots', '', '', 'supplementary only', 'Below top 5 in 5132.'),
    'Grammarly': ('5132', 'out-below-slots', '', '', 'supplementary only', 'Private; below top 5 in 5132.'),
    'Realtor.com': ('5312', 'out-not-on-roster', '', '', 'supplementary only',
                    'News Corp subsidiary (Move Inc.); parent classified elsewhere.'),
    'Khan Academy': ('6117', 'out-nonprofit', '', '', 'supplementary only',
                     'Nonprofit; excluded by the commercial-firm rule.'),
}
NON_US = {'Accor': '7211', 'IHG': '7211', 'Ada Health': '6211', 'Deutsche Telekom': '5171',
          'Telefonica': '5171', 'Vodafone': '5171', 'Monzo': '5221', 'NatWest': '5221',
          'Revolut': '5221', 'bunq': '5221', 'Nubank': '5221', 'Klarna': '5222', 'eToro': '5231',
          'Skyscanner': '5615', 'Trip.com': '5615', 'Rightmove': '5312', 'Zoopla': '5312'}
for co, code in NON_US.items():
    if co == 'Nubank':
        note = 'Non-US (Brazil); not EU/UK, so not a comparison-set candidate.'
    else:
        note = 'Non-US; candidate for the EU/UK comparison set (open bracket in 3.2).'
    M[co] = (code, 'out-non-us', '', '', 'hold for EU/UK comparison set', note)

cov = {r['naics4']: r for r in csv.DictReader(open('recollection/coverage-table.csv', encoding='utf8'))}
docs = list(csv.DictReader(open('documents.csv', encoding='utf8')))
nd = Counter(d['company'] for d in docs)
vert = {d['company']: d['vertical'] for d in docs}
assert set(M) == set(nd), set(M) ^ set(nd)

out = []
for co, (code, st, rf, rr, act, note) in M.items():
    c = cov[code]
    grp = c['group'] if st in (C, 'merged-into-roster-firm') else 'none'
    out.append({'company': co, 'old_vertical': vert[co], 'n_docs': nd[co], 'naics4': code,
                'industry': c['industry'], 'hh_rank': c['hh_rank'], 'industry_group': c['group'],
                'sample_group_v2': grp, 'status_v2': st, 'roster_firm': rf, 'roster_rank': rr,
                'action': act, 'note': note})
order = {C: 0, 'merged-into-roster-firm': 1, 'conflict-screen-excluded': 2}
out.sort(key=lambda r: (order.get(r['status_v2'], 3), r['sample_group_v2'] != 'main',
                        int(r['hh_rank']), r['company']))
with open('recollection/pilot-corpus-crosswalk.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)

by = {r['company']: r for r in out}
for d in docs:
    r = by[d['company']]
    d.update(naics4_v2=r['naics4'], industry_v2=r['industry'],
             sample_group_v2=r['sample_group_v2'], status_v2=r['status_v2'])
with open('documents.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=list(docs[0]))
    w.writeheader()
    w.writerows(docs)

print(Counter((r['status_v2'], r['sample_group_v2']) for r in out))
print('docs by v2 group:', Counter(d['sample_group_v2'] for d in docs))
