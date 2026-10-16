# AI-ToS Liability — Coding Manual (v1.1)

**Purpose.** This is the standalone instrument a second coder uses to code company
documents *independently*, without reading the primary coder's archive entries first.
It consolidates the decision rules, boundary examples, and conventions that were
developed across the pilot corpus (QSR voice, retail shopping, airlines, food
delivery, banking). Every rule here is illustrated with a real example from the
corpus so that a boundary call can be checked against a decided case.

**How to use it.**
1. Read Sections 1–5 once, in full, before coding anything.
2. Code each document blind to the primary coder's `clause_codes_present` line and
   coder note. Code from the fetched source document (or preserved `.txt`/`RAW.html`
   under `mastersheet-sources/` or `previous-tos/`), not from the archive summary.
3. Fill one coding row per **document** (Section 4 schema).
4. When a call is genuinely ambiguous, code your best judgment AND flag it in the
   `coder_uncertainty` field. Do not consult the other coder before the adjudication
   session (Section 13) — the disagreement is the signal we are measuring.

> The single most important rule in this manual: **distinguish AI-specific language
> from a generic clause that merely happens to reach a named AI feature** (Section 5).
> Almost every hard call reduces to this.

---

## 1. What we are measuring

For each consumer-facing AI feature, we are coding **how the firm's governing
documents disclose the AI and allocate liability for its outputs** — and critically,
*whether the liability language is written for the AI or is generic boilerplate that
would apply to anything on the site.* We are NOT evaluating whether the firm is
"good" or "bad"; we are characterizing drafting posture on three axes (disclosure,
disclaimer, responsibility allocation).

The anchor fact pattern is *Moffatt v. Air Canada* (2024 BCCRT 149): a chatbot
misstated a policy, the customer relied, and the company was held liable. Throughout,
ask of each clause: **would this clause change the outcome in a Moffatt-type dispute?**
That question is what separates a decorative disclaimer from an operative one.

---

## 2. Unit of analysis and workflow

- **Unit of coding = one document**, coded in the context of a single company's AI
  feature. A company with three relevant documents (e.g. site ToU + dedicated AI
  Terms + privacy notice) produces three rows.
- **Company-level roll-ups** (locus, overall posture, taxonomy placement) are derived
  *after* document coding, in a separate pass — do not pre-judge them while coding a
  single document.
- Code only what is **in the document text**. Do not import facts from press coverage
  into the clause codes. (Press/marketing is captured separately, for the say–do gap,
  in the `ai_named_in_marketing` context field — not in the B-codes.)

---

## 3. Eligibility gate (apply before coding)

Answer these three gates first. If a document fails a gate, record why and stop.

### 3.1 Is the AI feature in scope?
**In scope:** a consumer-facing AI *service* — something a customer directly talks to
(chat, voice), that answers them, or that acts on their behalf (agentic). Examples in
corpus: Delta Concierge, Walmart Sparky, Ask Instacart, Wells Fargo Fargo, Frontier
chat, Wendy's/Domino's/Fazoli's drive-thru voice ordering.

**Out of scope:** AI used purely internally (credit scoring, fraud detection, ad
targeting, backend automation) *unless the same system is also customer-facing.*
Also out of scope: an employee-/associate-facing assistant. Example: Lowe's "Mylow
Companion" (associate-facing) is OUT; Lowe's "Mylow" (customer-facing) is IN.

> Eligibility is normally pre-confirmed upstream — do not re-litigate it per company.
> Flag only if you find a clear scope error.

### 3.2 Whose document is it? (the vendor-exclusion rule)
Code **only the deploying company's own consumer-facing documents.** A third-party AI
vendor's terms are a B2B agreement between the vendor and the company; the end
consumer never saw or agreed to them, so they are **excluded as evidence** and are
NOT coded.

- Excluded vendor terms seen in corpus: Cognigy (Frontier), xAI/Grok (Gopuff),
  ConverseNow (Fazoli's), Momos (Burger King "Alfie"), SoundHound.
- A named third-party *source* inside the company's own document (e.g. Delta naming
  Sherpa/IATA as output sources) is different — that is the company's own text and IS
  coded (as B8).

