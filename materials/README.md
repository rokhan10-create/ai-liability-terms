# Materials: Disclosed, Disclaimed, or Absolved

Supporting materials for *Disclosed, Disclaimed, or Absolved: A Cross-Sector Audit of AI-Liability Terms at the Largest U.S. Consumer-Facing Firms* (Rohail Khan, Zara Liaqat and Hassan Khan, 2026). Data frozen 14 October 2026. The `in_paper_corpus` flag and the reliability files were added on 25 October 2026; no code was changed.

The full captured text of the company documents is not included, because those documents are copyrighted by the companies that publish them. Every document is identified by its URL, retrieval date, archived-snapshot link and SHA-256 hash. Full captured texts are available to researchers on request.

## The paper's numbers at a glance

| | |
|---|---|
| Firms screened | 560 distinct firms in 93 consumer industries (`screening/screening-log.csv` has 562 rows; Boot Barn and 1-800-Flowers.com each appear twice) |
| Firms analysed | 133, in 57 industries |
| Documents | 270 (`in_paper_corpus = 1` in `dataset/documents.csv`) |
| Incorporated documents | 148 |
| Firms with no AI-specific clause in incorporated terms | 77 of 133 |
| Documents with a usable November 2022 baseline | 137, at 93 firms |

## Contents

| Folder | What it holds |
|---|---|
| `dataset/documents.csv` | One row per document collected. **The paper's 270-document corpus is the rows with `in_paper_corpus = 1`.** These are the `new-v2-fullread` rows except GRY-P1, a UK sister-brand structural proxy that is never evidence for the U.S. firm, and COF-04, a Capital One disclosures page. Other rows are marketing, incident or regulatory sources (`t6-` document types, never coded), or were screened out (`out-…`, `merged-…`, `conflict-…`) and are kept for transparency. Columns `B1`–`B11` hold the clause codes (S = AI-specific, G = general clause that reaches the AI, A = absent after a full read, U = untested, na = not applicable). `binding_v2` records whether the document is incorporated for the AI channel (paper §2.2, Table B1). `ai_vector` records assistant capability; the paper's action-capable firms are those with a `generative-agentic`, `non-generative-agentic` or `hybrid` document. `sample_group_v2` marks firms from the 20 largest industries (`main`, roster depth 10) and the rest (`supplementary`, depth 5). It is used only for the rank comparison in §4.4; all statistics pool the 133 firms. |
| `dataset/taxonomy-v2-firms.csv` | Firm-level locus, Disclosure, Disclaimer and Absolution scores (0–3) and cluster (paper §3, Tables 2–3), produced by `scripts/analysis/taxonomy_v2.py`. |
| `dataset/firm-level-codings.csv` | Firm-level codings from the earlier pilot corpus. Not used in the paper. |
| `register/document-register-and-extracts.md` | For each document: a provenance header (URL, retrieval date, effective date, capture depth, clause codes), the coding-relevant extract and the coder's note. |
| `register/capture-manifest.csv` | File name, size and SHA-256 hash of every captured document. |
| `baselines/` | The November 2022 baselines (paper §2.4, Appendices C–D). `WAYBACK-MANIFEST.csv` and `v2-baseline-fetch-log.csv` give each Wayback Machine snapshot and timestamp, and the reason a document has none. `diff-results/` has the clause-level verdicts (carried over, mixed, new, retrofit), the per-document sentence statistics with each baseline's capture timestamp (`baseline_ts`), and the hand-check log. The diff files include HIL-01, which the paper excludes; `scripts/analysis/archival_figures.py` drops it and reproduces the paper's archival figures. `FINDINGS-v2-clause-continuity.md` holds earlier working notes, not the paper's figures. |
| `screening/` | `screening-log.csv` lists every firm screened, with rank, revenue and source, decision and evidence. `sample-crosswalk.csv` links each screened-in firm to its name in the dataset. The folder also has the industry rankings (Economic Census revenue × household share), the screening protocol and rank changes. |
| `codebook/` | The coding manual and the clause codebook (B1–B11, with the S/G/A/U rules). |
| `reliability/` | `full-recode/` holds the second LLM coder (GPT) for all 264 recoded documents: κ 0.85 AI-specific, 0.79 presence, 0.90 incorporation. `human-validation.md` and `human-coder-codings.csv` hold the human check (paper §2.3). `pilot/` holds reliability rounds from the earlier pilot corpus, which the paper does not use. |
| `scripts/` | `analysis/taxonomy_v2.py` builds the taxonomy, `analysis/figure1_taxonomy.py` draws Figure 1, and `analysis/segment_tests.py` runs the capability, industry and rank comparisons with Fisher's exact tests (§4.3–4.4), and `analysis/archival_figures.py` produces the archival figures (§2.4, §4.2, §4.5, Appendices C–D). `reliability/` scores both reliability checks. `sample/` builds the sample from the screening log. `baseline-tools/` fetches Wayback captures and runs the sentence-level comparison. |

**What the release reproduces.** Every count, table and test in the paper can be recomputed from the released codes and diff outputs. Two things need the full captured texts, which are available on request: re-coding a document from its source, including checking an "absent after a full read" code, and the sentence-similarity threshold sensitivity in Table C1.

Scripts run from the original project root, with `documents.csv` at the top level, the crosswalk in `recollection/` and the diff outputs in `previous-tos/clause-diff-results-v2/`. To run them here, adjust those paths.

## Notes

- **Snapshot.** Terms change. Every code describes the document as captured on the date recorded for it.
- **Screened-in firms not collected.** 141 firms passed the screen and 133 were coded. The other eight (JetBlue, Breeze, Optimum, Mediacom, Fifth Third, Nationwide, Allstate, Prudential) are all ranked 6–10 in top-20 industries. They entered the roster when the depth for those industries was raised from five to ten firms, could not be collected before the analysis freeze, and are excluded from all counts in the paper. `screening/sample-crosswalk.csv` marks them as not collected.
- **Corrections to the paper's references.** The H&R Block Online Services Agreement [HRB-03] was retrieved on 9 October 2026, not 20 October as the reference list states. The register and the capture manifest give the correct date.

## Licence

Data, codebook and documentation: CC BY 4.0. Scripts: MIT. Company documents excerpted in the register remain the property of their publishers; excerpts are reproduced for research and commentary.

## Citation

Rohail Khan, Zara Liaqat, and Hassan Khan. 2026. *Disclosed, Disclaimed, or Absolved: A Cross-Sector Audit of AI-Liability Terms at the Largest U.S. Consumer-Facing Firms.* Dataset and materials: https://github.com/rokhan10-create/ai-liability-terms
