# v2 clause-continuity: manual checks and method corrections

Running log of hand-verification of `v2-run-diffs.py` output. Every machine verdict that is cited
must be either verified here or of a class validated here.

## Method corrections (2026-10-09, after the first 30 pairs)

1. **S-code verdicts now come from AI sentences, not clause-family patterns.**
   - The pilot method judged every code by the sentences its family regex matched. On the first run, 12 S codes showed as "carried over from 2022" (BAC-01 B10; BBWI-01 B4/B6/B10; CVNA-01 B4/B10; TGT-01 B4/B6; WMT-01 B10; WFC-02 B6; FRO-02 B2/B3).
   - In all 12, the family-matched sentences contained **no AI wording**. The AI-specific operative text sat in separate sentences that the family regex does not catch. Only WFC-02 B6 (below) is genuinely 2022 text.
   - The runner now classifies S codes as new, retrofit or already-in-2022 using the AI-mentioning sentences: family-matched ones first, otherwise document-level (labelled "(document-level)").
2. **Stricter AI tagging.** Hits resting only on "automated system/tool/technology" or "concierge" are no longer AI.
   - Verified false positives: ACI-01/ACI-02 anti-robot clauses ("any automated system, including… robots, spiders"); CVNA-01 autodialer consent ("automated technology"); WMT-01 Photo Center "automated systems and algorithms".
   - After the fix, the only pre-2022 AI-category sentences are Wells Fargo's.
3. **Wider legal-sentence filter.**
   - The pilot filter silently dropped operative sentences without "you/we/terms…" vocabulary. Example: ELV-01 L549 item (10), Anthem's ban on access "through an artificial intelligence enabled system, agent, bot… unless expressly authorized by us".
   - The filter now also admits "us / must / unless / authoriz- / prohibit / artificial intelligence / AI".
   - ELV-01 B5 S now resolves to **new AI text**.
   - (A first attempt wrote control characters in place of `\b` in the regex; caught by byte inspection and rewritten.)

## Manually resolved verdicts

| Doc | Code | Machine verdict (document-level) | Verified verdict | Evidence |
|---|---|---|---|---|
| WFC-01 | B9 S | already in 2022 | **NEW AI TEXT** | "prompt-based manipulation, or 'jailbreaking'" sentence is new (ratio 0.27 vs the 2022 "means not intentionally made available" sentence) |
| WFC-01 | B10 S | already in 2022 | **2022 CLAUSE, AI-EXPANDED** | 2022: conversations "through use of chat, virtual assistant, or a similar service are monitored and retained". 2026 (ratio 0.65): adds "virtual AI assistant… human-simulated conversation… recorded, analyzed… by both Wells Fargo and our service providers" |
| WFC-02 | B6 S | already in 2022 | **ALREADY IN 2022 (verbatim)** | "Wells Fargo makes no warranty that the Chat service will be available… or be free of fault or error" (ratio 1.0; confirms the pilot) |
| WFC-02 | B10 S | already in 2022 | **NEW (rewritten)** | 2026 sentence (ratio 0.34) replaces 2022 "chats will be monitored and saved" with "monitored, recorded, analyzed, and retained by Wells Fargo and our service providers" |

## Open items

- **FRO-01 (Frontier Terms of Use):** both versions are short stubs (fewer than 15 legal sentences), so its "100% unchanged" is not comparable to the other documents. Report it separately.
- **G "NOT LOCATED BY PATTERN" (7):** pending a manual look once the full run is in.
- **ACI-02 (Safeway legacy terms):** baseline is Nov 2021, the latest capture on or before 2022-11-30. Pre-ChatGPT, but disclose the date.

## Full run (2026-10-12): 138 baselines, 728 coded clauses

