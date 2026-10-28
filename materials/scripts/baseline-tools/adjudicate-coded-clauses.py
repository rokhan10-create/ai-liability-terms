"""For every clause we coded present (S or G) in a baselined document, say whether its current language
is carried over from the Nov-2022 text, rewritten/new, or mixed. Reads documents.csv + clause-diff-results.
Run from project root after run-clause-diffs.py. Writes previous-tos/clause-diff-results/CODED-CLAUSES.csv"""
import csv, json, os, re

DOC_FOR = {  # clause-diff result slug -> documents.csv doc_id of the CURRENT coded document
    "delta-site-terms-of-use": "DAL-02", "delta-privacy-policy": "DAL-03", "united-legal-terms-conditions-notices": "UAL-01",
    "american-legal-info-platform-t-cs": "AAL-01", "frontier-terms-of-use": "FRO-01", "frontier-privacy-policy": "FRO-02",
    "walmart-terms-of-use": "WMT-01", "lowe-s-terms-conditions-of-use": "LOW-01", "target-terms-conditions": "TGT-01",
    "wells-fargo-general-terms-of-use": "WFC-02", "wells-fargo-online-access-agreement": "WFC-01", "dave-terms-of-use": "DAV-01",
    "natwest-privacy-policy": "NWB-01", "instacart-terms-of-service": "INS-01", "uber-eats-general-terms-of-use-us": "UBR-01",
    "gopuff-terms-conditions": "GP-01", "ihg-terms-of-use": "IHG-01", "klarna-user-terms-shopping-service": "KLR-01",
    "bunq-privacy-policy": "BUN-01", "amazon-conditions-of-use": "AMZ-05", "home-depot-terms-of-use": "HD-06",
    "hilton-site-usage-agreement": "HIL-02", "marriott-terms-of-use": "MAR-01",
}
FAM = {"B1": "B1 txn-error non-honoring", "B2": "B2 limitation of liability", "B3": "B3 user-responsibility",
       "B4": "B4 anti-reliance", "B5": "B5 agentic / agent", "B6": "B6 accuracy / no-warranty", "B7": "B7 indemnification",
       "B8": "B8 third-party carve-out", "B9": "B9 anti-scrape / no-training", "B10": "B10 IP over inputs / training",
       "B11": "B11 automated decisions"}
R = "previous-tos/clause-diff-results"
docs = {r["doc_id"]: r for r in csv.DictReader(open("documents.csv", encoding="utf-8"))}
out = []
for slug, doc_id in DOC_FOR.items():
    path = f"{R}/{slug}.json"
    if not os.path.exists(path):
        continue
    d = json.load(open(path, encoding="utf-8")); row = docs[doc_id]
    for code, fam in FAM.items():
        if row[code] not in ("S", "G"):
            continue
        sel = [x for x in d["rows"] if fam in x["families"]]
        u = sum(x["status"] == "unchanged" for x in sel); e = sum(x["status"] == "edited" for x in sel)
        n = sum(x["status"] == "new" for x in sel); tot = len(sel)
        if tot == 0:
            verdict = "NOT LOCATED BY PATTERN - manual"
        elif u / tot >= 0.75 and n == 0:
            verdict = "CARRIED OVER from 2022"
        elif (e + n) / tot >= 0.75:
            verdict = "NEW or REWRITTEN since 2022"
        else:
            verdict = "MIXED - part 2022, part new"
        flag = "CHECK: coded AI-specific but text is 2022" if row[code] == "S" and verdict.startswith("CARRIED") else ""
        out.append({"doc_id": doc_id, "company": row["company"], "doc": row["doc_title"][:60], "code": code,
                    "coded_as": row[code], "sents": tot, "unchanged": u, "edited": e, "new": n, "verdict": verdict, "flag": flag})
with open(f"{R}/CODED-CLAUSES.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
tally = {}
for o in out:
    tally.setdefault((o["coded_as"], o["verdict"].split(" -")[0].split(" from")[0].split(" since")[0]), 0)
    tally[(o["coded_as"], o["verdict"].split(" -")[0].split(" from")[0].split(" since")[0])] += 1
for o in out:
    print(f"{o['doc_id']:7s} {o['company'][:12]:12s} {o['code']:4s} {o['coded_as']}  {o['unchanged']:2d}/{o['edited']:2d}/{o['new']:2d}  {o['verdict']}  {o['flag']}")
print("\nTALLY (coded_as, verdict):"); [print(f"  {k}: {v}") for k, v in sorted(tally.items())]
