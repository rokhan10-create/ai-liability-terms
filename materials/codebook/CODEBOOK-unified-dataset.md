# Codebook — `documents.csv`

**What this file is.** The unified machine-readable dataset for the AI-ToS Liability project.
**One row = one document.** A company with five documents has five rows. It supersedes the four
per-vertical CSVs, which remain on disk as human-readable views.

**Scope:** 67 documents · 17 companies · 4 verticals (retail, airlines, food-delivery, banking) ·
compiled through 2026-08-29.

**Two files travel with it:**
- `mastersheet-sources/MANIFEST.csv` — every preserved file with its SHA-256
- `mastersheet-sources/_tools/Build-Explorer.ps1` — regenerates the HTML explorer from this CSV

---

# Part 1 — The 32 columns

## Identity (5)

### `doc_id`
Stable primary key. Format `{TICKER}-{NN}` — e.g. `WMT-01`, `DAL-04`. **Never reused and never
renumbered**, so a citation to `AAL-02` stays valid as rows are added. Tickers: WMT Walmart ·
AMZ Amazon · HD Home Depot · LOW Lowe's · TGT Target · DAL Delta · UAL United · AAL American ·
ALK Alaska · FRO Frontier · INS Instacart · UBR Uber Eats · DD DoorDash · GP Gopuff ·
WFC Wells Fargo · COF Capital One · DAV Dave.

### `vertical`
`retail` · `airlines` · `food-delivery` · `banking`

### `company`
Common name, consistent across all project files.

### `ai_feature`
The marketed consumer AI product the company deploys — e.g. `Sparky`, `Delta Concierge`,
`Magic Apron`. Repeated on every row for that company so the file filters cleanly.

### `ai_vector`
What kind of AI it is.

