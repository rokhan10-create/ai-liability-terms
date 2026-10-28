# Full-corpus GPT recode vs dataset

## Summary (2026-10-19)
- **Coverage.** All 264 coded documents (133 firms) were re-coded blind by a GPT coder from the frozen manual and the same cleaned texts. 144 were coded in Codex (batches 01–05, 11) and 120 in ChatGPT chat (chats 01–29, one document per reply). For every document, the coder's log either quotes the document's real last line (all ChatGPT documents and Codex batch 11) or lists headings that run to the end of the text (checked automatically, with flagged cases checked by hand).
- **Agreement with the dataset (pre-adjudication).**
  - AI-specific tag: κ 0.85 (96.9% of 2,904 cells).
  - Presence: κ 0.79 (90.1%).
  - Binding vs not binding: κ 0.90 (95.1%).
  - The two GPT setups agree with the dataset almost identically (AI-specific κ 0.85 Codex, 0.84 ChatGPT).
- **Repeat coding.** 30 documents were coded by both GPT setups. Between the two setups: AI-specific κ 0.96, presence κ 0.96.
- **Headline robustness.** Firms with no AI-specific clause in any incorporated document:
  - 77 of 133 using the dataset's codes;
  - 77 of 133 using GPT's codes with the dataset's binding calls;
  - 76 of 133 using GPT's codes and binding calls.
  - Three firms move out of the silent group (Frontier, KOA, Metropolis) and two move in (Cox, Publix).
- **Where disagreement concentrates** (from the per-family table below):
  - **B1, generic mispricing clauses.** The dataset codes 46 generic "we may cancel mispriced orders" clauses as B1 = G. GPT never codes a generic B1. On AI-specific B1 the two agree on 262 of 264 documents.
  - **B11.** The dataset codes 31 documents with ADM disclosures; GPT codes 5. GPT applies the manual's "same customer-facing system" test strictly and does not count statements denying significant-effect profiling.
  - **B10.** The dataset codes 81 AI-specific; GPT codes 56. GPT separates recording or "improving services" from express AI-model training.
  - **B8.** The dataset codes 24 AI-specific; GPT codes 14. This is the over-application pattern found in round 1: a vendor or agent mentioned near AI text gets coded S.
  - **These four are manual-boundary questions, not reading errors.** Each needs a v1.2 rule. The 90 AI-specific disagreements listed at the end are the adjudication set.
- **Method caveats to disclose.**
  - Two GPT interfaces were used.
  - Codex batches 04–05 used parallel sub-coders on Codex's own initiative.
  - Three ChatGPT documents were redone after the chat lost its place or misapplied the binding rule (M-01, NRDY-01, LUV-02), and chat-28's last three documents were resumed in a fresh chat after a tool failure. Every redo was verified by its quoted last line.
  - The prompt told coders to code clause families even in documents that do not govern the AI. This replaces manual §3 and matches the dataset's practice in 22 of 23 no-reach and adjacent documents (CI-02 is the exception).


Documents: 264 (144 Codex, 120 ChatGPT). Pre-adjudication. Dataset `na` cells are treated as A.

AI-specific disagreements to adjudicate: 90 cells (listed at the end).
| Setup | Measure | κ | n | % agree |
|---|---|---|---|---|
| All | AI-specific tag (S vs not), all cells | 0.85 | 2904 | 96.9% |
| All | Presence, all cells | 0.79 | 2904 | 90.1% |
| All | B1, AI-specific (S vs not) | 0.72 | 264 | 98.9% |
| All | Binding vs not binding | 0.90 | 264 | 95.1% |
| All | Binding, exact category | 0.84 | 264 | 87.1% |
| Codex | AI-specific tag (S vs not), all cells | 0.85 | 1584 | 96.8% |
| Codex | Presence, all cells | 0.77 | 1584 | 89.1% |
| Codex | B1, AI-specific (S vs not) | 1.00 | 144 | 100.0% |
| Codex | Binding vs not binding | 0.90 | 144 | 95.1% |
| Codex | Binding, exact category | 0.85 | 144 | 88.2% |
| ChatGPT | AI-specific tag (S vs not), all cells | 0.84 | 1320 | 97.0% |
| ChatGPT | Presence, all cells | 0.81 | 1320 | 91.3% |
| ChatGPT | B1, AI-specific (S vs not) | 0.56 | 120 | 97.5% |
| ChatGPT | Binding vs not binding | 0.90 | 120 | 95.0% |
| ChatGPT | Binding, exact category | 0.82 | 120 | 85.8% |

## Per clause family (all 264 documents)

