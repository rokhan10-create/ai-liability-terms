# Human validation: preliminary results

Status: in progress, 21 October 2026. The first 30 of 53 sampled documents are coded. All figures are pre-adjudication.

## Design

- **Sample.** 53 of the 264 coded documents (20%), stratified by document role (contract / privacy notice / in-product microcopy; binding or not; AI-specific codes or not). Every document with an AI-specific B1 code is included. Seed 20261020.
- **Order.** Documents are coded in one random order, so the first 30 positions are a fair subsample.
- **Coder.** The author, blind to the dataset's codes, coding from full reads under the frozen coding manual (`codebook/CODING-MANUAL.md`, v1.1).
- **Judgements.** Binding status for the AI feature (binding / not-binding), and S / G / A for each of the eleven clause families B1–B11.
- **Comparison.** Cohen's κ against the released dataset (`dataset/documents.csv`), before any adjudication. Dataset `NA` is scored as `A`.
- **Confidence intervals.** 95%, from 5,000 bootstrap resamples of documents (the 11 cells within a document are not independent).

## Results: 30 documents, 28 firms, 330 code cells

| Measure | κ | 95% CI | % agree | n |
|---|---|---|---|---|
| AI-specific tag (S vs not S) | **0.75** | 0.61–0.86 | 92.7% | 330 cells |
| Clause presence (S or G vs A) | **0.72** | 0.61–0.81 | 86.1% | 330 cells |
| Full S / G / A | 0.70 | 0.60–0.78 | 80.9% | 330 cells |
| B1 (S / G / A) | 0.62 | 0.29–0.87 | 80.0% | 30 docs |
| Binding vs not binding | 0.63 | 0.22–0.92 | 86.7% | 30 docs |

Documents: 21 governing terms, 2 site terms, 1 dedicated AI terms, 1 contract of carriage, 3 privacy notices, 2 in-product microcopy. Coding time: 136 minutes in total, median 4 minutes per document.

## Direction of disagreement

- **AI-specific language is not overstated.** The human coder tagged 54 cells S; the dataset has 62.
- **Generic clauses are under-coded in the dataset.** The human coder found 193 cells present against the dataset's 163. The most common disagreement is human G where the dataset has A.
- **B10 accounts for the largest share of AI-specific disagreements** (8 of 24 cells). This is the boundary between a generic submissions licence and training on AI inputs, which suggests a rule-boundary issue rather than random error.
- **Binding disagreements mostly run one way.** Three of the four are documents the dataset classes as not reaching the AI feature that the human coder read as binding.

## Limitations

- The coder is the paper's author, not an independent second coder.
- Partial sample: 30 of 53 documents. Stratum-weighted κ is not yet estimable.
- The comparison is against the dataset before adjudication or any proposed corrections.
- The binding and B1 κ rest on 30 documents and have wide intervals.

## Files

- `human-coder-codings.csv` holds the human codes for positions 1–30.
