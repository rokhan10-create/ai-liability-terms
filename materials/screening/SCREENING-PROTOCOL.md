# Recollection: sample construction and consumer-interaction screen (v2)

**v2 adopted:** 2026-10-05. v1 (industry pass/fail gate with a 2-per-sector cap) is archived
as `SCREENING-PROTOCOL_v1-industry-gate_2026-10-04.md`; see §7 for why it was replaced.
**Files:** `candidate-industries.csv` (103 candidate industries; 93 eligible),
`screening-log.csv` (one row per firm checked), `build_sample.py` (derives the sample from the
log, so nobody picks the sample by hand).

---

## 1. Industry universe

**Universe rule.** Every 4-digit NAICS 2022 industry whose output is bought principally by
households, using the BEA Personal Consumption Expenditures (PCE) accounts as the reference for
"household". An industry is out if its customers are mainly businesses or governments. The test
is applied at the 4-digit level, so consumer-facing industries inside a mostly-B2B sector (tax
preparation in 54 Professional Services) are still caught.

**Result:** 103 candidate industries across 13 two-digit sectors; **93 eligible**. Ten are
excluded before screening as predominantly public or nonprofit (6111, 6112, 6113, 6221, 4851,
6241, 6242, 6243, 7111, 7121 - see `screen_result = excluded-scope`). *Amendment 2026-10-05:*
the first list (59) omitted 44 qualifying industries (e.g., cruise lines 4831, movie theaters
5121, farm/garden supply 4442, senior living 6233, child care 6244, funeral services 8122);
they were added before any of them was screened.

Every code and title was checked against the U.S. Census Bureau's 2022 NAICS search on
2026-10-04. NAICS 2022 eliminated the old "nonstore retailers" subsector (454), so online-only
retailers are classified by what they sell (mostly 4552).

**There is no industry-level selection.** Every one of the 93 industries contributes its top 5
firms to the screen. Industries are a descriptive and analytic variable, not a gate.

## 2. Firm roster: the top 5 in every industry

For each industry, list the **5 largest US commercial firms by revenue**, using:
- the latest fiscal year ending on or before the cutoff (normalize any TTM figures before
  freezing);
- public and private firms alike (private firms from the best published figure, flagged);
- firm identity as of the cutoff date (30 June 2026): mergers closing after the cutoff are
  ignored (Charter–Cox closed 2026-08-20, so both are separate firms).

**Classification rule.** Each firm is assigned to the NAICS industry matching its **largest
revenue segment** in its latest 10-K / annual report (EDGAR's SIC code recorded as a
cross-check). A firm appears in one industry only.

**Slot rules.** A firm that cannot be a deployer under the study's definition does not occupy
one of the 5 slots, and the next firm by revenue moves up:
- foundation-model developers (e.g., Amazon);
- firms with no consumer-facing channel (owner REITs whose guests deal with the brand
  operator; B2B-only firms that sneak into an industry ranking);
- nonprofit or public bodies;
- non-US firms (by headquarters).

**Industries with fewer than 5 eligible US commercial firms** (e.g., local delivery: DoorDash,
Instacart, Grubhub) screen every eligible firm and report `k / n`; the build script flags them
so the shortfall is visible rather than filled with out-of-industry firms.

Every skipped firm is still logged with its reason. Firms that *are* consumer-facing but simply
lack qualifying AI (e.g., Costco) **do** occupy a slot. That is the adoption rate we measure.

## 3. The screen: does the AI interact with the consumer?

**A firm qualifies (`consumer_ai = yes`) if, by 30 June 2026, it offers an AI system that the
consumer engages with directly:**
- it **converses** with the customer (text chat, voice, phone IVR that understands open
  speech), or
- it **acts on the customer's behalf** (books, buys, changes, cancels, files).