| Family | κ S-tag | κ presence | % agree presence | dataset S | GPT S | dataset present | GPT present |
|---|---|---|---|---|---|---|---|
| B1 | 0.72 | 0.10 | 81.4% | 5 | 6 | 51 | 6 |
| B2 | 0.77 | 0.93 | 96.6% | 25 | 18 | 169 | 174 |
| B3 | 0.93 | 0.77 | 89.0% | 33 | 33 | 95 | 108 |
| B4 | 0.97 | 0.84 | 92.4% | 59 | 58 | 107 | 97 |
| B5 | 0.78 | 0.76 | 96.6% | 20 | 20 | 21 | 20 |
| B6 | 0.91 | 0.78 | 90.9% | 67 | 66 | 180 | 198 |
| B7 | 0.89 | 0.95 | 97.7% | 4 | 5 | 126 | 132 |
| B8 | 0.72 | 0.69 | 86.4% | 24 | 14 | 167 | 185 |
| B9 | 0.93 | 0.93 | 98.9% | 26 | 23 | 26 | 23 |
| B10 | 0.76 | 0.43 | 73.9% | 81 | 56 | 186 | 161 |
| B11 | -0.03 | 0.02 | 87.1% | 10 | 5 | 31 | 5 |

## B1 cross-tab (dataset → GPT)

| dataset | GPT | n |
|---|---|---|
| A | A | 211 |
| A | S | 2 |
| G | A | 46 |
| S | A | 1 |
| S | S | 4 |

## Repeat coding: Codex batch 06 vs ChatGPT, same documents

30 documents coded independently by both GPT setups. AI-specific tag κ 0.96 (99.1%); presence κ 0.96 (98.2%).

## AI-specific disagreements (for adjudication)