### 3.3 Does this document actually govern the AI feature?
A document sitting "near" the AI is not automatically the governing one. Determine
whether it (a) forms the contract and (b) reaches the AI feature. This is the
`attachment` judgment (Section 8.2). Do not assume a dedicated AI page is contractual —
check for incorporation language ("subject to", "governed by", "incorporated by
reference") versus mere signposting ("for more information, please visit"). Example:
Uber's ToU points to a separate AI page with "For more information, please visit" —
signposting, not incorporation → binding status is *contested*, not assumed.

---

## 4. The coding sheet (fields to record per document)

| Field | Values / format |
|---|---|
| `company` | name |
| `ai_feature` | marketed name if any (e.g. "Sparky", "Concierge") |
| `ai_vector` | generative / voice / agentic / hybrid / rules |
| `document_title` | exact |
| `document_type` | site ToU / product-service terms / dedicated AI terms / privacy notice / in-product microcopy / help article / contract-of-carriage / other |
| `governs_ai` | yes / contested / no |
| `names_ai_feature` | yes (by brand) / partially (by category, not brand) / no |
| `fetch_depth` | full-fetch / snippet-only / referenced-not-located / structural-proxy |
| `assent_mechanism` | clickwrap / browsewrap / affirmative-enrollment / none-at-AI-surface / contested |
| `clause_codes_present` | subset of B1–B11 (Section 6) |
| `ai_specific_codes` | which of the above are AI-*specific* vs generic-reaching (Section 5) |
| `b4_register` | directive / hedged / n/a (Section 11) |
| `special_flags` | PROTO-B1 / channel-limitation / compelled-disclosure / near-B1 / orphan-document (Section 7) |
| `locus` | 1–5 (+ privacy-notice / help-article variants) (Section 8) |
| `attachment` | attached / orphaned / contested (Section 8.2) |
| `coder_uncertainty` | free text on any call you were unsure of |

Keep controlled-vocabulary fields to the exact tokens above so the two coders' sheets
align cell-for-cell for kappa computation.

---

## 5. THE MASTER JUDGMENT: AI-specific vs. generic-reaching

Every B-code must be tagged as one of two kinds. This distinction matters more than
mere presence/absence and is the field most likely to drive inter-rater disagreement,
so read the rules carefully.

**AI-specific** = the clause *names* AI/generative AI/chatbot/Outputs/AI Tools (or an
equivalent defined term) and the liability language is written to attach to it.
- Example (B6 AI-specific): American Sec 10(a) extends "AT YOUR OWN RISK" to name
  "AI TOOLS AND OUTPUTS" expressly.
- Example (B6 AI-specific): Walmart Sec 16.J — the whole clause is about "Generative
  AI Features" and their "Output".

**Generic-reaching** = a general clause (AS IS, limitation of liability, indemnity,
content license) that *could* apply to the AI feature because the feature is part of
"the Site"/"the Services"/"Materials", but the clause does not mention AI at all.
- Example (B6 generic-reaching): Lowe's "THE SITE IS PROVIDED 'AS IS'… NO OPINION,
  ADVICE OR STATEMENT… SHALL CREATE ANY WARRANTY." Broad enough to touch a Mylow
  output, but AI is never named. Code B6, tag **generic-reaching**.
- Example (B6 generic-reaching): United's "may include inaccuracies or typographical
  errors" — generic, and the document is confirmed AI-silent.

**Decision rule.** If you would still code the clause identically for a company that
had no AI feature at all, it is generic-reaching. If the clause's wording depends on
the AI (defines it, names Outputs/Inputs/Prompts, addresses generation), it is
AI-specific.

**Why this matters:** a firm can appear "covered" on a naïve keyword scan while every
liability clause is boilerplate that predates the AI. The `ai_specific_codes` field is
what prevents that false positive.

---

## 6. Codebook (B1–B11)

For each code: **definition → include → exclude/boundary → adjacent-code
disambiguation**. Assign the code if the clause is present in *any* register, then use
the `ai_specific` tag (Section 5) to say whether it names the AI.

### B6 — Accuracy / no-warranty ("AS IS", may be inaccurate)
- **Include:** any disclaimer that outputs/materials/the service may be inaccurate,
  incomplete, out of date, or that the service is provided "AS IS"/"AS AVAILABLE"
  without warranty.
- **AI-specific example:** Delta — responses "are artificially generated and may
  contain inaccuracies", AI Tools provided "AS IS".
- **Generic-reaching example:** Fazoli's — materials "AS IS", no warranties of
  accuracy.
- **Exclude:** availability-only language that does not touch correctness. Wells
  Fargo's "no warranty that the Chat service will be available… or free of fault or
  error" is *thin B6* — it addresses availability/fault of the service, not the
  correctness of what the assistant says. Code B6 but note it is availability-scoped.
- **vs B4:** B6 = "it may be wrong"; B4 = "so you must not rely / must verify". A
  clause can be B6 only (states inaccuracy, no instruction to the user).

### B4 — Anti-reliance ("do not rely solely", "verify")
- **Include:** any instruction that the user should not rely on the output and/or must
  independently verify it.
- **Register matters — record `b4_register` (Section 11):**
  - *Directive:* Walmart "You should review and verify the Output before making any
    purchases"; Delta all-caps "IT IS YOUR SOLE RESPONSIBILITY TO VERIFY THE OUTPUTS".
  - *Hedged:* Alaska "Consider checking important information"; Frontier "encouraged
    to verify". These are permissive, not mandatory — still B4, tag `hedged`.
- **Exclude:** a general "use at your own risk" with no verify/reliance instruction
  (that is B6 or B3 flavor, not B4).
- **Generic B4 (v1.1 rule).** Code **B4 = G** only when an AI-silent clause *instructs*
  the user to verify or not to rely, and reaches the company's own content generally —
  e.g. "you should not rely solely on the product information... but should always read
  the labels" (Albertsons), "Before you act in reliance on any Materials, you should
  confirm any facts" (Wegmans), "should not be relied upon for significant... decisions"
  (AT&T). "Reliance is at your own risk" without an instruction is B3, not B4. An
  instruction aimed at one non-AI tool (stock prices, currency converter) or at
  third-party user posts is not B4 for the AI feature.
- **vs B3:** B4 tells you to check *before* relying; B3 assigns *responsibility* for
  what happens if you act on it.

### B3 — User-responsibility shift (you, not us, own actions on Output)
- **Include:** clause making the user responsible for their use of, and actions/
  decisions taken on, the output.
- **AI-specific example:** Delta "YOU — NOT DELTA — ARE RESPONSIBLE FOR YOUR USE OF,
  AND ANY ACTIONS YOU TAKE IN RELATION TO, OUTPUT". Instacart "You are responsible for
  your use of Outputs and any decisions or actions you take based on them."
- **Boundary:** Target's agentic clause "Actions taken by an Agentic Commerce Agent…
  will be treated as actions authorized by you" is B3 *and* B5 (it shifts
  responsibility for an agent's actions).
- **vs B4:** see above. B3 is about who bears the consequence, not about a verify duty.
- **Generic B3 (v1.1 rule).** Code **B3 = G** when an AI-silent clause allocates to the
  user the consequences of *reliance on, actions taken on, or use of* site content —
  e.g. "any reliance... is strictly at your own risk" (Centene), "not liable for any
  consequence... of any action or inaction you take based on the Materials" (Wegmans),
  "You assume total/all responsibility... with respect to your use of the Site"
  (McDonald's, J.Crew). A **bare** "you use the Site at your own risk" with no reliance,
  action or responsibility wording stays **A** (UnitedHealthcare). Responsibility for the
  user's own *inputs*/postings or account security is not B3.

### B2 — Limitation of liability
- **Include:** exclusions/caps on damages (no consequential/indirect/incidental/
  punitive; monetary caps).
- **AI-specific example:** American — aggregate liability capped at USD 500 where
  other limits are unenforceable, in the AI-aware terms.
- **Generic-reaching example:** almost every company has a general LoL that reaches
  the AI as part of "the Services" (Fazoli's cap at "amount you paid to access this
  site"; United full consequential-damages exclusion).
- **Note:** B2 is nearly ubiquitous and usually generic-reaching — the `ai_specific`
  tag is what carries the information here.

### B7 — Indemnification
- **Include:** user agrees to defend/indemnify the company.
- **AI-specific example:** Delta — user indemnifies Delta for "use of AI Tools".
- **Generic-reaching example:** standard user-indemnifies clauses (Domino's, Lowe's,
  United, etc.).

### B1 — Transaction-error non-honoring (the sharpest anti-Moffatt clause — always flag)
- **Definition:** an express statement that an AI-generated price/term/representation
  **does not bind the company** — i.e. the firm refuses to honor what the AI said.
  This is the clause that most directly defeats a Moffatt claim.
- **Canonical example (one of two clean B1s in corpus, with Marriott):** Walmart 16.J — "Pricing
  information provided by Generative AI Features does not constitute an offer to sell
  the item at the stated price or acceptance of an offer to purchase."
- **NOT B1 — record as `near-B1` instead:** Uber's "Pricing information… is an
  estimate… Please refer to the checkout page" — disclaims accuracy and redirects, but
  does **not** refuse to honor a stated price. Functionally protective, but a weaker
  device. Tag `near-B1`, do not code B1.
- **NOT B1 — record as `PROTO-B1` / channel-limitation instead:** Wells Fargo — "chat
  … does not constitute consent … to use electronic records" and "we cannot accept
  trade instructions in any chat". This removes the reliance interest by denying the
  *channel* legal effect, rather than disclaiming a *price*. Code as `channel-
  limitation` special flag (Section 7), not B1.
- **Because B1 is the analytically sharpest code, flag its presence AND its near-
  variants every time**, so the taxonomy can separate "inoculated" firms from
  "warned-only" firms.

### B10 — Training on prompts / IP over inputs (and output-ownership variant)
- **Include:** company may use prompts/inputs/outputs to train/improve models; and/or
  claims IP/license over user-submitted content or over Outputs.
- **AI-specific example:** Delta — Prompts+Outputs+Feedback are "your Content" but
  Delta may use them "to train artificial intelligence models". American — may use
  Inputs/Outputs "for machine learning purposes".
- **Standout variant — output ownership:** Instacart — "Instacart owns all
  AI-generated content ('Outputs')". Code B10 and note the ownership posture (stronger
  than a mere training license).
- **Generic-reaching example:** perpetual content-license over "Submissions" that
  would technically sweep in chat inputs (Fazoli's, Domino's "chats" named as
  Submissions, Walmart content license, Lowe's license over "outputs"). Tag
  generic-reaching.
- **vs B9:** B10 = company's rights to USE inputs/outputs (inbound to the company).
  B9 = company BARS the *user/third parties* from training on the company's content
  (outbound protection). A single document often has both, pointing in opposite
  directions — code both.

### B8 — Third-party source carve-out
- **Include:** disclaimer that output/content draws on third-party sources the company
  does not verify / is not responsible for.
- **AI-specific example:** Delta names Sherpa & IATA as output sources it does not
  warrant. Walmart — output may be based on manufacturer/seller/third-party sources
  "None of these sources have been verified by Walmart."
- **Boundary:** a generic Marketplace-seller disclaimer (Lowe's, DoorDash merchant
  carve-out) is B8-adjacent; code B8 and tag generic-reaching unless it specifically
  ties to AI output. DoorDash's clause is a hybrid — it says merchant listings "may
  have been generated or enhanced with…AI" AND disclaims liability for merchant acts;
  code B8 + AI-content-disclosure.

### B9 — Anti-jailbreak / no-model-training-on-outputs (company-protective)
- **Include:** prohibition on jailbreaking/"tricking" the AI; and/or prohibition on
  using the company's content/service to train a third-party AI; anti-reverse-
  engineering by tracking inputs/outputs.
- **Example:** Walmart bars "break/trick" attempts and bars using Materials to "train…
  any artificial intelligence". Instacart bars mimicking system behavior by tracking
  inputs/outputs. DoorDash bars using Services to train an ML/AI system.
- **vs B10:** see B10. B9 protects the company's stuff from others' AI; B10 grants the
  company rights over the user's inputs.

### B11 — Automated-decision-making disclosures (privacy-notice ADM)
- **Include:** privacy-notice ADM/profiling disclosures — **only relevant if the SAME
  system is also customer-facing.** A purely internal ADM disclosure is out of scope.
- **Coding discipline on absence:** B11 can only be "confirmed absent" if the privacy
  notice was actually read in full. If the privacy notice could not be fetched, B11 is
  **UNTESTED, not absent** (Alaska: privacy policy bot-walled → B11 untested). Gopuff:
  both docs read in full → B11 confirmed absent.
- **Do NOT confuse with compelled disclosure (Section 7):** Capital One's California
  AB 2013 training-data notice mentions "generative artificial intelligence" but is a
  *compelled* input-side transparency duty, not ADM risk-allocation. Tag
  `compelled-disclosure`; do not treat as a voluntary B11 liability posture.

### B5 — Agentic-AI / user-assigned-agent clause
- **Include:** any clause governing an AI acting *for* the customer (delegated
  authority), or a customer pointing their own agent at the service.
- **Two opposite architectures, both B5:**
  - *Customer authorizes the agent (Target):* "Agentic Commerce Agent"; actions
    "treated as actions authorized by you"; Target "not responsible for the conduct of
    the third-party" agent. B5 + B3.
  - *Company gates the agent (American):* third-party AI tool needs American's "express
    written consent" via AIRequest@aa.com; user must verify approval and "assume all
    responsibility". B5 as a permission gate.
- **Also B5:** Instacart §4.3 extends restrictions to "any…system you authorize…
  (including…AI Agents)".
- **Boundary:** a plain anti-bot/anti-scraping clause ("robots, spiders, avatars") is
  NOT B5 — it bars automation, it does not govern a *user-authorized* agent. Only code
  B5 when delegated/authorized agency is contemplated.
- **Restrictive B5 (v1.1 rule).** A clause that expressly bans or gates *AI agents
  acting on a user's behalf* ("buy-for-me agents, LLM-driven bots" — eBay; "an
  artificial intelligence enabled system, agent... acting on behalf of a user" — Anthem;
  "AI-powered assistants" — Booking.com) is **B5 = S**, noted "restrictive" in the key
  finding. It contemplates delegated agency, so it is not a plain anti-bot clause. Such a
  clause does NOT by itself create an AI locus for the firm's *own* AI feature: if it is
  the only AI language, set `locus: none` and say so.

---

## 7. Special conventions (sharp-edge rules — apply exactly)

These are non-obvious rules the pilot established. A second coder must apply them to
match the corpus.

1. **`channel-limitation` is its own technique, not B1.** Where a firm removes the
   reliance interest by denying the *channel* legal effect (Wells Fargo: chat can't
   form electronic records; can't carry trade instructions), flag `channel-limitation`.
   It is arguably the most robust anti-Moffatt device but must not be squeezed into B1.

2. **`compelled-disclosure` ≠ voluntary risk-shifting.** An AI mention that exists
   only because a statute requires it (Capital One / California AB 2013 training-data
   notice) is filed under `compelled-disclosure`. A keyword-presence coding would badly
   overstate such a firm's posture — do not let "artificial intelligence" appearing in
   a compelled notice count as liability drafting.

3. **`near-B1` for price-estimate-and-redirect clauses** (Uber). Disclaims AI price
   accuracy and redirects to checkout but does not refuse to honor the price. Track
   separately from clean B1.

4. **`orphan-document` / attachment flag.** A dedicated AI Terms document that the
   governing site ToU never routes the consumer to is an *orphan* (Delta: site ToU is
   AI-silent and contains no cross-reference to the AI Terms). Locus 1 (dedicated
   document) is therefore **not automatically stronger** than Locus 2 (AI section
   inside the main terms) — a dedicated doc can be better drafted but worse attached.
   Record `attachment: orphaned`.

5. **Do not miscode user-to-user chat/forums as an AI chatbot.** United's "Forums"
   section governs bulletin boards and human chat rooms, not an AI feature. A "chat"
   string is not an AI hit — read the surrounding text.

6. **Category-not-brand naming = `names_ai_feature: partially`.** Recurs in every
   vertical: the binding document defines a category ("AI Tools", "Generative AI
   Features", "Chatbot") and never uses the marketed persona name (Concierge, Sparky,
   Fargo, Mylow, Ask Instacart). Note it — it is itself a say–do finding (marketing
   names a persona; the contract names a category).

7. **Absence discipline (critical for honesty of the dataset).** Only code "confirmed
   AI-silent / code absent" when the document was **read in full** (`full-fetch`). If
   depth is `snippet-only` or `referenced-not-located`, code the gap as a gap, never as
   confirmed absence (Amazon Conditions of Use = snippet-only, robots-blocked →
   high-confidence *gap*, not confirmed absence; Alaska site ToU = referenced-not-
   located in both 2022 and 2026).

8. **Operative liability language can live in a non-contract container.** Frontier's
   B6+B4+B3 sit inside a *privacy notice*; DoorDash's sit inside an unincorporated
   *help article* whose only tie is a circular "governed by the Consumer Terms" line
   (and the Consumer Terms contain no assistant-output clause). Code the codes where
   they textually appear, but set `locus` to the privacy-notice / help-article variant
   and flag the enforceability question in `coder_uncertainty`.

---

## 8. Locus and attachment

### 8.1 Locus spectrum (where the AI-liability language lives)
1. **Dedicated standalone AI Terms** (Delta AI Terms of Use).
2. **Dedicated AI section inside general terms** (Walmart §16.J; American §15;
   Instacart §5.2).
3. **Generic clause reaching a named AI feature** (Lowe's — AI unnamed but "the Site"
   language reaches it; Wells Fargo — generic clauses reach the AI via the "chat,
   virtual assistant" definitional hook).
4. **Microcopy-only, in-product** (Alaska "This Generative AI powered experience can
   make mistakes. Consider checking important information.").
5. **No consumer terms — operational control only** (drive-thru voice confirmation;
   no click-through moment).

**Extension variants discovered in the pilot (record explicitly):**
- **Privacy-notice locus** — liability language placed in a privacy notice (Frontier;
  Capital One's compelled notice sits in a similar container for a different reason).
- **Help-article locus** — disclaimers in an unincorporated support article
  (DoorDash).

These variants matter because the container's enforceability differs from a contract's.

### 8.2 Attachment / binding-status (code alongside locus)
Independently of *where* the language lives, judge whether the consumer is actually
routed to it and bound:
- `attached` — the governing, contract-forming document reaches the AI (Walmart §16.J
  inside the ToU; Wells Fargo OAA reaching chat by live definition).
- `orphaned` — a well-drafted document nothing routes the consumer to (Delta AI Terms).
- `contested` — signposting rather than incorporation (Uber's "for more information,
  please visit"); or operative terms in a privacy notice / help article the consumer
  never affirmatively accepted.

---

## 9. Assent mechanism

Record how (if at all) the consumer assented *to the document that carries the AI
language, at the AI interaction*:
- `clickwrap` / clickwrap-by-reference — affirmative "by using the AI Tools you agree
  to be bound" (Delta).
- `browsewrap` — bound "by accessing and using this website", no click-through
  (United).
- `affirmative-enrollment` — an enrollment agreement the user actively signed up to
  (Wells Fargo OAA — strongest assent posture in corpus).
- `none-at-AI-surface` — the AI surface links to a privacy/cookie policy but to **no**
  terms, and there is no "by using this you agree" moment (Alaska destination search).
- `contested` — signposted-but-not-incorporated AI page (Uber).

**Special note for voice/drive-thru:** phone and drive-thru voice orders typically have
no click-through moment. Record explicitly whether *any* terms were presented to/
accepted by the customer for *that specific interaction*, not merely whether terms
exist somewhere on a website. This is often `none-at-AI-surface`.

---

## 10. Fetch depth (reliability flag — copy the primary value, verify against source)
- `full-fetch` — complete document read. Required before any "confirmed absence".
- `snippet-only` — search-result fragments only; absence is a gap, not a finding.
- `referenced-not-located` — existence confirmed but content not retrieved.
- `structural-proxy` — a different jurisdiction's/product's document used only to
  infer likely structure; **never** evidence for the target (Burger King Singapore
  mirror; Home Depot 2020 HubSpace app terms). Do not code B-codes from a structural
  proxy as if they were the target's.

---

## 11. The B4 register flag (directive vs. hedged)

Because anti-reliance is central to the Moffatt question, sub-code every B4:
- **`directive`** — mandatory verb: "must review and verify", "IT IS YOUR SOLE
  RESPONSIBILITY TO VERIFY" (Walmart, Delta).
- **`hedged`** — permissive verb: "consider checking", "encouraged to verify", "should
  always independently check" is a middle case — if it says *should/always* treat as
  directive-leaning; if it says *consider/may want to* treat as hedged. When genuinely
  on the line, code `hedged` and note it.

A hedged B4 coupled with `none-at-AI-surface` assent (Alaska) founds very little
consumer verification duty — this pairing is a key taxonomy signal.

---

## 12. Two fully worked examples (code these yourself first, then check)

Before coding live, code these two from their source docs and confirm you land on the
same values. If you diverge, re-read the relevant section above.

**Walmart — Terms of Use §16.J (retail).**
- `governs_ai`: yes · `names_ai_feature`: yes (defines Chatbot/Generative AI) ·
  `document_type`: dedicated AI section within product/service terms ·
  `clause_codes_present`: B6, B4, B3, B2(via general LoL), B1, B10, B9 ·
  `ai_specific_codes`: B6, B4, B3, B1, B9 AI-specific; B2/B10 partly generic ·
  `b4_register`: directive · `special_flags`: B1 (clean) · `locus`: 2 ·
  `attachment`: attached · `assent_mechanism`: clickwrap-by-reference.
- Why: the first clean B1 found (Marriott is the other); the "inoculated" benchmark.

**United — Terms, Conditions and Legal Notices (airline).**
- `governs_ai`: yes (but AI-silent) · `names_ai_feature`: no · `fetch_depth`:
  full-fetch · `clause_codes_present`: B6, B2, B7, B10 — **all generic-reaching, none
  AI-specific** · `ai_specific_codes`: none · `locus`: no AI locus · `assent_mechanism`:
  browsewrap.
- Traps: (a) the "chat rooms" in Forums is user-to-user, NOT an AI hit; (b) United
  *does* have a directive anti-reliance clause — but aimed at its Currency Converter,
  not the AI, so it is NOT coded as B4 for the AI feature; (c) confirmed absence is
  legitimate here only because the document was full-fetched.

---

## 13. Disagreement adjudication protocol (for the IRR pass)

1. Both coders code the shared subset **independently and blind** (no peeking at each
   other's sheets or the archive coder notes).
2. Compute agreement per field. For the B-codes, compute Cohen's κ per code
   (present/absent) across documents; for `ai_specific` tags, compute κ on the
   AI-specific/generic distinction; report per-code κ and an overall figure. Treat the
   `ai_specific` distinction as a first-class reliability target — it is where we most
   expect and most need reliability.
3. Meet to adjudicate disagreements. For each: identify whether it was (a) a *reading*
   error (missed text), (b) a *rule* ambiguity (manual unclear), or (c) a *genuine*
   judgment split. Log the cause.
4. Where the cause is (b), amend this manual (bump the version, note the change) and,
   if the rule change is material, re-code affected documents.
5. Record final adjudicated values plus the pre-adjudication κ (the κ we report is the
   *pre*-adjudication one).

---

## 14. Quick-reference decision checklist (per document)

1. In scope? whose document? does it govern the AI? → Section 3. If it fails, stop and
   log.
2. Read the FULL document (or note depth honestly). → Section 10.
3. Does it name the AI (brand / category / not at all)? → `names_ai_feature`.
4. Walk B6→B5. For each present code, tag AI-specific vs generic-reaching. → Sections
   5–6.
5. B1? If not clean, is it near-B1 / channel-limitation / PROTO-B1? → Sections 6, 7.
6. Any special flags (compelled-disclosure, orphan-document)? → Section 7.
7. B4 present? directive or hedged? → Section 11.
8. Locus (1–5 or privacy-notice/help-article) + attachment (attached/orphaned/
   contested). → Section 8.
9. Assent mechanism at the AI surface. → Section 9.
10. Record every uncertain call in `coder_uncertainty`. Do not consult the other coder
    yet.

---

*v1.1 (2026-10-06) — added three boundary rules from v2 coding (V1–V30): generic B3,
generic B4, restrictive B5 (Section 6). Carry-over firms re-checked against them.*

*v1.0 — derived from the pilot corpus (24 companies, 5 verticals + Nov-2022 Wayback
baseline). Amend and bump the version whenever an adjudication session resolves a rule
ambiguity (Section 13.4).*