### Capture-quality screen (all 138 baselines)
- Every baseline was screened for captcha, access-denied, geo-block and script-shell text, and for low word or legal-term counts.
- Flags fell only on long legitimate documents mentioning "outside the United States" or a captcha widget (ABB-02, SNAP-01, TSCO-01, CAR-01/02, AAL-01), plus the known FRO-01 stub.
- Two captures were rejected before filing and moved to `_manual-inbox/rejected/`:
  - PUB-01: the Publix "international visitors" geo-block page;
  - UAL-02: an empty script shell.
- Logged as archived-but-unusable (gaps): EBAY-01/02 (captcha), CHG-01 (bot wall, 403), EH-01/02 (access denied, 403), UAL-02 and JWN-01 (empty script shells; rendered view blank).

### 2023-dated baselines (11): generative-AI wording scan
- WMT-02, USB-01, HIL-01, WFC-03, CVS-02, ROKU-01, GRY-02, VZ-06, VZ-05, CMX-03, TSCO-01: no generative-AI wording.
- USB-01's "virtual assistant" hits are the Siri/Google Assistant voice-balance clause, which pre-existed.

### Hand-resolved S verdicts (13 flagged items, plus one false alarm)

| Doc | Code | Machine | Verified | Evidence (2022 → 2026) |
|---|---|---|---|---|
| USB-01 | B3 S | already in 2022 | **ALREADY IN 2022** | "responsible for confirming the on-screen action matches your request…": verbatim (ratio 1.0) |
| USB-01 | B5 S | already in 2022 | **ALREADY IN 2022** | Smart Assistant commands "even if not specifically intended by you, will be presumed to be authorized": verbatim |
| USB-01 | B2 S | already in 2022 | **RETROFIT** | "disclaim all liability… reliance on the information provided by any…" + "AI tools" (0.81) |
| USB-01 | B10 S | already in 2022 | **NEW** | "use any data that is input by you to further train or develop AI models" (0.35 vs a 2022 recording sentence) |
| WFC-01 | B9 S | already in 2022 | **NEW** | as verified 2026-10-09 |
| WFC-01 | B10 S | already in 2022 | **RETROFIT (AI-expanded)** | as verified 2026-10-09 |
| WFC-02 | B6 S | already in 2022 | **ALREADY IN 2022** | as verified 2026-10-09 |
| WFC-02 | B10 S | already in 2022 | **NEW** | as verified 2026-10-09 |
| CAR-02 | B11 S | already in 2022 | **ALREADY IN 2022** | "machine learning tools and statistical algorithms to confirm the authenticity of the driver's license…" (0.80, provider wording edited) |
| UBR-03 | B10 S | already in 2022 | **ALREADY IN 2022 (reworded)** | 2022 "product development and machine learning to improve the user experience" → "training machine learning models" (0.58) |
| ABB-01 | B4 S | no AI sentence located | **RETROFIT** | translation-accuracy duty extended to "generated Content" (0.85). The AI regex misses "generated". |
| ABB-01 | B6 S | no AI sentence located | **RETROFIT** | the same sentence (0.85): "does not guarantee the accuracy or quality of [generated Content or] translations". The companion "automated tools to translate Content" sentence was likewise extended to "generate or translate" (0.76). |
| NFLX-01 | B9 S | no AI sentence located | **NEW** | the ML-training ban ("machine learning", once in the current text) is absent from the 2022 copy. The sentence was missed by the filter. |
| LYFT-01 | (document level) | AI already in 2022 | **FALSE POSITIVE** | the hit is "autonomous vehicle", not AI-feature wording |

**Corrected S tallies.** Headline set = family-located plus hand-verified, n = 121: new 83, retrofit 33, already in 2022 = 5. The 89 document-level verdicts are reported separately (lower confidence).

### Known tool limits found in this run (not yet fixed in code)
- The AI regex misses "generated" (Airbnb) and some sentences built around "machine learning" (Netflix). Hand-check any S code whose verdict is "no AI sentence located".
- Document-level S verdicts mark every S code in a document "retrofit" if any one AI sentence is a retrofit. Treat them as low confidence.
