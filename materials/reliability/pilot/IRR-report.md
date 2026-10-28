# Inter-Rater Reliability Report (Pilot)

**Date:** 2026-08-25 · **Coders:** primary (archive) vs. second independent coder
(`coder2-codings.csv`) · **Instrument:** `CODING-MANUAL.md` v1.0 · **Unit:** document.

## Corpus
20 preserved, full-text, current-version documents across 3 verticals (airlines,
banking, food-delivery). QSR and retail are excluded — no preserved sources yet (needs
backfill before they can enter IRR).

## Method & important caveat
Coder1's values were **reconstructed from the MASTER archive prose**, because coder1
never produced a document-level sheet in the shared schema (the skipped "step 7.5").
Codes the archive did not enumerate at document level are recorded here as **absent
(conservative)**. This deflates agreement wherever coder1 under-recorded generic
boilerplate on silent/secondary documents. The κ below is therefore a **floor**, not
the true reliability; a clean re-code of coder1 into the schema is required before any
publishable κ (see Next steps).

Cohen's κ, presence/absence per code, per document.

## Results

| Scope | % agreement | Cohen's κ |
|---|---|---|
| All 20 docs, literal coder1 | 83.2 | 0.597 |
| 18 docs (2 capture artifacts removed) | 82.3 | 0.599 |
| **Signal codes** (B2,B3,B6,B9,B11) | 95.6 | **0.867** |
| Boilerplate codes (B1,B4,B5,B7,B8) | 65.6 | 0.353 |
| 11 docs (enumeration-artifact docs also removed) | 93.4 | 0.852 |

**Per-code κ (18 clean docs):** B3 1.00 · B11 1.00 · B6 perfect(all-absent) ·
B10 perfect(all-absent) · B2 0.77 · B9 0.73 · B1 0.48 · B7 0.40 · B5 0.37 · B4 0.28 ·
**B8 −0.09**.

## Interpretation
1. The analytically load-bearing codes (anti-reliance, responsibility-shift,
   transaction-error, anti-jailbreak, agentic) are **almost-perfect** (κ=0.87). The
   taxonomy axes replicate across independent coders.
2. Low overall κ is driven by **ubiquitous boilerplate** (B4/B5/B7/B8) and is largely
   an **instrument artifact** (coder1 archive not document-uniform), not interpretive
   disagreement.
3. **B8 (third-party carve-out) is a genuine codebook defect** (κ=−0.09): three
   same-text splits (American, Instacart, Uber AI page) on whether a marketplace/
   third-party carve-out counts. Resolve in adjudication.
4. Both coders assigned **zero AI-specific codes to every truly-silent document** —
   the master say–do judgment is consistent.

## Disagreement ledger
| Document | coder1-only | coder2-only | type |
|---|---|---|---|
| Delta site ToU | — | B1,B2,B4,B7,B8 | enumeration artifact |
| American platform | B8 | — | genuine (B8 rule) |
| Alaska microcopy | B1,B2 | — | capture artifact (shell file) |
| Frontier privacy | B4 | B7 | genuine |
| Capital One T&C | — | B1,B4,B5,B7,B8 | enumeration artifact |
| Dave ToU | — | B1,B2,B4,B5,B8 | enumeration artifact |
| WF General ToU | — | B4,B5 | enumeration artifact |
| WF OAA | — | B9 | genuine (jailbreak clause) |
| DoorDash terms | — | B1,B4,B5,B7,B8 | enumeration artifact |
| DoorDash article | — | B7 | genuine |
| Instacart | B8 | B4,B5 | genuine (B8 + generics) |
| Uber ToU | — | B5,B7,B8,B9 | enumeration artifact |
| Uber AI page | B8 | — | genuine (B8 rule) |

## Capture defects surfaced by the second coder
- `alaska_inspires-destination-search-page.txt` is a **bot-challenge shell**, not the
  microcopy. Re-capture required.
- `frontier_contract-of-carriage.txt` is a **landing page**, not the CoC body
  (coder1 used the PDF). Both concluded "no AI"; substance agrees.

## Next steps (in order)
1. **Regenerate coder1 into `irr/coder1-codings.csv`** in the identical schema, coding
   generic boilerplate on every document uniformly. Re-run κ — expect it to rise toward
   the signal κ.
2. **Set an enumeration policy:** either both coders enumerate all generic-reaching
   codes on every document, OR neither codes pure boilerplate on AI-silent documents
   (recommended — boilerplate presence carries little signal; the `ai_specific` tag is
   what matters). Amend manual §5/§6, bump version.
3. **Adjudicate B8** (third-party carve-out): write an explicit include/exclude rule;
   re-code the 3 affected docs; report post-adjudication κ.
4. **Re-capture** the two artifact documents; re-code Alaska microcopy.
5. Report the **pre-adjudication** κ (per manual §13.5) alongside the signal-code κ in
   the paper's methods section.
