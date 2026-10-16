# Independent Second-Coder Prompt — IRR Round 2

*Hand this entire file to a fresh agent that has NOT seen this project. It is the
complete brief. Round 1 of this exercise (Aug 2026) covered 20 documents across 3
verticals; this round expands the full-text corpus to ~51 documents across 4.*

---

## Where the files are

The project root is `.\`. Every path in this brief is
relative to that root — `CODING-MANUAL.md` sits in it, and the source documents are under
`mastersheet-sources\<vertical>\<company>\`. Read them directly from disk.

## Your role

You are an **independent second coder** for an inter-rater-reliability (IRR) pass on a
research dataset about how consumer-facing companies handle liability for their own
deployed AI features. Another coder has already coded this corpus. You will code it
**blind** — from the raw documents and one instrument only — so that agreement between
the two of you can be measured (Cohen's κ per clause code). Your value to this study is
entirely in your **independence**: if you peek at the other coder's work, the κ is
worthless. Treat that as the one unbreakable rule.

## Your sole instrument

Read and code against **`CODING-MANUAL.md`** (in the project root) and nothing else for
methodology. It is self-contained: it defines the eligibility gate (§3), the master
AI-specific-vs-generic judgment (§5), the B1–B11 codebook (§6), the sharp-edge
conventions (§7), locus/attachment (§8), assent (§9), fetch depth (§10), and the B2
register flag (§11). Apply it **exactly as written** — including any include/exclude
rules it already gives for B8, `near-B6`, `channel-limitation`, and boilerplate
enumeration. Do not import rules from memory or from other AI-ToS work; if the manual is
silent on something, decide it yourself from the clause text and **write the difficulty
into your log** rather than guessing at "house style."

## Blindness firewall — do NOT open any of these

These contain the other coder's judgments, extracts, or the reconciled dataset. Opening
any of them contaminates the IRR:

- `MASTER-source-archive.md` (the primary coder's per-document extracts + coder notes)
- `documents.csv`, `CODEBOOK-unified-dataset.md`, `coverage-matrix.csv`
- `analysis/` (firm-level codings, results, drafts) and `analysis/firm-level-codings.csv`
- `irr/` round-1 outputs — `coder2-codings.csv`, `coder2-log.md`, `IRR-report.md`
- `GAPS-REGISTER.md`, `gaps-register.csv`, `retrieval-queue.csv`, the per-vertical
  `*-governing-terms.csv` files, and any `*-explorer.html`
- Any file named `*CAPTURE-NOTE*`, `*FINDING*`, `*README*`, `*.md` sitting next to a
  source that reads as a coder's note, and any bracketed `[B#: …]` annotations embedded
  inside a capture (the American and United captures contain these — **ignore the
  annotations and code only the operative clause prose**).

You may read **only** `CODING-MANUAL.md` and the source files listed below.

## Corpus to code (~51 documents, 4 verticals)

Preserved full-text sources only. The 8 newer verticals (edtech, healthcare,
hospitality, insurance, investing, real-estate, telecom, travel-ota) are **excluded from
this round** because only curated extracts exist for them, which would break blindness.

Code every file below. For each, first run the **§3 eligibility gate** and record the
result even when the document gates out (e.g. a contract of carriage that does not govern
the AI feature is still a row: `governs_ai: no`, no B-codes). Files ending `_RAW.html`
are byte-for-byte duplicates of their `.txt`/`.pdf` sibling — **skip the RAW files.**

**airlines/**
- alaska-hawaiian: `AlaskaWebTOU.txt`, `alaska_contract-of-carriage_ENGLISH.pdf`, `alaska_inspires-destination-search-page.txt`, `alaska_privacy-notice_2026-08-19.pdf`
- american: `american_platform-terms-conditions.txt`, `AmericanPrivacyPolicy.txt`
- delta: `delta_ai-terms-of-use.txt`, `delta_site-terms-of-use.txt`, `delta_privacy-policy.txt`
- frontier: `frontier_terms-of-use.txt`, `frontier_privacy-policy.txt`, `frontier_contract-of-carriage_ENGLISH.pdf`, `frontier_legal-hub-index.txt`
- united: `united_legal-terms-conditions-notices.txt`, `UnitedContractOfCarriage.txt`, `UnitedPrivacyPolicy.txt`

**banking/**
- capital-one: `capitalone_terms-and-conditions.txt`, `capitalone_digital-disclosures.txt`, `capitalone_gai-transparency-disclosure.txt`, `capitalone_privacy-policy.txt` (or `capitalone_online-privacy-policy-may2026.pdf`)
- dave: `dave_terms-of-service.txt`, `dave_privacy-policy.txt`
- wells-fargo: `wellsfargo_general-terms-of-use.txt`, `wellsfargo_online-access-agreement.txt`, `wellsfargo_consumer-privacy-notice.pdf`

**food-delivery/**
- doordash: `doordash_consumer-terms-JUL2026.txt`, `doordash_ai-grocery-assistant-help-article.txt`
- gopuff: `gopuff_terms-and-conditions.txt`, `gopuff_us-privacy-notice.txt`
- instacart: `instacart_terms-of-service.txt`, `instacart_privacy-policy.txt`, `instacart_TYPE4_cart-assistant-help.txt`, `instacart_TYPE4_ask-questions-about-food-search.txt`
- ubereats: `uber_general-terms-of-use-US.txt`, `uber_privacy-notice.txt`, `uber_generative-ai-features-at-uber.txt`

**retail/**
- amazon: `amazon_conditions-of-use.txt`, `amazon_privacy-notice.txt`, `amazon_TYPE3_generative-ai-development-disclosure.txt`
- home-depot: `HomeDepotTOS.txt`, `homedepot_privacy-and-security-statement.txt`, `homedepot_TYPE4_magic-apron-assistant-surface.txt`
- lowes: `lowes_terms-conditions-of-use.txt`, `lowes_customer-privacy-statement.pdf`
- target: `TargetPrivacyPolicy.txt`
- walmart: `walmart_terms-of-use_S16J.txt`, `walmart_privacy-notice.txt`

All paths are under `mastersheet-sources/<vertical>/<company>/`.

## Capture-quality rules (learned in round 1 — apply generically)

Some `.txt` captures are **not the real document body**. Before coding, sanity-check each
file's actual content:
- A very small `.txt` (a few hundred bytes) that reads as a browser/bot challenge, a
  cookie wall, or a landing page **is not the document**. Where a `.pdf` sibling exists,
  read the PDF instead. Where no clean capture exists, code
  `fetch_depth: referenced-not-located`, leave B-codes empty, and **do not record
  confirmed absence** — an unread document is a gap, not a "no."
- Read PDFs in full, including any pages a terminal display truncates.
- A help-center article or in-product AI page (the `TYPE3`/`TYPE4` and Uber GenAI files)
  is a real coding surface for microcopy/say-do, but check the §8 attachment question:
  is it incorporated into binding terms, or merely informational? Record that honestly.

## What to produce

Two files, written to `irr/`:

### 1. `irr/coder2-codings-round2.csv`

One row per document, this exact header (matches the round-1 schema so κ can be computed
cell-for-cell):

```
company,ai_feature,ai_vector,document_title,document_type,governs_ai,names_ai_feature,fetch_depth,assent_mechanism,clause_codes_present,ai_specific_codes,b2_register,special_flags,locus,attachment,trigger_quotes,coder_uncertainty
```

- `clause_codes_present` — every B-code present, `;`-separated (e.g. `B1;B4;B5;B7`).
- `ai_specific_codes` — the subset that is **AI-specific** per §5, not merely
  generic-reaching. This split is the study's core measurement — get it right per §5.
- `governs_ai` — yes / no / contested (from the §3 gate).
- `names_ai_feature` — yes / partially / no (does the text name the marketed feature?).
- `b2_register` — directive / hedged / n/a (§11).
- `special_flags` — `orphan-document`, `near-B6`, `channel-limitation`,
  `AI-content-disclosure`, `compelled-disclosure`, etc., per the manual.
- `locus` — the §8.1 spectrum value (1–5). `attachment` — §8.2 (attached / orphaned /
  contested / none).
- `assent_mechanism` — clickwrap / browsewrap / contested / none (§9).
- `trigger_quotes` — the **short** operative phrase behind each code (a few words each,
  `;`-separated, code-prefixed). Quote sparingly — enough to justify the code, never a
  paragraph.
- `coder_uncertainty` — every close call, in prose. This is where adjudication happens.

### 2. `irr/coder2-log-round2.md`

- A one-paragraph method statement confirming you coded blind, naming the sole instrument
  and stating which files you excluded/couldn't read and why.
- One short entry per document: what it governs, which codes and why, and any close call.
- A closing **"Manual issues for adjudication"** section: every place the instrument was
  ambiguous, silent, or self-contradictory, and how you resolved it. (Round 1 surfaced a
  real B8 defect this way — this section is high-value, don't skip it.)

## Rules of engagement

- Code **from the clause text**, not from the document's reputation or the feature's
  marketing. A silent document is a finding; record it as silent, don't invent codes.
- Apply §5's boilerplate/enumeration rule **uniformly across every document** — do not
  enumerate generic codes richly on one document and skip them on another; inconsistent
  enumeration was the single largest source of spurious disagreement in round 1.
- When the manual and your reading genuinely conflict, follow the manual and log the
  conflict. Do not "fix" the manual.
- Do not open the firewall files. If you think you need one to code a document, you don't
  — code what the source says and log the uncertainty instead.
