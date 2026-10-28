"""Firm-level segment comparisons in paper §4.3 (capability) and §4.4 (industry group, revenue rank), with Fisher's exact tests.

Outcome: a firm is "silent" if no incorporated document (binding_v2 in BIND) carries an AI-specific (S) code in any clause family.
  Capability  action-capable = any of the firm's documents has ai_vector generative-agentic, non-generative-agentic or hybrid
  Industry    NAICS groups as in Table 6 (retail 44-45; restaurants 722; finance, insurance, health 52, 62;
              airlines, telecom, utilities, hotels 22, 481, 517, 721; everything else digital and other services)
  Rank        firms in the top-20 industries (sample_group_v2 = main), ranks 1-5 vs 6-10 from the screening crosswalk
Run from the project root: python analysis/segment_tests.py
"""
import collections, csv
from math import comb

BIND = ("governs-ai-expressly", "governs-surface", "governs-surface-partial")
FAM = [f"B{i}" for i in range(1, 12)]
ACTS = ("generative-agentic", "non-generative-agentic", "hybrid")
R = list(csv.DictReader(open("documents.csv", encoding="utf-8")))
X = {r["dataset_name"]: r for r in csv.DictReader(open("recollection/sample-crosswalk.csv", encoding="utf-8"))
     if r["status"] == "collected and coded"}
firms = sorted({r["company"] for r in R if r["status_v2"] in ("new-v2-fullread", "new-v2-PROVISIONAL", "carry-over")})
use = [r for r in R if r["status_v2"] == "new-v2-fullread" and r["doc_id"] != "HIL-01"]  # HGV excluded from Hilton
silent = {f for f in firms if not any(r["company"] == f and r["binding_v2"] in BIND and any(r[c] == "S" for c in FAM) for r in use)}


def fisher(a, b, c, d):
    """Two-sided Fisher's exact test for [[a, b], [c, d]]."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    p = lambda x: comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    return sum(p(x) for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1) if p(x) <= p(a) * (1 + 1e-7))


def compare(label, g1, g2):
    s1, s2 = len(set(g1) & silent), len(set(g2) & silent)
    print(f"{label}: {s1} of {len(g1)} ({s1 / len(g1):.0%}) vs {s2} of {len(g2)} ({s2 / len(g2):.0%}) silent; "
          f"Fisher p = {fisher(s1, len(g1) - s1, s2, len(g2) - s2):.2f}")


print(f"{len(firms)} firms, {len(silent)} silent")
acts = {r["company"] for r in R if r["company"] in firms and r["ai_vector"] in ACTS}
compare("Action-capable vs answer/recommend", sorted(acts), [f for f in firms if f not in acts])


def group(n):
    if n[:2] in ("44", "45"): return "Retail"
    if n[:3] == "722": return "Restaurants"
    if n[:2] in ("52", "62"): return "Finance, insurance, health"
    if n[:2] == "22" or n[:3] in ("481", "517", "721"): return "Airlines, telecom, utilities, hotels"
    return "Digital and other services"


G = collections.defaultdict(list)
for f in firms:
    G[group(X[f]["naics4"])].append(f)
for g, fs in G.items():
    print(f"  {g:38s} {len(fs):3d} firms, {len(set(fs) & silent):3d} silent")
compare("Retail vs airlines/telecom/utilities/hotels", G["Retail"], G["Airlines, telecom, utilities, hotels"])
main = [f for f in firms if X[f]["sample"] == "main"]
compare("Top-20 industries, rank 1-5 vs 6-10", [f for f in main if int(X[f]["industry_rank"]) <= 5],
        [f for f in main if int(X[f]["industry_rank"]) > 5])