*Interpretation (applied consistently since 2026-10-04):* natural-language search that interprets a
free-text request and answers with generated or curated results (Marriott's Ask Bonvoy, Hyatt's
intent search, Uber Eats' GenAI search) counts as conversing; log it with "NL search" in
`notes` so it can be separated in analysis. Plain keyword search, AI-written content the customer
doesn't interact with (e.g., AI menu descriptions, review summaries), and one-way AI-generated
messages do not count.

Generative and non-generative systems both count (decision of 2026-10-04: the test is
interaction, not technology; e.g., BofA's Erica can execute a wrong transaction).

**Does not count:** AI working only behind the scenes (credit scoring, fraud, pricing,
recommendations, routing), AI used only by employees, scripted fixed-button bots, and AI reached
only through a third-party platform (ChatGPT/Claude apps, Alexa skills, Facebook Messenger
bots).

**Evidence, in order of preference:** (1) live product; (2) firm help-center/support page;
(3) firm press release or filing; (4) vendor case study naming the firm and describing live
customer use, accepted only if tiers 1–3 aren't found within budget, and flagged. General press
is a lead, not evidence. Every `yes` needs an `evidence_url`.

**Pre-cutoff proof:** when no launch date is published, a dated firm-hosted page (help article,
newsroom, community post) or a pre-cutoff Wayback capture showing the feature in use satisfies
`by_cutoff = yes`. Pilots and tests that are live to real customers count as launched.

**Budget:** about 2 queries per firm; up to 4 for a top-5 firm that is genuinely ambiguous.
All 5 slots are checked in every industry: **no stopping rule**.

## 4. The sample

**Sample = every top-5 firm with `consumer_ai = yes` and `by_cutoff = yes`**, derived by
`build_sample.py` from the log.

- `unclear` firms are **not** in the main sample; they are listed in the log and included in a
  robustness check. Each affects only its own row.
- Report, for every industry, `k / 5` = the number of top-5 firms with consumer-facing AI. This
  adoption rate is a finding in itself.
- Sector imbalance (finance contributes several industries) is handled in reporting: results by
  sector, plus a robustness check excluding finance. No cap.

## 5. Locked decisions

| Decision | Value | Date |
|---|---|---|
| Cutoff date | 30 June 2026 | 2026-10-04 |
| Nonprofits | Excluded (commercial deployers only); 6113 and 6221 removed before screening | 2026-10-04 |
| AI test | Consumer interaction (generative or not) | 2026-10-04 |
| Firms per industry | Top 5 by revenue, all checked | 2026-10-05 |
| Industry gate / sector cap | None | 2026-10-05 |
| Ranking basis | Revenue (users only where revenue isn't reported) | 2026-10-04 |

## 6. Log field definitions

| Field | Values |
|---|---|
| `rank` | rank among eligible firms (skipped firms logged with their raw rank and a skip reason) |
| `classification_basis` | "10-K segment: <segment name>" |
| `consumer_ai` | yes / no / unclear |
| `interaction_type` | chat / voice / agentic / mixed |
| `channel` | web / app / phone / drive-thru / in-store / messaging |
| `by_cutoff` | yes / no |
| `evidence_type` | live-product / help-center / firm-announcement / vendor-case-study |
| `decision` | include / exclude / skip |
| `exclusion_reason` | no-consumer-ai / internal-only / after-cutoff / third-party-channel / model-developer / no-consumer-channel / nonprofit-public / non-us / other: … |

## 6b. v3 scope rule (adopted 2026-10-05, supersedes the "all industries, top 5" scope of v2)

- **Main sample = the 20 largest consumer-facing industries by household spending, top 10 firms
  each.** Household spending = 2022 Economic Census revenue × household share (Census class of
  customer where available, else BEA 2017 PCE ÷ commodity output). Ranking and sources:
  `industry-household-revenue-ranking.csv`, `SOURCES-industry-size.md`. The top 20 cover ~79% of
  household spending across the 93 eligible industries.
- **Supplementary set = all other eligible industries (ranks 21–92 plus rail), top 5 firms each.**
  All 93 were screened by 2026-10-05. Reported and released, but not in headline statistics.
- **Automated-transaction AI counts (decided 2026-10-05).** An AI that transacts with or bills the
  consumer automatically, without any conversation, passes the consumer-interaction test. Example:
  Metropolis plate-recognition parking that charges the card on exit. The company bears the risk
  of the AI's wrong charges, just as with Erica executing a mistaken transfer. AI that only detects
  or flags something so that a human then deals with the consumer (e.g., SimpliSafe camera
  detection) does not count by this rule alone; it stays unclear pending a separate decision.
- Why: v2 (all 93 industries × top 5) was not feasible with full document collection before the
  submission deadline, and most of the 93 are small or fragmented. The size ranking does not depend
  on AI adoption.
- All §2–§4 rules (slot rules, consumer-interaction test, evidence tiers, unclear handling) apply
  unchanged, with "top 5" read as "top 10" for main-sample industries.

## 6c. Resolving unclear firms (adopted 2026-10-05)

- **Check the live site for the chat vendor.** A known AI-agent platform (Ada, Sierra, Decagon,
  Quiq, Salesforce Einstein Bot, LivePerson bots, Oracle Digital Assistant) plus any firm or vendor
  description of a bot is enough for yes. A plain human-chat tool, or no chat at all, means no.
- **Test generic "virtual assistant" bots with a question that avoids keywords** (e.g., "everything
  in my house just went dark" for an outage). If the bot only reacts to keywords or menu buttons,
  it is scripted, not AI.
- **Dating:** prefer a firm or vendor source dated before the cutoff. An archived snapshot from
  before the cutoff is also acceptable.
- **Removing a firm:** mark it "no" when the only lead turns out to be refuted (rule-based bot,
  internal-only tool, feature never launched, or bot gone by June 2026). Keep it unclear while any
  positive lead is still unresolved.

## 7. Protocol history

- **v1 (2026-10-04):** industries passed if ≥5 of their top 15 firms had consumer-facing AI
  (stopping rule), capped at 2 per sector, PCE tiebreak. **Replaced 2026-10-05** after 11
  industries: four industries landed on exactly 4 qualifying firms, so single ambiguous firms
  (MGM, McDonald's, Sprouts, Meijer) decided whether whole industries entered the sample. The
  cap also excluded industries (investing) for reasons unrelated to them. v2 removes all
  industry-level selection. The 11 industries screened under v1 had all top-5 slots checked, so
  they convert without re-screening, except where a top-5 slot was covered only by a grouped
  check (filled individually under v2).
- Earlier amendments carried into v2: vendor-case-study evidence tier; firm identity at cutoff;
  private firms in rankings; dated firm-hosted pages as pre-cutoff proof.

---

## Sources used

- U.S. Census Bureau, NAICS 2022 search: https://www.census.gov/naics/
  (lookup: `https://www.census.gov/naics/resources/model/dataHandler.php?input=<code>&search=2022`)
- BEA, Consumer Spending / PCE: https://www.bea.gov/data/consumer-spending/main
- BEA FAQ on NIPA Table 2.4.5U: https://www.bea.gov/help/faq/84
- SEC SIC code list (EDGAR classification): https://www.sec.gov/search-filings/standard-industrial-classification-sic-code-list
- Revenue rankings: companiesmarketcap.com category pages (cited per row in the log)
