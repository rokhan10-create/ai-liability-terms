# ChatGPT coder prompt

Pasted into a fresh chat (memory off) with each chat-NN.zip, which held BRIEF.md, CODING-MANUAL.md and the document texts. NN is the zip number.


```
You are an independent blind coder. I've uploaded chat-NN.zip.

1. Unzip it with Python. Read BRIEF.md in full and follow it exactly. It is your complete brief. Ignore the folder paths it mentions: your files are the unzipped BRIEF.md, CODING-MANUAL.md and texts/.
2. Read CODING-MANUAL.md in full before coding anything.
3. Code every file in texts/, in filename order.

How to read:
- Read each document with Python by printing it in consecutive chunks (about 400 lines at a time) until you have printed its last line. Do not use file search or retrieval on these files, and do not read only selected passages.
- Never assign a code from a search hit alone, and code A only after you have printed and read the whole document.
- Before each new document, re-read sections 5, 6 and 7 of CODING-MANUAL.md.
- Do not use the web.

Rules:
- binding_status and B1–B11 are separate judgments. Code every clause family that appears in the text even when binding_status is adjacent-not-governing, no-reach, notice-not-contract, in-flow-microcopy or info-not-terms: S for AI-specific clauses, G for generic clauses. binding_status records whether the document reaches the AI, so do not code clauses A just because the document does not govern the AI. This replaces the manual's §3 instruction to "stop" when a document fails the governance gate. Use A only for a family that is truly absent from the text.
- Documents from the same company sit next to each other. Code each one on its own text.

Output:
- Build batch-NN.csv with exactly the header in BRIEF.md, one row per document. Build log-NN.md as BRIEF.md describes. In each log entry, also give "Headings read, first to last:" followed by the section headings separated by semicolons, and quote the document's last line.
- Give me both files as download links.
- Then reply with one line per document: doc_id, binding_status, B1–B11.
```

