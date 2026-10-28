# Disclosed, Disclaimed, or Absolved

Project page, dataset and materials for *Disclosed, Disclaimed, or Absolved: A Cross-Sector Audit of AI-Liability Terms at the Largest U.S. Consumer-Facing Firms*. The paper audits how 133 of the largest U.S. consumer-facing firms address their customer-facing AI assistants in 270 contractual and disclosure documents.

**Live page:** https://rokhan10-create.github.io/ai-liability-terms/

Rohail Khan (Independent Researcher), Zara Liaqat (Wilfrid Laurier University) and Hassan Khan (University of Guelph). Working paper, 2026.

## Data and materials

The materials supporting the paper are in [`materials/`](materials/) (data frozen 14 October 2026). See [`materials/README.md`](materials/README.md) for the file guide and the paper's numbers. They contain:

- **Dataset.** One record per document, with incorporation status, assent mechanism, where the AI language sits, and the code for each of the eleven clause families, plus the firm-level taxonomy.
- **Document register.** For every document: URL, retrieval date, stated effective date, capture method, SHA-256 hash, the coding-relevant extract and the coder's note.
- **November 2022 baselines.** The archived snapshot used for each comparison, the reason any document has none, and the sentence-level comparison output.
- **Screening log.** Every firm screened, with its industry rank, revenue source, decision, reason and evidence link.
- **Coding manual and codebook.**
- **Analysis scripts.** Sample construction, the archival comparison, the firm-level taxonomy, the segment comparisons and the figures.
- **Reliability data.** The second LLM coder's codes for the whole corpus and the human validation codes, with agreement reports.

The company documents themselves are copyrighted by the companies that publish them, so the repository gives each document's URL, archived-snapshot link and hash rather than its full text. Full captured texts are available to researchers on request.
