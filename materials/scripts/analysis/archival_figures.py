"""Archival-comparison figures in paper §2.4, §4.2, §4.5 and Appendices C-D, pooled over all 133 firms.

HIL-01 (Hilton Grand Vacations, excluded from the analysis as in analysis/taxonomy_v2.py) is dropped throughout;
the released diff files still contain it. Uses only released files: documents.csv and
previous-tos/clause-diff-results-v2/ (SUMMARY-v2.csv, CODED-CLAUSES-v2.csv, MANUAL-CHECKS-v2.md).
The sentence-level threshold sensitivity (Table C1) needs the per-document sentence files, which hold company
text and are not released; it is computed only if they are present.
Run from the project root: python analysis/archival_figures.py
"""
import collections, csv, json, os, re
from datetime import date

OUT = "previous-tos/clause-diff-results-v2"
DROP = {"HIL-01"}
BIND = ("governs-ai-expressly", "governs-surface", "governs-surface-partial")
FAM = [f"B{i}" for i in range(1, 12)]
LAUNCH = date(2022, 11, 30)
pct = lambda k, n: f"{k} of {n} ({100 * k / n:.0f}%)" if n else f"{k} of 0"

docs = {r["doc_id"]: r for r in csv.DictReader(open("documents.csv", encoding="utf-8"))}
summ = [r for r in csv.DictReader(open(f"{OUT}/SUMMARY-v2.csv", encoding="utf-8")) if r["doc_id"] not in DROP]
coded = [r for r in csv.DictReader(open(f"{OUT}/CODED-CLAUSES-v2.csv", encoding="utf-8")) if r["doc_id"] not in DROP]

print("== Baselines (§2.4, Appendix C)")
ts = [date(int(r["baseline_ts"][:4]), int(r["baseline_ts"][4:6]), int(r["baseline_ts"][6:8])) for r in summ]
print(f"  {len(summ)} documents at {len({r['company'] for r in summ})} firms; "
      f"{sum(t <= LAUNCH for t in ts)} captured on or before 30 Nov 2022, {sum(t > LAUNCH for t in ts)} after; "
      f"{sum(abs((t - LAUNCH).days) <= 31 for t in ts)} within a month of the launch")

print("\n== General clause families (§4.2, Table D1)")
G = [r for r in coded if r["coded_as"] == "G"]
print(f"  not located by pattern: {sum(r['verdict'] == 'NOT LOCATED BY PATTERN' for r in G)}")
G = [r for r in G if r["verdict"] != "NOT LOCATED BY PATTERN"]
V = ("CARRIED OVER", "MIXED", "NEW OR REWRITTEN")
for code in FAM + [None]:
    sel = [r for r in G if code is None or r["code"] == code]
    c = collections.Counter(r["verdict"] for r in sel)
    print(f"  {code or 'All':4s} located {len(sel):3d}  carried over {pct(c[V[0]], len(sel)):16s}  mixed {c[V[1]]:3d}  "
          f"new or rewritten {c[V[2]]:3d}")

print("\n== AI-specific clauses (§4.2)")
manual = {}  # hand-resolved verdicts; the last table row per document and code wins
for line in open(f"{OUT}/MANUAL-CHECKS-v2.md", encoding="utf-8"):
    m = re.match(r"\|\s*([A-Z]+-[0-9A-Z]+)\s*\|\s*(B\d+) S\s*\|[^|]*\|\s*\*\*([^*]+)\*\*", line)
    if m:
        v = m.group(3).upper()
        manual[(m.group(1), m.group(2))] = "pre" if "ALREADY" in v else "retro" if ("RETROFIT" in v or "EXPANDED" in v) else "new"
head = []
for r in (r for r in coded if r["coded_as"] == "S"):
    if (r["doc_id"], r["code"]) in manual:
        head.append(manual[(r["doc_id"], r["code"])])
    elif "(document-level)" not in r["verdict"] and "manual" not in r["verdict"]:
        head.append("pre" if "ALREADY" in r["verdict"] else "retro" if "RETROFIT" in r["verdict"] else "new")
corpus = [r for r in docs.values() if r["status_v2"] == "new-v2-fullread" and r["doc_id"] not in DROP]
nS = sum(r[c] == "S" for r in corpus for c in FAM)
print(f"  comparable: {len(head)} of {nS} AI-specific codes in the corpus; new {pct(head.count('new'), len(head))}, "
      f"retrofit {pct(head.count('retro'), len(head))}, already in 2022 {pct(head.count('pre'), len(head))}")

print("\n== Revision without AI language (§4.5)")
noai = lambda r: int(r["ai_sents"]) == 0
churn = [r for r in summ if int(r["pct_unchanged"]) <= 60 and noai(r)]
print(f"  at least 40% of sentences changed, no AI sentence: {len(churn)} documents at {len({r['company'] for r in churn})} firms")
frozen = sorted({r["company"] for r in summ if int(r["pct_unchanged"]) >= 90 and noai(r) and r["binding_v2"] in BIND})
print(f"  incorporated document at least 90% unchanged, no AI sentence: {len(frozen)} firms: {', '.join(frozen)}")

if all(os.path.exists(f"{OUT}/{r['doc_id']}.json") for r in G):
    print("\n== Threshold sensitivity (Table C1)")
    J = {d: json.load(open(f"{OUT}/{d}.json", encoding="utf-8"))["rows"] for d in {r["doc_id"] for r in G}}
    names = {"B1": "B1 txn-error non-honoring", "B2": "B2 limitation of liability", "B3": "B3 user-responsibility",
             "B4": "B4 anti-reliance", "B5": "B5 agentic / agent", "B6": "B6 accuracy / no-warranty",
             "B7": "B7 indemnification", "B8": "B8 third-party carve-out", "B9": "B9 anti-scrape / no-training",
             "B10": "B10 IP over inputs / training", "B11": "B11 automated decisions"}
    for hi in (0.85, 0.90, 0.95):
        k = 0
        for r in G:
            st = ["u" if x["ratio"] >= hi else "e" if x["ratio"] >= 0.60 else "n" for x in J[r["doc_id"]] if names[r["code"]] in x["families"]]
            k += st.count("u") / len(st) >= 0.75 and "n" not in st
        print(f"  {hi:.2f}: carried over {pct(k, len(G))}")
else:
    print("\n(Table C1 threshold sensitivity skipped: per-document sentence files not present.)")