| doc_id | company | code | dataset | GPT | GPT source |
|---|---|---|---|---|---|
| ANF-01 | Abercrombie & Fitch | B2 | S | G | codex batch-01 |
| ACI-04 | Albertsons Companies | B11 | A | S | codex batch-01 |
| AAL-01 | American | B8 | S | G | codex batch-02 |
| AEO-01 | American Eagle Outfitters | B2 | S | G | codex batch-02 |
| AEO-01 | American Eagle Outfitters | B8 | S | G | codex batch-02 |
| CAR-02 | Avis Budget Group | B11 | S | A | codex batch-02 |
| BBY-01 | Best Buy | B8 | S | G | codex batch-02 |
| BJS-01 | BJ's Wholesale Club | B10 | S | G | codex batch-02 |
| XYZ-01 | Block (Cash App) | B8 | S | G | codex batch-02 |
| BOB-01 | Bob's Discount Furniture | B11 | S | A | codex batch-02 |
| BKG-02 | Booking.com | B11 | A | S | codex batch-03 |
| KMX-01 | CarMax | B7 | G | S | codex batch-03 |
| CHM-02 | Chime | B10 | S | A | codex batch-03 |
| COUR-01 | Coursera | B2 | S | G | codex batch-03 |
| COUR-01 | Coursera | B10 | S | G | codex batch-03 |
| COX-01 | Cox Communications | B11 | S | A | codex batch-04 |
| DPZ-01 | Domino's | B10 | S | G | codex batch-04 |
| DD-01 | DoorDash | B6 | S | G | codex batch-04 |
| EBAY-02 | eBay | B11 | S | A | codex batch-04 |
| EXC-01 | Exelon | B10 | S | A | codex batch-04 |
| EXP-02 | Expedia | B3 | A | S | codex batch-04 |
| EXP-02 | Expedia | B5 | A | S | codex batch-04 |
| EXP-02 | Expedia | B10 | S | A | codex batch-04 |
| EXP-02 | Expedia | B11 | S | A | codex batch-04 |
| FID-01 | Fidelity Investments | B5 | A | S | codex batch-05 |
| FID-01 | Fidelity Investments | B6 | S | G | codex batch-05 |
| FRO-02 | Frontier | B2 | S | A | codex batch-05 |
| FRO-02 | Frontier | B10 | S | A | codex batch-05 |
| FRO-02 | Frontier | B11 | S | A | codex batch-05 |
| GEN-01 | Gen Digital | B8 | S | A | codex batch-05 |
| GE-02 | Giant Eagle | B10 | S | A | codex batch-05 |
| GRY-03 | Greystar | B10 | S | A | codex batch-05 |
| GRY-03 | Greystar | B11 | A | S | codex batch-05 |
| HRB-01 | H&R Block | B10 | S | A | codex batch-05 |
| HRB-01 | H&R Block | B11 | S | A | codex batch-05 |
| HIL-01 | Hilton | B2 | S | G | codex batch-05 |
| HIM-01 | Hims & Hers | B5 | S | A | codex batch-05 |
| HIM-01 | Hims & Hers | B9 | S | A | codex batch-05 |
| HIM-03 | Hims & Hers | B5 | A | S | codex batch-05 |
| HD-01 | Home Depot | B6 | S | G | codex batch-05 |
| HD-02 | Home Depot | B6 | A | S | codex batch-05 |
| HD-06 | Home Depot | B6 | S | G | codex batch-05 |
| INS-01 | Instacart | B8 | S | G | codex batch-05 |
| INS-03 | Instacart | B10 | S | A | codex batch-05 |
| INTU-01 | Intuit | B10 | S | G | codex batch-05 |
| KOA-01 | Kampgrounds of America | B6 | G | S | chatgpt chat-01 |
| KOA-02 | Kampgrounds of America | B10 | S | A | chatgpt chat-01 |
| KD-04 | Kinney Drugs | B10 | S | A | chatgpt chat-02 |
| LH-01 | Labcorp | B8 | S | G | chatgpt chat-02 |
| LH-01 | Labcorp | B9 | S | A | chatgpt chat-02 |
| LZ-04 | LegalZoom | B4 | A | S | chatgpt chat-02 |
| LTH-01 | Life Time Group Holdings | B2 | S | G | chatgpt chat-02 |
| MAR-02 | Marriott | B2 | S | G | chatgpt chat-04 |
| MAR-03 | Marriott | B11 | S | A | chatgpt chat-04 |
| MTCH-01 | Match Group | B5 | S | A | chatgpt chat-05 |
| MTCH-02 | Match Group | B3 | G | S | chatgpt chat-05 |
| MTCH-02 | Match Group | B5 | S | A | chatgpt chat-05 |
| MET-03 | MetLife | B10 | S | A | chatgpt chat-06 |
| MET-P-01 | Metropolis Technologies | B2 | G | S | chatgpt chat-06 |
| MET-P-01 | Metropolis Technologies | B6 | G | S | chatgpt chat-06 |
| PUB-01 | Publix | B10 | S | G | chatgpt chat-11 |
| RBLX-01 | Roblox | B8 | S | G | chatgpt chat-12 |
| RBLX-01 | Roblox | B11 | S | A | chatgpt chat-12 |
| SNAP-01 | Snap | B3 | S | A | chatgpt chat-14 |
| SNAP-01 | Snap | B8 | S | G | chatgpt chat-14 |
| TGT-01 | Target | B4 | S | A | chatgpt chat-16 |
| TGT-01 | Target | B8 | S | G | chatgpt chat-16 |
| CI-01 | The Cigna Group | B5 | S | A | chatgpt chat-16 |
| TRP-01 | Tripadvisor | B1 | S | A | chatgpt chat-18 |
| UBR-03 | Uber Eats | B10 | S | G | codex batch-11 |
| ULTA-01 | Ulta Beauty | B3 | S | A | codex batch-11 |
| ULTA-01 | Ulta Beauty | B10 | S | G | codex batch-11 |
| ULTA-02 | Ulta Beauty | B5 | A | S | codex batch-11 |
| ULTA-03 | Ulta Beauty | B2 | S | G | codex batch-11 |
| ULTA-03 | Ulta Beauty | B11 | A | S | codex batch-11 |
| UAL-03 | United | B10 | S | A | chatgpt chat-24 |
| UPBD-01 | Upbound Group | B10 | S | A | chatgpt chat-24 |
| UPBD-01 | Upbound Group | B11 | G | S | chatgpt chat-24 |
| VGD-01 | Vanguard | B1 | A | S | chatgpt chat-25 |
| VGD-03 | Vanguard | B1 | A | S | chatgpt chat-25 |
| VZ-01 | Verizon | B4 | S | A | chatgpt chat-25 |
| VZ-02 | Verizon | B10 | S | A | chatgpt chat-26 |
| WMT-02 | Walmart | B6 | A | S | chatgpt chat-27 |
| W-01 | Wayfair | B9 | S | A | chatgpt chat-27 |
| WFC-01 | Wells Fargo | B10 | S | A | chatgpt chat-28 |
| WFC-02 | Wells Fargo | B6 | S | G | chatgpt chat-28 |
| WFC-02 | Wells Fargo | B10 | S | G | chatgpt chat-28 |
| WSM-01 | Williams-Sonoma | B10 | S | G | chatgpt chat-28 |
| WSM-01 | Williams-Sonoma | B11 | S | A | chatgpt chat-28 |
| ZG-02 | Zillow | B10 | S | A | chatgpt chat-29 |
