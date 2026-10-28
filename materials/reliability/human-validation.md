# Human validation

This is the human check reported in paper §2.3. All figures are pre-adjudication: they compare the human codes with the released dataset (`dataset/documents.csv`) before any disagreement was resolved. Reproduce them with `scripts/reliability/score_human.py`.

## Design

- **Sample.** 53 of the coded documents, stratified by document role (contract, privacy notice or in-product microcopy; incorporated or not; with or without AI-specific codes). Every document with an AI-specific B1 code is included. Seed 20261020. Documents are coded in one random order.
- **Coder.** An author who did not do the primary coding, coding from full reads under the frozen coding manual (`codebook/CODING-MANUAL.md`, v1.1), without the dataset's codes.
- **Judgements.** Incorporation status for the AI feature (binding / not binding), and S, G or A for each of the eleven clause families B1–B11.
- **Scoring.** Cohen's κ against the dataset. Dataset `na` and `U` cells are scored as `A`. 95% confidence intervals come from 5,000 bootstrap resamples of documents, because the 11 cells within a document are not independent.

## Results

30 documents, 28 firms, 330 code cells: sample positions 1–29 and CMX-01 (position 39, coded out of order). Position 30 (WSM-01) was set aside because it was coded G in all eleven families.

| Measure | κ | 95% CI | % agree | n |
|---|---|---|---|---|
| AI-specific tag (S vs not S) | **0.79** | 0.71–0.87 | 94.2% | 330 cells |
| Clause presence (S or G vs A) | **0.74** | 0.63–0.83 | 86.7% | 330 cells |
| Full S / G / A | **0.73** | 0.64–0.80 | 83.0% | 330 cells |
| B1 (S / G / A) | 0.60 | 0.25–0.86 | 80.0% | 30 docs |
| Incorporation (binding vs not) | **0.66** | 0.30–0.92 | 86.7% | 30 docs |

Documents: 20 governing terms, 2 site terms, 1 dedicated AI terms, 1 contract of carriage, 3 privacy notices, 3 in-product microcopy.

## Direction of disagreement

- **AI-specific language is not overstated.** The human coder tagged 54 cells S; the dataset has 57.
- **Generic clauses are under-coded in the dataset.** The human coder found 182 cells present; the dataset has 154. The most common disagreement is human G where the dataset has A.
- **B10 accounts for the largest share of AI-specific disagreements** (7 of 19 cells). This is the boundary between a generic licence over submissions and training on AI inputs.
- **Incorporation disagreements mostly run one way.** Three of the four (C-02, DGX-01, AAL-02) are documents the dataset classes as not reaching the AI feature that the human coder read as binding. The fourth (LZ-01) runs the other way.

## Limitations

- The coder is one of the paper's authors, not an outside coder.
- 30 of the 53 sampled documents are scored. Stratum-weighted κ is not yet estimable.
- B1 and incorporation κ rest on 30 documents and have wide intervals.

## Files

- `human-coder-codings.csv` holds the human codes for the 30 documents.
- `human-sample.csv` lists the 53 sampled documents in coding order, with stratum and weight.
