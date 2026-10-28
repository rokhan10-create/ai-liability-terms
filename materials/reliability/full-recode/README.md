# Full-corpus GPT recode

This is the second, independent LLM coding behind the between-coder agreement in paper §2.3. GPT coded 264 documents (133 firms) blind, using the frozen coding manual and the same cleaned texts. It never saw the dataset's codes.

| Measure (pre-adjudication) | κ | % agree | n |
|---|---|---|---|
| AI-specific tag (S vs not S), all cells | 0.85 | 96.9% | 2,904 cells |
| Clause presence, all cells | 0.79 | 90.1% | 2,904 cells |
| Incorporation (binding vs not) | 0.90 | 95.1% | 264 docs |

**Coverage.** The paper's corpus has 270 documents. The 6 legal-hub index pages were not recoded, because they hold links rather than terms. Those pages carry no AI-specific codes.

**Coder setups.** Two GPT setups were used. 144 documents went through Codex (batches 01–05 and 11) and 120 through ChatGPT chat (chats 01–29, one document per reply). Results are reported for each setup separately in `RESULTS-full.md`, and they agree with the dataset almost identically (AI-specific κ 0.85 Codex, 0.84 ChatGPT). The Codex half is ordered alphabetically by firm, not randomly.

**Repeat coding.** 30 documents were coded by both setups (`retest_codex06.csv`). Between the setups, AI-specific κ is 0.96 and presence κ is 0.96.

## Files

| File | What it is |
|---|---|
| `gpt-full-sheet.csv` | GPT's codes for all 264 documents, one row each. `setup` and `source` give the coder setup and batch. |
| `retest_codex06.csv` | Codex batch 06 codes for the 30 repeat-coded documents. |
| `RESULTS-full.md` | Agreement overall, by setup and by clause family, and every AI-specific disagreement (the adjudication list). |
| `BRIEF.md` | The coder brief given with each batch. |
| `CHATGPT-PROMPT.md` | The prompt used for each ChatGPT chat. |

The scripts are in `scripts/reliability/`. `build_full_sheet.py` selects the documents, `merge_full.py` merges the batch outputs into `gpt-full-sheet.csv`, and `score_full.py` writes `RESULTS-full.md`. The raw per-batch files are not included, since `gpt-full-sheet.csv` holds their merged content.
