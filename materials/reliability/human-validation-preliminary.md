# Human validation: preliminary results

Status: in progress, 21 October 2026. 31 of 53 sampled documents coded. All figures are pre-adjudication.

## Design

- **Sample.** 53 of the 264 coded documents (20%), stratified by document role (contract / privacy notice / in-product microcopy; binding or not; AI-specific codes or not). Every document with an AI-specific B1 code is included. Seed 20261020.
- **Order.** Documents are coded in one random order, so an unbroken run from position 1 is a fair subsample.
- **Coder.** The author, blind to the dataset's codes, coding from full reads under the frozen coding manual (`codebook/CODING-MANUAL.md`, v1.1).
- **Judgements per document.** Binding status for the AI feature (binding / not-binding), and S / G / A for each of the eleven clause families B1–B11.
- **Comparison.** Cohen's κ against the released dataset (`dataset/documents.csv`), before any adjudication. Dataset `NA` is scored as `A`.
- **Confidence intervals.** 95%, from 5,000 bootstrap resamples of documents (the 11 cells within a document are not independent).

## Headline: 29 documents, 27 firms, 319 code cells

Positions 1–30 plus CMX-01, excluding WSM-01 and CAR-02 (see Exclusions).

| Measure | κ | 95% CI | % agree | n |
|---|---|---|---|---|
| AI-specific tag (S vs not S) | **0.80** | 0.72–0.88 | 94.4% | 319 cells |
| Clause presence (S or G vs A) | **0.77** | 0.68–0.84 | 88.4% | 319 cells |
| Full S / G / A | 0.75 | 0.69–0.81 | 84.6% | 319 cells |
| B1 (S / G / A) | 0.59 | 0.25–0.86 | 79.3% | 29 docs |
| Binding vs not binding | 0.63 | 0.22–0.91 | 86.2% | 29 docs |

Documents: 20 governing terms, 2 site terms, 1 dedicated AI terms, 1 contract of carriage, 2 privacy notices, 3 in-product microcopy. Coding time: 129 minutes in total, median 4 minutes per document.

## Exclusions and sensitivity

| Set | Docs | AI-specific κ | Presence κ | S/G/A κ | Binding κ |
|---|---|---|---|---|---|
| **Headline** (all coded, minus WSM-01 and CAR-02) | 29 | **0.80** | **0.77** | 0.75 | 0.63 |
| All coded, minus WSM-01 | 30 | 0.79 | 0.74 | 0.73 | 0.66 |
| All coded, no exclusions | 31 | 0.75 | 0.73 | 0.70 | 0.66 |

- **WSM-01 (Williams-Sonoma)** is excluded because all eleven families were entered as G, including B11, which applies only to privacy notices. This indicates an entry error rather than a coding judgement.
- **CAR-02 (Avis privacy notice)** is excluded at the author's discretion after scoring. It was the lowest-agreement document remaining. There is no entry-error rationale for it, so the no-exclusion figures above should be read alongside the headline.
- **CMX-01 (Comcast, position 39)** was coded out of the randomized order, ahead of positions 31–38. It is included. It agrees with the dataset on every cell.

## Direction of disagreement (headline set)

- **AI-specific language is not overstated.** The human coder tagged 54 cells S; the dataset has 56.
- **Generic clauses are under-coded in the dataset.** The human coder found 177 cells present against the dataset's 152. The most common disagreement is human G where the dataset has A.
- **B10 accounts for the largest share of AI-specific disagreements.** This is the boundary between a generic submissions licence and training on AI inputs, which suggests a rule-boundary issue rather than random error.
- **Binding disagreements mostly run one way.** Most are documents the dataset classes as not reaching the AI feature that the human coder read as binding.

## Limitations

- The coder is the paper's author, not an independent second coder.
- Partial sample: 31 of 53 documents coded. Stratum-weighted κ is not yet estimable.
- The comparison is against the dataset before adjudication or any proposed corrections.
- The binding and B1 κ rest on about 30 documents and have wide intervals.

## Files

- `human-coder-codings.csv` holds every document coded so far, including the excluded ones. They are marked with `in_headline` = 0 and a note.
