# Materials: AI liability in consumer terms of service

Supporting materials for the working paper *Disclosed, Disclaimed, or Absolved* (Rohail Khan, 2026). Released October 2026. Data frozen 14 October 2026.

The full captured text of the company documents is not included, because those documents are copyrighted by the companies that publish them. Every document is identified here by its URL, retrieval date, archived-snapshot link and SHA-256 hash. Full captured texts are available to researchers on request.

## Contents

| Folder | What it holds |
|---|---|
| `dataset/documents.csv` | One row per document collected. Use rows whose `status_v2` is `new-v2-fullread`, `new-v2-PROVISIONAL` or `carry-over`. Rows marked `out-…`, `merged-…` or `conflict-…` were screened out and are kept for transparency. Columns `B1`–`B11` hold the clause codes (S = AI-specific, G = generic clause that reaches the AI, A = absent after a full read, U = untested, na = not applicable). `binding_v2` records whether the document governs the AI channel. `sample_group_v2` separates the main sample from the supplementary set. Rows with a `t6-` document type are marketing, incident or regulatory sources, which are never coded. |
| `dataset/taxonomy-v2-firms.csv` | Firm-level locus, Disclosure, Disclaimer and Responsibility scores (0–3) and cluster, produced by `scripts/analysis/taxonomy_v2.py`. |
| `dataset/firm-level-codings.csv` | Firm-level codings from the pilot corpus. |
| `register/document-register-and-extracts.md` | For each document: provenance header (URL, retrieval date, effective date, capture depth, clause codes), the coding-relevant extract and the coder's note. |
| `register/capture-manifest.csv` | File name, size and SHA-256 hash of every captured document. |
| `baselines/` | The November 2022 baselines: `WAYBACK-MANIFEST.csv` and `v2-baseline-fetch-log.csv` give each Wayback Machine snapshot and timestamp, plus the reason a document has no baseline. `diff-results/` has the clause-level verdicts (carried over, mixed, new, retrofit), the per-document sentence statistics and the hand-check log. `FINDINGS-v2-clause-continuity.md` summarizes them. |
| `screening/` | `screening-log.csv` lists all 562 firms screened, with rank, revenue and source, decision and evidence. Also includes the industry rankings (Economic Census revenue × household share), the screening protocol, rank changes and the derived samples. |
| `codebook/` | The coding manual and the clause codebook (B1–B11, with the S/G/A/U rules). |
| `scripts/` | `sample/` builds the sample from the screening log. `baseline-tools/` fetches Wayback captures and runs the sentence-level comparison. `analysis/` produces the taxonomy and Figure 1. Paths are relative to the original project folder, so adjust them before running. |
| `reliability/` | Codes from both coders for the reliability-test documents, the second coder's instructions, the logs and the agreement reports. |

## Notes

- **Snapshot.** Terms change. Every code describes the document as captured on the date recorded for it.
- **Main-sample reconciliation.** `screening/sample.csv` is the output of the sample-building script. Its reconciliation with the 59-firm main sample reported in the paper is in progress. The paper's counts are computed from `dataset/documents.csv` (`sample_group_v2`).
- **Reliability.** The reliability files come from the pilot corpus. A human validation on the final dataset is in progress.

## Licence

Data, codebook and documentation: CC BY 4.0. Scripts: MIT. Company documents excerpted in the register remain the property of their publishers; excerpts are reproduced for research and commentary.

## Citation

Rohail Khan. 2026. *Disclosed, Disclaimed, or Absolved: AI liability in consumer terms of service* (working paper and materials). https://github.com/rokhan10-create/ai-liability-terms
