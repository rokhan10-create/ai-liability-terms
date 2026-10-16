"""Firm-level taxonomy for the v2 sample: three axes (0-3) and five clusters, derived by rule from documents.csv.

AXES (each scored from the firm's full-read documents; binding = binding_v2 in BIND below)
  Disclosure  - does the firm tell the customer an AI is involved?
     3  a binding document names the assistant by brand
     2  a binding document names AI by category or carries AI-specific language
     1  AI is disclosed only outside the binding contract (privacy notice, help page, microcopy, AI-info page)
     0  no AI language in any coded document
  Disclaimer  - does the firm disclaim responsibility for the AI's output? (B2 liability, B4 anti-reliance, B6 accuracy)
     3  two or three of {B2, B4, B6} coded S in binding documents
     2  exactly one of {B2, B4, B6} coded S in a binding document
     1  only generic (G) versions reach the AI in the contract, or the S version sits only outside it
     0  none of the three reaches the AI
  Responsibility - does the firm push the consequences onto the customer?
     (B1 non-honoring of AI errors, B3 responsibility for use of output, B5 own-assistant deemed authorization)
     3  two or more of those coded S in binding documents
     2  exactly one coded S in a binding document
     1  only generic B1 or B3 (G) in the contract
     0  none
  B7 (indemnity) and B10 are excluded from the axes: low inter-coder agreement (paper §3.8).

CLUSTERS (first rule that matches)
  Agentic-shift  an AI-specific clause (B5 S) in a binding document governing the firm's OWN acting assistant
                 (deemed authorization / acts assigned to the customer); outward-facing bans on customers' agents do not count
  Fortified      Disclaimer >= 2 and Responsibility >= 2
  Warned         Disclaimer >= 2 or Responsibility >= 2
  Peripheral     locus bucket Peripheral: AI-specific text or microcopy only outside the binding contract
  Exposed        everything else (no AI-specific protection in the contract)

Run from the project root: python analysis/taxonomy_v2.py   -> analysis/taxonomy-v2-firms.csv
"""
import collections, csv

BIND = ("governs-ai-expressly", "governs-surface", "governs-surface-partial")
# Firms whose own-assistant B5 clause assigns the assistant's acts to the customer. Hims & Hers removed 2026-10-15:
# its clause says the AI may help change the account but allocates responsibility neither way (paper §5.3).
OWN_AGENT = {"Bank of America", "U.S. Bancorp", "Exelon",                      # main sample (paper §5.3)
             "Block (Cash App)", "Chegg", "H&R Block", "Intuit"}              # supplementary
R = [r for r in csv.DictReader(open("documents.csv", encoding="utf-8"))]
use = lambda r: r["status_v2"] == "new-v2-fullread" and r["doc_id"] != "HIL-01"  # HGV excluded from Hilton
groups = {r["company"]: r["sample_group_v2"] for r in R if r["status_v2"] in ("new-v2-fullread", "new-v2-PROVISIONAL", "carry-over")}
out = []
for firm, grp in sorted(groups.items()):
    D = [r for r in R if r["company"] == firm and use(r)]
    T = [r for r in D if r["binding_v2"] in BIND]
    NB = [r for r in D if r["binding_v2"] not in BIND]
    S_in = lambda code: any(r[code] == "S" for r in T)
    G_in = lambda code: any(r[code] == "G" for r in T)
    S_out = lambda code: any(r[code] == "S" for r in NB)
    ai_lang = lambda docs: any(r["ai_language"] in ("ai-specific", "disclosure-only", "compelled-disclosure", "generic-reaching-ai")
                               or r["names_ai"] in ("brand", "category") for r in docs)
    # Locus bucket (paper §3.5 / Table 4), by rule
    if any(r["locus"] in ("1", "2") for r in T): locus = "Dedicated"
    elif any(r["locus"] == "3" for r in T): locus = "Integrated-generic"
    elif any(r["ai_language"] == "ai-specific" or r["locus"] in ("4", "anomalous-privacy-notice") for r in NB): locus = "Peripheral"
    else: locus = "Silent"
    # Disclosure
    if any(r["names_ai"] == "brand" for r in T): dis = 3
    elif any(r["names_ai"] == "category" or r["ai_language"] == "ai-specific" for r in T): dis = 2
    elif ai_lang(NB) or ai_lang(T): dis = 1
    else: dis = 0
    # Disclaimer
    nS = sum(S_in(c) for c in ("B2", "B4", "B6"))
    dsc = 3 if nS >= 2 else 2 if nS == 1 else 1 if (any(G_in(c) for c in ("B2", "B4", "B6")) or any(S_out(c) for c in ("B2", "B4", "B6"))) else 0
    # Responsibility
    b5own = S_in("B5") and firm in OWN_AGENT
    nR = sum([S_in("B1"), S_in("B3"), b5own])
    rsp = 3 if nR >= 2 else 2 if nR == 1 else 1 if (G_in("B1") or G_in("B3")) else 0
    if b5own: cl = "Agentic-shift"
    elif dsc >= 2 and rsp >= 2: cl = "Fortified"
    elif dsc >= 2 or rsp >= 2: cl = "Warned"
    elif locus == "Peripheral": cl = "Peripheral"
    else: cl = "Exposed"
    out.append(dict(company=firm, sample=grp, locus=locus, disclosure=dis, disclaimer=dsc, responsibility=rsp, cluster=cl,
                    s_disclaimer_families=nS, s_responsibility=nR, b5_s=S_in("B5"), b5_own=b5own, n_binding=len(T)))
with open("analysis/taxonomy-v2-firms.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for g in ("main", "supplementary"):
    sub = [o for o in out if o["sample"] == g]
    print(f"== {g} ({len(sub)})")
    for cl in ("Agentic-shift", "Fortified", "Warned", "Peripheral", "Exposed"):
        f = [o["company"] for o in sub if o["cluster"] == cl]
        print(f"  {cl:13s} {len(f):3d}  {', '.join(f)}")
    print("  locus", dict(collections.Counter(o["locus"] for o in sub)))
    for ax in ("disclosure", "disclaimer", "responsibility"):
        print(f"  {ax:14s}", dict(sorted(collections.Counter(o[ax] for o in sub).items())))