| Value | Meaning |
|---|---|
| `generative` | Produces text/recommendations; the customer reads the output |
| `generative-agentic` | Also **acts** — builds carts, transacts, or operates an account |
| `hybrid` | Mixed generative + rules-based (Frontier's Cognigy chat) |

## Document (5)

### `doc_type`
What kind of document this is. Aligned to the six-type search set in the acquisition protocol,
plus classes the protocol does not name but the corpus contains.

| Value | Meaning |
|---|---|
| `t1-governing-terms` | The governing product/service terms that reach the AI feature |
| `t2-site-terms` | Site terms of use, where distinct from t1 |
| `t3-dedicated-ai-doc` | A standalone AI document |
| `t4-in-product-microcopy` | The disclaimer actually shown during the AI interaction |
| `t6-marketing` | The company's own marketing/launch material — the "say" side |
| `t6-incident` | A documented customer-facing incident or accuracy investigation |
| `t6-regulatory` | A regulator-issued document bearing on the sector |
| `privacy-notice` | Privacy policy/notice. **Not a protocol type — but B11 lives here** |
| `contract-of-carriage` | Airline passenger contract |
| `legal-hub-index` | Index page enumerating a company's legal documents |
| `capture-note` | Project-authored provenance record where no verbatim capture was possible |

**Why there is no `t5`.** Protocol type 5 is the agentic-AI clause. In this corpus such clauses
always sit *inside* a t1 document rather than standing alone, so they are recorded by the `B5`
column on that document's row. Creating `t5` rows would duplicate documents.

### `doc_title`
Title as it appears on the document itself.

### `url`
Retrieval URL. `n-a` where no URL exists — app-only surfaces (Delta Concierge, Fargo,
Chat Concierge) genuinely have no addressable page.

### `effective_date`
ISO `YYYY-MM-DD`, or `not-stated`. **Always read together with `date_basis`.**

### `date_basis`
**How the date was established.** This column exists because every vintage-vs-launch claim in the
project depends on date quality, and the four bases are not equally good evidence.

| Value | Meaning | Strength |
|---|---|---|
| `stated` | An explicit effective/updated/revised date in the document | Strong — citable |
| `in-body-copyright` | Only a copyright year in the body text | Weak — a copyright year is not a revision date |
| `pdf-metadata` | From PDF file metadata, not the document text | Weak — reflects file creation, not the document |
| `reported-external` | From search metadata or press, **never verified in the document** | Weakest — verify before publishing |
| `not-stated` | No date anywhere | Record as unstated. **Never infer "old"** |

> Worked example: `ALK-02` (Alaska Contract of Carriage) carries `2026-05-26` with basis
> `reported-external`. That date came from search metadata and was not legible in the PDF's text
> layer. It should not appear in a published vintage claim until verified against the cover page.

## Retrieval and preservation (7)

### `status`
**The most consequential field in the file.** Three of these five values are *access states*, not
findings — and conflating them with `absent` is how false conclusions get made.

| Value | Meaning | Citable as evidence? |
|---|---|---|
| `held` | Preserved on disk | **Yes** |
| `absent` | Searched; established the document does not exist | **Yes — this is a finding** |
| `blocked` | Document exists; every retrieval route failed | **No** |
| `unpreserved` | Read and coded, but no file on disk | **No** |
| `not-sought` | Never searched; existence unknown | **No — never report as absence** |

### `fetch_depth`
How completely the document was read.

| Value | Meaning |
|---|---|
| `full-fetch` | Complete document retrieved directly |
| `full-fetch-browser` | Complete text via rendered DOM — faithful, but not byte-exact |
| `full-fetch-partial-verbatim` | Substantive contract captured verbatim; the remainder was keyword-scanned, verified zero-hit, and documented in a coverage statement inside the file |
| `snippet-only` | Search-result fragments only |
| `referenced-not-located` | Existence confirmed by cross-reference; content never retrieved |
| `structural-proxy` | A different jurisdiction's document used only to infer likely structure — **explicitly not evidence** |
| `n-a` | No retrieval attempted |

### `preservation`
What archival artefact actually exists.

| Value | Meaning |
|---|---|
| `raw-html` | Verbatim server response — the strongest copy |
| `pdf` | Binary preserved as served |
| `text-only` | Faithful text; no byte-exact copy, so a later re-fetch cannot be diffed against it |
| `none` | Nothing preserved |

### `capture_method`
`direct-fetch` · `direct-fetch-pdf` · `webfetch-pdf` · `browser-textContent` ·
`browser-textContent-accordion` · `browser-modal-click` · `user-supplied` · `app-only-no-url` · `n-a`

### `file` · `bytes` · `sha256`
Filename within `mastersheet-sources/{vertical}/{company}/`, size, and hash — all from
`MANIFEST.csv`. Empty for rows with no preserved file. The hash lets a future re-fetch be diffed
against exactly what was coded.

## Coding (14)

### `names_ai`
Does the document name the AI product?

| Value | Meaning |
|---|---|
| `brand` | Names the marketed product — "the Sparky AI shopping assistant", "Mylow" |
| `category` | Defines an AI class only — "AI Tools", "Generative AI Features", "AI Features" |
| `no` | No reference to the AI at all |
| `U` | Untested |

> This column carries a dataset-level finding: **no company names its AI in the instrument that
> allocates risk.** Two name it in a privacy notice (Walmart, Lowe's).

### `ai_language`
What *kind* of AI language the document contains.

| Value | Meaning |
|---|---|
| `ai-specific` | Language drafted for AI |
| `generic-reaching-ai` | A generic clause that reaches the AI only by construction |
| `compelled-disclosure` | Exists because a statute requires it — CA AB 2013, Brazil's LGPD. **Not liability drafting** |
| `disclosure-only` | Acknowledges AI without allocating any risk |
| `none` | No AI language |
| `n-a` | Non-coded document type (incidents, marketing, indexes) |

> `compelled-disclosure` is separated deliberately. Capital One, Amazon and American each contain
> AI or ADM text that exists *only* because a regulator demanded it. A keyword search scores them
> as AI-aware; none has an output-liability clause.

### `locus`
Where the AI liability language sits. Extends the project's five-point spectrum with two anomalous
types the corpus forced.

| Value | Meaning |
|---|---|
| `1` | Dedicated standalone AI terms (Delta, Uber) |
| `2` | Dedicated AI section inside general terms (Walmart §16.J, American §15, Instacart §5.2, Target) |
| `3` | Generic clause reaching a named AI feature (Wells Fargo, Uber ToU) |
| `4` | Microcopy-only, in-product (Alaska, Home Depot, Instacart help) |
| `5` | No consumer terms; operational control only |
| `anomalous-privacy-notice` | Operative AI language sits in a **privacy notice** — 5 companies |
| `anomalous-help-article` | Operative AI language sits in an unincorporated **help article** — DoorDash |
| `none` | No AI locus in this document |
| `n-a` | Non-coded document type |

### `B1`–`B11`
Eleven columns, one per clause family. **See Part 2.**

### `key_finding`
One-sentence analytical note: what this specific document contributes.

---

# Part 2 — The B-code system

Two things are easy to confuse, so they are stated separately.

## What B1–B11 *are*: the clause families

`B1` through `B11` are **eleven kinds of contractual provision** a company might use to shift AI
risk onto the consumer. They are the project's clause codebook, applied identically to every
document. Each column asks: *does this document contain a clause of this family, and if so, was it
written for AI?*

| Code | Clause family | What it does | Illustrative |
|---|---|---|---|
| **B1** | **Transaction-error non-honoring** | Refuses to be bound by what the AI stated | Walmart: AI pricing "does not constitute an offer to sell" |
| **B2** | Limitation of liability | Caps or excludes damages | American: USD 500 aggregate cap |
| **B3** | User-responsibility shift | Makes the *user* answerable for acting on output | Delta: "YOU — NOT DELTA — ARE RESPONSIBLE" |
| **B4** | Anti-reliance | Tells the user not to rely; to verify | Delta: "IT IS YOUR SOLE RESPONSIBILITY TO VERIFY THE OUTPUTS" |
| **B5** | Agentic-AI / user-assigned-agent | Governs an AI acting *for* the customer | Target's Agentic Commerce section |
| **B6** | Accuracy / no-warranty | States output may be wrong; provided "AS IS" | Delta: output "may contain inaccuracies" |
| **B7** | Indemnification | User indemnifies the company | Standard across the corpus |
| **B8** | Third-party source carve-out | Disclaims sources the output draws on | Delta names Sherpa and IATA |
| **B9** | Anti-jailbreak / no training on outputs | Stops *users* pointing AI at the company's content | American §6(n) |
| **B10** | Training on prompts / IP over inputs | Claims rights over what the user types or the AI produces | Instacart: "Instacart owns all AI-generated content" |
| **B11** | Automated-decision disclosure | Discloses automated decision-making; usually in a privacy notice | American, but **only under Brazil's LGPD** |

**B1 is the anti-*Moffatt* clause.** *Moffatt v. Air Canada* turned on a company being held to
what its chatbot said. B1 is the direct contractual answer. **Exactly one company in the corpus
has one: Walmart.**

## What S / G / A / U *are*: the values in those columns

Each B-column holds one of five values. They record **presence and kind**, not just presence.

| Value | Meaning | What it tells you |
|---|---|---|
| **`S`** | **AI-specific** — the clause was drafted for AI | Deliberate risk allocation. The company anticipated this |
| **`G`** | **Generic** — an ordinary clause that reaches the AI by construction | Protection may exist, but nobody drafted it for AI. This is the pre-AI contract doing double duty |
| **`A`** | **Absent** — a complete read established the clause is not there | **A finding.** Citable |
| **`U`** | **Untested** — not separately coded, or the document could not be read | **Not a finding.** Says nothing about the company |
| **`na`** | Not applicable to this document type | Incidents, marketing and index pages are not coded for clauses |

### The distinction that matters most: `A` vs `U`

- **`A` means we looked and it isn't there.**
- **`U` means nobody looked, or we couldn't.**

They look similar in a spreadsheet and mean opposite things. Collapsing them — counting `U` as
absence — manufactures findings that the evidence does not support. This is why the HTML explorer
renders `U` in **red**, more prominently than `A`.

### The distinction that matters second: `S` vs `G`

`S` and `G` both mean "a clause of this family exists." But:

- `S` shows the company **thought about AI** and wrote for it.
- `G` shows only that an old clause **might stretch** to cover AI if litigated.

Reporting them together as "clause present" erases the project's central question. Lowe's
`LOW-01` is `G` across the board: its warranty disclaimer ("NO OPINION, ADVICE OR STATEMENT BY
LOWE'S… SHALL CREATE ANY WARRANTY") would probably be argued to cover a Mylow misstatement — but
Lowe's never wrote a word about AI.

### Worked examples

| Row | Pattern | Reading |
|---|---|---|
| `WMT-01` | `S S S G G S S S S A A` | Nine clause families present, seven AI-specific — including the corpus's only B1. Deliberate, comprehensive AI drafting |
| `LOW-01` | `G A A G G G G G A A A` | Six families present, **none AI-specific**. Generic contract that might stretch |
| `DAL-01` | `S S S S S A S S S na A` | Eight AI-specific families. No B1 — Delta relies on anti-reliance instead of refusing to honour |
| `WMT-03` | `U U U U U U U U U U U` | Never captured. **Says nothing about Walmart's microcopy** |
| `TGT-01` | `U U S U U A U S U A S` | Agentic clause coded (B5 `S`); several families not separately coded (`U`). Partial coding, honestly marked |

---

# Part 3 — Known hazards

Six traps found the hard way. Each one nearly produced a false finding.

1. **`A` vs `U`.** Restated because it is the one that matters. Untested is not absence.

2. **`compelled-disclosure` is not AI-awareness.** Capital One's only AI text is a California
   AB 2013 training-data notice filed between credit-card boilerplate and the Ohio resident
   notice. Amazon's dedicated AI document is training-data transparency with zero output liability.

3. **B11 is jurisdiction-scoped.** Three companies disclose automated decision-making — Uber for
   **Quebec**, Gopuff for the **UK**, American for **Brazil**. None for US consumers. B11's
   scarcity in US documents is a finding about *US regulation*, not about firm practice.

4. **Substring keyword scans inflate counts.** A case-insensitive `"AI "` scan returned 21
   apparent hits in United's privacy policy; word-boundary `\bAI\b` returns **1**. Always use
   word boundaries.

5. **Disambiguate brand names.** Raw `Mylow` matching on Lowe's pages returns 300+ hits, ~99% of
   which are `MyLowes`, an unrelated loyalty programme. Use a negative lookahead: `Mylow(?!es)`.

6. **Hub pages mix documents.** `legal.gopuff.com` renders sidebar navigation for the UK,
   workforce and applicant notices alongside the US consumer notice — producing three phantom
   "automated decision" hits. Attribute every hit to a specific document before coding it.

**A seventh, specific to keyword scoring:** Home Depot's terms contain 11 instances of
"AI-generated" — every one is TCPA SMS consent boilerplate ("prerecorded, AI-generated, or
artificial messages"), repeated across five short codes. A keyword ranking would place Home Depot
among the most AI-aware contracts in the corpus. It is `none`.
