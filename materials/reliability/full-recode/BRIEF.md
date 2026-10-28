# Independent blind coder: brief (v2 validation sample, October 2026)

## Your role
You are an independent coder in a reliability check on a research dataset. The dataset records how U.S. consumer-facing companies allocate liability for their own customer-facing AI features in their terms. Another coder has already coded these documents. You code them **blind**, from the document text and one instrument only, so agreement can be measured with Cohen's kappa. If you see the other coder's work, the measurement is worthless. That is the one unbreakable rule.

## What you may open
Only files inside `input/` (in this folder), which contains:
- `CODING-MANUAL.md`: your sole instrument. It was frozen on 16 October 2026 (SHA-256 `22ffcd42cc8f1a2b936f3992368691a599b41fafd1bc5b290531d5381975488f`). Do not edit it.
- `BRIEF.md` (this file).
- `texts/NN_DOCID.txt`: the documents. Each one starts with a short header giving company, AI feature name and type, document type and URL. Below the `=====` line is the document text.

Open nothing outside this folder, and no other batch's output in `out/`. Do not use the web. If you think you need anything else, you don't: code what the text says and log the uncertainty.

## Method
1. Read `CODING-MANUAL.md` in full first, especially §§3, 5, 6, 7, 8 and 11.
2. For each assigned document, read the **whole text**. Long documents must be read in chunks until you reach the end. Searching may help you navigate, but a code may never rest on a search hit alone. `A` (absent) is allowed only after the whole document has been read.
3. Code the **document as a whole**, in the context of the named AI feature. (Exception: where the header note says only one instrument is shown, code that instrument.)

## Fields to record (one row per document)

**binding_status**: exactly one of the following (the manual's §3.3 and §8.2 discuss the idea; these are the category definitions):
- `governs-ai-expressly`: a contract whose scope names the AI, chat or assistant, or says AI features are part of the Services.
- `governs-surface`: a contract governing the website, app or service where the AI sits, without naming the AI.
- `governs-surface-partial`: a contract that reaches only part of the AI's channels (e.g. the website chat but not the phone assistant).
- `adjacent-not-governing`: a contract for a different relationship (contract of carriage, loyalty terms) that reaches the AI only indirectly.
- `no-reach`: its own scope excludes the surface where the AI runs.
- `notice-not-contract`: a notice the customer is told about, not asked to accept (privacy notices).
- `in-flow-microcopy`: text shown inside the AI interaction.
- `info-not-terms`: a help, FAQ or informational page.

**B1 … B11**: each is exactly one of:
- `S`: AI-specific (manual §5);
- `G`: a generic clause that reaches the AI;
- `A`: absent after a full read;
- `U`: untested, used only if part of the document could not be read.

Apply the manual's v1.1 rules for generic B3, generic B4 and restrictive B5 uniformly.

**names_ai**: `brand` (uses the marketed feature name), `category` (names AI only by category, e.g. "AI Tools", "chatbot"), or `none`.

**b4_register**: `directive`, `hedged` or `n/a`.

**special_flags**: any of `near-B1`, `channel-limitation`, `PROTO-B1`, `compelled-disclosure`, `orphan-document`, separated by `;`. Blank if none.

**trigger_quotes**: for every S or G code, a very short operative phrase (a few words) that justifies it, code-prefixed and `;`-separated, e.g. `B2: not liable for indirect damages; B6: AS IS`. Never a full sentence or paragraph.

**notes**: every close call, in prose.

## Output
Write two files to `out/` (create the folder if needed):
1. `batch-K.csv` (K = your batch number) with exactly this header, UTF-8, standard CSV quoting:
   `position,doc_id,company,binding_status,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,names_ai,b4_register,special_flags,trigger_quotes,notes`
2. `log-K.md`, containing:
   - a one-paragraph method statement confirming you coded blind, opened only the permitted files, and read every document in full (or saying exactly what you could not read);
   - one short entry per document: what it governs, the codes and why, and any close call;
   - a closing section, "Manual issues", listing every place the manual was ambiguous or silent and how you resolved it.

Code from the clause text, not from what you know about the company. A silent document is a finding: record it as silent and do not invent codes.
