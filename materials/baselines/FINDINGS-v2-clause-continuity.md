# v2 clause continuity, Nov 2022 → 2026: what is inherited, what is retrofitted, what is new

> **Working notes, 12 October 2026. Not the paper's figures.** This summary includes HIL-01 (Hilton Grand Vacations, a separate company excluded from the paper's analysis), splits results by the earlier main and supplementary samples, and counts a document as AI-silent by its coded `ai_language`, not by the absence of AI sentences. For those reasons its counts differ slightly from the paper (for example 475 rather than 473 general clause instances, 121 rather than 117 AI-specific clauses, and 29 rather than 33 revised documents without AI language). The paper's archival figures are produced by `scripts/analysis/archival_figures.py`.

**Purpose.** The pre-ChatGPT baseline is not for checking whether 2022 terms mentioned AI. It answers two questions:
1. Are firms revising their terms at all?
2. For every clause we coded, is the current language 2022 boilerplate, a 2022 clause with AI wording spliced in, or newly written?

Extends the pilot (`FINDINGS-clause-continuity.md`, 23 documents) to the v2 corpus. Machine output: `clause-diff-results-v2/`. Hand checks: `clause-diff-results-v2/MANUAL-CHECKS-v2.md`.

## Coverage

**Main sample:** 71 of 107 documents with a baseline (66%), 35 gaps, and 1 open (Publix).

| | Documents | Share |
|---|---|---|
| In the v2 baseline worklist | 215 | |
| **With a usable 2022 baseline** | **138** | 64% |
| Gap: no Wayback copy within 2021-01-01 to 2023-06-01 | 57 | 27% |
| Gap: URL never archived | 10 | 5% |
| Gap: archived copy unusable (captcha, bot wall/403, empty script shell) | 9 | 4% |
| Open: Publix (only snapshot tried was a geo-block page) | 1 | |

**Selection rule.** The Wayback copy closest to 2022-11-30 (either side), as in the pilot.
- Copies within one month of launch are treated as the baseline.
- The 11 copies dated 2023 (Jan-Apr) were each scanned for generative-AI wording; none contains any. The only hit is U.S. Bank's pre-existing Siri/Google Assistant clause.
- Exact dates are in `v2-baseline-fetch-log.csv`, in the `side` column (on-or-before / after).

**Capture routes.**
- Scripted CDX fetch until the Wayback index rate-limited this machine.
- Then playback via the researcher's own Chrome. This stored text only: raw bytes were hashed (SHA-256 recorded) and not retained.
- For two script-rendered pages (ThredUp, Roku): rendered-view text.

## Q1. Are firms revising their terms? Mostly, at very different rates

This is the share of each current document's legal sentences that are verbatim (similarity ≥ 0.90) from the 2022 copy. 137 documents; Frontier's stub site terms are excluded as a thin baseline.

| Group | Documents | Share |
|---|---|---|
| Frozen (≥ 90% unchanged) | 16 | 12% |
| Maintained (35–89%) | 78 | 57% |
| Rewritten (< 35% unchanged) | 43 | 31% |

The median document keeps 52% of its sentences verbatim since Nov 2022 (main sample: 56.5%). Privacy notices churn more than terms: 18 of 31 are rewritten.

**Frozen since before ChatGPT (≥ 90% unchanged), all with consumer AI in 2026:**
- Alaska site terms; Centene; Delta site terms; Duke Energy; Elevance; Giant Eagle; Hilton site agreement;
- Southwest terms; AT&T website terms; Caesars; MetLife; State Farm; FedEx;
- Roku device terms; Greystar; Vail (Epic Pass).

Any AI coverage these documents give comes through text written before ChatGPT.

**AI clauses bolted onto otherwise frozen documents (≥ 85% unchanged, with new AI sentences):**
- Bath & Body Works (89% unchanged; 7 new AI sentences)
- Elevance (93%; 1)
- Comcast Residential Services Agreement (86%; 2)
- H&R Block (87%; 3)
- Nerdy / Varsity Tutors (88%; 2)

These firms did not revise their contracts for AI; they inserted AI text into them.

**Revised but still AI-silent.** These documents had at least 40% of their sentences replaced or edited since 2022, and their current version is coded AI-silent (`ai_language` none/n-a).
- 29 documents in total, 13 of them in the main sample.
- **Main sample:** Albertsons; Comcast web terms; Gap; J.Crew; T-Mobile; UnitedHealth (terms and privacy); Verizon (two app documents); Casey's; Centene privacy; Elevance privacy; McDonald's.
- **Supplementary:** Avis; CVS ×4; Kendra Scott ×2; Pinterest; Remitly; Rocket; Royal Caribbean; Signet; Six Flags; Tractor Supply; Topgolf; Greystar app terms.

