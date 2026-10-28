# Inter-Rater Reliability Report — Round 2

**Date:** 2026-09-20 · **Coders:** coder-1 (primary, from `documents.csv`) vs. coder-2 (independent blind agent, `coder2-codings-round2.csv`) · **Instrument:** current `CODING-MANUAL.md` · **Unit:** document.

## Corpus

47 preserved full-text documents across 4 verticals (airlines, banking, food-delivery, retail). The 8 newer verticals are excluded (only curated extracts exist — blindness would be contaminated).

## Method

Cohen's kappa, presence/absence per code, per document. Coder-1 values are coder-1's own prior document-level codings in `documents.csv` (S=AI-specific, G=generic-reaching, A/na=absent, U=untested), NOT reconstructed from prose — this fixes round-1's largest defect. **Cells untested by either coder are pairwise-deleted** (round 1 counted them as absent, which floored kappa). `ai_specific` kappa scores the S-vs-not distinction (the study's core axis).

## Headline results

| Scope | Cohen's kappa | n cells | % agree |
|---|---|---|---|
| All B1-B11, presence | 0.758 | 479 | 91.0% |
| Signal codes (B2,B3,B6,B9,B11), presence | 0.885 | 225 | 97.8% |
| Boilerplate codes (B1,B4,B5,B7,B8), presence | 0.667 | 212 | 83.5% |
| AI-specific tag (S vs not), all codes | 0.802 | 479 | 96.5% |

## Per-code kappa (presence)

| Code | kappa | n | % agree | note |
|---|---|---|---|---|
| B1 | 0.720 | 43 | 86.0% |  |
| B2 | 0.933 | 45 | 97.8% |  |
| B3 | 0.808 | 45 | 95.6% |  |
| B4 | 0.858 | 43 | 93.0% |  |
| B5 | 0.795 | 42 | 90.5% |  |
| B6 | 0.656 | 45 | 97.8% |  |
| B7 | 0.335 | 40 | 65.0% |  |
| B8 | 0.615 | 44 | 81.8% |  |
| B9 | 1.000 | 45 | 100.0% |  |
| B10 | 0.364 | 42 | 92.9% |  |
| B11 | 0.789 | 45 | 97.8% |  |

## Per-code kappa (AI-specific S tag)

| Code | kappa | n | % agree | note |
|---|---|---|---|---|
| B1 | 0.932 | 43 | 97.7% |  |
| B2 | 1.000 | 45 | 100.0% |  |
| B3 | 0.808 | 45 | 95.6% |  |
| B4 | 0.788 | 43 | 97.7% |  |
| B5 | 0.656 | 42 | 97.6% |  |
| B6 | 1.000 | 45 | 100.0% |  |
| B7 | 0.553 | 40 | 90.0% |  |
| B8 | 0.542 | 44 | 93.2% |  |
| B9 | 0.877 | 45 | 97.8% |  |
| B10 | 0.364 | 42 | 92.9% |  |
| B11 | 0.789 | 45 | 97.8% |  |

## Disagreement ledger (presence; untested cells excluded)

| doc_id | company | document | coder1-only | coder2-only |
|---|---|---|---|---|
| ALK-01 | Alaska/Hawaiian | Legal — website terms of use | B8 | B2 |
| ALK-02 | Alaska/Hawaiian | Contract of Carriage | B1;B4;B5;B8 | - |
| AAL-03 | American Airlines | Privacy policy | B10 | - |
| DAL-02 | Delta Air Lines | Terms of Use | B8 | - |
| DAL-03 | Delta Air Lines | Privacy and Security | B7 | - |
| FRO-02 | Frontier Airlines | Privacy Notice | B4;B10 | - |
| UAL-01 | United Airlines | Terms, Conditions and Legal Notices for  | B8 | - |
| UAL-02 | United Airlines | Contract of Carriage | B1;B4;B5;B8 | - |
| UAL-03 | United Airlines | Global Privacy Policy | B7 | - |
| COF-04 | Capital One | Important Disclosures | - | B1;B8 |
| COF-02 | Capital One | Generative AI Development Disclosure | B7 | - |
| DAV-01 | Dave | Terms of Use | - | B7 |
| WFC-02 | Wells Fargo | General Terms of Use | B7 | - |
| WFC-01 | Wells Fargo | Online Access Agreement | B1;B5;B7;B8 | - |
| DD-01 | DoorDash | Consumer Terms and Conditions | - | B1;B7 |
| DD-02 | DoorDash | Meet Your New AI Assistant | B3 | - |
| UBR-03 | Uber | Uber Privacy Notice | B7 | - |
| UBR-02 | Uber | Generative AI Features at Uber | B7;B8 | - |
| AMZ-03 | Amazon | Amazon.com Privacy Notice | B7 | - |
| AMZ-02 | Amazon | Generative AI Development Disclosure | B7 | - |
| HD-03 | The Home Depot | Magic Apron assistant surface | B1 | - |
| LOW-01 | Lowe's | Terms and Conditions of Use | B6 | - |
| LOW-02 | Lowe's | Customer Privacy Statement | B7 | - |
| TGT-02 | Target | Target Privacy Policy | B7 | B3;B11 |
| WMT-01 | Walmart | Walmart.com Terms of Use | B5 | - |
| WMT-02 | Walmart | Walmart Customer Privacy Notice | B7 | B10 |