These are the strongest silence findings: the firm demonstrably revisited the document and wrote nothing about AI.

## Q2. Are our coded clauses new, or inherited?

### Generic codes (G: a generic clause that reaches an AI feature)

475 G-coded clause families were located in both versions. A further 43 were not located by pattern.

| Verdict | Count | Share |
|---|---|---|
| Carried over from 2022 (≥ 75% of the family's sentences verbatim, none new) | 244 | 51% |
| Mixed: part 2022, part new | 143 | 30% |
| New or rewritten | 88 | 19% |

Share carried over, by code:

| Code | Carried over | Share |
|---|---|---|
| B10 IP over inputs / content licence | 30 of 40 | 75% |
| B4 anti-reliance | 19 of 30 | 63% |
| B1 transaction error | 13 of 22 | 59% |
| B7 indemnity | 48 of 81 | 59% |
| B2 limitation of liability | 49 of 90 | 54% |
| B3 responsibility shift | 22 of 42 | 52% |
| B6 accuracy / as-is | 33 of 72 | 46% |
| B8 third-party carve-out | 29 of 91 | 32% |

**Implication.** Most of the generic protection that reaches a firm's AI is inherited pre-ChatGPT boilerplate. It still matters for exposure, because the clause reaches the AI whether or not anyone intended it to. But it must be framed as inherited, not as a drafting response to AI. This confirms the pilot's two-thirds finding at about half, on a corpus six times larger.

### AI-specific codes (S)

210 S-coded clauses. The verdict is based on the AI-mentioning sentences, not on clause-family patterns (see MANUAL-CHECKS-v2 §1).

**Headline set (121):** clauses whose operative AI sentence was located in the clause family, plus the 13 verified by hand.

| Verdict | Count | Share |
|---|---|---|
| New AI text | 83 | 69% |
| Retrofit: AI words spliced into a 2022 clause | 33 | 27% |
| AI-category text already in 2022 | 5 | 4% |

**Other 89:** verdict assigned at document level, so lower confidence. A single retrofit sentence anywhere in the document marks every S code in it "retrofit", which overstates retrofits. Raw split: 48 new, 41 retrofit.

**Retrofits (verified examples):**
- **Airbnb B4/B6:** the 2022 translation disclaimer ("does not guarantee the accuracy or quality of translations… Members are responsible for confirming the accuracy of such translations") now reads "generated Content or translations". It is a textbook retrofit.
- **U.S. Bank B2:** the 2022 "no liability for reliance on the information provided by any…" clause now adds "AI tools".
- **Wells Fargo Online Access Agreement B10:** the 2022 chat-monitoring sentence now names "virtual AI assistant… human-simulated conversation".
- **Pilot cases, re-confirmed:** American (AS-IS clause extended to "artificial intelligence tools and outputs"), Walmart (scope definition), Target (B3 + "Agentic Commerce Agent"), Home Depot (B10 + "training data for AI features"), Marriott.

**AI-category text already in 2022 (5, all verified):**
- **U.S. Bank B3 and B5:** Smart Assistant voice banking. "Verify the on-screen action"; commands "even if not specifically intended by you, will be presumed to be authorized". Verbatim from 2022: an agentic-style deemed-authorization clause that predates ChatGPT.
- **Wells Fargo general terms B6:** the Chat service is not warranted "free of fault or error"; verbatim 2022.
- **Avis privacy B11:** machine-learning identity verification, already in 2022.
- **Uber privacy B10:** 2022 "machine learning to improve the user experience" became "training machine learning models".

## Caveats
- **Pattern-based clause families.** Regex families can over-match (generic sentences in the same family) or miss (43 G codes not located). G verdicts are family-level; S verdicts rest on AI sentences.
- **Similarity is a floor on continuity.** A clause restructured under the same heading can score "new".
- **Text-only and rendered-view baselines.** The document text is complete, but the raw HTML was not kept (hash recorded). ThredUp and Roku are rendered-view captures.
- **Document-level S verdicts (89)** are reported separately and should not be pooled with the headline set without the caveat above.
- **Method corrections** (S-verdict basis, strict AI tagging, wider legal-sentence filter): see MANUAL-CHECKS-v2.
- **Gaps are disclosed, never treated as "unchanged" or "AI-silent".** Several gaps are themselves informative: Delta's AI Terms and Expedia's AI terms have no pre-2023 copy, consistent with being new documents.
