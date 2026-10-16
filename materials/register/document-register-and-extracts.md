# Master Source Document Archive â€” AI-ToS Liability Dataset

**Purpose:** single running file for every source document fetched across this project. Appended to continuously as new companies/documents are processed â€” do not create separate per-company files going forward; add new entries here instead.

**How to read an entry:** each document has a provenance header (company, type, URL, retrieval date, fetch depth, AI-named status, clause codes) followed by the coding-relevant extract and a coder note. Fetch depth is the key reliability flag: `full-fetch` = complete document read, `snippet-only` = search-result fragments only, `referenced-not-located` = existence confirmed but content not retrieved, `structural-proxy` = a different jurisdiction's document used only to infer likely structure, explicitly not evidence for the target company.

**Batches processed so far:** Retail generative shopping assistants (5 companies) Â· Airline generative assistants (5 carriers, 6 brands incl. Hawaiian) Â· Food-delivery generative assistants (4 companies) Plus a **November 2022 pre-ChatGPT baseline** for the airline, retail, banking, food-delivery, and hospitality batches, retrieved from the Wayback Machine and stored under `previous-tos/` (see the `previous-tos/FINDINGS-*-nov2022-baseline.md` files, one per batch).

**Preserved source documents:** from the airline batch onward, the fetched documents themselves are kept under `mastersheet-sources/<vertical>/<company>/` (raw HTML, plaintext, PDFs) with a SHA-256 manifest, so entries below can be re-coded later without re-fetching. See `mastersheet-sources/README.md`.

---

## Table of Contents

### Retail Generative Shopping Assistant Batch
1. [Walmart â€” Terms of Use Â§16.J (full)](#walmart)
2. [Amazon â€” Conditions of Use / Rufus gap](#amazon) â€” **superseded, see [correction](#amazon-correction-2026-09)**
3. [Home Depot â€” HubSpace app terms / Magic Apron gap](#homedepot) â€” **superseded, see [correction](#homedepot-correction-2026-09)**
4. [Lowe's â€” Terms & Conditions (full)](#lowes)
5. [Target â€” Agentic Commerce section (full)](#target)

### Airline Generative Assistant Batch
6. [Delta â€” AI Terms of Use (full, dedicated)](#delta)
7. [United â€” Legal Notices (full, AI-silent)](#united)
8. [American â€” Platform T&Cs Â§15 AI Tools (full)](#american)
9. [Alaska (+ Hawaiian) â€” microcopy + CoC (AI-silent)](#alaska)
10. [Frontier â€” AI clause inside Privacy Notice](#frontier)

### Food-Delivery Generative Assistant Batch
11. [Instacart â€” ToS Â§5.2 AI Features (full)](#instacart)
12. [Uber Eats â€” split locus: ToU pointer + separate AI page](#ubereats)
13. [DoorDash â€” recent terms, AI-aware but output-silent](#doordash)
14. [Gopuff â€” total silence (terms + privacy both read)](#gopuff)

### Banking Generative Assistant Batch
15. [Wells Fargo â€” channel-limitation strategy (full)](#wellsfargo)
16. [Capital One â€” compelled CA disclosure only](#capitalone)
17. [Dave â€” AI-silent terms updated Jul 2026](#dave)

### Hospitality Generative Assistant Batch
24. [Marriott - Ask Bonvoy: dedicated AI section + B1, in governing ToU (full)](#marriott)
25. [Hilton - AI Planner: dedicated AI Terms; site agreement AI-silent (mixed)](#hilton)
26. [IHG - frozen 2022 ToU, AI-silent over 2026 AI Planner (full)](#ihg)
27. [Accor - AI-silent terms; consumer AI lives in a ChatGPT app; EU ADM denial (full/mixed)](#accor)

### Banking/Fintech Expansion Batch (EU/UK anchors)
28. [Klarna - dedicated AI-assistant clause + developed credit-ADM; EUR 750k fine (full)](#klarna)
29. [Revolut - dedicated AI notice: directive verify + channel-limitation (full, EU)](#revolut)
30. [bunq - robust Art. 22 + Finn consent-gate (full, EU)](#bunq)
31. [NatWest - Cora generic; automated-loan-decision review right (mixed, UK)](#natwest)
32. [Monzo / Chime / Nubank - identified, AI terms not located (batch note)](#fintech-identified)

### Telecom Batch (new vertical)
33. [Verizon - consumer AI microcopy 'Verify if needed'; thin privacy ADM (US)](#verizon)
34. [Comcast/Xfinity - bare 'responses may be AI-generated' microcopy (US)](#comcast)
35. [Vodafone - dedicated TOBi chatbot T&Cs + fraud/AML ADM (EU, snippet)](#vodafone)
36. [Deutsche Telekom - Frag Magenta generative; data-privacy notice only (EU)](#deutsche-telekom)
37. [Telefónica - Aura generative; AI-ethics commitment, no output terms located (EU)](#telefonica)

### Travel / OTA Batch (new vertical - the Moffatt fact pattern)
38. [Expedia - dedicated AI Terms of Use + Art. 22 privacy (full, US)](#expedia)
39. [Booking.com - own AI ungoverned; anti-agent clauses + generic B1 (full, EU)](#booking)
40. [Kayak - dedicated AI terms; AI-specific B6 (snippet, US/Booking Holdings)](#kayak)
41. [Tripadvisor - generic ToU clause reaching AI + AI-summary harm (snippet, US)](#tripadvisor)
42. [Airbnb - custom-LLM support agent; disclaimer not located; anti-AI-evidence clause (US)](#airbnb) — **superseded: full read found s.9 generated-content clause (B4 S/B6 S), see [Batch 11–12 correction 1](#fullread-batch11-12-2026-10-09)**
43. [Priceline - Penny generative; general-terms governance; getpenny.com trap flagged (US)](#priceline)
44. [Skyscanner / Trip.com - identified, AI terms not located (batch note)](#travel-identified)

### Insurance Batch (new vertical - highest agentic-harm)
45. [Lemonade - AI-agent ToS + robust Art. 22 ADM; no-auto-reject claims (US)](#lemonade)
46. [GEICO - dedicated Kate AI disclaimer; B6/B3 + human fallback (US)](#geico)
47. [EU insurers (AXA/Allianz internal-only) - note on EU consumer-AI thinness](#insurance-eu-note)

### Edtech Batch (new vertical - misinformation-harm class)
48. [Khan Academy - dedicated AI clause: math-errors + fact-check + minors (US)](#khan-academy)
49. [Grammarly/Superhuman - dedicated AI clause: no-warranty + assume-risk (US)](#grammarly)
50. [Chegg - generic accuracy clause reaching AI + "AI Functions" (US)](#chegg)
51. [Duolingo - AI-silent terms revised post-Max-launch; say-do gap (US)](#duolingo)

### Investing / Brokerage Batch (new vertical - securities-law-driven)
52. [Robinhood - Cortex: near-complete dedicated AI disclosure + exec safeguard (full, US)](#robinhood)
53. [Coinbase - Advisor: SEC-registered AI FIDUCIARY (the outlier) (snippet, US)](#coinbase)
54. [Public - Alpha/Agentic Brokerage: no-advice + reach-own-conclusions (snippet, US)](#public)
55. [eToro - Tori: no-advice + accuracy disclaimer (snippet, EU/foreign)](#etoro)

### Healthcare / Telehealth Batch (new vertical - extreme harm; medical-advice class)
56. [Ada Health - AI-specific accuracy (names LLMs) + no-diagnosis; B11 absent (full, EU/DE)](#ada)
57. [K Health - strong no-advice + emergency; stale 2023 vintage (full, US)](#khealth)
58. [Teladoc - no-advice + emergency; AI clause not located (snippet, US)](#teladoc)
59. [Hims & Hers - Labs AI; FTC/states privacy enforcement 2026 (snippet, US)](#hims)

### Real Estate / Proptech Batch (new vertical - Fair-Housing dimension)
60. [Zillow - AI-silent terms; generic no-advice; operational Fair Housing Classifier (full, US)](#zillow)
61. [Redfin - AI-silent terms re Ask Redfin; generic AS-IS + B8 (full, US)](#redfin)
62. [Rightmove - AI microcopy 'can be inaccurate, check before relying' (snippet, UK)](#rightmove)
63. [Realtor.com / Zoopla - identified (ChatGPT app; OpenAI deal), terms not located](#realestate-identified)

### Airline Batch - November 2022 Pre-ChatGPT Baseline (Wayback Machine)
18. [Delta - Nov-2022 baseline: ToU + privacy, both AI-silent](#delta-2022)
19. [United - Dec-2022 baseline: the frozen 2018 document](#united-2022)
20. [American - Oct-2022 baseline + Jan-2025 birth version of Section 15](#american-2022)
21. [Alaska - Nov-2022 privacy notice (partial; bot-walled in 2022 too)](#alaska-2022)
22. [Frontier - Nov-2022 baseline + May-2026 birth version of the AI clause](#frontier-2022)
23. [Delta AI Terms - Feb-2025 birth version (first capture ever)](#delta-aiterms-birth)

### v2 Collection - top-firm roster (protocol v2, started 2026-10-06)
V1. [UnitedHealth Group - Avery: AI-silent site and myUHC terms; AI disclaimer only on firm web pages (full)](#unitedhealth)
V2. [Centene (Ambetter) - Amber: AI-silent, undated site terms; generic disclaimers only (full)](#centene)
V3. [Elevance Health (Anthem) - Virtual Assistant: Oct-2026 terms ban users' AI agents but say nothing of Anthem's own assistant (full)](#elevance)
V4. [State Farm - AI loss-reporting assistant (pilot): AI-silent terms, but a generic "submission does not commit coverage" clause reaches it (full)](#statefarm)
V5. [MetLife - Intelligent Virtual Agent (phone): AI only in privacy statement; terms AI-silent; no assent on the phone channel (full)](#metlife)
V6. [BJ's Wholesale Club - Ask Bev / virtual agents: dedicated AI section s.21 + AI-output carve-out in errors clause + generic order-cancellation (browser capture)](#bjs)
V7. [eBay - AI shopping agent: one-sentence AI accuracy disclaimer in User Agreement + ban on users' buy-for-me agents; AI section in privacy notice (full)](#ebay)
V8. [CarMax - Skye chat + Sierra voice agent: full AI subsection in Terms s.4 (Mar 2025); voice channel has no assent (browser capture)](#carmax)
V9. [Carvana - Shaqbot: AI paragraph in User Agreement (Oct 2025) + chatbot disclaimers incorporated by reference (full)](#carvana)
V10. [Albertsons - Safeway AI / Albertsons AI agentic assistant: AI-silent group terms (May 2025) with strong generic post-confirmation price-change clause (full)](#albertsons)
V11. [Publix - FAQ bot: AI-silent terms (Jun 2025); chat-box microcopy limits expectations and links Terms at point of use (full)](#publix)
V12. [Wegmans - AI shopping assistant (beta): terms AI-silent (Oct 2025); AI chatbot section only in privacy policy (full)](#wegmans)
V13. [Giant Eagle - AI Recipe Generator: AI-silent terms (Aug 2024), no AI document found (browser capture)](#gianteagle)
V14. [McDonald's - Archy AI drive-thru (pilot): no terms reach the drive-thru; online terms revised Aug 2026 and still AI-silent (browser capture)](#mcdonalds)
V15. [Chipotle - Pepper chatbot + AI phone ordering: AI-silent terms (Aug 2025); 2026 off-purpose/jailbreak incident; phone channel has no assent (full)](#chipotle)
V16. [Yum! Brands (Taco Bell) - Voice AI drive-thru: AI-silent terms that still describe a human "team member taking the order" (browser capture)](#yum)
V17. [Domino's - AI phone ordering ("Dom"): 2017 terms name Dom (data terms only, no accuracy disclaimer); Aug-2026 privacy says data sold may train third parties' LLMs (full)](#dominos)
V18. [Casey's - AI phone ordering + Darn-ell chatbot: AI-silent terms revised Mar 2026; phone channel has no assent (browser capture)](#caseys)
V19. [Ulta Beauty - Ulta AI: dedicated AI language in T&C incl. "not authorized to make any promises" (anti-apparent-authority); matching FAQ microcopy; ADMT notice (full)](#ulta)
V20. [Bath & Body Works - Gingham Genius: AI subsection s.5.D in Terms (Jan 2025, right after launch) + strong generic post-purchase price-revocation clause (full)](#bathbodyworks)
V21. [Kinney Drugs - "Burt" AI pharmacy voice/text assistant + Ask Burt vaccine chat: TWO dedicated AI terms; consent-by-phone-number; $100 cap; July 2026 VTDigger incident (full)](#kinney)
V22. [Warby Parker - customer-service virtual agent + Virtual Advisor: terms AI-silent (Apr 2026); AI named only in privacy policy (Jun 2026) (full)](#warbyparker)
V23. [AT&T - GenAI assistant in new AT&T app (Mar 2026): app EULA and 2020 website terms both AI-silent; generic price-error cancellation clause (full)](#att)
V24. [T-Mobile - Ask AI in T-Life: main T&Cs revised Sep 2026 and still AI-silent, though the AI quotes plans and promotion eligibility (full)](#tmobile)
V25. [Cox Communications - Oliver chat / Olive voice: AI clause in Customer Service Agreement (Jan 2025) that discloses AI and ADM but disclaims nothing (browser capture)](#cox)
V26. [Gap Inc. - AI customer-care digital assistant: AI-silent terms (Feb 2025) with strong generic post-order cancellation clause (full)](#gap)
V27. [American Eagle Outfitters - AI Chatbot: s.21 "AI Chatbot Disclosure" in Terms (Jun 19, 2026) with express no-liability for chatbot errors (full, PDF)](#americaneagle)
V28. [Abercrombie & Fitch - AI Stylist: brand-named "AI Tools" section (Jul 2023) - not liable for reliance; AI Response "does not necessarily represent" A&F's recommendation (browser capture)](#abercrombie)
V29. [J.Crew - AI Shopping Assistant (beta): AI-silent terms (Sep 2024) (browser capture)](#jcrew)
V30. [Bank of America - Erica: dedicated Erica section in Online Banking Service Agreement - user must confirm Erica's actions; voice-authorized-as-yours; non-generative by design (full)](#bankofamerica)
V31. [Citigroup - GenAI Enhanced IVR (phone pilot): voice channel, no terms at the call; governing documents not located (partial)](#citi)
V32. [U.S. Bancorp - Smart Assistant: Digital Services Agreement "Use of artificial intelligence" - expressly disclaims all liability for reliance on AI information; trains on inputs (full, undated)](#usbank)
V33. [Truist - Truist Assist: 250k-char Online & Mobile Banking Agreement (Apr 2026) never mentions AI, the assistant, or chat (full, PDF)](#truist)
V34. [Duke Energy - app AI chatbot + AI Bill Insights: AI-silent site terms (Apr 2023); chat only in a feedback-licence clause (full)](#dukeenergy)
V35. [PG&E - "Peggy" AI voice assistant (replaced IVR): phone channel, no assent; website terms not located (partial)](#pge)
V36. [Exelon (ComEd, PECO, BGE, Pepco...) - Chat Assistant: standalone Chat Assistant T&Cs that never say "AI"; text near-identical to BofA's Erica terms (full, PDF, undated)](#exelon)
V37. [Edison International (SCE) - AskSCE chatbot: 2019 website terms (chat mentioned only as a site service); 19-document legal hub has nothing for the chatbot (full)](#edison)
V38. [Caesars Entertainment - Ivy AI text concierge: SMS opt-in at check-in; terms not retrievable (site blocked to scripts and browser) (snippet-only)](#caesars)
V39. [Hyatt - generative natural-language search on Hyatt.com: Terms & Conditions bot-walled (scripts and browser); snippet shows searches/chats licensed to Hyatt (snippet-only)](#hyatt)
V40. [Vanguard - GenAI Voicebot (PoC): standalone "Vanguard Voicebot Terms of Use" (Feb 2026) - Output not Vanguard's assertions, not an offer, no fiduciary duty; output unreviewed (full); + GenAI Features Terms (Jul 2026) and Online Terms added on re-coding](#vanguard)
V41. [Wayfair - virtual assistant + Muse: "Chatbots and Use of Generative AI" section (Jan 2026) - verify pricing in Output; Output not attributable to Wayfair; no liability for inaccurate AI info (browser capture)](#wayfair)
V42. [Williams-Sonoma - Olive sous-chef agent + Agentforce support agents: Legal Statement (Apr 2026) mentions AI only to ban model training on WSI content (browser capture)](#williamssonoma)
V43. [Bob's Discount Furniture - BobBot (Quiq): terms page does not render (scripts time out; browser shows empty body) - not located (referenced-not-located)](#bobs)
V44. [Southwest Airlines - Agentforce AI assistant (refunds, policies): site terms 2017 + Contract of Carriage Sep 2026 both AI-silent - a near-replica of the Moffatt setting (full)](#southwest)
V45. [Best Buy - gen-AI virtual assistant: Terms (Sep 25, 2026) declare AI/chat statements about terms or policies "void and non-binding" - an express anti-Moffatt clause; AI liability carve-in; user-agent rules (browser capture)](#bestbuy)
V46. [Newegg - AI Mode shopping assistant: Policy Agreement updated Jul 2026 (after AI Mode launch) still AI-silent; AI Mode landing screen shows no disclaimer (full)](#newegg)
V47. [DICK'S Sporting Goods - Coach by DICK'S (agentic, May 2026): AI-silent terms (Mar 2024); a human-employee no-authority clause but none for the AI agent (browser capture)](#dicks)
V48. [Michaels - Ask Mike (live since May 2026): Terms & Conditions (Mar 2025) and Privacy Statement (Dec 2025) both AI-silent (browser capture)](#michaels)
V49. [Intuit (TurboTax) - Intuit Assist: "Digital Assistants" section in TurboTax ToS (TY2025, v.02122026) - user solely responsible for outcomes of AI use; sits beside a calculation-accuracy guarantee (full)](#intuit)
V50. [Electronic Arts - EA Help AI chat (intake bot): User Agreement (May 2026) AI-silent (full)](#ea)
V51. [Roblox - Assistant / AI chat features: "AI Features" section ("You, not Roblox, are responsible"), training licence on Prompts/Outputs; no AI accuracy clause; version dated Nov 1, 2026 (browser capture)](#roblox)
V52. [Gen Digital (Norton) - Norton Genie: LSA (Jan 2026) names Genie only for Norton Money (not advice, not a fiduciary); no detection-accuracy clause for Genie scam checks; Smart Chat subject to OpenAI's terms (full)](#gendigital)
V53. [Camping World - "Arvee" virtual agent: terms (Jun 2025) AI-silent; firm publishes an "AI Info" page for LLMs, not for customers (full)](#campingworld)
V54. [LegalZoom - Doc Assist AI: standalone "AI Additional Terms" (Dec 2024) + clickwrap at upload + ToS acknowledgement of AI use (full)](#legalzoom)
V55. [Rocket Lawyer - Rocket Copilot: standalone "Terms of the Rocket Copilot Service" (Nov 2024) - experimental, AS-IS, user assumes responsibility for AI errors; general terms AI-silent (browser capture)](#rocketlawyer)
V56. [Fidelity - Virtual Assistant: dedicated section in Terms of Use (Jul 1, 2026) - not a recommender, cannot trade, not advice; contact-page microcopy contradicts the Terms on data use (full)](#fidelity)
V57. [Charles Schwab - Schwab Assistant (virtual agent): AI-silent website terms; how-to page suggests keyword-style bot (full)](#schwab)
V58. [Equity Residential (now "Vivmark Residential") - Ella / digital leasing agents: s.13 "Artificial Intelligence" (Aug 2026) - no liability for any loss from reliance; user must confirm accuracy; output "does not represent our views" (full)](#equityresidential)
V59. [AvalonBay - EliseAI leasing assistant: current terms are post-merger Vivmark terms (Aug 17, 2026) identical to EQR's s.13 AI clause; pre-merger AvalonBay terms needed (full)](#avalonbay)
V60. [Neighborly (Molly Maid) - AI Receptionist that quotes prices and books via Neighborly APIs: brand-wide terms (Sep 2023) AI-silent (full)](#neighborly)
V61. [Synchrony - Sydney virtual assistant (white-labeled for retail card partners): site terms and online credit-site terms (2021) AI-silent (full)](#synchrony)
V62. [Ally Financial - Ally Assist (voice/text, executes transfers): Online Banking Services Agreement and Deposit Agreement (Aug 2026) never mention it or AI (full)](#ally)
V63. [Rocket Companies - Rocket AI Agent (Rocket.com): group Terms of Use (Jul 2025, rocketmortgage.com) AI-silent; strong generic disclaimer on model-generated home values (full)](#rocket)
V64. [NiSource (Columbia Gas, NIPSCO) - chatbot: Columbia Gas Terms (Oct 2025) define "Website" to include "chat/chatbots" so generic disclaimers reach them; no AI-specific language (full)](#nisource)
V65. [Vail Resorts - My Epic Assistant: Epic Pass policies (website terms, terms of sale, privacy) AI-silent across all tabs; app page has no disclaimer (browser capture)](#vailresorts)
V66. [Life Time - L•AI•C AI health companion + AI chatbots: Terms of Use (May 30, 2024) name OpenAI GPT-3.5/Azure; not responsible for incorrect AI info; user solely responsible - paragraph appears copied from a B2B chat-vendor template (full)](#lifetime)
V67. [Topgolf - AI Player Assistant (Sierra): Terms (Nov 2023) and Privacy (Oct 2026) both AI-silent (full)](#topgolf)
V68. [Macy's - Ask Macy's (Gemini agent, Mar 2026): Terms of Use Legal Notice AI-silent; strong generic post-order correction/cancellation clause (browser capture)](#macys)
V69. [Nordstrom - natural-language search: Terms (May 27, 2026) disclose AI-generated product descriptions (incl. safety warnings) may contain errors; nothing on the search assistant (browser capture)](#nordstrom)
V70. [Labcorp - MyLabcorp AI results explanations: User Agreement (Jul 22, 2026) s.6 "Use of LLMs and AI" - not a source of truth; sole risk; not for clinical decisions; may not reflect Labcorp's views (full)](#labcorp)
V71. [Quest Diagnostics - Quest AI Companion (Gemini, Mar 2026): Terms & Conditions AI-silent; disclaimer lives only in a MyQuest FAQ ("may make mistakes") (full + browser capture; full-read addendum: questhealth article registered as DGX-04 - consent click-through, B10 S; governing MyQuest terms gated/unfetched)](#quest)
V72. [Signet Jewelers (Kay, Zales, Jared, Blue Nile) - LivePerson chatbot: group Terms of Use (Oct 2024) AI-silent (full)](#signet)
V73. [Kendra Scott - GenAI shopping assistant (iAdvize Copilot): Terms (Jun 22-23, 2026) mention "chat" only as a contact channel; privacy calls it a "virtual chat feature"; no AI language (full)](#kendrascott)
V74. [Tractor Supply - website AI assistant (OpenAI): terms blocked to scripts and browser ("Access Denied") - not located; existence confirmed by CIO quote (referenced-not-located)](#tractorsupply)
V75. [Netflix - generative AI conversational search (opt-in beta): Terms of Use (Apr 2026) mention ML only to ban users training models on Netflix content (full)](#netflix)
V76. [Snap - My AI: Terms of Service (Sep 21, 2026) s.6 "AI Features" - "Outputs are not Snap representations"; as-is; don't rely for any purpose; names My AI as a Service (full)](#snap)
V77. [Roku - AI-upgraded Roku Voice (conversational Q&A, Oct 2025): Products Terms of Use (Oct 2020) cover voice only as data collection; no AI language; Roku Services Agreement not located (browser capture)](#roku)
V78. [Pinterest - Pinterest Assistant: ELIGIBILITY FLAG (develops own foundation models: Canvas, Navigator-1); Terms (Nov 2026 version) contain zero AI language (full)](#pinterest)
V79. [Match Group (Tinder, Hinge) - AI photo selector / Prompt Feedback: Tinder Terms (Mar 2026) "AI Technology" - user solely responsible for AI-generated content; training licence ("cannot unlearn"); Hinge Terms (Aug 2025) ML-only (full)](#matchgroup)
V80. [1-800-Flowers.com - intelligent virtual assistant (hybrid with agents): Terms of Use (Jun 2025) AI-silent; generic post-order correction clause (browser capture)](#1800flowers)
V81. [H&R Block - AI Tax Assist: Terms of Use "AI and Automated Features" - solely responsible, no warranty, liability disclaimed - while marketing says AI Tax Assist is "backed by" the 100% accuracy guarantee; wording near-identical to Intuit's (browser capture)](#hrblock)
V82. [Avis Budget Group - AI customer-support agent (Decagon): Terms (Dec 2023) AI-silent; privacy (Dec 2025) discloses ML biometric ID verification for QuickPass but nothing on the support agent (full)](#avis)
V83. [Turo - multilingual AI virtual agent (Voiceflow): Terms of Service revised Jun 24, 2026 still AI-silent; web chat covered only by a recording-consent clause (full)](#turo)
V84. [Metropolis - computer-vision checkout-free parking (auto-charge): Terms (Jul 2026) describe its "vision AI" Recognition Platform at length but contain no clause on misreads or wrong charges; refunds discretionary (full)](#metropolis)
V85. [ODP Corp (Office Depot/OfficeMax) - Oracle Digital Assistant chat: Terms of Use (May 18, 2026) AI-silent; generic order-cancellation for pricing errors (full)](#odp)
V86. [Liberty Media (Formula 1) - F1 fan companion agent (Agentforce, Mar 2026): F1.com Legal Notices AI-silent; English law (UK operating subsidiary) (browser read)](#libertymedia)
V87. [Six Flags - GenAI virtual assistant (Vertex AI Conversation): Terms of Use (Oct 2025, post-merger) AI-silent (full)](#sixflags)
V88. [Nerdy (Varsity Tutors) - AI chat tutoring / Live+AI: Terms (Oct 2025) one AI sentence - users acknowledge AI may operate "without direct human oversight"; no accuracy disclaimer (full)](#nerdy)
V89. [ThredUp - Style Chat + AI image search: Terms of Use (Jul 2025) "AI Features" section - user solely responsible for evaluating accuracy; no accuracy guarantee; ThredUp owns AI-generated content made from user content (browser capture)](#thredup)
V90. [PayPal - PayPal Assistant: User Agreement (Sep 2026) mentions AI only to require verification of AI-generated arbitration filings; in-chat disclaimer "AI can make mistakes, so double-check responses" (full)](#paypal)
V91. [Block (Cash App) - Moneybot (agentic AI): Terms of Service carry s.XXII "Generative AI Terms of Use" + "AI-Powered Interactions" - no advice, no fiduciary duty, user confirms every AI-suggested action (full)](#block)
V92. [Remitly - AI-powered virtual support assistant: User Agreement (Feb 2026) AI-silent (full)](#remitly)
V93. [Royal Caribbean - virtual assistant in chat: Digital Terms of Use & EULA (Mar 2023) AI-silent; strong generic clause to cancel bookings made at erroneous rates (full)](#royalcaribbean)
V94. [Norwegian Cruise Line - Nora GenAI itinerary assistant: NCL terms hub (Jan 26, 2026; ~440k chars incl. guest ticket contract) AI-silent (full)](#norwegian)
V95. [Barnes & Noble - Ada AI support agent: Terms of Use (Sep 2024) AI-silent; generic price-error clause (may cancel, or honor "to the benefit of the User") (full)](#barnesnoble)
V96. [Coursera - Coursera Coach (Gemini): Terms of Use (Jan 1, 2026) s.10 - AI services AS IS; "you must verify any AI outputs"; not responsible for inaccurate AI outputs; Honor Code bans unauthorized gen-AI use (full)](#coursera)
V97. [Upbound (Rent-A-Center) - Digital Assistant chatbot: no general terms of use on the site; AI disclosed only in privacy policy (Sep 2026) incl. AI risk models using income and biometric data (browser capture)](#upbound)
V98. [Live Nation (Ticketmaster) - virtual assistant for fan support + Agentforce venue agents: Ticketmaster Terms of Use (Aug 2025) AI-silent (browser read)](#livenation)
V99. [2U (edX) - Xpert AI learning assistant: edX Terms of Service & Honor Code (Nov 2025) AI-silent in body (full)](#2u)
V100. [Lyft - customer care AI assistant (Claude via Bedrock): Terms (Feb 2026) add "artificial intelligence tools" to the Lyft Platform definition so generic terms reach it; no AI-specific clause (full)](#lyft)
V101. [UPS - UPS Virtual Assistant (AI chatbot): Website Terms of Use AI-silent (browser read)](#ups)
V102. [FedEx - FedEx Virtual Assistant: website Terms of Use AI-silent (full)](#fedex)
V103. [KOA - KOA AI chatbot: chat onboarding says AI "may occasionally generate incorrect or misleading information" and use is "covered by our Terms of Service" - but those Terms were last updated in 2011 (full)](#koa)
V104. [Greystar - AI leasing chatbots (EliseAI; Microsoft-GPT site chatbot): US terms AI-silent; only AI text is a privacy-statement "AI tools" section; UK sister brand has full dedicated AI terms with anti-attribution (proxy) (full)](#greystar)
V105. [CVS Health / Aetna - Aetna generative-AI conversational navigation (Oct 2025 beta): Aetna Digital Terms of Use revised June 24, 2026 still AI-silent; CVS terms AI-silent (full)](#cvs-health)
V106. [The Cigna Group - myCigna generative-AI Virtual Assistant (June 2025): Terms of Use v2.2 (June 4, 2026) mention AI only to bar USERS from AI scraping; silent on Cigna's own assistant (browser capture)](#cigna)
V107. [eHealth - "Alice" AI voice agent (Medicare calls, 2025): Terms of Use (Sep 25, 2025) expressly reach "telephone call centers" but are AI-silent; generic oral-advice non-warranty clause reaches Alice; privacy AI-silent (browser capture)](#ehealth)

### Re-capture pass (2026-10-09)
R1. [Full-text re-capture log: 26 excerpt-only documents now preserved in full; 15 previously unsaved or unlocated documents captured; Cox CSA URL now redirects to Spectrum terms; remaining gaps](#recapture-2026-10-09)
R2. [Gap-fill pass 2: legal hub completed (Verizon, Comcast, Chime), binding status + vintage for all full-text docs, ~38 more full-text captures, Aetna Live Chat AI clause verified via Wayback (since removed), 11 documented gaps](#gapfill-2026-10-09)
R3. [Full-text pass 3: t6 marketing/incident documents, MyQuest FAQ and State Farm privacy notice captured; 96% full-text coverage; 11 non-public gaps](#fulltext-pass3-2026-10-09)
R4. [User-supplied Hyatt and Bob's terms; app-only/in-product microcopy declared out of scope (disclosed); 3 remaining gaps](#usersupplied-2026-10-09)
R5. [Full-read coding Batches 11–12: 127 rows coded line-by-line; corrections to earlier archive claims (Airbnb, Chime, Cigna, Verizon, HGV, State Farm); principal findings; COX-01 partial status; adjudication record](#fullread-batch11-12-2026-10-09)
R6. [Privacy-notice fallback pass: 18 privacy notices for Silent main-sample firms read in full; no locus change; 10 firms now disclose AI outside the contract](#privacy-fallback-2026-10-14)

---


---

---
<a name="walmart"></a>
company: Walmart
document_title: Walmart.com Terms of Use â€” Section 16.J "Chatbots and Use of Generative AI"
document_type: dedicated AI section within governing product/service terms
url: https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0
retrieved: 2026-08-02
effective_or_revised: Last Updated June 23, 2026
names_ai_feature: yes â€” defines "Chatbot," "Generative AI," and "Generative AI Features" as formal terms
ai_vector: generative
fetch_depth: full-fetch
clause_codes_present: B6, B4, B3, B2(via general LoL), B1(pricing non-binding), B10, B9
vendor: in-house (Sparky)
---

## Full coding-relevant extract

**Defined terms (introduction).** "Generative AI" = "artificial intelligence, including large language models made by us or third parties, capable of generating new text, images, or other media." "Chatbot" = "an application feature or interface by which you are able to engage in voice or text communications that are intended to mimic human interactions and conversations, including through the use of Generative AI and third-party large language models." "Walmart Sites" explicitly includes "Chatbots and other Generative AI Features."

## Section 16.J â€” Chatbots and Use of Generative AI (full text)

"The Walmart Sites may include Chatbots and other Generative AI, and Materials on the Walmart Sites may be generated by Generative AI (the 'Generative AI Features'). The Generative AI Features are subject to the following additional terms.

- Due to the nature of Generative AI, the information, responses and recommendations generated for you and other users through Generative AI Features (collectively, the 'Output') may not be accurate, complete or up-to-date and may be misleading or contain errors and omissions, or the Generative AI Features may misunderstand the Content that you input (the 'Input') and may be responding to a different question than asked. **You should review and verify the Output before making any purchases, engaging in other transactions from the Walmart Sites, or taking any other action based on any such Output.**

- Pricing information generated by Generative AI Features may be inaccurate, incomplete, or out of date. **Pricing information provided by Generative AI Features does not constitute an offer to sell the item at the stated price or acceptance of an offer to purchase the item at the stated price.** Refer to Walmart's Terms of Use at Section 8.B. Pricing Information; Availability for further information on item pricing.

- Unless an associated disclosure states otherwise, the Output may be based on information available on Walmart.com or provided by manufacturers, suppliers, or sellers of items, Walmart service providers, customer reviews, or other publicly available information, and third-party AI models. **None of these sources have been verified by Walmart.** Any views or opinions expressed in the Output do not necessarily reflect those of Walmart and should not be attributed to Walmart.

- Using the Generative AI Features to produce violent, abusive, or deceptive content or to otherwise cause harm is strictly prohibited. You are also prohibited from attempting to 'break' or 'trick' the Generative AI Features into disregarding safeguards or other features or messages aimed to protect the public.

The Output provided by the Generative AI Features are intended for general informational purposes only. **You should not use any Output provided by the Generative AI Features as the basis for making any legal, safety, health, regulatory, or similarly important decision. Users of the Generative AI Features are solely responsible for independently verifying and evaluating the Output, and for any decisions they make based on the Output.**"

## Related general clauses (Section 2 / 3 / 11)
- Prohibits using data mining/robots to gather Materials "or use any Materials to develop, train, or improve any artificial intelligence or machine learning model" without Walmart's consent (B9 â€” protects Walmart's content from third-party AI training).
- Broad Content License over user-submitted Content/Ideas (perpetual, royalty-free, sublicensable) (B10).
- General warranty disclaimer and limitation-of-liability sections (17, 18) referenced but not independently re-quoted here â€” Section 16.J layers AI-specific language on top of these.

## Coder note
The single strongest AI-specific liability clause found across both the original 6-company corpus and this expanded batch, comparable to or exceeding Delta's dedicated AI Terms of Service. Contains all three of the highest-value clause codes: B4 (explicit anti-reliance: "review and verify... before making any purchases"), B3 (explicit responsibility shift: "solely responsible for independently verifying"), and B1 (AI-generated pricing does not constitute a binding offer â€” directly closes the exact fact pattern in *Moffatt v. Air Canada*, where a chatbot's price/policy representation was treated as binding). This is the clearest "inoculated" case in the full corpus to date.


---

---
<a name="amazon"></a>
company: Amazon
document_title: Conditions of Use â€” Rufus/Alexa for Shopping AI-specific clause not located
document_type: governing product/service terms
url: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM
retrieved: 2026-08-02
effective_or_revised: Last updated May 30, 2025 (per search snippet; predates or coincides with Rufus's continued scale-up)
names_ai_feature: not confirmed â€” no AI/Rufus-specific language located
ai_vector: generative â€” exposure not assessable without full document access
fetch_depth: snippet-only (direct fetch blocked by robots.txt disallow)
clause_codes_present: B6, B2 (generic only, from available snippets)
vendor: in-house (Rufus, renamed "Alexa for Shopping" May 2026)
---

## What was retrieved (snippet-only)

General warranty disclaimer: "TO THE FULL EXTENT PERMISSIBLE BY LAW, AMAZON DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. AMAZON DOES NOT WARRANT THAT THE AMAZON SERVICES, INFORMATION, CONTENT, MATERIALS, PRODUCTS (INCLUDING SOFTWARE) OR OTHER SERVICES INCLUDED ON OR OTHERWISE MADE AVAILABLE TO YOU THROUGH THE AMAZON SER[VICES...]" (snippet truncated).

License restrictions: prohibits "any collection and use of any product listings, descriptions, or prices," "any derivative use of any Amazon Service or its contents," and "any use of data mining, robots, or similar data gathering and extraction tools."

## What was NOT found

No section, defined term, or clause referencing "Rufus," "Alexa for Shopping," "generative AI," "chatbot," or "AI" of any kind was located in available Conditions of Use snippets, despite Rufus's scale (~300M+ users, ~$12B annualized incremental sales per press coverage) and despite the same search approach successfully surfacing Walmart's, Target's, and other companies' AI-specific clauses.

## Coder note
**This is a genuine, high-confidence gap, not a confirmed absence.** The direct fetch was blocked by Amazon's robots.txt, so only search-engine-indexed snippets were available â€” meaning sections deep in the document (which is typically long, with numbered subsections on many topics) could exist without surfacing in snippets. However, the fact that targeted searches for "Rufus... terms," "generative AI... terms," and similar combinations consistently returned marketing/press/seller-forum content rather than any clause of the Conditions of Use itself is itself informative: if a Rufus-specific clause existed, it would likely be a well-indexed, frequently-linked section (as Walmart's and Target's AI clauses were). This should be flagged as the **single highest-priority follow-up** in the retail batch â€” ideally via a non-robots-blocked mirror, a legal-database aggregator (e.g. a ToS-tracking service), or manual review.


---

---
<a name="homedepot"></a>
company: Home Depot
document_title: HubSpace App Terms of Use (2020) â€” adjacent document; Magic Apron governing terms not located
document_type: adjacent app terms (smart-home product, NOT Magic Apron) + open item on main site ToU
url: https://www.homedepot.com/hdus/en_US/DTCCOMNEW/fetch/THD-App-Terms-of-Use-6-4-2020-Final.pdf
retrieved: 2026-08-02
effective_or_revised: June 4, 2020 â€” approximately 5 years before Magic Apron's March 2025 launch
names_ai_feature: no (predates Magic Apron entirely; governs a different product â€” the HubSpace smart-home device app)
ai_vector: n/a for this document; Magic Apron's actual governing terms remain unconfirmed
fetch_depth: full-fetch (of this adjacent document only)
clause_codes_present: B6, B4(gen), B2, B7, B10(gen), B9(gen)
vendor: in-house (Magic Apron)
---

## What was retrieved (HubSpace App Terms â€” NOT Magic Apron's governing document)

This is Home Depot's Terms of Use for the **HubSpace app** (controls smart-home devices), dated 2020 â€” included here only because it demonstrates Home Depot's generic disclaimer style and because no Magic-Apron-specific or main-site governing document could be located within the query budget. Key generic clauses:

**Warranty disclaimer / no reliance (B6, B4-generic).** "THE HOME DEPOT MAKE[S] NO REPRESENTATION ABOUT THE SUITABILITY OF THE MATERIALS ON THIS APP FOR ANY PURPOSE. ALL SUCH MATERIALS ARE PROVIDED 'AS IS' WITHOUT WARRANTY OF ANY KIND..." Also: "YOU MAY NOT ACT OR RELY ON ANY INFORMATION OR MATERIALS IN THIS APP AND YOU PARTICULARLY SHOULD NOT MAKE ANY INVESTMENT DECISIONS BASED ON ANY INFORMATION OR MATERIALS IN THIS APP. YOU MUST INDEPENDENTLY VERIFY THE ACCURACY OF ALL SUCH INFORMATION AND MATERIALS BEFORE ACTING OR RELYING THEREON..." â€” a real anti-reliance clause, but written for financial/investment-decision contexts on a 2020 smart-home app, not for a 2025 conversational shopping assistant.

**Limitation of liability (B2).** No direct/indirect/punitive/incidental/special/consequential damages; New Jersey carve-out for negligent/reckless acts.

**Indemnification (B7).** Standard user-indemnifies-Home-Depot clause for submitted content.

**IP over submissions (B10-generic).** Perpetual, irrevocable, royalty-free, transferable license over submitted content (photos, etc.), same family as Walmart/T-Mobile/Domino's submissions clauses.

**Arbitration (B9-adjacent).** Binding AAA arbitration, Atlanta GA venue, individual-capacity-only claims.

## Coder note
**Genuine open item, not a finding.** Home Depot's press coverage extensively confirms Magic Apron is powered by "advanced large language model tools" and is "grounded in [Home Depot's] proprietary knowledge base," but no governing consumer document specific to Magic Apron â€” nor a confirmed main homedepot.com Terms of Use with AI-specific language â€” was located within this session's query budget. The 2020 HubSpace terms above predate Magic Apron by 5 years and govern an unrelated product; they should NOT be cited as evidence of how Home Depot treats Magic Apron liability. Highest-priority follow-up: locate and fetch the actual homedepot.com/c/Terms_of_Use (or equivalent) page directly.


---

---
<a name="lowes"></a>
company: Lowe's
document_title: Terms & Conditions of Use for Lowe's Websites
document_type: governing product/service terms (site + Personal Account + PRO Account + MyLowe's Rewards, comprehensive)
url: https://www.lowes.com/l/about/terms-and-conditions-of-use
retrieved: 2026-08-02
effective_or_revised: Effective Date July 15, 2026 â€” approximately 15 months after Mylow's May 2025 launch
names_ai_feature: no â€” confirmed AI-silent after full-document review
ai_vector: n/a (no AI-specific provisions found anywhere in the document)
fetch_depth: full-fetch (entire document, including Marketplace, Content/UGC, Warranty/LoL, Indemnification, Dispute Resolution, Registered User, Personal Account, and PRO Account sections)
clause_codes_present: B6, B2, B7, B10(gen), B8(Marketplace)
vendor: OpenAI (Mylow, customer-facing) â€” distinct from associate-facing "Mylow Companion," which is out of scope as internal/employee-facing
---

## Coding-relevant extract

**AI mentions: NONE.** The word "Mylow" does not appear anywhere in this document. This is confirmed via full-document review (not a sampling of snippets) â€” the fetched page includes every major section: Introduction, Your Use of the Site, Placing Orders, Lowe's Online Marketplace Program, Copyrights, Links to Other Sites, Content, User-Generated Content, DMCA, Warranty Disclaimer/Limit of Liability, Indemnification, Dispute Resolution/Arbitration, Changes to Terms, Miscellaneous, Registered User Terms, Personal Account/MyLowe's Rewards Terms, and PRO Account/MyLowe's Pro Rewards Terms. None reference AI, chatbots, virtual advisors, or Mylow specifically.

**Warranty Disclaimer; Limit of Liability (B6, B2 â€” generic, the provision that would have to reach Mylow if anything does).** "YOU ASSUME ALL RESPONSIBILITY AND RISK FOR THE USE OF THE SITE... THE SITE IS PROVIDED 'AS IS' AND 'AS AVAILABLE'... LOWE'S... DISCLAIM[S] ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, IMPLIED WARRANTIES OF TITLE, NONINFRINGEMENT, ACCURACY, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE." Also: "NO OPINION, ADVICE OR STATEMENT BY LOWE'S OR LOWE'S LICENSORS, SUPPLIERS, ADVERTISERS, SPONSORS, AGENTS, MEMBERS OR VISITORS, WHETHER MADE ON THE SITE OR OTHERWISE, SHALL CREATE ANY WARRANTY." This last clause is broad enough that it plausibly reaches a Mylow statement (as a statement made "on the Site"), but it is entirely generic â€” no chatbot, AI, or virtual-advisor language anywhere near it.

**Information Posted on the Site.** "Lowe's cannot and does not guarantee the accuracy or completeness of the Materials displayed on the Site, including, without limitation, prices, product images, specifications, dimensions, availability and services... The Materials may contain technical inaccuracies, typographical errors, and errors or omissions related to the product descriptions, pricing and availability." Again generic â€” could be read to cover Mylow's outputs as "Materials," but not written with AI in mind.

**Indemnification (B7).** Standard user-indemnifies-Lowe's clause.

**Content License (B10-generic).** Worldwide, perpetual, irrevocable license over Content the user submits/generates through use of the Site, "including without limitation any analytics, summaries, programs, improvements, derivative works, compilations and outputs" â€” broad enough in principle to sweep in a user's Mylow chat inputs, though written generically for all site content.

**Marketplace disclaimer (B8).** Lowe's not liable for Marketplace Sellers' products/actions â€” a third-party carve-out, structurally similar to but not the same as an AI carve-out.

## Coder note
This is the **cleanest confirmed-AI-silent governing document in the entire corpus to date** â€” unlike Klarna or T-Mobile (where the "silent" finding initially rested on the wrong document), this is Lowe's actual, current (July 2026), comprehensive site-wide Terms & Conditions, read in full, and it simply never mentions its own AI product. The 15-month gap between Mylow's launch and this document's effective date (which nonetheless doesn't add AI language) is a strong vintage-vs-launch signal in the same family as the T-Mobile T&Cs finding from the earlier corpus. **Locus (Axis A): position 4 (generic clause only, AI unnamed) â€” arguably closer to Klarna's original (corrected) profile than to Walmart's dedicated Section 16.J.**


---

---
<a name="target"></a>
company: Target
document_title: Terms & Conditions â€” "Agentic Commerce and Delegated Access" section
document_type: dedicated agentic-AI clause within governing product/service terms
url: https://www.target.com/c/terms-conditions/-/N-4sr7l
retrieved: 2026-08-02
effective_or_revised: LAST UPDATED April 15, 2026 (press coverage places the substantive revision at March 22, 2026)
names_ai_feature: yes â€” defines "Agentic Commerce Agent" as a formal term
ai_vector: generative/agentic (third-party AI agents, e.g. Google Gemini, acting on the customer's behalf) â€” distinct from any Target-native shopping-recommendation chatbot
fetch_depth: full-fetch
clause_codes_present: B4, B3, B2(via general LoL), B7(via general indemnification), B5
vendor: Google Gemini (Agentic Commerce Agent, via Universal Commerce Protocol) â€” third-party, not Target's own generative assistant
---

## Full text â€” Agentic Commerce and Delegated Access

"The terms in this section apply if you expressly authorize an agent powered through AI ('Agentic Commerce Agent') to access and perform certain functions in your Target account on your behalf. Only Agentic Commerce Agents expressly approved by you and by Target are considered Agentic Commerce Agents. Other automated or unauthorized agentic tools are expressly prohibited.

By enabling an Agentic Commerce Agent, you expressly authorize that Agent to act on your behalf in your Target account. These permissions may include signing in to your account, creating or modifying carts, placing orders, and initiating returns, subject to any limits you approve. **Actions taken by an Agentic Commerce Agent within the scope of your approved permissions will be treated as actions authorized by you.** You are responsible for reviewing activity performed by your Agentic Commerce Agent and for promptly notifying the Agentic Commerce Agent and Target of any activity you believe is unauthorized or outside the scope of permissions you approved.

You may revoke an Agentic Commerce Agent's access at any time through the account settings in your Target profile. Upon revocation, the Agent will no longer be permitted to act on your behalf. Target may suspend or revoke an agent's access, in whole or in part, if we detect suspected fraud, misuse, policy violations, security concerns, or other activity that may pose risk to you or to Target.

**Target is not responsible for the conduct of the third-party Agentic Commerce Agent.** Your use of the Agentic Commerce Agent may also be subject to that Agent's separate terms and conditions. Authorizing an Agentic Commerce Agent does not make that Agent an employee, partner, or representative of Target.

By authorizing an Agentic Commerce Agent, you consent to Target sharing necessary account, order, and transaction information with that agent consistent with Target's Privacy Policy.

**Purchases and other actions taken by an Agentic Commerce Agent that you have authorized are considered transactions authorized by you.** Target will evaluate disputes involving Agentic Commerce Agent based on the permissions in effect at the time of the transaction, applicable account protections, relevant evidence of authorization, and applicable law.

**Target does not purport to guarantee that an Agentic Commerce Agent will act exactly as you intend in all circumstances.** You should review orders, account activity, and settings regularly."

## Related clause â€” Unlawful or Prohibited Uses
Explicitly carves out "approved Agentic Commerce Agents" from the general prohibition on using "any engine, software, tool, agent, data, or other device or mechanism (including browsers, spiders, robots, avatars, or intelligent agents)" to navigate/search the Site â€” i.e., an authorized Agentic Commerce Agent is affirmatively permitted where other automated tools are banned.

## Related clause â€” Your Account
"You agree to accept responsibility for all activities that occur under your account or password, **including when using an Agentic Commerce Agent**" â€” reinforces the responsibility-shift language.

## Coder note
This is a genuinely distinct clause type from anything else in the corpus (Klarna's "User-Assigned Agent" clause is the closest precedent). Two things worth flagging for the taxonomy:
1. **This governs a THIRD-PARTY AI (Google Gemini via UCP), not a Target-built assistant.** Target explicitly disclaims responsibility for "the conduct of the third-party Agentic Commerce Agent" â€” structurally different from Walmart's Section 16.J, which governs Walmart's *own* Generative AI Features.
2. **B3 (user-responsibility shift) is present and strong** ("actions... will be treated as actions authorized by you"; "considered transactions authorized by you") â€” but paired with an explicit acknowledgment that the agent may not "act exactly as you intend," which is an unusually candid admission of expected error sitting directly next to the clause that assigns the customer full responsibility for that error.
3. Whether Target's separate, non-agentic recommendation tools (Gift Finder, Shopping Assistant) have their own governing language was not confirmed within this session â€” this document covers only the agentic-commerce surface.



---

# AIRLINE GENERATIVE ASSISTANT BATCH
*Retrieved 2026-08-11. Source documents preserved under `mastersheet-sources/airlines/`.*

---
<a name="delta"></a>
company: Delta Air Lines
document_title: AI Terms of Use
document_type: dedicated standalone AI terms
url: https://www.delta.com/us/en/legal/ai-terms-of-use
retrieved: 2026-08-11
effective_or_revised: no effective/revision date stated in the document
names_ai_feature: partially - by CATEGORY, not by brand. Defines "AI Tools" as "generative AI tools and features, such as chatbots and AI-powered search, Reservations Interactive Voice Response and messaging". The string "Concierge" appears ZERO times.
ai_vector: generative (chat, AI search, IVR voice, messaging)
fetch_depth: full-fetch
clause_codes_present: B6, B4, B3, B2, B7, B10, B8, B9
vendor: in-house deployment; names Visa Run Inc. (d/b/a "Sherpa") and IATA as Output sources
files: mastersheet-sources/airlines/delta/delta_ai-terms-of-use_RAW.html (+ .txt)
       delta_site-terms-of-use_RAW.html, delta_privacy-policy_RAW.html
---

## Coding-relevant extract

**Scope and assent.** The AI Terms bind by use: using the AI Tools means you "agree to be bound by these AI Terms, the Terms of Use and any other applicable terms and policies." Age floor of 16.

**B6 - accuracy/no-warranty.** Responses are "artificially generated and may contain inaccuracies." AI Tools provided "AS IS" and "AS AVAILABLE"; Delta "does not give any warranties and disclaims all responsibility for any inaccuracies in Outputs."

**B4 - anti-reliance (directive, all-caps).** "YOU SHOULD NOT RELY SOLELY UPON OUTPUTS FOR ANY PURPOSE OR USE OUTPUTS TO INFORM IMPORTANT DECISIONS. IF YOU PLAN TO USE OUTPUTS FOR ANY REASON, IT IS YOUR SOLE RESPONSIBILITY TO VERIFY THE OUTPUTS." Body text adds a human fallback: if Output conflicts with other official information, contact a Delta Reservations specialist.

**B3 - user-responsibility shift.** "YOU - NOT DELTA - ARE RESPONSIBLE FOR YOUR USE OF, AND ANY ACTIONS YOU TAKE IN RELATION TO, OUTPUT GENERATED BY THE AI TOOLS BASED ON YOUR PROMPTS."

**B2 - limitation of liability.** No lost profits/revenue/data, no consequential, special, indirect, exemplary, punitive or incidental damages, on any theory including negligence.

**B7 - indemnification.** User indemnifies Delta for use of AI Tools, breach, or violation of third-party rights.

**B10 - training on prompts.** Prompts + Outputs + Feedback are collectively "your Content"; user retains IP in Prompts, but Delta may use Content "including to train artificial intelligence models and machine learning algorithms," via automated or human review and third-party vendors.

**B8 - third-party source carve-out (named).** Section 3 names delta.com, Sherpa and IATA as Output sources; none "can guarantee and make no representation or warranties about the accuracy of, and accept no liability for, information about travel restrictions or visa and entry requirements."

**B9 - anti-jailbreak / anti-training.** Prohibits using Service content "for AI training or identifying people"; also prohibits claiming "any output from the Service as human-generated if it is not."

## Coder note
1. **Locus 1 - dedicated standalone AI Terms.** Corpus benchmark alongside Walmart Sec 16.J.
2. **The AI apparatus is fully segregated.** Delta's site Terms of Use was separately fetched and is AI-SILENT (0 hits across 12,841 chars for AI keywords). All AI liability language lives in the dedicated document.
3. **Named by category, not by brand.** Despite "Delta Concierge" being the marketed product, the binding document never names it - it governs "AI Tools" generically. This is a say-do asymmetry worth coding: the marketing names a persona, the contract names a category.
4. **NO B1.** Delta has no transaction-error non-honoring clause - no analogue to Walmart's "pricing information... does not constitute an offer to sell." The direct Moffatt fact pattern is addressed by anti-reliance only, not by an express refusal to honor AI-stated terms.
5. Privacy policy contains 1 "automated decision" hit - B11 not yet extracted (open item).


---
<a name="united"></a>
company: United Airlines
document_title: Terms, Conditions and Legal Notices for united.com
document_type: site terms of use
url: https://www.united.com/en/us/fly/legal.html
retrieved: 2026-08-11
effective_or_revised: none stated; in-body copyright notice reads 2018 (page footer 2026)
names_ai_feature: NO - confirmed AI-silent across the complete document
ai_vector: generative (Every Flight Has a Story - AI-written delay explanations, GenAI added 2024)
fetch_depth: full-fetch (browser-rendered; direct HTTP timed out repeatedly)
clause_codes_present: B6, B2, B7, B10 - all generic, none AI-specific
vendor: AWS "Mars" platform per press coverage; not named in the terms
files: mastersheet-sources/airlines/united/united_legal-terms-conditions-notices.txt
---

## Coding-relevant extract

**Confirmed silence.** Keyword scan over all 16,881 chars: 0 hits for "artificial intelligence", "generative", "chatbot", "AI", "machine learning". The single "automated" hit is "automated device" in the anti-scraping clause.

**B6/B2 - generic liability disclaimer.** Content "may include inaccuracies or typographical errors"; provided "as is" without warranty of any kind; full exclusion of direct, indirect, punitive, incidental, special and consequential damages.

**B7 - indemnity.** Standard user-indemnifies-United clause.

**B10 - inbound communications.** Emails to United are non-confidential and United may reproduce/publish/use them freely. No Prompt/Input/Output language of any kind.

**Assent.** Browsewrap - bound "by accessing and using this website." No click-through described.

**Incorporation.** Contract of Carriage is incorporated and GOVERNS on conflict; not captured this pass.

## Coder note
1. **Strongest vintage-vs-launch gap in the batch.** In-body copyright 2018; generative AI added to Every Flight Has a Story in 2024. The governing terms predate the AI deployment by roughly six years and never mention it.
2. **United demonstrably knows how to write anti-reliance language** - it wrote a directive one for its Currency Converter ("United advises the User to consult a qualified professional to verify the accuracy"). It did not write one for AI-generated flight information. This is a sharper finding than mere absence.
3. **Do not miscode the "chat rooms" clause.** The Forums section governs user-to-user bulletin boards and chat rooms, not an AI chatbot. It must not be counted as a generic clause reaching an AI feature.
4. **Scope caveat.** Every Flight Has a Story generates delay explanations pushed TO customers rather than a surface customers converse with. It is customer-facing AI output but not a conversational assistant - a modality distinction worth carrying in the dataset rather than silently flattening.


---
<a name="american"></a>
company: American Airlines
document_title: American Airlines Platform terms and conditions - Section 15 "Artificial Intelligence Tools"
document_type: governing product/service terms (site + app + retail outlets)
url: https://www.aa.com/i18n/customer-service/support/legal-information.jsp
retrieved: 2026-08-11
effective_or_revised: effective January 1, 2026
names_ai_feature: partially - defines "Artificial Intelligence Tool", "AA AI Tool", "Third Party AI Tool", "Inputs", "Outputs"; no consumer AI product named by brand
ai_vector: generative + agentic (definition expressly covers "generative, agentic, or otherwise")
fetch_depth: full-fetch (browser-rendered, 46,610 chars; direct HTTP returns 403)
clause_codes_present: B6, B4, B3, B2, B7, B10, B8, B9, B5
vendor: unnamed third-party service providers referenced at 15(c) and 20(a)
files: mastersheet-sources/airlines/american/american_platform-terms-conditions.txt
---

## Coding-relevant extract

**Definition (2(g)) - B5 foundation.** An "Artificial Intelligence Tool" is any tool relying on "artificial intelligence (whether generative, agentic, or otherwise) machine learning, large language models, or other similar or successor technologies." American's own are "AA AI Tools"; anything else is a "Third Party AI Tool."

**B5 - agentic gate, inverted vs Target.** Before using any Third Party AI Tool the customer "must verify that the third party provider... has obtained American's express written consent" - approvals routed through AIRequest@aa.com. Where an authorized third-party tool acts for the customer, "you assume all responsibility for such usage or access."

**B6 - AI-specific warranty disclaimer (Sec 10(a)).** Drafted to name AI expressly: "YOU USE THE AMERICAN PLATFORMS AND ACCESS THE CONTENT, INCLUDING AI TOOLS AND OUTPUTS... AT YOUR OWN RISK"; AS IS / AS AVAILABLE.

**B6/B4 (Sec 15(d)).** Outputs may be "inaccurate or otherwise not fit for use (including from a legal or business perspective)"; "American Airlines assumes no responsibility and disclaims all warranties in any Outputs. Before using any Output, you should carefully review all Outputs to ensure that each Output meets your needs."

**B3 (Sec 15(b)).** User is responsible for ensuring Inputs are appropriate, non-infringing, and free of confidential/personal data.

**B2 - hard cap.** Aggregate liability capped at USD 500 where limitation provisions are otherwise held unenforceable.

**B10 (Sec 15(e)).** American and its vendors may "access, use and store any Inputs and Outputs" and use them "for machine learning purposes" to develop, train, fine-tune and improve the tools and platforms.

**B9.** Sec 6(n) bars using Content to train any Third Party AI Tool; Sec 7(b)(x) bars using the Platforms or Content "for any Artificial Intelligence Tool training purposes"; Sec 6(m) bars unauthorized Third Party AI Tools from making or managing bookings or managing an AAdvantage account.

## Coder note
1. **Locus 2 - dedicated AI section inside general terms.** Structurally the Marriott pattern, but far more developed.
2. **The agentic regime is the inverse of Target's.** Target lets the CUSTOMER authorize a third-party agent (Gemini) and treats its actions as the customer's own. American requires the VENDOR to be pre-approved by American, and places the verification burden on the CUSTOMER (2(e)) to confirm that approval exists. Both end at the same place - the customer bears the consequences - by opposite routes. This pairing is the best agentic contrast in the corpus so far.
3. **AI-aware drafting throughout, not bolted on.** AI language appears in the definitions (2(g)), the misuse list (6(m)-(n)), the commercial-use bar (7(b)(x)), the warranty disclaimer (10(a)), the dedicated section (15) and the vendor clause (20(a)). Effective January 2026 - genuinely current.
4. No B1 transaction-error non-honoring clause.


---
<a name="alaska"></a>
company: Alaska Airlines (+ Hawaiian, post-acquisition; legal pages co-branded "Alaska Hawaiian")
document_title: (a) Alaska Inspires in-product microcopy; (b) Contract of Carriage
document_type: (a) in-product disclaimer/microcopy; (b) contract of carriage
url: https://www.alaskaair.com/nls/destination ; https://resource.alaskaair.net/v3/assets/blt2cefe12c88e9dd91/blta6d545d0295aad57/CoC%20English
retrieved: 2026-08-11
effective_or_revised: CoC reported Revised May 26, 2026 - NOT verified in the PDF text layer
names_ai_feature: no binding document names it; named only in on-screen microcopy
ai_vector: generative (natural-language/voice destination search, Azure OpenAI / Microsoft Foundry)
fetch_depth: microcopy full-fetch (rendered); CoC full-fetch (PDF preserved); privacy policy referenced-not-located; site ToU not located
clause_codes_present: B6 (weak), B4 (hedged)
vendor: Microsoft Azure OpenAI - infrastructure vendor; Alaska is the deployer
files: mastersheet-sources/airlines/alaska-hawaiian/alaska_CAPTURE-NOTE.md
       alaska_contract-of-carriage_ENGLISH.pdf (839,251 bytes)
---

## Coding-relevant extract

**The entire AI-liability apparatus, verbatim:**
"This Generative AI powered experience can make mistakes. Consider checking important information."

**Contract of Carriage.** Full text searched for artificial intelligence, AI, generative, chatbot, virtual assistant, automated system, algorithm, machine-generated content. **Zero hits.**

**Assent gap.** The AI surface links to a Privacy Policy and a cookie policy and to NO terms of use, conditions of carriage, or AI terms. No click-through, no "by using this you agree," no incorporation by reference at the point of the AI interaction.

## Coder note
1. **Locus 4 - microcopy-only, in-product.** Weakest posture in the batch and the closest structural analogue to Moffatt in the airline vertical.
2. **"Consider checking" is permissive, not directive.** Contrast Walmart ("must review and verify the Output before making any purchases") and Delta ("IT IS YOUR SOLE RESPONSIBILITY TO VERIFY THE OUTPUTS"). Coupled with the absence of any assent mechanism at the AI surface, there is very little on which to found a consumer verification duty.
3. **Recently-revised binding contract that stays AI-silent** - if the reported May 2026 CoC revision holds, Alaska revised its passenger contract roughly a year after launching the first guest-facing GenAI tool in the US airline industry without adding any AI language. Verify the date against the PDF cover page before publishing.
4. **ACCESS CAVEAT - do not read gaps as findings.** alaskaair.com and its CDN serve a fixed 3,038-byte Akamai client challenge to every non-browser client. The privacy policy could not be read by any available route, so **B11 is UNTESTED for Alaska** - not absent.
5. Hawaiian carried as part of the combined entity; no Hawaiian-specific AI feature or terms sought this pass.


---
<a name="frontier"></a>
company: Frontier Airlines
document_title: Privacy Notice - section "Use of AI-Assisted Customer Interactions"
document_type: privacy notice (carrying an operative liability disclaimer)
url: https://www.flyfrontier.com/legal/privacy-policy/
retrieved: 2026-08-11
effective_or_revised: Privacy Notice in-body copyright 2023; Terms of Use in-body copyright 2020 (both page footers 2026)
names_ai_feature: yes in the privacy notice; NO in the Terms of Use and NO in the Contract of Carriage
ai_vector: hybrid (generative + rules) - Cognigy-powered chat; Frontier eliminated telephone customer service in favour of AI chat
fetch_depth: full-fetch (ToU, privacy notice, CoC landing page, CoC PDF 1.2 MB)
clause_codes_present: B6, B4, B3, B2 (privacy notice); B6, B2 generic (ToU)
vendor: Cognigy - B2B vendor; its ToS does NOT bind the consumer and is excluded as evidence
files: mastersheet-sources/airlines/frontier/frontier_privacy-policy_RAW.html (+ .txt)
       frontier_terms-of-use_RAW.html, frontier_contract-of-carriage_ENGLISH.pdf
---

## Coding-relevant extract

**From the Privacy Notice, section "Use of AI-Assisted Customer Interactions":**

Disclosure: Frontier "may use automated and artificial intelligence-enabled systems to assist with certain customer interactions, including through chat, voice, and other customer care channels."

**B6 + B4.** "AI-assisted systems may occasionally generate responses that are incomplete, inaccurate, or outdated. Customers are encouraged to verify important information, including flight details, schedules, fares, and policies, through Frontier Airlines' website or with a live customer service representative."

**B3/B2 - the operative shift.** "By engaging with Frontier Airlines' AI-assisted services, you (i) acknowledge and agree that, to the extent permitted by law, Frontier is not responsible for errors or misunderstandings that may result from reliance on AI-generated responses."

**Terms of Use (separate document).** AI-silent - 0 AI keywords across 4,052 chars. Carries only generic AS IS warranty disclaimer and a broad limitation of liability. In-body copyright 2020.

**Contract of Carriage.** AI-silent.

## Coder note
1. **NEW LOCUS TYPE - liability language inside a privacy notice.** This does not fit the existing five-point locus spectrum. An express liability disclaimer and a use-based assent trigger ("By engaging with... you acknowledge and agree") are placed in a disclosure instrument rather than in the contract. **Recommend extending the locus spectrum to capture this**, since it is a materially different drafting choice from all ten companies coded so far.
2. **Enforceability is genuinely questionable.** A privacy notice is conventionally a disclosure document, not a bilateral contract; substantive liability terms buried in one are weak. Frontier's actual Terms of Use - the document that would normally carry this - remains AI-silent with a 2020 copyright.
3. **Aggravating context for the say-do gap.** Frontier eliminated telephone customer service in favour of AI chat, making the AI the primary support channel. Yet the disclaimer tells customers to verify "with a live customer service representative" - the very channel Frontier removed. This internal contradiction is the sharpest finding in the batch.
4. **"Encouraged to verify" is hedged**, like Alaska's "consider checking" - not directive like Walmart's or Delta's.
5. **Vendor exclusion applied.** Cognigy's own terms are a B2B agreement between Cognigy and Frontier; the consumer never saw or agreed to them. Only Frontier's own consumer-facing documents are treated as evidence here, per project rule.


---

# FOOD-DELIVERY GENERATIVE ASSISTANT BATCH
*Retrieved 2026-08-11. Source documents preserved under `mastersheet-sources/food-delivery/`.*

---
<a name="instacart"></a>
company: Instacart (Maplebear Inc.)
document_title: Instacart Terms of Service - Section 5.2 "AI Features"
document_type: governing consumer terms
url: https://www.instacart.com/terms
retrieved: 2026-08-11
effective_or_revised: not stated on page
names_ai_feature: partially - defines "AI Features", "Inputs", "Outputs", "AI Agents"; "Ask Instacart" appears ZERO times
ai_vector: generative + agentic (definition expressly names "large language models, agentic AI")
fetch_depth: full-fetch (87,680 chars; raw HTML preserved)
clause_codes_present: B6, B4, B3, B10, B8, B9, B5
vendor: "Some AI Features may be powered by third-party technology providers" - unnamed
files: mastersheet-sources/food-delivery/instacart/instacart_terms-of-service_RAW.html (+ .txt)
---

## Coding-relevant extract

**Definition (5.2).** AI Features are automated systems and means "including large language models, agentic AI, and other AI technologies" used to "generate, summarize, rank, recommend, or assist with information, content, or actions."

**B6 + B4 - accuracy and anti-reliance.** "AI outputs may be incomplete, inaccurate, outdated, inappropriate, or inconsistent and may change over time. They are not a substitute for professional advice (including medical, legal, financial, business, or safety advice). Use your own judgment and verify important information before relying on it."

**B3 - user responsibility.** "You are responsible for your use of Outputs and any decisions or actions you take based on them."

**Variability clause (unusual).** Results "may differ across users and time and are not guaranteed to be identical or consistent" - a hedge against consistency claims that no other company in the corpus has.

**B10 + OWNERSHIP (distinctive).** User retains rights in Inputs, but "Instacart owns all AI-generated content ('Outputs')." User gets only a personal, non-commercial use right and "does not acquire any ownership interest in Outputs or any rights in the underlying models, algorithms, datasets, or technology." Inputs/Outputs/interactions may be processed to "improve the Services."

**B8.** IP non-warranty: "We do not promise that Outputs or any AI-assisted results will be free of third-party rights."

**B5 - agent attribution.** Section 4.3 extends every technical restriction to "you-and any person or system you authorize, permit, enable, deploy, delegate to, or otherwise cause to access or use the Services (including household members, employees, contractors, recipients, and any Automated Systems or AI Agents)."

**B9.** Anti-reverse-engineering including "by tracking inputs and outputs to mimic or recreate system behavior"; robots.txt expressly "incorporated into these Terms by reference."

## Coder note
1. **Locus 2 - dedicated AI section inside general terms.** Strongest posture in the food-delivery batch and among the better-drafted clauses in the corpus.
2. **The ownership posture is the standout finding.** Delta lets users retain Prompts and takes a licence; American makes users responsible for Inputs. Instacart goes further and **claims outright ownership of Outputs**. For a shopping assistant whose Output is a cart, this is worth flagging: the company owns the recommendation and simultaneously disclaims all responsibility for its accuracy.
3. **Category-not-brand naming again** - the third consecutive vertical where the marketed product name never appears in the binding document (cf. Delta Concierge, AA AI Tools).
4. The "verify important information before relying on it" formulation is directive but softer than Delta's all-caps SOLE RESPONSIBILITY construction.


---
<a name="ubereats"></a>
company: Uber Technologies (Uber Eats)
document_title: General Terms of Use (US) + "Generative AI features at Uber"
document_type: governing consumer terms + separate AI disclosure page
url: https://www.uber.com/legal/en/document/?name=general-terms-of-use&country=united-states&lang=en ; https://www.uber.com/legal/en/document/?name=generative-ai-features-at-uber&country=united-states&lang=en
retrieved: 2026-08-11
effective_or_revised: ToU not stated; **AI page last modified 6/18/2025**
names_ai_feature: no - "Cart Assistant" appears in neither document
ai_vector: generative + agentic (Cart Assistant builds carts on the user's behalf)
fetch_depth: full-fetch both (ToU 92,935 chars; AI page 5,975 chars; raw HTML preserved for both)
clause_codes_present: B6, B4, B10, B8 (AI page); B6, B2 generic (ToU)
vendor: names Google, OpenAI, Meta as possible model providers; menu item descriptions built with Meta Llama 3
files: mastersheet-sources/food-delivery/ubereats/uber_general-terms-of-use-US_RAW.html ; uber_generative-ai-features-at-uber_RAW.html
---

## Coding-relevant extract

**The only AI sentence in the binding ToU:** "Some content, features, or interactions within the Services may be generated or enhanced by artificial intelligence technologies. For more information, please visit Generative AI Features at Uber."

**From the separate AI page (B6).** "GenAI can make mistakes and provide misleading, outdated or incorrect information. This includes responses that do not reflect Uber's views, policies or accurately reflect our relationship with our users."

**B4.** "Our GenAI features are not specifically trained to provide legal, financial, medical or nutritional advice and shouldn't be relied upon for these purposes. You should always independently check answers provided by GenAI features before relying on any output." Plus item-level cautions on product safety/allergens, medical advice, and dietary information.

**Near-B1 pricing clause.** "Pricing information provided or used to generate responses is an estimate and excludes taxes, Service Fees and promotions. Please refer to the checkout page for the most accurate information." - the closest thing to a transaction-error clause in this batch, but it stops short of Walmart's express "does not constitute an offer to sell."

**B10 / B8.** Inputs "may be shared with such third parties in order to provide the responses you request"; inputs "may be used to further train and improve our products, but will not be used to separately train other third-party models." Where models are trained on protected content "their output may contain the intellectual property of others."

## Coder note
1. **Split locus, and the split is the finding.** Uber has the most detailed consumer-facing AI disclaimer in the batch sitting in the document with the **weakest claim to bind**. The ToU cross-reference reads "For more information, please visit" - signposting language, not incorporation language ("subject to", "governed by", "incorporated by reference"). Code the binding status as contested rather than assuming the AI page is contractual.
2. **Vintage gap against the AI, not just the terms.** The AI page was last modified **18 June 2025**; Cart Assistant launched **February 2026**. The AI document predates the agentic feature by roughly eight months and contains **no agentic or delegated-authority language at all** - nothing addressing an AI that builds and modifies a cart on the customer's behalf. Contrast American Â§15 and Instacart Â§4.3, both of which do.
3. Neither document names Cart Assistant.
4. The pricing-estimate clause deserves separate tracking as a partial-B1: it disclaims accuracy of AI-stated prices and redirects to checkout, which is functionally protective, but it does not refuse to honor an AI-stated price the way Walmart's clause does.


---
<a name="doordash"></a>
company: DoorDash
document_title: Consumer Terms and Conditions (+ Help Center article "Meet Your New AI Assistant")
document_type: governing consumer terms + unincorporated help article
url: https://help.doordash.com/en-us/legal/article/cx-terms-and-conditions ; https://help.doordash.com/en-us/consumers/article/meet-your-new-ai-grocery-assistant
retrieved: 2026-08-11
effective_or_revised: **Consumer Terms effective July 1, 2026**
names_ai_feature: no - "Ask DoorDash" appears ZERO times in the Terms
ai_vector: generative (conversational discovery, meal planning, cart building)
fetch_depth: full-fetch both (Terms 137,289 chars; article 5,890 chars; raw HTML preserved for both)
clause_codes_present: B9 + AI-content disclosure (Terms); B6, B4, B3 (help article only)
vendor: AWS Bedrock / Anthropic Claude per published case study - not named in any consumer document
files: mastersheet-sources/food-delivery/doordash/doordash_consumer-terms-JUL2026_RAW.html ; doordash_ai-grocery-assistant-help-article_RAW.html
---

## Coding-relevant extract

**All three AI references in the binding Terms:**

1. **B9 - anti-training.** Users may not use the Services or its content "in connection with the development of any software program, including, but not limited to, training a machine learning or artificial intelligence (AI) system."
2. **AI-content disclosure tied to a merchant carve-out.** Merchant "menu, product, or catalog listings, descriptions, or other information (including videos, photographs, or images, or nutrition, ingredient, and/or allergen information) displayed through the Services may not have been provided directly by the Merchant and/or **may have been generated or enhanced with the assistance of artificial intelligence**. DoorDash has no responsibility or liability for acts or omissions by any Merchant or Contractor."
3. **AI review summaries.** "We may create summaries of written Reviews using artificial intelligence or other means and display such summaries." No liability language attached.

**Nothing in the Terms governs the accuracy of the assistant's own Output.**

**From the Help Center article (NOT the contract).** "AI can make mistakes: The Assistant is powered by AI and can make mistakes"; "Informational use only: All AI-generated responses and suggestions are provided for reference only"; "Always review the items in your cart to ensure they fit your specific requirements, quantities, and dietary needs before checking out"; not-a-substitute-for-medical-advice; "Always verify the physical packaging for the most accurate information regarding safety, nutrition, and ingredients (especially regarding allergens)." The article then states: "your use of this feature is governed by the DoorDash Consumer Terms, Privacy Policy, and all other DoorDash policies."

## Coder note
1. **The circularity is the finding.** The help article says the feature is "governed by" the Consumer Terms; the Consumer Terms contain no assistant-output clause. Every disclaimer a consumer actually reads lives in an unincorporated support article. This is structurally similar to Frontier's privacy-notice placement in the airline batch - operative language parked outside the contract - and reinforces the case for extending the locus spectrum.
2. **Strongest "recent but selectively silent" case in the corpus.** The Terms took effect **1 July 2026, after Ask DoorDash launched**, and DoorDash plainly had AI in mind while drafting - it wrote three AI provisions. It protected its own content from AI training and disclosed that merchant listings may be AI-generated, but wrote nothing governing its own assistant's accuracy. The asymmetry looks deliberate rather than accidental: the AI clauses that exist all run in DoorDash's favour.
3. **Allergen exposure is material.** The sharpest verification instruction in the whole batch - check physical packaging for allergen information - sits in the unincorporated article, not the contract.
4. Separate SMS assent exists for the text-message channel ("you agree to receive recurring automated text messages"), which is a narrower and more conventional consent than anything covering AI output.


---
<a name="gopuff"></a>
company: Gopuff (GoBrands, Inc.)
document_title: GoBrands End-User License and Terms of Service + Privacy Center
document_type: governing consumer terms + privacy notice
url: https://www.gopuff.com/e/terms-and-conditions ; https://legal.gopuff.com/policies/en
retrieved: 2026-08-11
effective_or_revised: **Terms last updated December 13, 2024**
names_ai_feature: NO - confirmed AI-silent in both documents
ai_vector: generative + agentic (Go predicts and pre-builds a cart; one-tap checkout)
fetch_depth: full-fetch both via browser (Terms 68,717 chars; Privacy 31,764 chars). Raw HTML NOT preservable - both hosts return HTTP 403 to non-browser clients
clause_codes_present: none AI-specific. B11 tested and CONFIRMED ABSENT
vendor: **xAI / Grok - third party.** xAI's own terms are a B2B agreement and do NOT bind the consumer
files: mastersheet-sources/food-delivery/gopuff/gopuff_CAPTURE-NOTE.md
---

## Coding-relevant extract

**Terms & Conditions keyword scan over the complete rendered document:** artificial intelligence 0 Â· generative 0 Â· chatbot 0 Â· machine learning 0 Â· automated 0 Â· Grok 0 Â· xAI 0 Â· "AI " 0.

**Privacy Center keyword scan over the complete rendered document:** the same terms plus "automated decision" 0 and "profiling" 0.

**Open-ended incorporation clause (the one live avenue).** The preamble binds the user to the Agreement "TOGETHER WITH OUR PRIVACY POLICY ... AND ALL OTHER TERMS GOVERNING SPECIFIC GOPUFF PRODUCTS, SERVICES, OR MATERIALS, WHETHER OR NOT INCLUDED ON THIS PAGE (THE 'SUPPLEMENTAL TERMS')."

## Coder note
1. **Cleanest total silence in the corpus to date.** No AI language anywhere in Gopuff's consumer legal stack.
2. **Stronger evidentially than Alaska's silence.** Alaska's Contract of Carriage was confirmed silent but its privacy policy could not be read, leaving B11 untested. Here **both** documents were read in full, so B11 is a confirmed absence rather than a gap.
3. **Sharpest capability/contract inversion in the dataset.** Go is the most capable consumer AI in this vertical - agentic, predictive, one-tap checkout, built on Grok - and it sits behind the least AI-aware contract. The Terms were last updated **December 2024, roughly eighteen months before Go launched in June 2026**, and have not been revisited since.
4. **Vendor exclusion applied.** Press reporting that the integration prevents Grok from training on customer data describes a vendor arrangement between Gopuff and xAI. It is not a consumer-facing term, the consumer never saw or agreed to it, and it is excluded as evidence per project rule.
5. **Open item.** Go-specific "Supplemental Terms," if any exist, would be swept in by the open-ended incorporation clause. None were located within the query budget - logged `referenced-not-located`, not confirmed absence.



---

# BANKING GENERATIVE ASSISTANT BATCH
*Retrieved 2026-08-11. Source documents preserved under `mastersheet-sources/banking/`.*

---
<a name="wellsfargo"></a>
company: Wells Fargo
document_title: Online Access Agreement (governing) + General Terms of Use (site)
document_type: governing online banking agreement + site terms of use
url: https://www.wellsfargo.com/online-banking/online-access-agreement/ ; https://www.wellsfargo.com/privacy-security/terms/
retrieved: 2026-08-11
effective_or_revised: **Online Access Agreement Version Effective May 21, 2026**
names_ai_feature: by CATEGORY only. ToU defines "Chatbot" = "a bot, chatbot, virtual assistant, virtual concierge, or other non-human". The assistant "Fargo" is NOT named in the OAA - every occurrence of the string is "Wells Fargo" the company.
ai_vector: generative, task-constrained (in-app assistant)
fetch_depth: full-fetch both (OAA 185,457 chars; ToU 17,577 chars; raw HTML preserved)
clause_codes_present: B6 (thin, availability-scoped), B2, B7, B10 (monitoring); PROTO-B1 x2
vendor: none named in consumer documents
files: mastersheet-sources/banking/wells-fargo/wellsfargo_online-access-agreement_RAW.html ; wellsfargo_general-terms-of-use_RAW.html
---

## Coding-relevant extract

**The definitional hook (this is what makes the generic clauses reach the AI).** "Online Financial Service" is defined to include "Each product or service you may access or enroll in through the Website, including the Mobile Banking Service and **any chat, virtual assistant, or similar service that may be available**."

**PROTO-B1 (a) - channel denied legal effect (ToU).** "Participating in the Chat service does not constitute consent by you or us to use electronic records and signatures as a substitute for written documents."

**PROTO-B1 (b) - transaction type barred from the channel (OAA).** "You will not provide, and we cannot accept, trade instructions in any chat, virtual assistant, or similar service."

**B6 - thin and availability-scoped (ToU).** "Wells Fargo makes no warranty that the Chat service will be available at any particular time or be free of fault or error." Also: "The Chat service is provided as a convenience."

**Chatbot disclosure (ToU).** "During your use of the Chat service, you may interact with a bot, chatbot, virtual assistant, virtual concierge, or other non-human (each, a 'Chatbot'). We will disclose the use of the Chatbot to the extent required by applicable law."

**B10 - monitoring.** "Any conversations with us through use of chat, virtual assistant, or a similar service are monitored, recorded, analyzed, and retained by Wells Fargo and our service providers, potentially without any further notice to you."

**B2 / B7 via OAA §19.** No warranties express or implied; no warranty the Service will be "uninterrupted or error free"; limits on liability and obligations; indemnification.

## Coder note
1. **The most interesting liability architecture in the corpus so far, and a distinct strategy type.** Every other company that addresses AI at all does so by disclaiming the accuracy of the OUTPUT. Wells Fargo instead **constrains the CHANNEL**: chat cannot produce binding electronic records, and cannot carry trade instructions at all. That removes the reliance interest rather than merely warning against it — arguably a more robust anti-*Moffatt* device than any accuracy disclaimer in the dataset, and it should be coded as a separate technique rather than squeezed into B1.
2. **Not a vintage-gap case.** The OAA is effective **May 2026** and reaches the assistant by live definition. Contrast United (2018), Gopuff (Dec 2024) and Dave (July 2026 but silent).
3. **Strongest assent posture in the corpus.** The OAA is an affirmative enrollment agreement, not browsewrap; the chat/VA channel is pulled inside it definitionally rather than by a separate AI consent.
4. **Category-not-brand naming again** — fifth consecutive vertical.
5. Accuracy language is genuinely thin: it addresses availability and "fault or error" of the *service*, not the correctness of what the assistant *says*. Wells Fargo's protection rests on the channel limits, not on B6.


---
<a name="capitalone"></a>
company: Capital One
document_title: Terms & Conditions + Digital Disclosures
document_type: site terms and conditions + disclosures index
url: https://www.capitalone.com/legal/terms-conditions/ ; https://www.capitalone.com/digital/disclosures/
retrieved: 2026-08-11
effective_or_revised: **Last modified 07/14/2026**
names_ai_feature: no. "Chat Concierge" appears ZERO times. The only AI string is inside a compelled California statutory notice.
ai_vector: generative + **agentic** (negotiates/transacts on auto-dealer properties)
fetch_depth: full-fetch both (T&C 17,091 chars; disclosures 5,732 chars; raw HTML preserved). Referenced "AI data disclosure" page NOT located.
clause_codes_present: none AI-specific; B11-adjacent (compelled training-data disclosure)
vendor: in-house; deployed on third-party dealer sites
files: mastersheet-sources/banking/capital-one/capitalone_terms-and-conditions_RAW.html ; capitalone_digital-disclosures_RAW.html
---

## Coding-relevant extract

**The entire AI content of both documents, verbatim, under the heading "NOTICE FOR CALIFORNIA RESIDENTS":**
"For information regarding the datasets used to train our generative artificial intelligence systems as required by the California Generative AI Transparency Act, please review our AI data disclosure."

It sits between boilerplate about credit-card joint applicants and the Delaware/Ohio/New York resident notices.

**Generic liability language only.** "Capital One assumes no liability for any errors or omissions"; third-party site disclaimers ("cannot make any representations respecting them").

**Absent:** no accuracy clause, no anti-reliance clause, no user-responsibility shift, no agentic or delegated-authority clause.

## Coder note
1. **New finding type: COMPELLED disclosure vs VOLUNTARY risk-shifting.** Capital One's only AI language exists because California AB 2013 (effective 1 Jan 2026) requires it, and it concerns **training data** — an input-side transparency duty — not output liability. It is filed in the compelled-notice bucket, not the risk-allocation bucket. **Going forward the dataset should code these separately**: a hit on "artificial intelligence" here signals regulatory compliance, not liability drafting, and a naive keyword-presence coding would badly overstate Capital One's posture.
2. **Recent document, agentic AI, still no clause.** Modified **14 July 2026**, well after Chat Concierge deployed. This is not staleness.
3. **Genuine scope question I could not resolve from the documents.** Chat Concierge runs on **dealer** websites, not capitalone.com. Whether capitalone.com's site Terms & Conditions reach a consumer transacting with Chat Concierge on a third-party dealer property is unestablished. Flag as an open legal question, not a coding gap — it may require the dealer-side terms to answer.
4. **Open item.** The referenced "AI data disclosure" page was not linked in the captured HTML and was not located within budget — `referenced-not-located`.


---
<a name="dave"></a>
company: Dave (Dave Inc.)
document_title: Terms of Use
document_type: governing consumer terms
url: https://dave.com/terms
retrieved: 2026-08-11
effective_or_revised: **Last Updated July 13, 2026**
names_ai_feature: NO - confirmed AI-silent
ai_vector: generative (DaveGPT, in-app assistant)
fetch_depth: full-fetch (58,584 chars; raw HTML preserved)
clause_codes_present: none AI-specific
vendor: none named; banking services via partner banks (Coastal Community Bank, Member FDIC)
files: mastersheet-sources/banking/dave/dave_terms-of-service_RAW.html (+ .txt)
---

## Coding-relevant extract

**Keyword scan over the complete document:** artificial intelligence 0 · generative 0 · chatbot 0 · virtual assistant 0 · machine learning 0 · large language 0 · automated 0 · DaveGPT 0.

## Coder note
1. **Sharpest recency gap in the entire corpus.** The terms were updated **13 July 2026 — roughly four weeks before retrieval — and still contain no AI reference at all**, despite DaveGPT being a named, marketed, consumer-facing generative assistant.
2. **This is the cleanest counterexample to the "they just haven't updated their terms yet" hypothesis.** United's silence sits behind a 2018 document and Gopuff's behind a Dec 2024 one, both of which predate their AI. Dave's document is *current*. Whatever explains the silence, it is not staleness.
3. **Heightened consumer-protection salience.** Dave serves cash-advance (ExtraCash) and checking customers. Erroneous AI statements about advance amounts, fees, or timing carry direct financial consequence for a population with thin liquidity buffers — the harm profile is closer to *Moffatt* than a restaurant recommendation is.
4. No AI-specific assent mechanism identified.
5. **Launch date (added 2026-09-30, `fetch_depth: snippet-only`):** DaveGPT was announced 16 Jan 2024 in an Aisera/Dave press release (https://investors.dave.com/news-releases/news-release-details/aisera-dave-launch-davegpt-generative-ai-customer-service). The July 2026 revision therefore came ~30 months after launch.


---

---
<a name="delta-2022"></a>
company: Delta Air Lines
document_title: Terms of Use + Privacy and Security - November 2022 pre-ChatGPT baseline
document_type: governing site terms + privacy notice (historical versions)
url: https://www.delta.com/us/en/legal/terms-of-use ; https://www.delta.com/us/en/legal/privacy-and-security
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: snapshots 2022-11-26 (ToU) and 2022-11-30 (privacy) - the latter is the exact day of the ChatGPT public release
names_ai_feature: NO - confirmed AI-silent in both documents
ai_vector: n/a in 2022 (Delta Concierge announced CES January 2025)
fetch_depth: full-fetch (Wayback `id_` raw modifier; RAW HTML preserved for both)
clause_codes_present: none AI-specific
vendor: n/a
files: previous-tos/airlines/delta/delta_site-terms-of-use_20221126120150_RAW.html (+ .txt) ; previous-tos/airlines/delta/delta_privacy-policy_20221130032232_RAW.html (+ .txt)
---

## Coding-relevant extract

**Keyword scan over both complete documents (body text only):** artificial intelligence 0 - generative 0 - chatbot 0 - virtual assistant 0 - machine learning 0 - large language 0.

The single "automated" hit across both documents is absent from the ToU entirely; the privacy policy's is not an AI reference.

**Comparison to the current version.** Delta's site Terms of Use is substantively unchanged between Nov 2022 and Aug 2026: 1,799 to 1,994 word tokens, and a token-level diff is dominated by navigation-menu chrome ("Rent A Car" becoming "Delta Rentals", "In-Flight" becoming "Onboard") rather than contract text. It remains AI-silent today, and it contains **no cross-reference to Delta's AI Terms of Use**.

## Coder note
1. **Clean pre-treatment baseline.** The privacy policy snapshot is dated 30 November 2022 - the day ChatGPT launched. This is the strongest possible "before" reading for the corpus.
2. **The orphan-document problem.** Delta is coded at Locus 1 (dedicated standalone AI Terms), the corpus's apparent best practice. But the governing site ToU never routes a consumer to that document, and has not been revised to do so in the ~18 months since the AI Terms appeared. **Locus 1 is not automatically stronger than Locus 2** - a dedicated document can be better drafted and worse attached. Recommend adding a separate *attachment / binding-status* judgment alongside the locus code, and re-testing the rest of the corpus for it (Walmart Section 16.J sits inside the ToU and does not have this problem).


---
<a name="united-2022"></a>
company: United Airlines
document_title: Terms, Conditions and Legal Notices for united.com - December 2022 baseline
document_type: governing site terms (historical version)
url: https://www.united.com/ual/en/us/fly/legal.html (the 2022-era path; the current document lives at https://www.united.com/en/us/fly/legal.html, which has no snapshots in the target window)
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: snapshot 2022-12-20; **in-body copyright notice reads 2018**
names_ai_feature: NO - confirmed AI-silent
ai_vector: n/a in 2022 (United added generative AI to "Every Flight Has a Story" in 2024)
fetch_depth: full-fetch (RAW HTML preserved)
clause_codes_present: B6, B2, B7, B10 - all generic, none AI-specific
vendor: n/a
files: previous-tos/airlines/united/united_legal-terms-conditions-notices_20221220171554_RAW.html (+ .txt)
---

## Coding-relevant extract

**Keyword scan:** artificial intelligence 0 - generative 0 - chatbot 0 - virtual assistant 0 - machine learning 0 - large language 0. The single "automated" hit is "any robot, spider or other automated device" in the anti-scraping clause.

**Identical clauses in 2022 and 2026.** All three of the following appear, in the same form, in both the Dec-2022 capture and the Aug-2026 live fetch:
- content "may include inaccuracies or typographical errors"
- provided "without warranty of any kind"
- users advised to "consult a qualified professional to verify the accuracy" **of the Currency Converter**

**Copyright marker:** "Copyright(c) 2018 United Airlines" in the 2022 capture; "Copyright(c) 2018 United Airlines" in the 2026 document.

## Coder note
1. **THE FROZEN DOCUMENT - the sharpest result in the diachronic pass.** United's governing terms carry the same 2018 in-body copyright notice and the same substantive liability clauses in December 2022 and in August 2026. The document did not lag behind the generative-AI era; it never moved through it at all.
2. **The template existed and was never pointed at the AI.** United wrote a *directive anti-reliance clause* - the exact drafting move that would have mattered in *Moffatt* - and aimed it at a **currency conversion widget**. It has never written one for the generative system it deployed in 2024 to explain flight delays to passengers. This is not a firm that lacks the drafting vocabulary; it is a firm that did not apply it here.
3. **This settles the staleness hypothesis for the vertical.** Read alongside the Dave finding (terms updated Jul 2026, still AI-silent), the two ends of the range now both point the same way: neither a current document nor a frozen one produces AI language absent a decision to write it.
4. **URL migration caution for the corpus.** The current document's URL has zero snapshots in the 2022 window; the historical version lives at a different path. Any future diachronic work must search for the 2022-era path rather than concluding "not archived" from the current URL.


---
<a name="american-2022"></a>
company: American Airlines
document_title: Legal information / Platform terms and conditions - October 2022 baseline, plus the January 2025 birth version of Section 15
document_type: governing platform terms (historical versions, two points in time)
url: https://www.aa.com/i18n/customer-service/support/legal-information.jsp
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: baseline snapshot 2022-10-17; birth-version snapshot 2025-01-16
names_ai_feature: NO in the 2022 baseline; YES from the Jan-2025 version onward (by category, not by brand)
ai_vector: generative (unbranded booking/search assistant; terms define "AA AI Tools")
fetch_depth: full-fetch both (RAW HTML preserved for both)
clause_codes_present: 2022 - none AI-specific (B6, B2, B7 generic). Jan-2025 - AI-specific Section 15 appears. Jan-2026 - B6, B4, B3, B10, B5 AI-specific
vendor: not named
files: previous-tos/airlines/american/american_legal-information_20221017155337_RAW.html (+ .txt) ; previous-tos/airlines/american/american_legal-information_BIRTH-VERSION_20250116002447_RAW.html (+ .txt)
---

## Coding-relevant extract

**2022 baseline keyword scan:** artificial intelligence 0 - generative 0 - chatbot 0 - machine learning 0 - large language 0. The document is substantive (28,973 chars of real contract text - indemnification, "AS IS", warranty disclaimers all present), so this is confirmed absence, not a capture failure.

**Birth-dating by binary search over the Wayback capture list:** "artificial intelligence" is absent at **2024-12-06** (43,750 bytes) and present at **2025-01-16** (75,094 bytes). The ~31 KB jump marks a wholesale document rewrite, not an insertion.

**Stage 1 (Jan 2025), ~5 mentions.** Section 15 "Artificial Intelligence Tools" appears in the table of contents. American "may offer or integrate certain artificial intelligence features as part of the American Platforms (each, an 'AI Tool')"; any AI Tool "is considered part of the American Platform." Also present is a *defensive* provision in Section 2 barring users from using the Platform "for any artificial intelligence training purposes," plus a clause assigning responsibility to a user who employs "an automated process, artificial intelligence tool, algorithm, software or other technical means" against the Platform.

**Stage 2 (effective 1 January 2026), ~20 mentions.** The section roughly quadruples and adds:
- **Future-proofed definition** - an "Artificial Intelligence Tool" is anything relying on AI "(whether generative, agentic, or otherwise) machine learning, large language models, or other similar or successor technologies."
- **B6** - the "AS IS" disclaimer is *explicitly extended* to name "AI TOOLS AND OUTPUTS," which the generic 2022 disclaimer did not reach by name.
- **B6/B4** - Outputs may be "inaccurate or otherwise not fit for use (including from a legal or business perspective)"; American "assumes no responsibility and disclaims all warranties in any Outputs"; the user must "carefully review all Outputs."
- **B3** - the user is responsible for all Inputs.
- **B10** - American and its third-party providers may use Inputs and Outputs to "develop, train, test, fine-tune, modify, improve or otherwise revise" its AI Tools.
- **B5** - "Third Party AI Tools" are defined, and a consumer's own agent requires American's **express written consent**, obtained via a named mailbox (AIRequest@aa.com), with the third party required to demonstrate development "in accordance with best practices in the artificial intelligence industry."

## Coder note
1. **The only two-stage escalation in the batch, and the shape is informative.** The first draft (Jan 2025) does little more than pull AI Tools inside the Platform definition. The rewrite a year later is where the actual risk allocation is written. A single-snapshot coding would have missed that the aggressive version is roughly seven months old.
2. **B5 is the standout.** American is the only carrier in the batch that anticipated consumers pointing *their own* agents at the airline - and it answered with a permission gate rather than a liability disclaimer. That is a categorically different move from the rest of the corpus and should be tracked as its own pattern.
3. **Defensive-before-protective ordering.** The clause barring users from training on American's content (an inbound, IP-protective move) appears in the same rewrite as, and is written more tightly than, the outbound consumer-facing accuracy language. Consistent with the anti-scraping-as-pre-history pattern in the 2022 baselines.


---
<a name="alaska-2022"></a>
company: Alaska Airlines (+ Hawaiian, post-acquisition)
document_title: Online privacy notice + Contract of Carriage - November 2022 baseline (PARTIAL)
document_type: privacy notice + contract of carriage (historical versions)
url: https://www.alaskaair.com/content/legal/privacy-policy ; https://www.alaskaair.com/content/legal/contract-of-carriage/rule-1
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: privacy notice snapshot 2022-11-30 (the exact ChatGPT launch day); CoC snapshot 2023-01-31 (the Nov-2022 capture returns 403)
names_ai_feature: NO - confirmed AI-silent in the privacy notice
ai_vector: n/a in 2022 (Alaska Inspires is a later Azure OpenAI deployment)
fetch_depth: privacy notice full-fetch; CoC full-fetch but off-target date; **site Terms of Use referenced-not-located**
clause_codes_present: none AI-specific
vendor: n/a
files: previous-tos/airlines/alaska-hawaiian/alaska_privacy-policy_20221130175505_RAW.html (+ .txt) ; previous-tos/airlines/alaska-hawaiian/alaska_contract-of-carriage_rule-1_20230131214401_RAW.html (+ .txt)
---

## Coding-relevant extract

**Keyword scan of the privacy notice:** artificial intelligence 0 - generative 0 - chatbot 0 - virtual assistant 0 - machine learning 0. Four "automated" hits, all data-handling: collecting data "through automated means" (cookies and similar technology) and "the availability of automated controls that enable users to delete data."

Both captures are verified substantive documents rather than challenge shells - the privacy notice returns 21 hits across "personal information / we collect / cookies", and the CoC page carries the full rule index including "Rule 8. Liability for Delays, Cancellations, and Denied Boarding" and "Rule 19. Additional Liability Limitations for International Carriage."

## Coder note
1. **The bot wall is not new.** `alaskaair.com` returned **HTTP 403 to the Wayback crawler across nearly every legal path in 2022**, exactly as it returns 403 to ordinary HTTP clients today (see `mastersheet-sources/README.md`). Alaska's terms have been unusually difficult to archive for at least four years - which is itself a finding about the auditability of this company's consumer contracts, and worth a sentence in the paper's methods section.
2. **Baseline is PARTIAL and must be coded as such.** Two paths returned 200 and were captured. The site Terms of Use was not located in 2022 and has not been located in 2026 - `referenced-not-located` in both periods. Do **not** code Alaska as confirmed AI-silent across its full document set; code the privacy notice as confirmed AI-silent and disclose the ToU gap.
3. **Date caveat on the CoC.** The Nov-2022 capture is a 403; the nearest 200 is 2023-01-31, two months after the target. Used as an approximate baseline and labelled accordingly.


---
<a name="frontier-2022"></a>
company: Frontier Airlines
document_title: Terms of Use + Privacy Policy - November 2022 baseline, plus the May 2026 birth version of the AI clause
document_type: governing site terms + privacy notice (historical versions, two points in time)
url: https://www.flyfrontier.com/legal/terms-of-use/ ; https://www.flyfrontier.com/legal/privacy-policy/
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: baseline snapshots 2022-11-02 (ToU) and 2022-11-16 (privacy); birth-version snapshot 2026-05-13
names_ai_feature: NO in the 2022 baselines; YES in the privacy notice from May 2026
ai_vector: hybrid (Cognigy-powered chat assistant, generative + rules)
fetch_depth: full-fetch all three (RAW HTML preserved)
clause_codes_present: 2022 - none AI-specific. 2026 privacy notice - B6, B4, plus a reliance disclaimer
vendor: Cognigy (not named in the consumer documents)
files: previous-tos/airlines/frontier/frontier_terms-of-use_20221102020018_RAW.html (+ .txt) ; previous-tos/airlines/frontier/frontier_privacy-policy_20221116203715_RAW.html (+ .txt) ; previous-tos/airlines/frontier/frontier_privacy-policy_BIRTH-VERSION_20260513004159_RAW.html (+ .txt)
---

## Coding-relevant extract

**2022 keyword scan, both documents:** artificial intelligence 0 - generative 0 - chatbot 0 - virtual assistant 0 - machine learning 0. The single "automated" hit is the anti-scraping clause: no person may employ "any automated or computerized device, process, program, algorithm or methodology" to access the site.

**Birth-dating by binary search:** "artificial intelligence" is absent at **2026-04-08** and present at **2026-05-13**. Frontier's AI clause is roughly **41 months** post-ChatGPT and roughly **three months** older than the corpus entry that first coded it.

**The clause as written (privacy notice, section "Use of AI-Assisted Customer Interactions").** Frontier "may use automated and artificial intelligence-enabled systems to assist with certain customer interactions, including through chat, voice, and other customer care channels." It concedes such systems "may occasionally generate responses that are incomplete, inaccurate, or outdated" (B6) and encourages customers to verify flight details, schedules, fares and policies via the website or a live representative (B4). It then provides that by engaging with the AI services the customer acknowledges Frontier "is not responsible for errors or misunderstandings that may result from reliance on AI-generated responses."

The Terms of Use - the document that actually forms the contract - remains AI-silent and is only ~4 KB.

## Coder note
1. **The newest AI clause in the corpus.** Added between 8 April and 13 May 2026. Any claim about "what airlines say about AI" that rests on Frontier is describing a policy roughly one quarter old.
2. **The only carrier in the batch that concedes anything.** The B6 admission plus the B4 verify-with-a-human instruction is genuinely two-sided drafting, not pure risk-shifting - closer to the Verizon microcopy pattern than to American's Section 15.
3. **Locus is the weak point, and it is the interesting part.** A liability-allocation clause placed inside a **privacy notice** - a document consumers are notified of rather than asked to accept, and whose function is to describe data handling - is doing work its container was not built for. Whether that clause is enforceable against a consumer who never assented to the privacy notice is an open legal question, and one worth flagging as a corpus-wide pattern (Capital One's compelled AI disclosure sits in a similar container for a different reason).


---
<a name="delta-aiterms-birth"></a>
company: Delta Air Lines
document_title: AI Terms of Use - February 2025 birth version (first Wayback capture in existence)
document_type: dedicated standalone AI terms (historical version)
url: https://www.delta.com/us/en/legal/ai-terms-of-use
retrieved: 2026-08-20 (via Wayback Machine)
effective_or_revised: snapshot 2025-02-07; **no capture of this URL exists at any earlier date**
names_ai_feature: partially - by CATEGORY, not by brand. "Concierge" appears ZERO times, exactly as in the current version.
ai_vector: generative (Delta Concierge, announced CES January 2025)
fetch_depth: full-fetch (RAW HTML preserved)
clause_codes_present: B6, B4, B3, B2, B7, B10, B8, B9 - all present from the first capture
vendor: not named
files: previous-tos/airlines/delta/delta_ai-terms-of-use_BIRTH-VERSION_20250207024638_RAW.html (+ .txt)
---

## Coding-relevant extract

**Zero Wayback captures of this URL predate 2025-02-07.** A CDX query with no date bound returns 2025-02-07 as the earliest record.

**Birth version vs. current, compared directly:**

| Marker | Feb-2025 birth version | Aug-2026 current |
|---|---|---|
| chars | 16,262 | 17,339 |
| defined term "AI Tool" | 38 | 41 |
| "as is" | 1 | 1 |
| "accurate" | 3 | 4 |
| indemnification refs | 2 | 2 |
| "Concierge" | 0 | 0 |
| "agentic" | 0 | 0 |

## Coder note
1. **Arrived fully formed.** The document was not iterated toward - the entire clause set (B6 through B9) is present in the first capture and the text has barely moved in the ~18 months since. This reads as a template dropped in alongside the product launch rather than a policy developed in response to experience.
2. **Timing tracks the product, not the case law.** The first capture is ~1 month after Delta Concierge was announced at CES (January 2025), and ~12 months after *Moffatt v. Air Canada* was decided (February 2024). Across the batch the product launches line up far better than the judgment does - stated as a timing observation only, since no carrier documents its drafting motive.
3. **The category-not-brand convention was there from day one.** "Concierge" has never appeared in this document. Delta defines "AI Tools" by category and lets the definition sweep in whatever it ships - which means the document survives a product rename but also never tells a consumer that the thing they are talking to is governed by it.
4. **No agentic language, then or now.** "agentic" is absent from both versions - a gap relative to American (B5 from Jan 2026) and Target/Instacart in other verticals.

---

---
<a name="marriott"></a>
company: Marriott International
document_title: Marriott Terms of Use (governing) + Homes & Villas ToS + Global Privacy Statement
document_type: dedicated AI section within governing product/service terms (+ second AI surface + privacy notice)
url: https://www.marriott.com/about/terms-of-use.mi
retrieved: 2026-09-18
effective_or_revised: Terms of Use "Last revised July 2026"; Homes & Villas ToS Apr 15 2025; Global Privacy Statement Last Updated Aug 5 2026
names_ai_feature: yes - governing ToU names "Ask Bonvoy" (an AI search engine) in Definitions; Homes & Villas names "Search with AI"
ai_vector: generative (decisional vector checked: B11 absent)
fetch_depth: full-fetch (ToU Sections 3/4/7/8 browser-rendered; Homes & Villas ToS full; Privacy Statement full). Marketing/press snippet-only; Section 6 Reservation Terms and RENAI microcopy not captured.
clause_codes_present: B6(AI), B4(AI, directive), B3(AI), B2(gen), B1(reaches AI), B10(AI), B8(~gen), B9(AI); B7 absent; B11 absent
vendor: in-house (Ask Bonvoy AI search engine; Homes & Villas "Search with AI")
locus: 2 (dedicated AI section inside general ToS)
---

## Coding-relevant extract (governing Terms of Use, revised July 2026)

**Definitions (S3).** "Ask Bonvoy" = "advanced search capabilities within the Services that are powered by an Artificial Intelligence ('AI') search engine." The AI feature is named in the binding contract - rare in the corpus (only Walmart names its assistant, and only in a privacy notice).

**S4.C - training on prompts [B10, AI-specific].** If a user uses "automated or AI-powered chat technologies, we may use the information that you submit, including Prompts and behavior in connection with Ask Bonvoy ... for quality and training purposes."

**S4.D - Inaccuracies and Errors [B6 + B1, AI-reaching].** "The Services, including Ask Bonvoy, may contain technical inaccuracies or typographical errors, including those arising from automated or AI-powered technologies and/or relating to pricing or availability." And: "We or the relevant service provider may make changes, corrections, cancellations and/or improvements ... at any time, including after confirmation of a transaction. If a transaction is affected by an error, neither we nor the relevant service provider will be obligated to honor the transaction, although we or the service provider will undertake reasonable efforts to work with you on available options to correct or remedy the error." This is a B1 transaction-error non-honoring clause whose introductory scope expressly includes AI-arising errors - the SECOND B1 in the corpus after Walmart, and the first where the honoring clause itself reaches AI. Softened by a reasonable-efforts remediation promise (Walmart's is a flatter "does not constitute an offer").

**S4.E.** Marriott may cancel/modify transactions resulting from "a mistake or error" [reinforces B1]; "not responsible for any failure by a Property or third-party service provider to accept, process, honor, or fulfill a transaction" [B8-adjacent].

**S4.G - Ask Bonvoy subsection.** "You are responsible for all activities conducted by you (a) to access Ask Bonvoy or (b) because of accessing Ask Bonvoy" [B3, AI-specific]; "You are responsible for all Prompts you submit." Prohibited-use list bars using "the AI Services, Responses, related data, or models to ... develop ... any other AI model or AI system," removing provenance/watermark signals, and any use "prohibited ... under the EU AI Act" [B9]; anti-jailbreak: no bypassing "content filters, or security measures, including through specially crafted Prompts (commonly known as 'jailbreaking')," no reverse engineering / extracting "system prompts, or training data" [B9, explicit]. "Reliance on Responses": Responses "may contain material inaccuracies, even if they appear detailed or specific" [B6]; "You should not rely on any Response without independently confirming its accuracy" [B4 - directive anti-reliance, AI-specific].

**S7.** Browsing-only license; limits over Responses; broad User Content license; chat data monitored/retained "for quality and training purposes" [B10]. No user indemnity [B7 absent].

**S8.** 8.A warranty "AS IS" incl. merchantability/fitness/non-infringement [B6, generic]; 8.B LoL excludes indirect/consequential loss "whether caused by tort (including negligence)," remedy capped at amounts paid, 1-year limitations, death/PI/fraud carve-out, and a carve-out preserving "direct financial loss" not otherwise excluded [B2, generic]. AAA arbitration + class-action waiver. No B7.

**Homes & Villas by Marriott Bonvoy - ToS (Apr 15 2025), a SECOND AI surface.** Names "Search with AI (beta)": "trained to be accurate ... may contain errors or omissions, including descriptions, pricing, promotions, availability" [B6]; "AS IS/AS AVAILABLE"; "HVMB suggests that you use the Search with AI tool only as a source of ideas and carefully review all options before finalizing a booking" [B4, hedged]; "YOU ASSUME ALL RISKS ASSOCIATED WITH ITS USE" [B3]; "HVMB SHALL NOT BE LIABLE FOR ANY RELIANCE ON AI-GENERATED CONTENT" [B2, AI-specific]; consent to monitoring/retention "for quality and AI training purposes" [B10].

**Global Privacy Statement (Aug 5 2026) - decisional vector.** B11 ABSENT (tested): no "automated decision", "profiling", "solely automated", or "human intervention" language; GDPR/US-state individual rights present but no Art. 22 ADM regime, despite named EU controller (Luxury Reservations Ltd, Dublin) and UK controller (Marriott Hotels Ltd). Generative-chat processing IS disclosed (Bonvoy-profile personalization; prompts used for quality/training).

**The "say" (marketing/press, snippet-only).** Ask Bonvoy launched beta 2026-06-16 (US English, Marriott.com + apps, subset of members). Marketed on reliability - responses "grounded exclusively in Marriott-owned, verified property data" - and on personalization/trip-purpose inference across ~10,000 properties. Separate surface RENAI by Renaissance (ChatGPT-backed virtual concierge) not separately coded.

## Coder note
1. **Strongest hospitality posture and one of the strongest in the whole corpus.** The governing ToU - revised July 2026, AFTER the June 2026 launch - carries a complete AI-specific stack (B6/B4/B3/B10/B9) with a directive anti-reliance clause AND a B1 transaction-error non-honoring clause that expressly reaches AI-arising errors and applies "after confirmation of a transaction." Only Walmart also has a B1; Marriott's is the first to name AI in the honoring clause itself. This is a deliberate anti-Moffatt posture -> Moffatt exposure LOW for the generative vector.
2. **Feature named in the binding contract.** Unlike every firm to date (none named its assistant in the governing terms; eight named it only in privacy/marketing), Marriott defines "Ask Bonvoy" in Section 3 of the ToU. Closes the "not one firm names its AI in the document that binds" finding - restate as a near-universal, not universal, pattern.
3. **Two AI surfaces, two regimes, two vintages.** Ask Bonvoy (main ToU, July 2026, directive B4) vs. Homes & Villas "Search with AI" (Apr 2025, hedged "suggests ... source of ideas"). Same firm, bifurcated drafting - a within-firm locus/vintage contrast.
4. **Two notable absences.** No user indemnity (B7) anywhere; no ADM/Art. 22 regime (B11) even though the firm is GDPR-subject. The decisional vector is thin at consumer scale.
5. **Say-do gap present but narrow.** Marketing sells reliability ("grounded in verified data"); the contract disclaims accuracy and directs independent verification. The gap is real but far from the Air Canada cell because the contract both names the feature and carries AI-specific anti-reliance plus a B1 device.
6. **Collection limits.** ToU captured via rendered browser (marriott.com 403s non-browser clients; Akamai-style challenge resolved on load). Section 6 (Reservation Terms), RENAI microcopy, and the press-release body were not fetched in full; marketing is snippet-only. A follow-up should expand S6 and capture in-product disclaimers.

---

---
<a name="hilton"></a>
company: Hilton
document_title: Hilton AI Terms (dedicated) + Site Usage Agreement + AI Planner
document_type: dedicated standalone AI terms + AI-silent site terms
url: https://www.hilton.com/en/p/site-usage-agreement/ (AI Terms URL not pinned; 404 on guessed slug; content corroborated across search)
retrieved: 2026-09-18
effective_or_revised: Site Usage Agreement not dated; AI Planner beta Mar 10 2026 (site-wide Mar 17 2026)
names_ai_feature: category ("AI Tools"); AI Planner named in marketing
ai_vector: generative
fetch_depth: mixed - Site Usage Agreement full-fetch (browser); AI Terms snippet-only (exact hilton.com URL not resolved)
clause_codes_present: AI Terms: B6(AI), B4(AI), B10(AI), B9(AI). Site Usage Agreement: B6(gen), B2(gen), B7(gen), B1(~gen reservation error), B8(gen). B11 present (privacy Appendix A: right to object to profiling/ADM). B3/B5 untested/absent.
vendor: in-house (multi-LLM: Google, ChatGPT, Claude)
locus: 1 (dedicated AI Terms), with an AI-silent general site agreement
---

## Coding-relevant extract

**Dedicated Hilton AI Terms (snippet-only).** Separate from the site agreement -
"These AI Terms apply when you access and use generative AI tools and features,
such as chatbots." [B6, AI] "The AI Tools provide responses that are artificially
generated and may contain inaccuracies," provided "'as is' and 'as available',"
disclaiming "all responsibility for any inaccuracies in any Output"; Output "may
not reflect real-time availability for purchases or bookings." [B4, AI, directive]
Hilton "encourages users to verify all booking details independently before making
any decisions or commitments based on any Output." [B10, AI] Hilton "may ... train
artificial intelligence models and machine learning algorithms" and monitor use.
[B9, AI] prohibits "using the Site to train a machine learning or artificial
intelligence system."

**Site Usage Agreement (full-fetch) - AI-silent.** find() for "artificial
intelligence"/"AI Tools"/"machine learning" = 0. Generic B6 ("AS IS/AS AVAILABLE
... accuracy, reliability, usefulness or completeness"), generic B2 (sole remedy =
reimbursement; 1-yr limitations), generic B7 (Forum indemnity; "Indemnified
Parties"), a generic reservation-error clause ("cancel or modify reservations ...
mistake or error"; "Hotels are not obligated to honor rates if you do not
qualify") [B1-ish, generic - not AI-tied], generic B8 (linked sites). The Forum
"may not be reliable" language is about USER forums, not the AI Planner.

**The "say".** Hilton AI Planner = generative digital concierge at hilton.com
(beta Mar 2026), recommends destinations/properties/amenities but does NOT
complete the reservation. Also surfaces via Google AI Mode + a ChatGPT app
(multi-LLM). Marketing frames "real-time responses and curated recommendations."

## Coder note
1. Delta-style bifurcation: a **dedicated AI Terms** doc (locus 1) carries the
   AI-specific stack (B6/B4/B10/B9) while the general Site Usage Agreement is
   AI-silent. AI-specific directive anti-reliance ("verify all booking details
   independently") -> Moffatt exposure LOW for the generative vector.
2. **Lower stakes than Marriott:** the Planner recommends but does not book, so an
   erroneous Output is a step removed from a completed transaction. No B1 in the
   AI Terms.
3. **B11 present + a second surface.** Global Privacy Statement (upd. Aug 31
   2026), Appendix A "Right to Object to Profiling and Automated Decision Making"
   (consent-based automated offers + objection right) = B11 present; it also names
   a distinct GenAI chatbot, the **Hilton Digital Assistant**, and carries a CA AB
   2013 GenAI training-data transparency section (compelled).
4. Collection limits: AI Terms are snippet-only (exact hilton.com URL not
   resolved; an HGV mirror exists but HGV is a separate entity - not primary
   evidence); AI-Terms effective date untested.

---

---
<a name="ihg"></a>
company: IHG Hotels & Resorts
document_title: IHG Terms of Use (Terms and Copyright Notices)
document_type: site Terms of Use (governing) - AI-silent
url: https://www.ihg.com/content/us/en/customer-care/tc
retrieved: 2026-09-18
effective_or_revised: Effective Date 13 April 2022 (copyright 2001-2022)
names_ai_feature: no
ai_vector: n/a (AI-silent)
fetch_depth: full-fetch (browser-rendered)
clause_codes_present: B6(gen), B2(gen), B8(gen); B4/B7/B1/B10/B9 absent; B11 jurisdiction-scoped (Brazil LGPD); B3 untested; B5 absent
vendor: n/a
locus: silent
---

## Coding-relevant extract

Full read via rendered browser. **Effective 13 April 2022** - a frozen
pre-generative-AI contract governing IHG's 2026 AI surfaces (its generative AI
travel planner + apps inside ChatGPT and Google AI Mode). find("artificial
intelligence") = 0; no AI/chatbot/ML/generative language anywhere.

- [B6, generic] "THE MATERIALS ARE PROVIDED 'AS IS' ... MERCHANTABILITY,
  NON-INFRINGEMENT ... FITNESS"; "does not warrant the accuracy or completeness";
  "may make changes ... at any time without notice."
- [B2, generic] no "SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES ... whether ...
  based on contract, negligence" (reaches negligence; not AI-specific).
- [B8] currency "guidelines only ... do not warrant ... accuracy"; linked-sites
  carve-out.
- AAA arbitration; class/mass/collective waiver; 1-yr limitations. No user
  indemnity located (B7 absent). Generic anti-interference only (not AI B9).

## Coder note
The hospitality analogue of **United**: a governing ToU frozen in 2022, entirely
AI-silent, still operative over 2026 generative AI features - and part of the AI
surface lives inside third-party ChatGPT/Google apps. Exposed / silent locus;
generative Moffatt exposure HIGH (no clause reaches AI outputs; the planner
post-dates the contract by ~4 years). Decisional vector: B11 jurisdiction-scoped to
Brazil (LGPD) - a review right for solely-automated decisions - plus a general
profiling disclosure; no EU/UK Art. 22 rights and no AI feature named in the privacy statement.

---

---
<a name="accor"></a>
company: Accor (Accor SA)
document_title: ALL Loyalty Program Terms and Conditions + Customer Personal Data Protection Charter + ALL app in ChatGPT
document_type: AI-silent binding consumer terms + privacy charter (ADM denial); consumer AI displaced to a ChatGPT app
url: https://all.accor.com/a/en/loyalty-program/legal/terms-and-conditions.html
retrieved: 2026-09-18
effective_or_revised: ALL T&Cs Effective Sep 3 2026; ALL app in ChatGPT launched Jan 29 2026
names_ai_feature: no (terms); the ChatGPT app is the AI surface
ai_vector: generative (surface in ChatGPT) + decisional (charter denial)
fetch_depth: ALL T&Cs full-fetch (WebFetch); Data Protection Charter full-fetch (WebFetch); site CGU not fetched
clause_codes_present: T&Cs B6(~gen), B2(~gen), B1(~gen user-error), B8(~gen); B11 jurisdiction-scoped (China/PIPL grants rights; US denial; EU profiling without Art. 22 rights); B4/B3/B7/B10/B9/B5 absent
vendor: n/a (ALL Accor app inside ChatGPT)
locus: silent / displaced (AI lives in a third-party ChatGPT app)
---

## Coding-relevant extract

**ALL Loyalty T&Cs (full-fetch, eff Sep 3 2026) - AI-silent.** No AI/chatbot/
generative/ADM language. Booking-error responsibility on the customer (S4.3);
partner-limitation carve-out (S3); points-claim liability capped to "correctly
recording Points" (S11.1); Member Rate availability caveat (S9.2).

**Customer Personal Data Protection Charter (full-fetch, upd. Apr 8 2025) - B11
jurisdiction-scoped.** Explicit automated-decision rights (explanation + refuse
solely-automated decisions with material impact) appear ONLY in the China/PIPL
addendum (S14.3.8). The US State-Privacy section DENIES qualifying ADM ("we do not
use personal data for profiling in furtherance of decisions that produce legal or
similarly significant effects"). The EU/GDPR main body discloses profiling
("predicting and anticipating future customer behaviors"; "develop your customer
profile") but grants NO Art. 22 rights. Mentions "conversations with chatbot" as a
collected data category. Accor SA is GDPR-home (Issy-les-Moulineaux; Art. 32 cited).

**The "say".** ALL Accor app in ChatGPT (launched Jan 29 2026, 20+ languages):
natural-language hotel search, public + ALL member rates, property info, then
"redirected to ALL Accor booking platform for a secured reservation." Marketing:
"intuitive, personalized experiences"; no explicit accuracy/reliability guarantee.

## Coder note
Accor's binding terms are AI-silent and its consumer generative AI is an **app
inside ChatGPT** - so the AI interaction runs on OpenAI's surface under OpenAI's
terms, and Accor's own contract neither names nor governs it (the "whose terms
bind the consumer?" locus, alongside Capital One-dealer and Target-Gemini).
EU-comparator value (striking): the French, GDPR-home firm grants explicit
automated-decision rights only in its CHINA (PIPL) addendum - its EU/GDPR section
discloses profiling but confers no Art. 22 rights, and its US section denies
qualifying ADM. Jurisdiction-scoped B11, same family as American (Brazil) and Uber
(Quebec), but with the rights under Chinese, not European, law. Generative
Moffatt exposure: HIGH within Accor's own terms (silent), though the OpenAI layer
carries its own disclaimers. Collection limits: site CGU and full charter text not
fetched (the site CGU is a follow-up item).

---

---
<a name="klarna"></a>
company: Klarna
document_title: User Terms for Klarna Shopping Service (AI assistant clause) + Privacy Policy
document_type: dedicated AI-assistant section in governing terms + privacy-notice credit-ADM
url: https://cdn.klarna.com/1.0/shared/content/legal/terms/0/en_us/user
retrieved: 2026-09-19
effective_or_revised: User Terms + Privacy both Last Updated August 14, 2026
names_ai_feature: yes - "Klarna AI assistant"
ai_vector: both (generative assistant; decisional credit/fraud ADM)
fetch_depth: full-fetch (WebFetch, en_us)
clause_codes_present: User Terms B6(AI), B4(AI directive), B3(AI), B9(AI/AUP), B2(gen), B7(gen); Privacy B11 (developed, credit/fraud largely exempt), B10. B1 absent; B5 absent.
vendor: in-house (OpenAI-powered)
locus: 2 (dedicated AI-assistant section in the binding user terms)

## Coding-relevant extract

**User Terms (AI assistant clause, upd 8/14/2026).** [B6] "AI assistant outputs
are generated probabilistically and may not reflect real-world facts. Answers ...
might be incorrect, and prices and discounts presented might be wrong." [B4,
directive] "Always check and verify information and recommendations"; "should
especially not be relied on to provide financial, legal, tax, medical ... advice."
[B3] "You are solely responsible for deciding whether to act on any information."
[B9/AUP] prohibited uses. **Severing clause:** "AI-generated recommendations ...
do not constitute automated decisions with legal or similarly significant effects
without human involvement in any credit, account, or underwriting determination."
General [B6] "AS IS", [B2] no consequential damages, [B7] user indemnity.

**Privacy Policy (upd 8/14/2026).** [B11] Probability-of-Default credit modeling +
real-time fraud AI = automated decisions determining eligibility/credit limits;
right to opt out of "solely automated decisions that produce legal or similarly
significant effects" + 60-day appeal; BUT "certain automated processing ...
integral to the financial services ... may be exempt from opt-out rights ...
(contract necessity, fraud prevention, or ... law)." [B10] AI-assistant
conversations processed + retained in a "memory tab."

**Adjacent evidence.** Swedish DPA fined Klarna ~EUR 750,000 for insufficient
explanation of automated credit decisions; AlgorithmWatch documented a wrongful
fraud flag ("Klarna Thought I'm a Fraudster"). Real decisional-AI harm + EU
enforcement.

## Coder note
Strongest banking firm in the corpus and a model dual-vector case: a dedicated,
directive AI-specific generative regime (B6/B4/B3/B9) in the binding terms PLUS
the clearest consumer credit-ADM disclosure (B11), joined by a bespoke clause that
severs the assistant from Art. 22. Generative Moffatt exposure LOW. Decisional
vector developed but the core credit/fraud ADM is largely carved out of the
opt-out. EU anchor (en_us fetched; Swedish DPA fine is the EU-enforcement hook).

---

---
<a name="revolut"></a>
company: Revolut
document_title: Revolut's AI Assistants (dedicated AI notice; EU/Ireland)
document_type: dedicated AI notice (AI-specific; privacy-supplement, non-clickwrap)
url: https://www.revolut.com/en-IE/legal/rita-disclaimer/
retrieved: 2026-09-19
effective_or_revised: not dated ("regularly reviewed")
names_ai_feature: yes - "AI Support" (chatbot/voice) + "AI Revolut Assistant"
ai_vector: generative (decisional/B11 in main privacy notice, not fetched)
fetch_depth: full-fetch (browser, en-IE); en-US variant 404'd; main privacy notice referenced-not-located
clause_codes_present: B6(AI), B4(AI directive), B3(AI), B10(AI); channel-limitation device; B2/B7/B11 untested; B1 absent; B5 absent
vendor: in-house (AI Support + AI Revolut Assistant)
locus: 1 (dedicated AI notice; privacy-supplement rather than clickwrap terms)

## Coding-relevant extract

Names AI Support (chatbot + voice in some countries) and AI Revolut Assistant
(financial/travel info from app data; investments info). "fully automated service
... not a human." [B6] "AI can sometimes be wrong or provide incomplete
information. Always double-check critical information"; responses "provided 'as is'
with no direct function to verify them with a human agent within those specific
tools." [B4, directive] "You should always make your own independent judgment ...
It is not investment, financial, tax, or legal advice ... You should not rely on
the AI Assistants for investment advice or recommendations of any sort." [B3]
obtain "independent ... advice from qualified professionals ... before ... making
any financial decisions." **Channel limitation (Wells-Fargo-style):** "You will
not be able to place, modify, or cancel any order in relation to financial
instruments, nor take any other action that would result in you entering into a
transaction." **Human fallback:** type "live agent" (AI Support); auto-redirect to
a live agent (AI Revolut Assistant). [B10] recorded/assessed for quality; "express
waiver of banking secrecy" + disclosure of "client secrets" to technology partners.

## Coder note
Dedicated AI-specific notice with directive anti-reliance (B4), accuracy
disclaimer (B6), responsibility shift (B3), a human fallback, AND a
channel-limitation (the AI cannot transact) - the Wells Fargo device applied to a
fintech assistant. Generative Moffatt exposure LOW. Caveat: it's a privacy-
supplement NOTICE, not clickwrap terms (binding Personal Terms sit elsewhere).
Published across US + many EU markets (captured en-IE). B11 (main Customer Privacy
Notice) referenced but not fetched this pass.

---

---
<a name="bunq"></a>
company: bunq
document_title: bunq Privacy Policy (Finn + Article 22 ADM)
document_type: privacy-notice ADM (decisional) + generative AI disclosure
url: https://www.bunq.com/documents/privacy-policy
retrieved: 2026-09-19
effective_or_revised: Last Updated August 5, 2026
names_ai_feature: yes - "Finn" (GenAI chatbot)
ai_vector: both (Art. 22 ADM; generative Finn)
fetch_depth: full-fetch (WebFetch); bunq user terms (Finn generative disclaimer) not fetched
clause_codes_present: B11 present (robust); B10 (Finn processing, multi-LLM); generative "do" not located
vendor: multi-LLM (Microsoft Azure OpenAI, Google Gemini, AWS Anthropic)
locus: n/a (privacy notice; no dedicated Finn output disclaimer located)

## Coding-relevant extract

[B11] "Right not to be subject to automated decision-making (Article 22 GDPR):
You have the right not to be subject to a decision based solely on automated
processing, including profiling, if it produces legal or similarly significant
effects." Finn gate: "We will not, without your explicit consent, use Finn to make
automated decisions which produce legal effects concerning you or similarly
significantly affect you." ADM in "account opening, fraud detection, and credit
line eligibility determinations, with manual review available upon request." [B10]
Finn (inquiries, invoices, onboarding, support, budgeting) runs on Azure OpenAI,
Google Gemini, AWS Anthropic.

## Coder note
Dutch/EU neobank with a robust decisional regime: general Art. 22 right + explicit
Finn consent-gate + human review on request for account/fraud/credit ADM. Finn
(generative) disclosed here; a dedicated Finn output disclaimer was not located in
a separate terms doc this pass - the generative "do" appears governed via general
terms + this notice. Strong EU B11 comparator.

---

---
<a name="natwest"></a>
company: NatWest
document_title: NatWest Privacy Policy (web summary) - automated decisions + Cora
document_type: privacy-notice ADM (decisional) + AI chatbot reference
url: https://www.natwest.com/privacy-policy.html
retrieved: 2026-09-19
effective_or_revised: not stated (full notice also a 254KB PDF, not fetched)
names_ai_feature: partial - references Cora
ai_vector: decisional (checked); generative Cora referenced
fetch_depth: full-fetch of web summary; full PDF referenced-not-located
clause_codes_present: B11 present (review + human intervention + appeal); generative Cora "do" not located
vendor: in-house (Cora / Cora+, IBM watsonx + OpenAI)
locus: n/a (Cora governed by general banking terms; no dedicated disclaimer located)

## Coding-relevant extract

[B11] users may "ask for a review of a decision that has been made automatically,
like if a loan has been refused"; right to appeal a refused application; "any
automated decision is always reviewed by the business and arbitrated with human
intervention." Cora referenced under Support/Contact; conversations stored for
monitoring; no dedicated Cora output disclaimer located.

## Coder note
Decisional vector present and reasonably strong (human-review + appeal for
automated loan decisions; UK GDPR). Generative vector thin: Cora+ is generative
(IBM watsonx + OpenAI) but appears governed by general banking terms with no
dedicated AI output disclaimer located this pass. Follow-up: fetch the full
privacy PDF + account/website terms for any Cora-specific clause.

---

---
<a name="fintech-identified"></a>
company: Monzo (UK) / Chime (US) / Nubank (Brazil)
document_title: Identified consumer generative AI - AI-specific terms not located this pass
document_type: batch note (register of identified-but-uncoded firms)
retrieved: 2026-09-19
names_ai_feature: yes (features named below)
ai_vector: generative (Nubank also testing decisional credit GenAI)
fetch_depth: referenced-not-located (marketing/operational confirmed; legal AI terms not located within budget)

## Note
Three additional verified-generative fintech assistants were identified but their
AI-specific consumer terms were not located within this batch's query budget.
Registered here so their silence is not later mistaken for a coded finding:
- **Monzo (UK)** - in-house LLM customer-support agent (Gradient Labs). No
  dedicated AI ToS/disclaimer located; likely generic governance. B11 (UK GDPR)
  not fetched.
- **Chime (US)** - "Jade" AI support agent (~70% of interactions). No member-
  agreement AI disclaimer located; expected to follow the silent US-challenger
  pattern (cf. Dave).
- **Nubank (Brazil)** - GPT-4o customer assistant + GenAI credit-experience
  testing (a decisional angle). No AI-specific terms located; Brazil LGPD ADM
  rights may apply.
These are candidates for a follow-up pass, not confirmed absences.

---

---
<a name="verizon"></a>
company: Verizon
document_title: Verizon consumer AI chatbot microcopy ("Verify if needed") + Privacy Policy
document_type: in-product microcopy (locus 4) + privacy-notice ADM
url: https://www.verizon.com/support/my-verizon-app-service-chat-bot-video/ ; https://www.verizon.com/about/privacy/full-privacy-policy
retrieved: 2026-09-19
effective_or_revised: not dated in fetched sections
names_ai_feature: category (My Verizon service chatbot; Google/Gemini "Project 624")
ai_vector: both
fetch_depth: microcopy snippet-only; privacy full-fetch (WebFetch)
clause_codes_present: microcopy B6(AI), B4(AI hedged-directive), B3(AI); B10 negative (no LLM training on personal data); B11 thin (profiling opt-out only)
vendor: in-house consumer assistant; a separate B2B "Verizon Business Assistant" T&C does NOT bind consumers
locus: 4 (microcopy-only)

## Coding-relevant extract

**Microcopy [locus 4].** Consumer chatbot shows "Generated by AI. Verify if
needed." and "Verify details" (the CLAUDE.md exemplar, now confirmed). Verizon
states AI "uses probabilistic techniques and may not always be accurate" and it
"is not responsible for inaccurate determinations made by the AI system." [B6 + B4
hedged-directive + B3, AI-specific, but delivered as microcopy, not binding terms.]

**Privacy (decisional).** "We may use automated processing, including artificial
intelligence, to assist us." "We do not collect, use or sell personal information
for the purpose of training large language models" [B10 negative]. Profiling via
Custom Experience / Plus with an opt-out; NO Art. 22 ADM rights or human-review
guarantee [B11 thin].

**Adjacent evidence.** Documented AI-chatbot service failures (The Register 2020;
Pivot-to-AI 2025 "customer disservice") - billing dead-ends, Moffatt-adjacent.

## Coder note
Closes the CLAUDE.md Verizon microcopy citation hole: consumer AI liability lives
in **microcopy** ("Verify if needed"/"Verify details"), not binding terms - the
Alaska/Home Depot locus-4 pattern at a telecom. AI-specific hedged-directive
anti-reliance but informal. Decisional vector thin (profiling opt-out, no ADM
regime); notable no-LLM-training commitment. Generative Moffatt exposure MODERATE-
HIGH (only informal microcopy reaches the outputs). B2B "Business Assistant" T&C
is out of scope as consumer-binding.

---

---
<a name="comcast"></a>
company: Comcast (Xfinity)
document_title: Xfinity Assistant - in-product microcopy
document_type: in-product microcopy (locus 4)
url: https://www.xfinity.com/xfinityassistant/
retrieved: 2026-09-19
effective_or_revised: n/a
names_ai_feature: yes - "Xfinity Assistant"
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: thin AI-generated notice only; no anti-reliance/verify; B11 not located
vendor: in-house
locus: 4 (microcopy-only)

## Coding-relevant extract

Bare in-product notice: "Responses may be AI-generated, and chats may be monitored
or recorded. By continuing, you agree to our Privacy Policy." No accuracy
disclaimer, no verify/anti-reliance instruction, no dedicated AI terms located.
Adjacent: documented billing-query mishandling (Houston Chronicle op-ed, 2024).

## Coder note
Weakest telecom posture captured - a bare "responses may be AI-generated" flag
(locus 4) with no accuracy disclaimer or verify instruction. No dedicated AI
terms; B11 (Comcast privacy) not fetched. Peripheral/thin; Moffatt exposure HIGH.

---

---
<a name="vodafone"></a>
company: Vodafone
document_title: TOBi Chatbot Terms and Conditions + Vodafone Privacy (automated decisions)
document_type: dedicated AI chatbot terms (locus 1) + privacy-notice ADM
url: https://static.vodafone.ro/dA/d984f94eb9dea68d68f9679c5c0e6569 (TOBi T&Cs, RO/EU) ; https://www.vodafone.co.uk/privacy
retrieved: 2026-09-19
effective_or_revised: not captured (TOBi doc is a file download)
names_ai_feature: yes - "TOBi" (SuperTOBi; Microsoft/OpenAI)
ai_vector: both
fetch_depth: snippet-only (host serves TOBi T&Cs as a file download; WebFetch ECONNRESET, browser save-dialog)
clause_codes_present: TOBi T&Cs B6(AI) + transparency + data-screening; Privacy B11 (fraud/AML ADM + Art. 22 rights)
vendor: third-party generative AI (Microsoft/OpenAI); Vodafone-branded
locus: 1 (dedicated standalone TOBi chatbot T&Cs)

## Coding-relevant extract (snippet-only)

**TOBi T&Cs (RO/EU).** Names TOBi as generative AI. [B6, AI-specific] "Because of
the nature of generative AI, it is possible that information provided by the
Chatbot may not be 100% accurate, or may include inaccurate, inappropriate or
misleading content ... and which does not represent Vodafone's views." Data-
screening of personal details; **transparency duty** to disclose users are talking
to AI. **Privacy [B11]:** Vodafone "may automatically decide that customers pose a
fraud or money laundering risk"; customers "have rights in relation to automated
decision making by contacting their privacy team" (Art. 22).

## Coder note
EU high-water mark for telecom generative terms: a **dedicated TOBi chatbot T&Cs**
(locus 1) with AI-specific accuracy disclaimer (B6) + an explicit transparency
duty, plus decisional B11 (fraud/AML ADM + Art. 22 rights). Snippet-only: the TOBi
T&Cs are served as a file download neither WebFetch nor the browser could open -
follow-up should grab the PDF. Generative Moffatt exposure LOW-MODERATE (AI-specific
B6 but no directive verify located; T&Cs are dedicated).

---

---
<a name="deutsche-telekom"></a>
company: Deutsche Telekom
document_title: Frag Magenta (OneBOT) - chatbot data-privacy notice
document_type: chatbot data/privacy notice; AI output disclaimer not located
url: https://www.telekom.de/hilfe/frag-magenta ; https://csdchatbot.telekom.net/docs/data_privacy_csdnl_de.pdf
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Frag Magenta" / "Frag Magenta OneBOT"
ai_vector: generative
fetch_depth: snippet-only; AI output disclaimer + full ADM not fetched
clause_codes_present: generative confirmed; no dedicated AI output disclaimer located; B11 referenced-not-located (German GDPR)
vendor: in-house on LMOS; processor IBM Deutschland GmbH
locus: not located (data-privacy notice only)

## Coding-relevant extract (snippet-only)

Frag Magenta "makes extensive use of Generative AI" (~10M conversations in 2024).
Its data-privacy notice covers data handling (chat history + logged-in customer
data to a dialogue platform; two cloud systems; pseudonymization before transfer
to processor IBM Deutschland GmbH). No dedicated AI accuracy/liability/anti-
reliance disclaimer located.

## Coder note
Generative surface confirmed; governance via a **data-privacy notice** rather than
a dedicated AI output disclaimer (not located). German GDPR ADM (B11) likely in the
full German data-privacy PDF - referenced-not-located. Honest partial entry.

---

---
<a name="telefonica"></a>
company: Telefónica (Movistar)
document_title: Aura - AI assistant (AI-ethics commitment; dedicated output terms not located)
document_type: AI-ethics/commitment page; no dedicated AI output terms located
url: https://aura.telefonica.com/en/commitment-ai
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Aura"
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: generative confirmed; no dedicated AI output disclaimer or ADM regime located
vendor: in-house (Aura; Microsoft partnership)
locus: not located (AI-ethics commitment only)

## Coding-relevant extract (snippet-only)

Aura is Telefónica's multi-channel generative AI assistant (app, devices, TV, web,
call centres). Telefónica publishes an "Aura makes responsible use of AI"
commitment (transparency, data control) and describes Aura's "intelligent
suggestion modules that ... decide what needs to be done." No dedicated Aura terms
of use / accuracy disclaimer / anti-reliance clause and no explicit Art. 22 ADM
regime located.

## Coder note
Generative surface confirmed with AI-ethics framing but no dedicated consumer AI
output disclaimer or ADM regime located; governance likely sits in Movistar's
general terms + privacy (not fetched). Honest partial entry; B11 (ES/EU GDPR)
referenced-not-located.

---

---
<a name="expedia"></a>
company: Expedia (Expedia Group)
document_title: Expedia AI Terms of Use + Privacy Statement
document_type: dedicated standalone AI terms + privacy-notice ADM
url: https://www.expedia.com/legal/ai-terms ; https://www.expedia.com/legal/privacy
retrieved: 2026-09-19
effective_or_revised: not dated on AI Terms page
names_ai_feature: yes - "AI Tools" (Property Q&A, AI Compare, Activity Planner); Romie is the assistant brand
ai_vector: both
fetch_depth: AI Terms full-fetch (browser); privacy snippet-only (WebFetch 429)
clause_codes_present: B6(AI), B4(AI verify-before-booking), B10(AI owns outputs+feedback), B8(AI third-party unverified), B2(incorporated ToS s8); B11 present (Art.22 object/manual/contest)
vendor: in-house + third-party LLMs
locus: 1 (dedicated AI Terms of Use)

## Coding-relevant extract (AI Terms, full-fetch)

Dedicated "AI Terms of Use" for the AI Tools (Property Q&A, AI Compare, Activity
Planner). "Responses ... are generated by a machine and not written by a human ...
may ... use third-party large language models." [B6] "may generate unexpected or
inaccurate responses ... provided on an 'as-is' and 'as-available' basis. We make
no representations ... as to the relevancy, accuracy, or completeness." [B8]
responses "may also be based on publicly available information (the accuracy of
which has not been verified by Expedia) ... should not be attributed to Expedia."
[B4] "check the relevant information page for the hotel or activity prior to
booking." [B10] "All AI-generated content ... is owned by us"; processes Feedback
for improvement. [B2] incorporates "Section 8 Liability" of the ToS; consumer-
rights carve-out (fraud/PI/death). Privacy [B11]: right to object to fully
automated decisions with significant legal effect, request a manual decision, and
contest a decision based solely on automated processing.

## Coder note
Travel high-water mark on the generative side: dedicated AI Terms (locus 1) with
AI-specific B6 + B8 + verify-before-booking B4, IP over outputs (B10), incorporated
B2, and a decisional B11 (Art. 22 object/manual/contest). Generative Moffatt
exposure LOW-MODERATE. Privacy snippet-only (expedia.com 429s WebFetch).

---

---
<a name="booking"></a>
company: Booking.com (Booking Holdings)
document_title: Booking.com Terms & Conditions
document_type: governing terms - own AI ungoverned; anti-agentic-AI clauses; obvious-error non-honoring
url: https://www.booking.com/content/terms.html
retrieved: 2026-09-19
effective_or_revised: Last Updated August 25, 2025
names_ai_feature: no (own AI Trip Planner not named); names third-party "AI-powered assistants" only to prohibit them
ai_vector: generative (own Trip Planner, ungoverned)
fetch_depth: full-fetch (WebFetch)
clause_codes_present: B1(gen, obvious-error non-honoring), B6(gen); B5-adverse (bars third-party AI agents); own AI silent
vendor: in-house AI Trip Planner (OpenAI) - ungoverned
locus: silent (own AI) / anti-agent

## Coding-relevant extract

**Own AI Trip Planner UNGOVERNED** - no mention of an AI Trip Planner/chatbot/
generative AI tool offered to users. **Anti-agentic-AI [B5-adverse]:** A15.2 bars
accessing the site via "automated assistants (including ... AI-powered
assistants)" without permission; A15.3 blocks AI-powered assistants without
express permission; A18.3 = "irreparable harm"; A20.1 carves such disputes out of
arbitration. **B1 (generic):** A7.3 "Obvious errors and obvious misprints are not
binding" (e.g. luxury room at a nominal price; may be cancelled + refunded). **B6
(generic):** A4.1 cannot "guarantee that everything on it is accurate."

## Coder note
Distinctive dual posture: Booking.com's OWN generative AI (Trip Planner) is
ungoverned/silent, while the terms devote several sections to PROHIBITING
third-party AI agents from accessing the platform (the eBay pattern; B5-adverse).
Carries a generic **B1** obvious-error non-honoring clause - third B1 in corpus
(Walmart, Marriott, Booking), though generic and framed as "obvious misprints,"
not AI-tied. EU (Netherlands); GDPR privacy (B11) not fetched this pass.

**Launch date (added 2026-09-30, `fetch_depth: snippet-only`):** AI Trip Planner announced
27 Jun 2023, beta to US Genius members from 28 Jun 2023 (Booking.com press release,
https://news.booking.com/bookingcom-launches-new-ai-trip-planner-to-enhance-travel-planning-experience/).
The Aug 2025 terms revision therefore came ~26 months after launch and is still AI-silent.

---

---
<a name="kayak"></a>
company: Kayak (Booking Holdings)
document_title: Kayak.ai Terms of Use (AI Mode / Ask AI)
document_type: dedicated AI terms
url: https://kayak.ai/terms-of-use ; https://www.kayak.com/terms-of-use
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - Kayak AI Mode / Ask AI (ChatGPT)
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6(AI), B8(AI third-party LLM); warranty disclaimer
vendor: third-party LLMs (ChatGPT)
locus: 1-2 (dedicated AI terms / kayak.ai)

## Coding-relevant extract (snippet-only)

"Kayak's services use artificial intelligence, including generative AI, and
Kayak.ai may partner with third-party entities or utilize third-party large
language models" [B8]. "All information and content generated by Kayak's AI tools
are provided on an 'as-is' and 'as-available' basis ... expressly disclaims all
warranties ... merchantability, fitness ... and accuracy" [B6]. "does not
guarantee AI-output accuracy, relevance or completeness."

## Coder note
Dedicated AI terms with AI-specific B6 + third-party-LLM carve-out (B8). Drafting
closely parallels Expedia's AI Terms ("may partner with or use ... third-party
large language models"), suggesting a common travel-industry template. Snippet-
only; follow-up should full-fetch kayak.ai/terms-of-use. Booking Holdings sibling.

---

---
<a name="tripadvisor"></a>
company: Tripadvisor
document_title: Tripadvisor Terms, Conditions and Notices (AI-reaching clause) + AI-summary harm
document_type: governing terms (generic clause reaching named AI) + adjacent evidence
url: https://tripadvisor.mediaroom.com/us-terms-of-use
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: category - content "created or powered by AI"; AI Assistant / "Ollie" (in development)
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6(AI-reaching), B8(gen obvious errors)
vendor: in-house + OpenAI/Perplexity
locus: 3 (generic clause expressly reaching AI-created content)

## Coding-relevant extract (snippet-only)

ToU accuracy disclaimer extended to AI: "The information, software, products and
services ... (including those created or powered by AI) may include inaccuracies
or errors, including reservation availability and pricing errors" [B6, reaches
AI]. "do not guarantee the accuracy of, and disclaim all liability for any obvious
errors or other inaccuracies" [B8/B6 generic]. Adjacent harm: Tripadvisor AI
review-summaries criticized for whitewashing negative reviews / misleading
(Travel Weekly; Futurism).

## Coder note
Tripadvisor takes the "generic clause that expressly reaches AI" route (locus 3):
it amended the ToU accuracy disclaimer to name AI-created content and flag
"reservation availability and pricing errors," rather than a dedicated AI doc.
AI-reaching B6 present; AI Assistant ("Ollie") in development. Documented AI-summary
accuracy harm makes a useful say-do/harm pairing. Snippet-only.

---

---
<a name="airbnb"></a>
company: Airbnb
document_title: Airbnb AI customer-support agent - governance note (+ anti-AI-evidence clause)
document_type: generative support agent; dedicated AI output disclaimer not located
url: https://www.airbnb.com/help/article/4097 ; general Terms of Service
retrieved: 2026-09-19
effective_or_revised: Host Damage Protection terms eff. August 2026
names_ai_feature: category - AI customer-support agent (custom LLM)
ai_vector: generative
fetch_depth: snippet-only; dedicated AI output disclaimer not located
clause_codes_present: none AI-specific located for the support agent; novel anti-AI-fabrication clause (user evidence)
vendor: in-house custom LLM (post-trained third-party models)
locus: not located

## Coding-relevant extract (snippet-only)

AI customer-support agent now handles ~33% of US/Canada support autonomously
(global rollout; voice planned). No dedicated AI ToS/accuracy/anti-reliance
disclaimer for the support agent located - appears governed by the general Terms
of Service. Novel adjacent clause: Host Damage Protection (eff. Aug 2026) requires
claim evidence "not doctored or falsified in any way, including by the use of
artificial intelligence" (polices USER AI use, not the assistant).

## Coder note
Material generative support agent (a third of NA support) but its output
disclaimer was not located - governance appears to sit in the general ToS. The
anti-AI-fabrication clause is a distinctive different-vector provision. B11
(Airbnb Ireland/EU) not fetched. Honest partial entry.

---

---
<a name="priceline"></a>
company: Priceline (Booking Holdings)
document_title: Priceline "Penny" AI assistant - governance note
document_type: generative assistant; AI-specific terms not cleanly located
url: https://media.travsrv.com/appSkins/64/v6/themes/global/static/pricelineterms.html
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Penny" (OpenAI-/Claude-powered; agentic)
ai_vector: generative
fetch_depth: snippet-only; AI-specific disclaimer not cleanly located
clause_codes_present: not located AI-specific; general terms govern
vendor: third-party LLMs (OpenAI/Anthropic)
locus: not located

## Coding-relevant extract (snippet-only)

Penny is a generative, increasingly agentic travel assistant (OpenAI, later Claude
multi-agent). A dedicated Priceline AI terms / Penny-specific disclaimer was not
cleanly located; Penny appears governed by Priceline's general T&C. **Caution:**
"getpenny.com" ("Penny AI Technologies Inc.") is an UNRELATED company - NOT
Priceline's Penny; do not attribute its "AS IS" language to Priceline. Adjacent:
Singer v. Priceline (resort-fee onsite-disclosure reliance) is a pre-AI analogue
of microcopy-based protection.

## Coder note
Generative Penny confirmed (Booking Holdings sibling); consumer AI governance not
cleanly isolated (likely general T&C). getpenny.com trap flagged. B11 not fetched.
Honest partial entry.

---

---
<a name="travel-identified"></a>
company: Skyscanner (EU/UK) / Trip.com (Asia)
document_title: Identified consumer generative AI - AI terms not located this pass
document_type: batch note (register of identified-but-uncoded firms)
retrieved: 2026-09-19
names_ai_feature: yes (features named below)
ai_vector: generative
fetch_depth: referenced-not-located

## Note
- **Skyscanner (EU/UK)** - "Savvy Search" generative trip planner (ChatGPT-powered;
  app-exclusive) + a flights app inside ChatGPT. Dedicated AI terms/disclaimer not
  located this pass; ChatGPT-app locus for part of the surface.
- **Trip.com (Asia)** - "TripGenie" generative copilot (text+voice; proactive
  suggestions). AI terms/disclaimer not located this pass.
Registered so their silence is not mistaken for a coded finding; candidates for a
follow-up pass, not confirmed absences.

---

---
<a name="lemonade"></a>
company: Lemonade
document_title: Lemonade Terms of Service (AI Maya/AI Jim) + Privacy Policy (ADM)
document_type: governing terms (AI-agent clause) + privacy-notice ADM
url: https://www.lemonade.com/terms-of-service ; https://www.lemonade.com/uk/privacy-policy
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "AI Maya" (sales) + "AI Jim" (claims)
ai_vector: both (generative-agentic; decisional underwriting/claims ADM)
fetch_depth: snippet-only
clause_codes_present: ToS B4(AI policy-governs), B3(AI); Privacy B11 robust (Art. 22 underwriting + claims); operational no-auto-reject safeguard
vendor: in-house
locus: 2 (AI-agent provisions in governing terms) + privacy ADM

## Coding-relevant extract (snippet-only)

**ToS.** "AI Maya functions as an agent of Lemonade Insurance Company." [B3]
purchasing decisions (coverage, limits, deductibles) "completely and solely the
responsibility of the insured." [B4 / reliance-limiter] at claim time "coverage and
benefits will be determined in accordance with the terms and conditions of your
insurance policy" - the policy governs, not the bot. AI Jim handles claims (55%
fully automated) but Lemonade "has never, and will never, let AI auto-reject
claims" [operational safeguard]. **Privacy [B11, robust].** automated decision-
making to "calculate your individual risk profile ... determine whether we can
extend insurance coverage ... limits and premiums ... or ... process claims";
rights to human intervention, express views, contest, and notification (Art. 22).
**Adjacent:** 2021 privacy/biometric class action (AI claims video); Raizner
commentary on AI wrongful-claim-denial risk.

## Coder note
Insurance flagship / model dual-vector firm: generative-agentic assistant with a
responsibility shift (B3) and a **policy-governs** reliance-limiter (bot statements
can't override policy terms - a structural anti-Moffatt move), plus a **robust
Art. 22 B11** (underwriting + claims), rivaling Klarna. "AI as agent of the
insurer" framing + explicit no-auto-reject-claims safeguard are distinctive.
Highest agentic-harm vertical. Snippet-only.

---

---
<a name="geico"></a>
company: GEICO
document_title: GEICO AI Virtual Assistant (Kate) - disclaimer
document_type: dedicated AI assistant disclaimer/terms
url: https://www.geico.com/ai-assistant/
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Kate" / GEICO AI Virtual Assistant
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6(AI), B4(AI hedged/no-advice), B3(AI); human fallback + AI-transparency; B11 not located
vendor: in-house
locus: 1 (dedicated AI assistant disclaimer)

## Coding-relevant extract (snippet-only)

"intended for informational purposes only, and a live agent may be requested at any
time" [human fallback + hedged anti-reliance]. "not intended as insurance advice"
[no-advice]. "Any insurance decision ... solely and ultimately the responsibility
of the insured, and GEICO is not liable for any information that is inaccurate,
missing, or misinterpreted" [B3 + B6]. "makes no guarantee about the quality or
accuracy" [B6]. Discloses when users interact with the AI (transparency).

## Coder note
AI-specific disclaimer (B6 + B3 + no-advice + human fallback + transparency) on a
dedicated AI-assistant page (locus 1) - the insurance pattern of pushing final
decisions onto the insured plus a live-agent escape. B11 (GEICO privacy ADM) not
located this pass. Generative Moffatt exposure LOW-MODERATE.

---

---
<a name="insurance-eu-note"></a>
company: EU insurers (AXA, Allianz; Getsafe/Wefox)
document_title: Note - EU consumer-facing insurance AI is thin
document_type: batch note (vertical-coverage caveat)
retrieved: 2026-09-19
ai_vector: n/a
fetch_depth: n/a

## Note
Verification (see banking-batch prep) found the big EU insurers run **internal-
only** generative AI: AXA "Secure GPT" and Allianz "AllianzGPT" are employee tools,
not consumer chatbots - out of scope as consumer-facing. AI-native EU insurers
(Getsafe, Wefox) were not scanned this pass. Consequently the insurance vertical is
US-led (Lemonade, GEICO); a matched EU consumer-insurance comparator is a genuine
gap, not a coded absence. Progressive/Allstate (US) had voice/internal AI and
weren't coded either.

---

---
<a name="khan-academy"></a>
company: Khan Academy
document_title: Khan Academy Terms of Service - AI-Enabled Features (Khanmigo)
document_type: dedicated AI section within governing terms
url: https://www.khanacademy.org/about/docs/khan-academy-terms-of-service
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Khanmigo" / "AI-Enabled Features"
ai_vector: generative
fetch_depth: snippet-only (JS-rendered; content via search)
clause_codes_present: B6(AI), B4(AI directive fact-check); minors caveat
vendor: nonprofit; GPT-4/Claude
locus: 2 (dedicated AI section in governing ToS)

## Coding-relevant extract (snippet-only)

[B6] "output from Khanmigo or other AI-enabled features may include errors
(including without limitation math errors), may reflect biased, incomplete or
incorrect information ... and have other limitations." [B4, directive] users
"should not rely on factual assertions in the output without independently fact
checking their accuracy." Minors: "learners under 18 should use AI-Enabled Features
with the guidance of a parent, teacher, or other trusted adult" (COPPA/FERPA).

## Coder note
Strong AI-specific accuracy disclaimer (B6, with a concrete math-errors example) +
directive fact-check (B4) + an edtech-distinctive minors caveat. Nonprofit; harm =
misinformation/education. Snippet-only (JS-rendered ToS).

---

---
<a name="grammarly"></a>
company: Grammarly (parent rebranded "Superhuman")
document_title: Grammarly/Superhuman Terms of Service - Generative AI Features
document_type: dedicated AI section within governing terms
url: https://www.grammarly.com/terms
retrieved: 2026-09-19
effective_or_revised: Effective October 29, 2025
names_ai_feature: category - "generative AI features"
ai_vector: generative
fetch_depth: full-fetch (WebFetch; grammarly.com/terms resolves to the Superhuman-branded ToS)
clause_codes_present: B6(AI), B4(AI), B3(AI assume-risk), B10(AI license for improvement); user owns outputs
vendor: generative AI writing assistant
locus: 2 (dedicated AI clause)

## Coding-relevant extract (full-fetch)

[B6] "DO NOT MAKE ANY REPRESENTATION OR WARRANTY REGARDING THE OUTPUTS ...
INCLUDING WITH RESPECT TO THE FACTUAL ACCURACY OF ANY OUTPUTS OR SUITABILITY FOR
YOUR USE-CASE." [B4] "YOU SHOULD NOT RELY ON [OUR] GENERATIVE AI AS A SINGLE SOURCE
OF FACTUAL INFORMATION." [B3] "YOUR USE OF ANY GENERATIVE AI OUTPUTS IS DONE AT
YOUR SOLE RISK. YOU ASSUME ALL RISKS ... INCLUDING ANY POTENTIAL COPYRIGHT
INFRINGEMENT CLAIMS." User "own[s] all right, title, and interest in ... User
Content" (incl. AI outputs); [B10] content license for operating/improving/
developing features.

## Coder note
Dedicated all-caps AI-specific regime (B6 + B4 single-source + B3 assume-all-risk),
user owns outputs, B10 improvement license. grammarly.com/terms resolves to a
"Superhuman"-branded ToS (corporate rebrand; eff Oct 29 2025). Strong.

---

---
<a name="chegg"></a>
company: Chegg
document_title: Chegg Terms of Use - general accuracy disclaimer + "AI Functions"
document_type: site/service terms (generic clause reaching AI)
url: https://www.chegg.com/en-US/termsofuse/
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: category - "AI Functions"
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6(gen reaching AI), B8-ish (AI Functions -> third-party providers); no dedicated GenAI accuracy disclaimer
vendor: in-house + third-party LLMs
locus: 3 (generic clause reaching AI)

## Coding-relevant extract (snippet-only)

No dedicated generative-AI accuracy disclaimer. [B6, generic] "does not make any
representations or warranties regarding the content ... or ... the results of the
use of the services in terms of their completeness, correctness, accuracy,
reliability, usefulness or otherwise." Discloses "AI Functions" (features "based on
artificial intelligence") that may transmit personal data "to third-party
providers" [B8-ish/data].

## Coder note
Generic route (locus 3): general accuracy disclaimer reaches Chegg's AI with no
AI-specific output/anti-reliance clause; only AI-named provision is the "AI
Functions" data disclosure. Weaker than Khan/Grammarly. Snippet-only.

---

---
<a name="duolingo"></a>
company: Duolingo
document_title: Duolingo Terms and Conditions of Service (AI-silent re: Duolingo Max)
document_type: governing terms - AI-silent
url: https://www.duolingo.com/terms
retrieved: 2026-09-19
effective_or_revised: Last revised September 8, 2025
names_ai_feature: no
ai_vector: generative (Duolingo Max, ungoverned)
fetch_depth: full-fetch (browser)
clause_codes_present: B2(gen LoL); AI-silent (no AI-specific B6/B4/B3); "Additional Terms" mechanism may cover Max
vendor: in-house (Duolingo Max; GPT-4)
locus: silent

## Coding-relevant extract

AI-SILENT (find() = 0 for "artificial intelligence"/"generative"; "Max" only in
"MAXIMUM EXTENT PERMITTED"). Duolingo Max (flagship GPT AI tutor: Explain My
Answer, Roleplay, Video Call) not named or governed by AI-specific terms.
**Revised Sept 8 2025 - ~2 yrs after Max launched (2023)** = current choice, not
staleness. [B2] arbitration + class waiver + "IN NO EVENT WILL DUOLINGO BE LIABLE."
"Additional Terms" mechanism: some Services have in-product additional terms
(Max's may exist there - referenced-not-located).

## Coder note
Silent-governing-terms firm despite a heavily marketed flagship AI, with a
post-launch revision that kills the staleness story - a clean edtech say-do gap
(cf. Dave/Lowe's), contrasting Khan/Grammarly's dedicated AI clauses. Silence
qualified by the "Additional Terms" hook (Max in-product terms not captured).

---

---
<a name="robinhood"></a>
company: Robinhood
document_title: Robinhood Cortex Assistant Disclosure (summarizes the Cortex Assistant Agreement)
document_type: dedicated standalone AI disclosure/terms
url: https://cdn.robinhood.com/assets/robinhood/legal/cortex_assistant_disclosure.pdf
retrieved: 2026-09-19
effective_or_revised: 2026-06-16
names_ai_feature: yes - "Cortex Assistant"
ai_vector: generative-agentic (conversational AI that can initiate trades on user confirmation)
fetch_depth: full-fetch (PDF read)
clause_codes_present: B6(AI), B4(AI directive), B3(AI), B2(AI-specific), B8(AI); no-advice; execution-confirmation safeguard
vendor: third-party LLMs (OpenAI, Google)
locus: 1 (dedicated standalone AI disclosure/agreement)

## Coding-relevant extract (full-fetch)

Robinhood Gold conversational AI (iOS) that analyzes the portfolio, manages
watchlists/alerts, and initiates supported transactions by natural language.
- **S2 Not Investment Advice** "Assistant is not an investment advisor and does not
  provide investment advice, recommendations, or endorsements ... solely for
  informational and educational purposes"; Responses "not a recommendation ... not
  research." "You are responsible for conducting your own due diligence ... and
  should not rely solely on Responses." [B4 + B3]
- **S4 AI Limitations** [B6] "Responses may contain errors, inaccuracies,
  omissions, or outdated information"; "Accuracy not guaranteed"; "No obligation to
  update"; "**Verify before acting:** You are responsible for verifying information
  in Responses before taking action." [B4 directive]
- **S5 Data Sources** [B8] restricted web search (no open web / no social media);
  third-party info "not ... independently verified"; relies on OpenAI/Google.
- **S6 Initiating Transactions** "No transaction will be executed without your
  explicit confirmation on the final order confirmation screen" [execution
  safeguard; non-discretionary].
- **S10** "as is"/"as available" [B6]; **S11 LoL** [B2] no indirect/consequential
  incl. "investment losses," sole remedy = stop using; **S12** incorporated into
  Customer Agreements (which control). **S14** acknowledgment: won't rely solely,
  will verify before acting.

## Coder note
Among the most complete AI-specific regimes in the corpus (dedicated standalone
disclosure, 6/16/2026): no-advice + B6 + directive B4 + B3 + B2 (investment-loss
LoL) + B8, plus a non-discretionary execution-confirmation safeguard. Securities-
law-driven; generative Moffatt exposure LOW. Firm's-own agentic tool with mandatory
user confirmation (B5 user-assigned-agent n/a).

---

---
<a name="coinbase"></a>
company: Coinbase
document_title: Coinbase Advisor Terms of Service (SEC-registered AI investment adviser)
document_type: dedicated AI adviser terms
url: https://www.coinbase.com/legal/coinbase-advisor
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Coinbase Advisor"
ai_vector: generative-agentic (non-discretionary AI adviser)
fetch_depth: snippet-only (403; corroborated across Coinbase press + trade coverage)
clause_codes_present: B6(AI), B4(AI), B3(AI); registered-adviser/fiduciary structure; B1 absent
vendor: in-house (Coinbase Advisors, LLC)
locus: 1 (dedicated Advisor ToS)

## Coding-relevant extract (snippet-only)

**The corpus outlier - embraces advice rather than disclaiming it.** Coinbase
incorporated **Coinbase Advisors, LLC**, registered with the **SEC as a Registered
Investment Adviser** (+ CFTC/NFA CTA), and the AI "took on fiduciary duty under the
Investment Advisers Act of 1940" - so the AI legally CAN give investment advice.
Still limits/disclaims: [B6] "Outputs are limited and may be inaccurate or
incomplete and should not be your only source"; "outcomes cannot be guaranteed";
[B3] "cannot replace your judgment for your trades." Scope exclusions (no financial
planning/retirement/tax/legal advice, etc.). **Non-discretionary** (user confirms
every trade; "you still bear the risk").

## Coder note
Unique posture: rather than the standard "not an investment adviser" disclaimer,
Coinbase stood up a **registered fiduciary** entity so the AI can advise (a
consumer-favorable raising of the standard) while still disclaiming accuracy (B6),
preserving user judgment (B3), and keeping execution non-discretionary. The most
distinctive single data point in the investing vertical. Snippet-only (403;
corroborated across Coinbase's Advisor page + multiple trade/press sources).

---

---
<a name="public"></a>
company: Public (Public Holdings)
document_title: Public "Alpha" AI + Agentic Brokerage - disclaimers
document_type: dedicated AI disclaimers
url: https://public.com/alpha ; https://public.com/ai-agents/how-it-works
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: yes - "Alpha" (+ "Agentic Brokerage")
ai_vector: generative-agentic
fetch_depth: snippet-only
clause_codes_present: B6(AI), B4(AI no-advice), B3(AI reach-own-conclusions)
vendor: in-house + third-party LLMs
locus: 1 (dedicated AI disclaimers)

## Coding-relevant extract (snippet-only)

"Alpha does not provide financial advice but offers in-depth market data, insights,
and analysis to help you reach your own conclusions about your investments." [B4 +
B3] Material "is not and should not be construed as investment research, advice, or
recommendation to buy or sell a security" [B6/B4]. Agentic Brokerage outputs "for
informational and illustrative purposes only, and should not be considered
investment recommendations or advice."

## Coder note
Standard investing posture: dedicated AI-specific no-advice + accuracy disclaimers
(B6 + B4 + B3 reach-your-own-conclusions) across Alpha and the Agentic Brokerage.
Securities-law-driven. Snippet-only.

---

---
<a name="etoro"></a>
company: eToro
document_title: eToro "Tori" AI investing companion - disclaimer
document_type: dedicated AI disclaimer
url: https://www.etoro.com/trading/platforms/tori/
retrieved: 2026-09-19
effective_or_revised: not captured (relaunched Apr 2026, Grok-powered)
names_ai_feature: yes - "Tori"
ai_vector: generative-agentic (Agent Portfolios)
fetch_depth: snippet-only
clause_codes_present: B6(AI), B4(AI no-advice/no-reliance)
vendor: third-party LLM (xAI Grok)
locus: 1 (dedicated AI disclaimer)

## Coding-relevant extract (snippet-only)

"Tori does not provide investment advice. Tori is an AI-powered tool designed to
offer educational content, data and general market insights. It does not consider
personal circumstances and should not be relied upon for investment decisions."
[B4] "responses may be inaccurate or incomplete and should not be considered
investment advice." [B6]

## Coder note
EU/foreign investing comparator (Grok-powered, agentic Agent Portfolios); standard
securities-law no-advice + accuracy disclaimer (B6 + B4). Snippet-only.

---

---
<a name="ada"></a>
company: Ada Health
document_title: Ada Terms & Conditions (medical AI disclaimer)
document_type: governing terms - dedicated medical/AI disclaimer
url: https://ada.com/us/terms-and-conditions/
retrieved: 2026-09-19
effective_or_revised: Last Updated November 6, 2025
names_ai_feature: yes - "Ada Assess", "Ada PHC"; references third-party LLMs
ai_vector: generative
fetch_depth: full-fetch (WebFetch)
clause_codes_present: B6(AI), B4(AI directive), B3(AI), B8(AI third-party partners), B2(gen); B11 absent
vendor: in-house symptom engine + third-party LLMs
locus: 2 (dedicated medical/AI disclaimer in governing terms)

## Coding-relevant extract (full-fetch)

No diagnosis/advice: "NEITHER ADA ASSESS, ADA PHC NOR OUR WEBSITE MAKE ANY MEDICAL
DIAGNOSES NOR PROVIDE ANY TREATMENT PLANS"; "NOT a suitable substitute for medical
advice." [B6, AI-specific] "Ada does not guaranty accuracy of any output generated
by the Ada PGM, Ada PHC or third party large language AI models"; probabilistic
reasoning "may result in incorrect output." [B4, directive] "evaluate the accuracy
of any output and shall not rely on Ada to do so." [B3] user responsible for
whether to consult a professional. [B8] Ada PHC info "not originated by Ada Health,
but rather from Ada Partners." [B2] sole remedy = cease use. Emergency: contact
emergency services. B11: no GDPR ADM/profiling provision (absent).

## Coder note
EU/DE anchor and strongest healthcare generative posture: an AI-specific accuracy
disclaimer that NAMES LLMs + probabilistic error, directive B4 ("evaluate accuracy
/ do not rely on Ada"), no-diagnosis, B8 third-party carve-out, emergency
escalation. Current (Nov 2025). B11 absent despite GDPR (Marriott pattern).
Generative Moffatt exposure LOW; harm class medical (extreme).

---

---
<a name="khealth"></a>
company: K Health
document_title: K Health Terms of Use (medical disclaimer)
document_type: governing terms - dedicated medical disclaimer
url: https://khealth.com/terms-of-use
retrieved: 2026-09-19
effective_or_revised: Last Updated June 6, 2023
names_ai_feature: yes - "artificial intelligence-enabled symptom checker" (markets "AI Physician")
ai_vector: generative
fetch_depth: full-fetch (WebFetch)
clause_codes_present: B6(AI informational-only), B4(directive + emergency), B3, B2(gen, $100/12mo cap); no AI-specific inaccuracy clause
vendor: in-house
locus: 2 (dedicated medical disclaimer)

## Coding-relevant extract (full-fetch)

"K HEALTH, INC. IS NOT A PROVIDER OF CLINICAL ADVICE"; materials "FOR INFORMATIONAL
PURPOSES ONLY AND ARE NOT A SUBSTITUTE"; the Symptom Checker (defined as "an
artificial intelligence-enabled symptom checker") "DO[ES] NOT CONSTITUTE CLINICAL
CARE, ADVICE OR DIAGNOSIS." [B4] "NEVER DISREGARD PROFESSIONAL CLINICAL ADVICE OR
DELAY... BECAUSE OF ANY INFORMATION"; emergency "CALL YOUR LOCAL EMERGENCY PHONE
NUMBER... IMMEDIATELY"; suicide hotline 988. [B3] user must give accurate info.
[B2] no indirect/consequential; no liability for provider acts or personal injury;
cap = paid in prior 12 months or $100.

## Coder note
Strong no-advice + emergency, names the AI symptom checker - but the disclaimer is
"informational-only / not diagnosis," NOT an AI-specific "may be inaccurate"
accuracy clause (contrast Ada). Terms Last Updated JUNE 2023 - stale vs K Health's
2024-26 "AI Physician" expansion (say-do / vintage-gap). Harm class medical.

---

---
<a name="teladoc"></a>
company: Teladoc Health
document_title: Teladoc disclaimers (no medical advice; Non-Advice Programs)
document_type: site/service disclaimers
url: https://member.teladoc.com/terms/disclaimers ; https://www.teladochealth.com/legal/legal-disclaimer
retrieved: 2026-09-19
effective_or_revised: not captured
names_ai_feature: category - AI assistant / Non-Advice Programs (Livongo, myStrength)
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6(no-advice), B4(emergency); AI-specific accuracy disclaimer not located
vendor: in-house
locus: 3 (generic no-advice clause reaching AI programs)

## Coding-relevant extract (snippet-only)

"The Websites do not provide medical advice and do not create a healthcare
provider/patient relationship." Non-Advice Programs (Livongo, myStrength) "do not
provide medical advice, diagnosis or treatment"; "should not ignore or delay
obtaining professional medical advice"; "call 911 ... for all medical emergencies."

## Coder note
No-advice + emergency (B6/B4) reaching Teladoc's non-clinical AI programs
generically (locus 3). Core telehealth is human clinicians; AI = symptom/nav
assistant + Livongo/myStrength. AI-specific accuracy disclaimer not located.
Snippet-only.

---

---
<a name="hims"></a>
company: Hims & Hers
document_title: Hims & Hers - AI care governance + FTC/states privacy enforcement (adjacent)
document_type: governing terms (AI disclaimer not located) + adjacent enforcement
url: https://www.hims.com/terms-and-conditions ; https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-act-against-hims-hers-deceptive-unlawful-privacy-practices
retrieved: 2026-09-19
effective_or_revised: FTC action July 2026
names_ai_feature: category - "Labs AI" care agent / AI-native care experience
ai_vector: generative (+ health-data harm via enforcement)
fetch_depth: snippet-only
clause_codes_present: dedicated AI medical disclaimer not located; adjacent FTC/states privacy enforcement
vendor: in-house (Labs AI)
locus: not located

## Coding-relevant extract (snippet-only)

Generative "Labs AI" care agent + "AI-native care experience." A dedicated AI
MEDICAL disclaimer was not located in the general T&C (liability/account/privacy
focus); governance likely general T&C + Notice of Privacy Practices (HIPAA).
Adjacent: **FTC + states action, July 2026, for deceptive/unlawful privacy
practices**; separate health-data lawsuit.

## Coder note
Generative care agent confirmed; consumer AI medical disclaimer not located
(registered, not confirmed absent). FTC + states enforcement (privacy/health-data)
is a strong real-world harm anchor - the healthcare counterpart to DoNotPay (legal)
and Klarna (fintech). Follow-up: full-fetch Hims/Hers T&C + Notice of Privacy
Practices.

---

---
<a name="zillow"></a>
company: Zillow
document_title: Zillow Terms of Use (AI-silent) + AI Mode / Fair Housing Classifier
document_type: governing terms (AI-silent, generic no-advice) + operational Fair-Housing guardrail
url: https://www.zillow.com/corporate/terms-of-use/
retrieved: 2026-09-19
effective_or_revised: Updated October 28, 2025
names_ai_feature: no (terms); "AI Mode" launched Mar 2026 (marketing)
ai_vector: generative
fetch_depth: full-fetch (browser); AI Mode via marketing
clause_codes_present: B6/B3(gen no-advice + no-responsibility reaching AI); "Product's Terms" hook; Fair Housing Classifier (operational, not contractual)
vendor: in-house (Zillow AI Mode)
locus: silent/generic

## Coding-relevant extract

Terms **AI-silent** (Oct 28, 2025): no "artificial intelligence"/"generative"/"AI
Mode"; "Fair Housing" only as external links. [B6/no-advice, generic] Sec 1: "THE
SERVICES ARE NOT INTENDED TO provide you with any financial, real estate, or
related advice of any kind." [B3/B2, generic] "Zillow, Inc. assumes no
responsibility for any result or consequence ... any action or inaction that you or
any consumer takes based on the Services." "Product's Terms" hook (per-service terms
may exist). **Fair Housing Classifier (operational):** AI Mode (Mar 2026) ships a
real-time classifier screening user questions AND AI responses to prevent
discriminatory steering - in marketing/engineering, not the contract. Grounded in
"verified listings."

## Coder note
AI-silent governing terms (Oct 2025, pre-AI-Mode) reach the AI only via generic
no-advice + no-responsibility (B6/B3 generic). Distinctive move is the
**operational anti-discrimination Fair Housing Classifier** (Axis D operational +
discrimination-law dimension beyond Moffatt), but it lives outside the contract.
"Product's Terms" hook qualifies the silence. Locus generic/silent.

---

---
<a name="redfin"></a>
company: Redfin
document_title: Redfin Terms of Use (AI-silent re: Ask Redfin)
document_type: governing terms - AI-silent
url: https://www.redfin.com/about/terms-of-use
retrieved: 2026-09-19
effective_or_revised: Effective September 29, 2025
names_ai_feature: no
ai_vector: generative (Ask Redfin, ungoverned)
fetch_depth: full-fetch (WebFetch)
clause_codes_present: B6(gen AS-IS), B8(gen MLS/third-party), B2(gen); AI-silent
vendor: in-house (Ask Redfin; RAG)
locus: silent/generic

## Coding-relevant extract (full-fetch)

Terms **AI-silent** (Sept 29, 2025). [B6] Sec 2.10 "'AS IS' AND 'AS AVAILABLE' ...
DO NOT PROVIDE ANY EXPRESS OR IMPLIED WARRANTIES." [B8] Sec 2.9.7 "Redfin makes no
guarantees as to the reliability, accuracy, or up to date nature of any information
from MLS sources"; third-party content "at your own risk." Generic verify (BAREIS
data "independently reviewed and verified"). [B2] Sec 2.11 excludes indirect/
consequential.

## Coder note
Ask Redfin (RAG virtual assistant, nationwide since 2024; marketed Fair-Housing-
tested) governed by AI-silent general terms - generic AS-IS (B6) + MLS/third-party
carve-out (B8). No AI-specific or Fair-Housing clause. Same pattern as Zillow:
silent contract, operational Fair-Housing testing outside it. Locus generic/silent.

---

---
<a name="rightmove"></a>
company: Rightmove
document_title: Rightmove AI tools - in-product microcopy disclaimer
document_type: in-product microcopy (locus 4)
url: https://www.rightmove.co.uk/press-centre/rightmove-unveils-ai-tools-to-enhance-home-search-experience/ ; https://www.rightmove.co.uk/c/terms-of-use/
retrieved: 2026-09-19
effective_or_revised: not captured (AI tools 2026)
names_ai_feature: category - AI keywords / conversational search / "Style with AI"
ai_vector: generative
fetch_depth: snippet-only
clause_codes_present: B6+B4 (AI-specific microcopy)
vendor: in-house
locus: 4 (microcopy)

## Coding-relevant extract (snippet-only)

Rightmove (UK) AI features "may be marked with a symbol and/or disclaimer": "AI is
smart but can be inaccurate and you should check important information before
relying on it." [B6 + B4, AI-specific microcopy]. Tools: AI keywords, conversational
search, "Style with AI."

## Coder note
UK comparator using the microcopy locus (like Verizon/Alaska): concise AI-specific
accuracy + directive-verify line, not a dedicated AI terms doc. Snippet-only.

---

---
<a name="realestate-identified"></a>
company: Realtor.com (US) / Zoopla (UK)
document_title: Identified consumer generative AI - terms not located this pass
document_type: batch note (register of identified-but-uncoded firms)
retrieved: 2026-09-19
names_ai_feature: yes
ai_vector: generative
fetch_depth: referenced-not-located

## Note
- **Realtor.com (US)** - launched a **ChatGPT app** (+ Spotlight Listings) - the
  app-inside-ChatGPT locus; dedicated AI terms not located.
- **Zoopla (UK)** - enterprise agreement with OpenAI, building an AI roadmap; no
  consumer AI disclaimer located yet.
Registered so their silence is not mistaken for a coded finding; candidates for a
follow-up pass, not confirmed absences.

---

<a name="gapfill-2026-09-23"></a>
## Gap-fill log — 2026-09-23 (registered → coded)

Five firms previously logged `referenced-not-located` were located and coded this pass. Coded set
48 → 53; registered set 12 → 7 (remaining: Monzo, Nubank, Telefónica, Skyscanner, Trip.com,
Realtor.com, Zoopla). documents.csv + analysis/firm-level-codings.csv updated accordingly.

- **Deutsche Telekom → warned (dedicated).** Located a dedicated **"AGB Magenta AI"**
  (https://www.telekom.de/agb/downloads/54806.pdf, Stand 22.08.2025), full-fetch. Names Magenta AI
  / Frag Magenta. Sec 3.4: output "can contain inaccurate or false information," directive "should
  not rely on output without verifying accuracy yourself," no legal/financial/medical advice,
  "hallucinations" acknowledged; Sec 6.1 no warranty; Sec 6.5-6.6 LoL. B6(AI)+B4(directive)+B3+B2.
  Locus 1. Row DT-02 (DT-01 privacy notice retained).
- **Airbnb → warned (integrated).** ToS (help/article/2908, Updated 2026-02-05, full-fetch) Sec 9:
  "Airbnb does not guarantee the accuracy or quality of generated Content or translations and
  Members are responsible for confirming the accuracy of generated Content and translations."
  B6(AI)+B4(verify)+B3. Row ABB-01 upgraded.
- **Hims & Hers → warned (integrated).** ToS states Hims "does not use AI to make clinical
  decisions"; AI-interaction transparency; ALL messages "reviewed and approved by a qualified
  licensed healthcare professional and the provider remains fully responsible for your care"
  (human-review safeguard; responsibility stays with the provider, not shifted to the user).
  Row HIM-01 upgraded; HIM-02 (FTC+states privacy action, July 2026) retained.
- **Chime → peripheral.** Disclosures: guidance "for informational purposes only. Chime does not
  provide financial, legal, or tax advice"; and "where AI impacts member outcomes - like financial
  advice or money movement - humans stay in the loop" (no-advice + human-in-loop). Generative Jade
  agent (~70% of support); no dedicated Jade output disclaimer. Row CHM-01 upgraded.
- **Priceline → peripheral.** Penny (Claude-powered, agentic) carries a microcopy disclaimer
  "Penny can make mistakes" (B6, AI-specific microcopy). Dedicated Penny terms within the general
  T&C not isolated; getpenny.com remains an unrelated entity. Row PCL-01 upgraded.

Analysis layer refreshed to 53 firms: analysis/firm-level-codings.csv, analysis/descriptive-results.md,
analysis/taxonomy-figure.html, coverage-matrix.csv.

---

<a name="b10-sweep-2026-09-23"></a>
## Privacy-notice B11 sweep — 2026-09-23

Swept automated-decision-making (B11) across the previously-untested coded firms. Added 13 new
privacy-notice rows (CHM-02, TRP-03, GRM-02, ABB-02, CHG-02, CNB-02, RMV-02, BKG-02, ZG-02,
KH-02, CMX-02, KHN-02, KAY-02) and upgraded 2 referenced rows (REV-02, GEI-02). documents.csv now
150 rows. **B11 among the 53 coded firms: present (S) = 19 · denial/tested-absent (A) = 25 ·
untested (U) = 9** (was ~half untested).

**Present (B11=S), 19:** Accor, Airbnb, American, Chegg, Chime, Coinbase, Expedia, Frontier,
Grammarly, Hilton, IHG, Klarna, Lemonade, NatWest, Revolut, Tripadvisor, Uber Eats, Vodafone, bunq.

**Two distinct "present" flavours:**
- **Rights-bearing (Art. 22 style):** Revolut (manual review + challenge), Klarna, bunq, NatWest
  (human review/appeal), Chime (inform + explain + human review), Tripadvisor (human intervention),
  Lemonade (underwriting/claims + rights). Concentrated in EU/UK + a few US challengers.
- **Disclosure-only / exemption-framed / jurisdiction-scoped:** Coinbase ("regulatory and
  contractual obligations," no rights), Grammarly/Chegg/Airbnb (disclose ADM/profiling),
  Accor (rights only in the China/PIPL section), American (Brazil LGPD), Uber (Quebec),
  IHG (Brazil), Vodafone (fraud/AML).

**Denial / tested-absent (B11=A), 25 — US-heavy:** the dominant US pattern is the express denial
("we do not make automated decisions with a legal or similarly significant effect") — Booking.com,
Zillow, Rightmove, K Health, Comcast, Khan Academy, Kayak, Target, plus tested-absent GEICO,
Marriott, etc.

**Region split:** EU/UK **55%** carry a B11 regime (6/11) — and rights-bearing; US/other **31%**
(13/42), skewed to disclosure-only or denial. **A (denial) is 22 US vs 3 EU.** This is the
cleanest evidence in the corpus that GDPR Art. 22 makes consumer ADM rights both common and
substantive in the EU, while US firms predominantly disclaim qualifying ADM or scope it to a
specific state/foreign statute.

**Still untested (B11=U), 9:** Deutsche Telekom (German-language privacy), Duolingo, Hims & Hers,
Priceline, Public, Redfin, Robinhood, Teladoc, eToro (several are .com legal pages that bot-wall
non-browser fetch).

---

<a name="find-missing-2026-09-23"></a>
## Find-missing-docs pass — 2026-09-23 (continued)

Located AI/privacy terms for 6 more registered firms via privacy-notice ADM sweep; coded set
53 -> 59; registered 7 -> 1 (only Realtor.com remains, whose consumer AI is a ChatGPT app).

- **Monzo (banking) -> peripheral.** Data privacy policy: if a solely-automated decision
  significantly affects you (e.g. credit refusal), right to manual review by a person + share
  perspective + challenge. B11=S. Generative support-agent output disclaimer still not located.
- **Nubank (banking) -> peripheral.** Privacy: LGPD right not to be subject to solely-automated
  decisions with legal/significant effects; object/review/information. B11=S. Generative terms n/l.
- **Telefónica (telecom) -> peripheral.** Privacy: GDPR right against solely-automated decisions +
  profiling. B11=S. Aura generative output disclaimer not located (AI-ethics page only).
- **Trip.com (travel) -> peripheral.** Privacy: denies qualifying ADM ("does not use AI or other
  automated methods to profile users for decisions that produce legal or similarly significant
  effects") + no AI-training on personal data. B11=A. Output disclaimer not located.
- **Skyscanner (travel) -> peripheral.** Privacy addresses AI: no third-party AI training on
  personal/sensitive platform data; uses genAI features (third-party LLMs) after risk review.
  B11=U. No output disclaimer/ADM regime located.
- **Zoopla (real estate) -> exposed.** Own AI (OpenAI deal) ungoverned; terms carry only a
  third-party-AI carve-out + anti-scraping. B11=U.

Also B11-coded this pass: Priceline (A - profiling/ad opt-out only), Duolingo (A - profiling for
ads, no legal-effect ADM). documents.csv now 158 rows. Analysis layer regenerated (firm-level 59,
descriptive-results, taxonomy figure, coverage-matrix).

**Still open:** Realtor.com (registered); B11 untested (9): Deutsche Telekom (German privacy),
Hims & Hers, Public, Redfin, Robinhood, Skyscanner, Teladoc, Zoopla, eToro; snippet-only anchors
(14) for full-fetch; 5 app-only microcopy (need screenshots).

---

<a name="retail-nov2022-baseline-2026-09-23"></a>
## November 2022 (pre-ChatGPT) baseline â€” Retail batch â€” 2026-09-23

Second batch of the diachronic baseline project (first was airlines, see
`previous-tos/FINDINGS-airlines-nov2022-baseline.md`). Wayback CDX snapshots pinned to the
closest available capture to **2022-11-30** were retrieved for all five retail-batch companies'
governing consumer terms and stored under `previous-tos/retail/<company>/`. Tooling
(`previous-tos/_tools/wb-fetch.sh`, `wb-save.sh`, `wb-birthdate.sh`) was generalized to take a
`vertical` parameter (previously hardcoded to `airlines`).

| Company | Nov-2022 snapshot ts | AI keyword hits (baseline) | Current status |
|---|---|---|---|
| Walmart | 20221130080639 | 0 | AI-specific Â§16.J "Chatbots and Use of Generative AI" (see [#walmart](#walmart)) |
| Amazon | 20221113103941 | 0 | Now AI-specific â€” see [correction](#amazon-correction-2026-09) below |
| Lowe's | 20221130195140 | 0 | Still confirmed AI-silent as of Aug 2026 full-fetch (see [#lowes](#lowes)) â€” only company in the batch with **zero movement** in ~4 years despite Mylow's (May 2025) |
| Target | 20221128074519 | 0 | AI-specific "Agentic Commerce and Delegated Access" section (see [#target](#target)) |
| Home Depot | 20221130131408 | 0 | Now AI-specific â€” see [correction](#homedepot-correction-2026-09) below |

All five governing documents are **completely AI-silent at the Nov-2022 baseline** â€” zero hits for
any of: artificial intelligence, generative ai, ai-powered, chatbot, ai-generated, large language
model, ai features, ai tool, rufus, agentic. This is the cleanest baseline result across either
batch retrieved so far (contrast Delta/Alaska in the airline batch, where some adjacent documents
already carried non-AI anti-reliance boilerplate at baseline).

Manifest rows appended to `previous-tos/WAYBACK-MANIFEST.csv` (vertical="retail").
Home Depot's baseline URL (`homedepot.com/c/Terms_of_Use`) was itself a new find this session â€”
the live document had previously been marked `referenced-not-located` (see original
[#homedepot](#homedepot) entry); CDX confirmed continuous archival coverage 2013â€“present, so it is
in fact Home Depot's real, actively-revised main site ToU, not a dead/moved page.

**Birth-dating â€” CORRECTED 2026-09-25.** This paragraph originally said Home Depot's post-2024
Wayback captures were empty JS shells and that birth-dating was blocked. That was wrong on both
counts. The captures contain the full Terms text as JSON inside `<script>` tags, which this
project's plaintext extractor strips (hence only ~5,200 chars survived). The birth-date search
failed because of a Windows CRLF bug in `wb-birthdate.sh`, not because of the snapshots. With the
script fixed, the AI clause birth is **absent 2025-05-25 â†’ present 2025-05-31**, preserved at
`previous-tos/retail/homedepot/homedepot_terms-of-use_BIRTH-VERSION_20250531095350_RAW.html`.
**Rule going forward:** keyword-scan the RAW HTML, not only the derived plaintext, then inspect each
hit's context to exclude site-configuration noise.

---

<a name="amazon-correction-2026-09"></a>
## CORRECTION â€” Amazon Conditions of Use, re-fetched 2026-09-23

The original entry above ([#amazon](#amazon), retrieved 2026-08-02) logged Amazon's Conditions of
Use as snippet-only/robots-blocked. A later full-fetch (`AMZ-01` in documents.csv, captured
2026-08-26 via direct fetch, 21,967 chars) confirmed the document **AI-silent** â€” zero hits for
AI/generative/Rufus/Alexa/machine learning. **That finding is now superseded.** A rendering-browser
fetch on 2026-09-23 shows the document, dated "Last updated: August 14, 2026" in-body, has been
revised to add two AI-relevant clauses absent from the 2026-08-26 capture:

**1. Anti-training clause (B9), inside LICENSE AND ACCESS:**
> "You will not, and will not allow any third party to, use AI-generated content from the Amazon
> Services to, directly or indirectly, develop or improve large language or multimodal models,
> machine learning models or related technology."

This runs the opposite direction from a typical B9: it is Amazon restricting *customers* from
using Amazon's AI output to train competing models, not a disclaimer about Amazon's own AI
reliability.

**2. Dedicated "Agents" section (B5) â€” full standalone agentic-AI clause:**
Defines "Agent" as any software taking autonomous/semi-autonomous action on a user's behalf;
requires every Agent to self-identify via a `User-Agent: Agent/[name]` header on all requests; bars
concealment of automated behavior (mimicking human keystroke timing, bypassing CAPTCHAs); requires
truthful answers to bot-detection challenges; and reserves Amazon's right to block Agents at its
sole discretion. Structurally parallel to Target's "Agentic Commerce and Delegated Access" clause
(see [#target](#target)) and part of the same 2025-26 wave of retailer agentic-commerce clauses,
but framed entirely around anti-scraping/bot-detection compliance â€” **no B1 transaction-error /
non-honoring language specific to agent-placed orders was found** in this section or elsewhere in
the document.

Neither new clause names Rufus or "Alexa for Shopping" â€” the gap in the *original* finding (no
Rufus-specific clause located) still stands. What has changed is that the document is no longer
AI-silent in the aggregate; it now carries a generic (Locus 3) but genuinely AI-specific clause
family. Full excerpt saved to
`mastersheet-sources/retail/amazon/amazon_conditions-of-use_LIVE-2026-09-23.txt`; coded as
`AMZ-05` in documents.csv (supersedes nothing â€” `AMZ-01` is kept as the dated historical capture).
Direct fetch remains robots.txt-blocked; this and all `LIVE-2026-09-23` captures in this session
used the rendering browser.

**fetch_depth:** full-fetch-browser (AI-relevant sections; boilerplate sections unchanged from
AMZ-01 and not re-transcribed, consistent with the project's quote-sparingly rule)

---

<a name="homedepot-correction-2026-09"></a>
## CORRECTION â€” Home Depot Terms of Use, re-fetched 2026-09-23

The original entry above ([#homedepot](#homedepot), retrieved 2026-08-02) could not locate Home
Depot's main site ToU at all. That gap was closed on 2026-08-27 via a user-supplied file
(`HomeDepotTOS.txt`, coded `HD-01`), which found the document **confirmed AI-silent** with respect
to Magic Apron â€” 0 hits for "Magic Apron," and the document's 11 "AI-generated" hits were all TCPA
SMS-consent boilerplate, not shopping-assistant language (see
`mastersheet-sources/retail/home-depot/homedepot_terms-of-service_CAPTURE-NOTE.md` for the full
prior analysis, which remains a correct read of the document *as it stood on 2026-08-27*).

**That AI-silent finding is now superseded.** A rendering-browser fetch on 2026-09-23 of the live
`homedepot.com/c/Terms_of_Use` (same URL, confirmed via Wayback CDX to be continuously archived
since 2013 and hence the genuine governing document, not a dead page) shows two new AI-relevant
passages, both absent from the 2026-08-27 capture:

**Â§3(d) Prices and Errors â€” AI accuracy/anti-reliance language (B6 + B4):**
> "We may also provide AI powered features to provide a better online shopping experience for our
> customers. We aim to have these features be as accurate as possible; however, always read
> labels, warnings, and directions and other information provided with a product before using a
> product."

**Â§7 Uploaded Content â€” AI-training-data license (B10), appended to the existing perpetual
content license:**
> "...or use such content as training data for AI features or tools, throughout the world without
> compensation to you."

Both clauses use the generic term "AI powered features" â€” Magic Apron is still never named by
brand anywhere in the document (Locus 3, not a dedicated AI section). The Â§12 Texting Programs
"AI-generated... messages" boilerplate that the 2026-08-27 note correctly identified as unrelated
TCPA consent language is unchanged and still not evidence of Magic Apron liability drafting.

**Vintage note:** the in-body copyright line still reads "Â© 2016 â€“ 2025," unchanged from the prior
capture, confirming CLAUDE.md's instruction to use the stated revision date rather than the
copyright line as the vintage signal â€” the copyright line is not being updated in step with
substantive revisions.

~~This is the fastest observed AI-silent â†’ AI-aware turnaround documented anywhere in this
corpus: under four weeks (2026-08-27 â†’ 2026-09-23).~~ **CORRECTED 2026-09-25: no such flip
occurred.** A Wayback birth-date search shows both clauses above were live by **2025-05-31**
(absent 2025-05-25). The 2026-08-27 "AI-silent" capture (`HD-01`, a user-supplied file) was
therefore a stale copy predating the May 2025 revision, and its coding was wrong at its own capture
date. Home Depot's actual timeline: silent 2022-11-30 â†’ AI clause added between 2025-05-25 and
2025-05-31, about two to three months after Magic Apron's March 2025 launch â†’ unchanged through
2026-09-23. This fits the airline-batch pattern (clause follows product), not a sudden late flip.

Full excerpt saved to
`mastersheet-sources/retail/home-depot/homedepot_terms-of-use_LIVE-2026-09-23.txt`; coded as
`HD-06` in documents.csv. Direct/curl fetch of this URL remains bot-walled (confirmed again this
session); the rendering browser also required a scroll event before the Terms body hydrated â€” a
plain unscrolled DOM read returns only nav chrome and would misreport this document as still
AI-silent.

**fetch_depth:** full-fetch-browser (AI-relevant sections)

---

<a name="banking-nov2022-baseline-2026-09-23"></a>
## November 2022 (pre-ChatGPT) baseline â€” Banking batch â€” 2026-09-23

Third batch of the diachronic baseline project (after airlines, then retail). Full write-up in
`previous-tos/FINDINGS-banking-nov2022-baseline.md`; summary here per the project's
always-append convention.

| Company | Document | Snapshot | AI hits at baseline |
|---|---|---|---|
| Wells Fargo | Online Access Agreement | 2022-12-01 | 0 |
| Wells Fargo | General Terms of Use | **2022-11-24** (6 days pre-ChatGPT) | **"chatbot" Ã—3** â€” see finding below |
| Dave | Terms of Use | 2022-08-03 | 0 |
| Klarna | User Terms for Shopping Service | 2022-06-23 | 0 |
| bunq | Privacy Policy | 2022-12-29 | 0 |
| NatWest | Privacy Policy | 2022-12-08 | 0 |
| Capital One | Terms & Conditions | not retrievable â€” genuine Wayback capture gap since Apr 2021, not a robots block | n/a |
| Revolut | AI Assistants disclaimer | confirmed non-existent at baseline â€” earliest capture anywhere is 2023-06-02 | n/a |

**Headline finding: Wells Fargo's chatbot-disclosure clause pre-dates ChatGPT.** The Nov-24-2022
capture of the General Terms of Use â€” six days before ChatGPT's 30 Nov 2022 launch â€” already
reads: "During your use of the Chat service, you may interact with a bot, chatbot, virtual
assistant, virtual concierge, or other non-human (each, a 'Chatbot'). We will disclose the use of
the Chatbot to the extent required by applicable law... chats will be monitored and saved." The
live document (fetched Aug 2026, see [#wellsfargo](#wellsfargo) if present or the Wells Fargo entry
above) carries the identical clause with one word changed ("saved" â†’ "retained"). Wells Fargo's
generative assistant Fargo launched years after this clause was written and is still not named by
it. This is the project's first document-level proof (not an inference from a copyright year) that
a chatbot-disclosure clause can predate the generative-AI era entirely and simply be left to cover
a later, functionally different product without revision.

**Two gaps, kept distinct rather than merged into one "not found":** Capital One's governing terms
page has zero successful Wayback captures since April 2021 (confirmed not a robots.txt block;
cause otherwise undetermined) â€” an archival gap, the live document is still held and coded. Revolut's
dedicated AI-assistants disclaimer page itself did not exist before 2023-06-02 â€” a document-absence
finding, not a fetch failure. See the FINDINGS doc Â§4 for the full distinction.

bunq's currently-coded privacy-policy URL (`/documents/privacy-policy`) did not exist under that
path until 2025; the Nov-2022 baseline was fetched from `/doc/privacy`, an earlier path in the same
document's history, confirmed via a domain-wide CDX check. Flagged as a general method note: a
single-URL CDX query can produce a false "no baseline" for any company that has restructured its
site since 2022 â€” check the whole domain before concluding a document has no archived history.

---

<a name="food-delivery-nov2022-baseline-2026-09-24"></a>
## November 2022 (pre-ChatGPT) baseline â€” Food-delivery batch â€” 2026-09-24

Fourth batch of the diachronic baseline project (after airlines, retail, banking). Full write-up
in `previous-tos/FINDINGS-food-delivery-nov2022-baseline.md`; summary here per the project's
always-append convention.

| Company | Document | Snapshot | AI hits |
|---|---|---|---|
| Instacart | Terms of Service | 2022-11-29 | 0 |
| Uber Eats | General Terms of Use (US) | 2022-06-26 | 0 |
| Uber Eats | "Generative AI features at Uber" (dedicated page) | confirmed non-existent (earliest capture 2025-11-14) | n/a |
| Gopuff | Terms & Conditions | 2022-11-28 | 0 |
| Gopuff | Privacy Center | captured, **unreadable** â€” JS-only shell, 1,651 bytes | n/a |
| DoorDash | Consumer Terms and Conditions | captured (3 fragments), **unreadable** â€” JS-only shell | n/a |

**Headline: an archival failure mode, confirmed for two companies.** *(Corrected 2026-09-25:
originally "three companies, following Home Depot". Home Depot's captures were JSON-embedded, not
empty; see the retail correction above.)* Gopuff's Privacy Center (Transcend.io) and DoorDash's
Consumer Terms (Salesforce Community Hub, split across three separate Knowledge articles) captured
as empty JavaScript application shells. Re-checked on the **raw** HTML: no legal vocabulary at all. A
rendering-browser workaround was deliberately not attempted for the archived copies, because a
Wayback SPA shell's JS typically calls the site's *live, current* API rather than replaying
archived data â€” doing so risks silently loading 2026 content into a document labeled 2022. DoorDash's
live 2026 document remains held/coded separately (direct fetch succeeded then); only the archived
Nov-2022 baseline is unreadable. Where content *was* retrievable (Instacart, Uber Eats, Gopuff's
Terms & Conditions), the baseline is clean: zero AI-specific hits, continuing the pattern from every
prior batch except Wells Fargo.

Two URL-history recoveries, same method as bunq in the banking batch: Uber Eats' current coded URL
has no capture under its literal query-string ordering (the real 2022 capture uses different
tracking-parameter ordering, found via a domain-wide CDX prefix search); Gopuff's current `/e/`
path has no captures before mid-2023 (the 2022-era document lived at the pre-redesign `/go/` path).

---

<a name="hospitality-nov2022-baseline-2026-09-25"></a>
## November 2022 (pre-ChatGPT) baseline — Hospitality batch — 2026-09-25

Fifth batch of the diachronic baseline project. Full write-up in
`previous-tos/FINDINGS-hospitality-nov2022-baseline.md`.

| Company | Document | Snapshot | AI hits |
|---|---|---|---|
| Marriott | Terms of Use | 2022-11-26 ("Effective December 5, 2019") | 0 |
| IHG | Terms of Use | 2022-11-29 ("Effective Date: 13 April 2022") | 0 |
| Hilton | Site Usage Agreement | 2022-11-26 | 0 |
| Accor | ALL Loyalty T&Cs | not located in window | n/a |

**IHG — verbatim-frozen.** A sentence-level diff of the Nov-2022 capture against the 2026-09-10
capture of the same URL: 139 of 149 sentences identical, and every difference is navigation chrome
(new brand-selector entries; a "Chat with us" header link). No legal sentence changed. The contract
governing IHG's 2026 generative travel planner is the one in force before ChatGPT existed.

**Marriott — B1 retrofitted, not drafted.** The current AI-reaching transaction-error clause
(Section 4.D, see [#marriott](#marriott)) is the 2022 "Inaccuracies and Errors" typo clause, edited:
"including Ask Bonvoy" and "including those arising from automated or AI-powered technologies"
inserted; "including after confirmation of a transaction" added; a reasonable-efforts remediation
promise added. The non-honoring core ("no obligation to honor") predates ChatGPT. Birth bound for
the AI language: absent in the latest archived capture (2026-06-06) → present in the live fetch
(2026-09-18), consistent with the July 2026 revision after the June 2026 Ask Bonvoy launch.

**Hilton** — Site Usage Agreement AI-silent then and now; its dedicated AI Terms still have no pinned
URL, so no baseline exists for them. **Accor** — archived copy `referenced-not-located`; low impact
(its consumer AI is a ChatGPT app launched Jan 2026).

**Tooling:** `wb-birthdate.sh` had been silently broken on Windows (CRLF from Python kept by
`mapfile` corrupted every probe URL) — this, not a network error, caused the retail batch's Home Depot
birth-date failure. Fixed, along with an open-ended date window, a non-looping unreadable-skip, and a
thin-capture guard.

---

<a name="clause-continuity-2026-09-27"></a>
## Clause continuity, Nov 2022 → 2026 (cross-batch) — 2026-09-27

Reframes the baseline work around two questions: are firms changing their terms, and are our coded
clauses new or inherited 2022 text? Full analysis: `previous-tos/FINDINGS-clause-continuity.md`.
Summary:

- **Churn varies widely.** Frozen: IHG ToU 99% of sentences verbatim since Nov 2022, Hilton Site
  Usage Agreement 97%, Delta site terms 92%. Rewritten: Instacart 3%, American 15%, Marriott 24%,
  Home Depot 33%, each alongside new AI terms. Lowe's, Gopuff and Dave each replaced roughly half
  their text and still added no AI language (the strongest silence findings).
- **Generic (G) codes are mostly inherited boilerplate:** 66% of sentences in G-coded families are
  verbatim 2022 text (B6 79%, B7 79%, B2 78%).
- **AI-specific (S) language is overwhelmingly new** (157 of 170 AI-mentioning sentences). There are
  8 retrofits where AI words were spliced into 2022 sentences: American AS-IS, Walmart site
  definition and anti-scrape, Target B3, Home Depot B10, Marriott IP clause and B1. Wells Fargo is the
  only firm with pre-2022 AI-category language.
- **AMZ-01 was a stale kiosk-mirror copy**: Amazon's Agent Terms date from 2025-05-13 → 2025-06-20.

---

<a name="unitedhealth"></a>
## UnitedHealth Group (UnitedHealthcare) - Avery - collected 2026-10-06

**AI feature.** Avery, a generative-AI "companion" in the UnitedHealthcare app and on myuhc.com,
launched 2026-03-26. Chat modality. It answers coverage, cost-estimate, claim-status and EOB
questions, does provider search and appointment scheduling, and hands off to human advocates
(UHC says 90% of Avery sessions need no handoff). Transaction stakes: benefit and coverage
information (financial-decisional and advisory). Roster: NAICS 5241, rank 1, main sample.

company: UnitedHealth Group (UnitedHealthcare)
document_title: Terms of Use (UnitedHealthcare online and mobile services)
document_type: t1-governing-terms (site + app terms)
url: https://www.uhc.com/privacy/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Effective Date July 10, 2023 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (chat)
fetch_depth: full-fetch
clause_codes_present: B6 (generic: AS-IS, no warranty of error-free service), B2 (generic)
vendor: none named
files: mastersheet-sources/insurance/unitedhealth/uhc_terms-of-use_RAW.html (+ .txt)

company: UnitedHealth Group (UnitedHealthcare)
document_title: Terms of Use (myUHC messaging / online services, PDF)
document_type: t1-governing-terms
url: https://messaging.myuhc.com/public/terms
retrieved: 2026-10-06
effective_or_revised: Effective Date December 13, 2024 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (chat)
fetch_depth: full-fetch
clause_codes_present: B6 (generic), B2 (generic)
vendor: none named
files: mastersheet-sources/insurance/unitedhealth/myuhc_messaging-terms.pdf (+ .txt)

company: UnitedHealth Group (UnitedHealthcare)
document_title: Meet Avery: One AI Companion elevating health care experiences (broker news page, "Disclaimers" block)
document_type: t4-in-product-microcopy (disclaimer text published on a firm web page; in-app display NOT verified) + t6-marketing
url: https://www.uhc.com/agents-brokers/employer-sponsored-plans/news-strategies/avery-ai-companion
retrieved: 2026-10-06
effective_or_revised: page dated May 22, 2026
names_ai_feature: yes - by brand (Avery)
ai_vector: generative (chat)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific), B4 (AI-specific), B1-analog (AI-specific; see note)
vendor: none named
files: mastersheet-sources/insurance/unitedhealth/uhc_TYPE6_avery-broker-page_RAW.html (+ .txt)

company: UnitedHealth Group (UnitedHealthcare)
document_title: UnitedHealthcare Introduces AI Companion ... (newsroom release)
document_type: t6-marketing
url: https://www.uhc.com/news-articles/newsroom/avery-announcement
retrieved: 2026-10-06
effective_or_revised: March 26, 2026
names_ai_feature: yes - by brand
ai_vector: generative (chat)
fetch_depth: full-fetch
clause_codes_present: n-a (say side)
files: mastersheet-sources/insurance/unitedhealth/uhc_TYPE6_avery-announcement_RAW.html (+ .txt)

company: UnitedHealth Group (UnitedHealthcare)
document_title: Privacy hub page (uhc.com/privacy)
document_type: privacy-notice (index page)
url: https://www.uhc.com/privacy
retrieved: 2026-10-06
effective_or_revised: Effective Date July 10, 2023 (stated)
names_ai_feature: no
fetch_depth: full-fetch (hub page only; the HIPAA Notice of Privacy Practices was not separately fetched)
clause_codes_present: none (B11 not present on this page)
files: mastersheet-sources/insurance/unitedhealth/uhc_privacy-hub_RAW.html (+ .txt)

## Coding-relevant extract

**Governing terms are AI-silent and pre-launch.** Both the uhc.com Terms of Use (eff. 2023-07-10)
and the myUHC terms PDF (eff. 2024-12-13) cover UHC's "Online Services" including the apps, so
they reach Avery generically. Neither mentions AI, chat assistants, or outputs. Both predate
Avery's March 2026 launch and were not revised for it. Their only relevant language is generic:
services "as is", no promise of error-free operation, standard damages limits.

**The only AI-specific language is a disclaimer on firm web pages.** The broker page carries a
"Disclaimers" block, paraphrased: Avery uses generative AI to give general information; responses
may be incomplete or inaccurate and "should not be relied upon as error-free" (B6 + B4); Avery is
informational only and is not medical advice, a benefit determination, a guarantee of coverage,
a referral, or an authorization for services; it does not replace a provider's judgment.

**B1-analog.** "Not a benefit determination / guarantee of coverage / authorization" is the
insurance version of a transaction-error non-honoring clause: it pre-declares that what the AI
says about coverage does not bind the insurer. That is the exact *Moffatt* fact pattern (an AI
misstating what the firm will pay). Coded B1-analog rather than B1 because it disclaims the
legal effect of the statement instead of refusing to honor a transaction.

## Coder note
1. **Locus 4 (microcopy-only), with an open question.** The disclaimer is not incorporated into
   any binding document found. Whether the same text is shown inside Avery in the app was not
   verified (no member login). If it is, it is in-product microcopy; if not, it is marketing-page
   text with no assent at all. Assent: Avery is reached after myUHC login (the online-services
   terms bind by use), but nothing AI-specific is presented at that point as far as captured.
2. **Vintage finding.** Terms dated 2023 and 2024, AI launched 2026: silence is pre-launch, not a
   recent AI-silent revision.
3. **Say-do.** The announcement stresses "rigorous oversight and governance" and human expertise
   guiding output, and a 90% containment rate; the binding terms say nothing about the AI.
4. **Incident context (not customer-facing AI, not coded):** *Estate of Lokken v. UnitedHealth*
   (D. Minn., Feb 2025 ruling) concerns the nH Predict model in Medicare Advantage claim
   decisions. That is internal decisional AI, out of scope under the consumer-interaction test,
   but relevant background for B11.
5. **Gaps:** HIPAA Notice of Privacy Practices not fetched (B11 unchecked); Avery in-app
   microcopy not verified; no dedicated AI terms found (2 targeted searches).

---

<a name="centene"></a>
## Centene (Ambetter Health) - Amber - collected 2026-10-06

**AI feature.** Amber, an "AI-powered virtual assistant" for Ambetter marketplace members,
announced 2020-11-12. Chat modality. Answers benefit/deductible/cost questions, delivers the
digital ID card, helps set up the portal account, and **takes premium payments** (a transactional,
partly agentic function). Roster: NAICS 5241, rank 2, main sample. **Liveness flag:** the only
firm-source evidence is the 2020 release; no 2025-26 firm page naming Amber was found in one
targeted search. The screen counted it, but its pre-cutoff liveness should be re-verified.

company: Centene Corporation (Ambetter Health)
document_title: Terms & Conditions (ambetterhealth.com)
document_type: t1-governing-terms (site + "Service")
url: https://www.ambetterhealth.com/terms-conditions.html (redirects to /en/terms-conditions/)
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no - zero AI-keyword hits; "chat" appears only in a legacy "chat rooms, bulletin boards" user-contribution clause
ai_vector: generative/assistive (chat) + transactional (premium payment)
fetch_depth: full-fetch
clause_codes_present: B6 (generic: AS-IS, no warranty of accuracy/reliability), B4 (generic: reliance on site information at your own risk), B2 (generic, s.9)
vendor: none named
files: mastersheet-sources/insurance/centene/ambetter_terms-conditions_RAW.html (+ .txt)

company: Centene Corporation (Ambetter Health)
document_title: Ambetter Privacy Policy
document_type: privacy-notice
url: https://www.ambetterhealth.com/privacy-policy.html
retrieved: 2026-10-06
effective_or_revised: LAST UPDATED February 17, 2025 (stated)
names_ai_feature: no - lists "online chats" among collected communications records; no AI or ADM language
fetch_depth: full-fetch
clause_codes_present: none (no B11)
files: mastersheet-sources/insurance/centene/ambetter_privacy-policy_RAW.html (+ .txt)

company: Centene Corporation (Ambetter Health)
document_title: Use of Artificial Intelligence (AI)-Based Algorithms in Health Care Service Reviews (member news, Nebraska page)
document_type: t6-regulatory (state-mandated style AI-use disclosure; decisional AI, not the chat assistant)
url: https://www.ambetterhealth.com/en/ne/resources/member-news/artificial-intelligence-based-algorithms-health-care-service-reviews/
retrieved: 2026-10-06
effective_or_revised: dated 12/18/25
names_ai_feature: no (concerns utilization-review algorithms)
fetch_depth: full-fetch
clause_codes_present: B11-adjacent (disclosure of decisional AI; not a consumer-facing system, so not coded)
files: mastersheet-sources/insurance/centene/ambetter_ai-algorithms-notice_RAW.html (+ .txt)

company: Centene Corporation (Ambetter Health)
document_title: Ambetter Leverages Technology to Improve the Enrollment and Membership Experience (press release)
document_type: t6-marketing
url: https://investors.centene.com/2020-11-12-Ambetter-Leverages-Technology-to-Improve-the-Enrollment-and-Membership-Experience
retrieved: 2026-10-06
effective_or_revised: 2020-11-12
names_ai_feature: yes - by brand (Amber)
fetch_depth: full-fetch
files: mastersheet-sources/insurance/centene/ambetter_TYPE6_amber-launch-2020_RAW.html (+ .txt)

## Coding-relevant extract

**Governing terms: undated, AI-silent.** The site Terms & Conditions govern "the Site" and "the
Service" and so reach Amber generically. No AI or assistant language. Relevant generic clauses:
use is at your sole risk; site, service and materials "AS IS"/"AS AVAILABLE" with an express
disclaimer of reliability and accuracy warranties (B6); reliance on site information is at your
own risk (B4, generic); standard damages exclusion (B2). No transaction-error clause (no B1),
although Amber can take premium payments.

**AI disclosure exists, but for decisional AI only.** A Dec 2025 member-news notice says AI
algorithms may help *approve* service requests, are never used to deny, and that licensed
clinicians make adverse determinations. This is a regulator-driven disclosure about internal
utilization review, not about Amber.

## Coder note
1. **Locus 5 / generic-only.** No AI-specific language reaches Amber in any document found. Code
   as generic clauses reaching an (unnamed) AI feature; Amber is never named in a legal document.
2. **Vintage:** terms undated, so vintage vs. the 2020 launch cannot be assessed (`date_basis:
   not-stated`). Privacy policy (Feb 2025) postdates launch and is AI-silent.
3. **Say-do:** the 2020 release claims 60%+ of members introduced to Amber engage with it and
   report high satisfaction; terms are silent on it.
4. **Gaps:** Amber's in-chat microcopy not captured (behind member login); member-portal terms
   (my.ambetterhealth.com) not located; state Evidence of Coverage not checked for AI language.

---

<a name="elevance"></a>
## Elevance Health (Anthem) - Virtual Assistant in Sydney Health - collected 2026-10-06

**AI feature.** "Virtual Assistant" in the Sydney Health app and on Elevance-affiliated plan
websites, a conversational assistant for coverage, cost-estimate and provider-search questions
(e.g. "is my surgery covered, and how much will it cost?"). Expanded to ~22M commercial members
on 2025-12-05. The app also has an AI-driven symptom checker. Chat modality. Roster: NAICS 5241,
rank 3, main sample. The app is provided "through an arrangement with Carelon Digital Platforms",
an Elevance subsidiary (same corporate group, so not a third-party-vendor document problem).

company: Elevance Health (Anthem Blue Cross Blue Shield)
document_title: Anthem Terms Of Use
document_type: t1-governing-terms (applies to Anthem "mobile applications and websites", i.e. reaches Sydney Health)
url: https://www.anthem.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Effective October 1, 2026; Last Reviewed October 1, 2026 (stated). NOTE: after the 2026-06-30 cutoff
names_ai_feature: no. One AI hit, and it is about the USER's AI agents, not Anthem's assistant
ai_vector: generative (chat) + symptom checker
fetch_depth: full-fetch
clause_codes_present: B5 (AI-specific, restrictive: user AI agents prohibited), B9-adjacent (anti-scraping), B6 (generic AS IS), B2 (generic "No Liability"), B8 (generic: third-party health content), plus a generic not-medical-advice clause
vendor: Carelon Digital Platforms (affiliate); LiveHealth Online terms incorporated for virtual visits
files: mastersheet-sources/insurance/elevance/anthem_terms-of-use_RAW.html (+ .txt)

company: Elevance Health (Anthem)
document_title: Anthem Privacy statement (website)
document_type: privacy-notice
url: https://www.anthem.com/privacy
retrieved: 2026-10-06
effective_or_revised: effective January 1, 2020 (stated; revision clause not parsed)
names_ai_feature: no - zero AI-keyword hits
fetch_depth: full-fetch
clause_codes_present: none
files: mastersheet-sources/insurance/elevance/anthem_privacy_RAW.html (+ .txt)

company: Elevance Health (Anthem)
document_title: Sydney Health app page
document_type: t6-marketing
url: https://www.anthem.com/member-resources/sydney-app
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: names the app; Carelon arrangement disclosed in footer
fetch_depth: full-fetch
files: mastersheet-sources/insurance/elevance/anthem_sydney-app-page_RAW.html (+ .txt)

company: Elevance Health
document_title: Elevance Health Expands Virtual Assistant to Help Members Navigate Healthcare with Confidence
document_type: t6-marketing
url: https://www.elevancehealth.com/newsroom/elevance-health-expands-virtual-assistant-to-help-members-navigate-healthcare-with-confidence
retrieved: 2026-10-06
effective_or_revised: 2025-12-05
names_ai_feature: yes (by generic name "Virtual Assistant")
fetch_depth: full-fetch
files: mastersheet-sources/insurance/elevance/elevance_TYPE6_virtual-assistant-expansion_RAW.html (+ .txt)

## Coding-relevant extract

**Assent and reach.** The Terms bind by use and apply to every Anthem app and website linking to
them, so they reach the Virtual Assistant generically.

**B5, restrictive form (AI-specific).** A new prohibited-use item bars accessing any Application
"through an artificial intelligence enabled system, agent, bot, or other automated means",
including technologies acting for a user to retrieve claims, benefit or account information,
unless Anthem authorizes it in writing; Anthem may suspend such access. This is the first
anti-user-agent clause in the v2 collection: AI language aimed at the customer's AI, not the firm's.

**Nothing about Anthem's own assistant.** No clause addresses the Virtual Assistant, its answers,
or their accuracy. Coverage and cost answers fall under generic clauses only: Application,
services, content and information "AS IS" with all warranties disclaimed (B6); "No Liability"
for any damages, capped at actual damages (B2); not a substitute for medical advice, do not
delay care because of something read on the Application; no representation about third-party
health content (B8). There is a provider-directory accuracy caveat (directories may be out of
date) but no equivalent for cost estimates or coverage answers. No B1.

## Coder note
1. **Strong vintage finding.** The Terms were revised on 2026-10-01, ten months after the
   assistant reached 22M members, and the revision added AI language, but only to restrict users'
   AI agents. The firm's own AI remains unaddressed. Locus 5 for the deployed assistant (generic
   clauses only); the new AI clause is B5-restrictive.
2. **Version problem.** The coded version postdates the 2026-06-30 cutoff. The version in force at
   the cutoff was not retrieved (Wayback CDX timed out). Whether the agent ban existed before
   October is unknown. Re-try the archived copy before freezing.
3. **Say-do.** Release reports that ~9 in 10 pilot users found answers and promotes personalized
   cost estimates and coverage breakdowns in seconds; no document disclaims those estimates.
4. **Gaps:** in-app microcopy for the Virtual Assistant not captured (member login); Sydney Health
   app store terms / Carelon EULA not separately located; HIPAA NPP not fetched (B11 unchecked).

---

<a name="statefarm"></a>
## State Farm - AI virtual assistant for first notice of loss (pilot) - collected 2026-10-06

**AI feature.** An "AI-powered virtual assistant" being piloted to streamline initial
loss reporting (first notice of loss): gathers accident facts, connects customers to services,
routes to a human claims professional. Announced in the "Next Gen Good Neighbor" release
(May 2026; trade press dates it 2026-05-12), alongside an OpenAI partnership. Modality not stated
(voice or digital). Navi and Household Story are agent-facing tools (out of scope). Roster: NAICS
5241, rank 5, main sample. **Liveness flag:** "piloting" in May 2026; no evidence found on whether
the pilot was live to real customers by 2026-06-30, or in which channel.

company: State Farm Mutual Automobile Insurance Company
document_title: Terms of Use (statefarm.com)
document_type: t1-governing-terms (site; includes an "Online Claims Submissions" clause)
url: https://www.statefarm.com/customer-care/disclosures/terms-of-use
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative/assistive (claims intake)
fetch_depth: full-fetch
clause_codes_present: B1-analog (generic: claim submission does not commit coverage; quotes are estimates, not a contract or binder), B6 (generic AS IS), B2 (generic, no liability for any damages)
vendor: none named in terms (OpenAI named as partner in the release)
files: mastersheet-sources/insurance/state-farm/statefarm_terms-of-use_RAW.html (+ .txt)

company: State Farm
document_title: Privacy policy landing page
document_type: privacy-notice (hub page only)
url: https://www.statefarm.com/customer-care/disclosures/privacy-policy
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no
fetch_depth: full-fetch (thin hub page; the full privacy notice was not reached)
clause_codes_present: none
files: mastersheet-sources/insurance/state-farm/statefarm_privacy-policy_RAW.html (+ .txt)

company: State Farm
document_title: Our Next Gen Good Neighbor Customer Experience (newsroom)
document_type: t6-marketing
url: https://newsroom.statefarm.com/state-farm-details-next-gen-good-neighbor/
retrieved: 2026-10-06
effective_or_revised: May 2026
names_ai_feature: yes (generic "AI-powered virtual assistant")
fetch_depth: full-fetch
files: mastersheet-sources/insurance/state-farm/statefarm_TYPE6_next-gen-good-neighbor_RAW.html (+ .txt)

## Coding-relevant extract

**Generic clauses that happen to fit the AI channel.** The Terms of Use contain an "Online Claims
Submissions" clause: reporting a claim online does not commit State Farm to coverage for the
loss, and all policy provisions stay in effect. A separate clause says site quotes are estimates
and not a contract, binder, or agreement to insure. Neither mentions AI, but if the pilot runs
through State Farm's online channels, these are the clauses that would govern a misstatement
during AI-assisted loss reporting. Coded B1-analog (generic). Also: site content, services and
calculators provided "as is", entire risk on the user (B6); no liability for any damages from use
of the site (B2).

## Coder note
1. **Locus 3 (generic clause reaching the AI channel), conditional.** It reaches the assistant only
   if the assistant sits inside statefarm.com or the app; if the pilot is phone-based, no terms
   were presented and assent is "none".
2. **Vintage:** terms undated; cannot compare to the May 2026 pilot.
3. **Say-do:** release frames the AI as speeding claims "from first notice of loss to payment" while
   stressing that claims professionals make coverage and payment decisions (human-in-the-loop as
   the stated safeguard, not a disclaimer).
4. **Gaps:** full privacy notice not reached (hub only, B11 unchecked); pilot channel and liveness
   unverified; no dedicated AI terms or in-product microcopy found (2 searches). Confirm pilot
   status before keeping State Farm in the main sample.

---

<a name="metlife"></a>
## MetLife - Intelligent Virtual Agent / AI-driven service - collected 2026-10-06

**AI feature.** MetLife's US customer-facing AI is mainly voice: an "Intelligent Virtual
Assistant" program on customer phone lines (natural-language self-service, opt out to a human),
plus AI used in call centers for authentication and intent confirmation. The screening evidence
also mentions a "digital virtual assistant / AI-driven chat", not separately located. Launch date
not stated. Roster: NAICS 5241, rank 7, main sample (logged "stop" under v1; included in v2).

company: MetLife, Inc.
document_title: Legal Notices (metlife.com website terms)
document_type: t2-site-terms
url: https://www.metlife.com/about-us/terms-and-conditions/
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no - zero AI-keyword hits
ai_vector: voice IVA (+ possible chat)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B4 (generic, but only for stock-price data), B2 (generic)
files: mastersheet-sources/insurance/metlife/metlife_legal-notices_RAW.html (+ .txt)

company: MetLife, Inc.
document_title: MetLife Online / MyBenefits Terms of Use (Legal Notices)
document_type: t1-governing-terms (benefits portal)
url: https://mybenefits.metlife.com/Mbpp/legalNotices.html
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: B2 (generic), B6 (generic)
files: mastersheet-sources/insurance/metlife/metlife_mybenefits-terms_RAW.html (+ .txt)

company: MetLife, Inc.
document_title: MetLife Privacy Statement (online)
document_type: privacy-notice
url: https://www.metlife.com/about-us/privacy-policy/online-privacy-policy/
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: yes - by category: lists interacting with "a live call center support agent or intelligent virtual agent and interactive voice response technologies" as a collection context; states MetLife may process information through AI, ML and generative AI tools, its own and third-party
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: personal information processed by AI/ML/genAI tools "to enhance" services and support), no B11 ADM section found
files: mastersheet-sources/insurance/metlife/metlife_online-privacy_RAW.html (+ .txt)

company: MetLife, Inc.
document_title: Making Financial Services Easier to Use and Understand (sustainability report chapter)
document_type: t6-marketing
url: https://www.metlife.com/global/impact/sustainability/report/for-our-customers/making-financial-services-easier-to-use-and-understand/
retrieved: 2026-10-06
effective_or_revised: 2026 report
names_ai_feature: category (AI in global call centers; auto-adjudication in claims)
fetch_depth: full-fetch
files: mastersheet-sources/insurance/metlife/metlife_TYPE6_sustainability-va_RAW.html (+ .txt)

## Coding-relevant extract

**Terms: AI-silent.** Neither the metlife.com Legal Notices nor the MyBenefits terms mention AI,
virtual agents or automated responses. Generic: site content "AS IS" (B6); damages exclusion (B2);
the only anti-reliance language is about stock-price data (B4, not reaching the IVA).

**Privacy statement is the only document that names the AI.** It lists the "intelligent virtual
agent" alongside IVR as a source of collected information and says MetLife may process personal
information with AI, ML and generative AI tools (its own and third parties') to improve products,
support and technology (B10, AI-specific). No automated-decision-making disclosure.

## Coder note
1. **Locus 5 (operational only) for the voice IVA.** The AI is on the phone, where no terms are
   presented. Assent: none. The privacy statement is notice, not contract.
2. **Vintage:** no dates in any captured document.
3. **Say-do:** report describes AI as a "force multiplier" for personalized experiences and
   reports increased self-service and fewer transfers; nothing disclaims IVA answers.
4. **Gaps:** the chat assistant named in screening was not located; IVA launch date unknown;
   no in-call disclosure script captured (would need a test call). Low incremental yield
   expected from further web searching.

---

<a name="bjs"></a>
## BJ's Wholesale Club - Ask Bev and virtual customer-service agents - collected 2026-10-06

**AI feature.** Generative "virtual agent chatbots" on BJs.com (member care: late orders, returns,
membership questions, handoff to a live agent), branded **Ask Bev** and described as an AI shopping
assistant in beta from Q1 2026 (CEO on the earnings call: "more personalized, intuitive, and
efficient product discovery and support"). Vendor per vendor case study: delight.ai. AI review
summaries also named in the terms. A voice-based virtual assistant for older members was reported
earlier (trade press). Roster: NAICS 4552, rank 7, main sample.

company: BJ's Wholesale Club Holdings, Inc.
document_title: Terms of Use (s.21 "Use of Artificial Intelligence (AI)")
document_type: t1-governing-terms (website + stores)
url: https://www.bjs.com/info/terms-of-use/
retrieved: 2026-10-06
effective_or_revised: "Terms of Use as of 9/19/2025" (stated)
names_ai_feature: by CATEGORY ("generative AI tools (e.g., virtual agent chatbots, review summaries)"); "Bev" not named
ai_vector: generative (chat) + generative content (review summaries)
fetch_depth: full-fetch (read in full in browser) - preservation: CAPTURE-NOTE with verbatim AI passages + innerText SHA-256; no raw HTML (HTTP 403 to scripts)
clause_codes_present: B6 (AI-specific, s.21 and s.5), B4 (AI-specific: user "assume[s] sole responsibility for verifying"), B3 (AI-specific, via sole-responsibility wording), B10 (AI-specific: inputs may be used by BJ's and the AI tools), B1 (generic: may cancel even accepted orders where price or other information is inaccurate), B2 (generic, s.23)
vendor: delight.ai (per vendor case study; not named in terms)
files: mastersheet-sources/retail/bjs/bjs_terms-of-use_CAPTURE-NOTE.md

## Coding-relevant extract

**s.21, a dedicated AI section.** BJ's Stores and Website may offer generative AI tools such as
virtual agent chatbots and review summaries; they are provided "as is, as available" with no
warranties; they are for general information and convenience; BJ's does not warrant that their
output is accurate, complete, reliable, current or error-free (B6); the user assumes sole
responsibility for verifying output (B4/B3); information given to the tools may be used by BJ's
and by the tools (B10).

**s.5, AI written into the errors clause.** The general misprints-and-errors disclaimer lists
"the output of any artificial intelligence tools" alongside product photos and descriptions as
Materials not warranted to be accurate.

**B1 (generic, but linked).** BJ's may cancel or decline to process orders, including accepted
ones, where the price or other information on the Website or in Stores is inaccurate. Read with
s.5, which makes AI output part of the site's Materials, this is a non-honoring clause that
reaches a wrong price or promise stated by Ask Bev, though the cancellation clause itself does not
mention AI.

## Coder note
1. **Locus 2 (dedicated AI section inside general terms)**, the same tier as Marriott.
2. **Vintage:** s.21 is dated 9/19/2025, before Ask Bev's Q1 2026 beta but after earlier virtual
   agents existed; the clause names the category, so it reaches Bev without amendment.
3. **Assent:** browsewrap/use of the website; the chat is on BJs.com.
4. **Gaps:** privacy policy not captured (403; B11 unchecked); Ask Bev in-chat microcopy not
   captured (needs a member session); first-party announcement of Bev not fetched (earnings call
   quote via trade press only).

---

<a name="ebay"></a>
## eBay - AI shopping agent - collected 2026-10-06

**AI feature.** An agentic AI shopping assistant announced 2025-05-06 ("eBay Uses Agentic AI to
Supercharge Personalized Ecommerce"), first to a small subset of US users and expanding on a
rolling basis; also AI review summaries, AI listing tools for sellers, and real-time AI answers
in customer-service chat. eBay is a marketplace, so the AI recommends third-party sellers' items.
Roster: NAICS 4552, rank 9, main sample.

company: eBay Inc.
document_title: User Agreement
document_type: t1-governing-terms
url: https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259
retrieved: 2026-10-06
effective_or_revised: effective June 28, 2026 for existing users (stated); previous amendment effective February 20, 2026
names_ai_feature: by category ("artificial intelligence or AI-powered tools and products"); shopping agent not named
ai_vector: generative + agentic (shopping agent); generative content (summaries, seller listing tools)
fetch_depth: full-fetch (captured text contains the agreement twice, likely current plus a version toggle; both copies identical in the AI passages)
clause_codes_present: B6 (AI-specific, one clause), B5 (AI-specific, restrictive: user buy-for-me agents/LLM bots banned), B3 (AI-specific, sellers own AI-generated listing content), B8 (generic: eBay not party to sales; no guarantee of items or listings), B2/B7 (generic, s.16 and s.18)
vendor: none named
files: mastersheet-sources/retail/ebay/ebay_user-agreement_RAW.html (+ .txt)

company: eBay Inc.
document_title: User Privacy Notice (s.12 "eBay and AI"; s.5.8 Automated decision-making)
document_type: privacy-notice
url: https://www.ebay.com/help/policies/member-behaviour-policies/user-privacy-notice-privacy-policy?id=4260
retrieved: 2026-10-06
effective_or_revised: effective April 21, 2025 (stated)
names_ai_feature: by category ("AI assistants", real-time answers in chat, AI review summaries)
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: user personal data used to train own and third-party models where permitted), B11 (ADM section; says no significant automated decisions except where necessary for a contract or permitted by law)
files: mastersheet-sources/retail/ebay/ebay_privacy-notice_RAW.html (+ .txt)

company: eBay Inc.
document_title: eBay Uses Agentic AI to Supercharge Personalized Ecommerce
document_type: t6-marketing
url: https://innovation.ebayinc.com/stories/ebay-uses-agentic-ai-to-supercharge-personalized-ecommerce/
retrieved: 2026-10-06
effective_or_revised: May 6, 2025
names_ai_feature: yes (AI shopping agent)
fetch_depth: full-fetch
files: mastersheet-sources/retail/ebay/ebay_TYPE6_agentic-ai-story_RAW.html (+ .txt)

## Coding-relevant extract

**s.2, one AI sentence.** After saying eBay's pricing, shipping, listing and sourcing guidance is
"solely informational", the agreement says eBay may use AI-powered tools for services,
personalization, customer service and fraud detection, and that "availability and accuracy of
these tools are not guaranteed" (B6, AI-specific). It sits next to the marketplace carve-out:
eBay does not guarantee items, listings, or that a transaction will complete (B8, generic).

**B5, restrictive.** The prohibited-conduct list now bars accessing the Services with automated
means "including, without limitation buy-for-me agents, LLM-driven bots, or any end-to-end flow
that attempts to place orders without human review", unless eBay permits it. As with Anthem, the
AI-agent language targets the customer's agents, while eBay's own shopping agent gets one
accuracy sentence.

**B3 (sellers).** Sellers assume full responsibility for listing content, expressly including
content created with eBay's generative AI tools.

**Privacy notice s.12.** Lists AI assistants, AI chat answers and review summaries among uses;
promises to tell users when an AI system interacts with them directly; uses personal data to
train its own and third-party models where permitted (B10). s.5.8 ADM disclosure (B11).

## Coder note
1. **Locus 3 bordering 2.** No dedicated AI section in the User Agreement; a single AI-specific
   sentence inside the general "About eBay" clause. Code generic-plus-one-AI-sentence.
2. **Vintage:** User Agreement amended Feb 2026 and June 2026, both after the May 2025 agent
   launch. Both amendments touched AI (the agent ban) but added no disclaimer for eBay's own agent
   beyond the accuracy sentence. A strong "recently revised, own-AI-thin" finding.
3. **Marketplace structure** makes B8 the main liability shield: wrong agent recommendations are
   about third-party listings eBay disclaims anyway.
4. **Gaps:** shopping-agent in-product microcopy not captured; Mobile Application Terms of Use
   (incorporated) not fetched.

---

<a name="carmax"></a>
## CarMax - Skye virtual assistant and Sierra AI voice agent - collected 2026-10-06

**AI feature.** (1) Skye, CarMax's 24/7 virtual assistant on CarMax.com (in use since about
2020; generative per screening). (2) Sierra AI voice agents on inbound sales calls, deployed
May 2026; the release says they give "conversational and knowledgeable guidance" through
car-shopping decisions. CarMax also has a ChatGPT app (third-party channel, out of scope).
Roster: NAICS 4411, rank 4, main sample.

company: CarMax, Inc.
document_title: Terms of Use (s.4 "Account Creation; User Material Guidelines; Artificial Intelligence")
document_type: t1-governing-terms
url: https://www.carmax.com/terms
retrieved: 2026-10-06
effective_or_revised: Last updated March 28, 2025 (stated)
names_ai_feature: by category ("AI Features", "AI-powered chatbots provided by CarMax or its third-party service providers"); Skye not named
ai_vector: generative (chat) + voice agent
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI section + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B6 (AI-specific), B4 (AI-specific, strong: Outputs "cannot be, relied on"), B3 (AI-specific: actions in reliance at your own risk; you assume all risks), B10 (AI-specific: Inputs and Outputs used to train and fine-tune), B9 (AI-specific: no passing AI output off as human; no training ML on site content), B1-weak (generic: incorrect prices and credit terms may appear; pricing may change without notice), B2 (generic)
vendor: "third-party service providers" (Sierra named only in the press release)
files: mastersheet-sources/auto-dealers/carmax/carmax_terms-of-use_CAPTURE-NOTE.md

company: CarMax, Inc.
document_title: CarMax Teams with Sierra to Enhance Inbound Sales Call Experience
document_type: t6-marketing
url: https://investors.carmax.com/news-and-events/news/news-details/2026/CarMax-Teams-with-Sierra-to-Enhance-Inbound-Sales-Call-Experience/default.aspx
retrieved: 2026-10-06
effective_or_revised: 2026 (deployed May 2026)
names_ai_feature: yes (Sierra agents; Skye)
fetch_depth: full-fetch
files: mastersheet-sources/auto-dealers/carmax/carmax_TYPE6_sierra-release_RAW.html (+ .txt)

## Coding-relevant extract

**s.4 "Artificial Intelligence."** Defines "AI Features" as AI tools, including AI-powered
chatbots from CarMax or its vendors. The user is solely responsible for Inputs. Outputs may be
inaccurate, unsafe, out of date or biased; even an Output that looks like a factual assertion may
be false; Outputs "cannot be, relied on" to be accurate (B6 + B4, among the strongest
anti-reliance wording in the corpus). Actions taken in reliance are at the user's own risk; the
user assumes all risks and must verify Outputs independently (B3). CarMax says it does not intend
to verify all Outputs. Inputs and Outputs are used to train and fine-tune AI Features (B10).

**s.6 accuracy clause (generic).** Expressly anticipates incorrect prices, vehicle features,
credit availability and credit terms, including "features that may estimate credit terms";
accuracy not guaranteed; reliance on listings at own risk. It does not refuse to honor a
transaction (so B1-weak, not B1), but it covers exactly what a car-sales chatbot is likely to
misstate.

## Coder note
1. **Locus 2 (dedicated AI subsection inside general terms).**
2. **Assent splits by channel.** Skye on CarMax.com: browsewrap (use = acceptance). Sierra voice
   agent on phone: no terms presented, so the s.4 regime does not obviously reach a caller who
   never used the website. A clean within-firm contrast for the assent variable.
3. **Vintage:** s.4 dated March 2025, after Skye's launch and before the May 2026 voice agent; the
   "AI Features" definition reaches the voice agent only if it is part of the "Services".
4. **Gaps:** privacy policy not captured (403; B10/B11 detail unchecked); Skye in-chat microcopy
   not captured.

---

<a name="carvana"></a>
## Carvana - Shaqbot - collected 2026-10-06

**AI feature.** Shaqbot, an AI customer assistant with Shaquille O'Neal's voice and persona,
launched 2025-09-15 with a brand campaign; reachable via the Shaqvana microsite
(shaqvana.com, which redirects to carvana.com/shaqvana). Text and text-to-speech. Carvana also
runs a general website chatbot. Roster: NAICS 4411, rank 5, main sample.

company: Carvana Co.
document_title: Terms of Use (User Agreement)
document_type: t1-governing-terms
url: https://www.carvana.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Effective Date October 17, 2025 (stated)
names_ai_feature: by category ("artificial intelligence and machine learning", "a chatbot"); Shaqbot not named
ai_vector: generative (chat + voice persona)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific: Output may be inaccurate), B4 (AI-specific, soft: evaluate accuracy "as appropriate"), B10 (AI-specific: User Content and Output used to improve services), B8 (generic: no duty to flag discrepancies in third-party vehicle listings), B2/B7 (generic)
vendor: none named
files: mastersheet-sources/auto-dealers/carvana/carvana_terms-of-use_RAW.html (+ .txt)

company: Carvana Co.
document_title: Shaqvana microsite (carvana.com/shaqvana)
document_type: t6-marketing (landing copy; in-chat microcopy not reached)
url: https://www.shaqvana.com (redirects to https://www.carvana.com/shaqvana)
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: yes (Shaqbot)
fetch_depth: full-fetch of the static shell (443 chars; JS-rendered) + browser read of rendered landing text
files: mastersheet-sources/auto-dealers/carvana/shaqvana_microsite_RAW.html (+ .txt)

company: Carvana Co.
document_title: Carvana's Newest Teammate, Shaquille O'Neal ... Launch World's First AI "Shaqbot"
document_type: t6-marketing
url: https://www.carvana.com/press/carvanas-newest-teammate-shaquille-oneal-to-star-in-digitally-led-campaign-and-launch-worlds-first-ai-shaqbot/
retrieved: 2026-10-06
effective_or_revised: 2025-09-15
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/auto-dealers/carvana/carvana_TYPE6_shaqbot-release_RAW.html (+ .txt)

## Coding-relevant extract

**AI paragraph (item 11 of the use section).** The Services may use AI and machine learning;
because of its probabilistic nature, use may "result in Output that is inaccurate", and the user
should evaluate Output accuracy "as appropriate" (B6 + soft B4). No AS-IS wording specific to AI,
no sole-responsibility shift, no B1.

**Chatbot clause.** The site offers a chatbot; using it means consenting to recording and
retention of transcripts; it may not be monitored in real time. Chatbot use is governed by the
User Agreement, the Privacy Notice "and any other specific disclaimers associated with the
chatbot, which are incorporated here by reference". That is an express incorporation of
in-product microcopy into the contract, unusual and worth noting for the binding-status variable.
User Content and Output may be used to provide and improve services (B10); Output may not be
unique across users.

## Coder note
1. **Locus 2-lite (short AI paragraph inside general terms).** Effective 2025-10-17, one month
   after the Shaqbot launch, so plausibly revised for it; prior version not compared.
2. **Say-do.** The microsite tells users "Got a question? Shaq's A.I. twin has the answer."; the
   terms say Output may be inaccurate. A clean say-do pair.
3. **Incorporated microcopy:** whatever disclaimer Shaqbot shows in-chat is contractually
   incorporated. It was not captured (chat launcher not reachable without interaction).
4. **Gaps:** Shaqbot in-chat disclaimer; privacy notice not fetched (B11 unchecked); no
   transaction-error clause found by keyword search.

---

<a name="albertsons"></a>
## Albertsons Companies - Albertsons AI shopping assistant (Safeway AI, Vons AI, ...) - collected 2026-10-06

**AI feature.** An agentic conversational shopping assistant launched 2025-12-03 on every
banner website (Albertsons AI, Safeway AI, Vons AI, Jewel-Osco AI, ...). It digitizes recipes and
handwritten lists, builds carts "from recipe to cart", and holds "intelligent two-way
conversations"; it follows an earlier "Ask AI" tool from 2025. Powered by OpenAI models per
trade press. Requires sign-in. Roster: NAICS 4451, rank 2, main sample.

company: Albertsons Companies, Inc.
document_title: Terms of Use (Albertsons Companies, all banners)
document_type: t1-governing-terms (applies to all Company websites, online ordering and apps across all banners)
url: https://www.albertsonscompanies.com/policies-and-disclosures/terms-of-use/default.aspx
retrieved: 2026-10-06
effective_or_revised: Last Updated May 14, 2025 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative + agentic (cart building)
fetch_depth: full-fetch
clause_codes_present: B1 (generic, strong: may change prices, offers and descriptions "even after your receipt of an order confirmation", no further obligation), B6 (generic: Sites and Content may contain errors, no responsibility), B2/B7 (generic)
vendor: none named (OpenAI per press)
files: mastersheet-sources/grocery/albertsons/albertsons_corporate-terms_RAW.html (+ .txt). The Safeway footer links "special-terms-of-use" and "mobile-app-terms-of-use" resolve to this same document (identical SHA-256 0E779B0B5B8E...; saved as safeway_special-terms and safeway_mobile-app-terms)

company: Albertsons Companies (Safeway banner)
document_title: Terms of Use | Safeway (legacy page)
document_type: t2-site-terms (legacy banner page)
url: https://www.safeway.com/terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: Last updated March 12, 2015 (stated)
names_ai_feature: no (only the "Safeway AI" navigation link in page chrome)
fetch_depth: full-fetch
clause_codes_present: generic only
files: mastersheet-sources/grocery/albertsons/safeway_terms-of-use_RAW.html (+ .txt)

company: Albertsons Companies, Inc.
document_title: Albertsons Companies Accelerates Digital Transformation with the Albertsons AI Shopping Assistant
document_type: t6-marketing
url: https://www.albertsonscompanies.com/newsroom/press-releases/news-details/2025/Albertsons-Companies-Accelerates-Digital-Transformation-with-the-Albertsons-AI-Shopping-Assistant-Redefining-the-Grocery-Shopping-Experience/default.aspx
retrieved: 2026-10-06
effective_or_revised: 2025-12-03
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/grocery/albertsons/albertsons_TYPE6_ai-assistant-release_RAW.html (+ .txt)

## Coding-relevant extract

**Governing terms are AI-silent.** The group Terms of Use cover all banner sites and apps and so
reach the assistant generically, with no mention of AI, assistants, or generated content.

**s.32, a strong generic B1.** Sites and Content may contain errors and may be inaccurate or
out of date, and the Company takes no responsibility (B6). The Company may delete or change
prices, offers, discounts and product descriptions "with no further obligation to you, even after
your receipt of an order confirmation". For an assistant that builds carts and quotes prices, this
is the anti-*Moffatt* clause in substance, though written for typos.

**Legacy page.** safeway.com/terms-of-use.html still shows a 2015 document, while its own footer
links point to the 2025 group terms. Coded as a legacy site page, not the governing document.

## Coder note
1. **Locus 3 (generic clause reaching a named AI feature).** The AI is agentic, but nothing AI-
   or agent-specific exists in the terms.
2. **Vintage:** group terms May 2025, after "Ask AI" (early 2025) and before the Dec 2025
   agentic launch; not revised for it.
3. **Say-do:** "intelligent two-way conversations", shopping in "as little as four minutes",
   "recipe to cart"; terms have no AI acknowledgement at all.
4. **Gaps:** in-product microcopy behind login (safeway.com/assistant redirects to SSO); privacy
   policy not fetched (B10/B11 unchecked).

---

<a name="publix"></a>
## Publix Super Markets - FAQ bot - collected 2026-10-06

**AI feature.** A free-text "FAQ bot" on publix.com/contact that answers short customer questions
(up to 256 characters) from a set of common FAQs. Whether it is generative or retrieval-based is
not stated; it passed the screen as a free-text bot (not menu-driven). Launch date not stated.
Low-stakes, informational. Roster: NAICS 4451, rank 3, main sample.

company: Publix Super Markets, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.publix.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last updated 6/30/2025 (stated)
names_ai_feature: no - zero AI hits; prohibits users accessing Services by "electronic agent or 'bot'"
ai_vector: chat (FAQ retrieval; generative status unknown)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS, sole risk), B2 (generic, s.14), B5-restrictive-generic (no electronic agents or bots)
files: mastersheet-sources/grocery/publix/publix_terms-of-use_RAW.html (+ .txt)

company: Publix Super Markets, Inc.
document_title: Contact us page (FAQ bot chat box microcopy)
document_type: t4-in-product-microcopy
url: https://www.publix.com/contact
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: yes (calls it "our FAQ bot"; no AI wording)
fetch_depth: full-fetch
clause_codes_present: B4-soft (capability limit: bot "will try to help" and has answers to some common questions only), notice-of-terms at point of use ("Terms of Use and Privacy Policy apply"), storage notice
files: mastersheet-sources/grocery/publix/publix_contact-page_RAW.html (+ .txt)

## Coding-relevant extract

**Terms: AI-silent.** The June 2025 Terms of Use have no AI or bot-output language. Generic: the
Services and all information "AS IS", "AS AVAILABLE", use at sole risk (B6); standard damages
limits (B2). The only "bot" reference bans users' bots and electronic agents.

**Microcopy at the chat box.** Paraphrased: type a short question and the FAQ bot will try to help;
it only knows some common questions and handles up to 256 characters; by using the chat you agree
it will be stored by Publix and its service providers; Terms of Use and Privacy Policy apply.
This is an expectation-lowering capability statement, not an accuracy disclaimer, plus a
point-of-use notice linking the terms (closer to sign-in-wrap than pure browsewrap).

## Coder note
1. **Locus 4 (microcopy-only), weak form.** No accuracy or no-reliance statement anywhere; the
   microcopy limits scope rather than disclaiming output.
2. **Assent:** notice of terms shown at the chat itself; stronger than most firms' browsewrap.
3. **Generative status unknown.** If the bot is retrieval-only FAQ matching, it is at the edge of
   the consumer-AI definition; flag for the screening reviewer.
4. **Gaps:** privacy policy not captured (/privacy-policy 404; the footer points to
   /consumer-privacy, not fetched); bot vendor unknown.

---

<a name="wegmans"></a>
## Wegmans Food Markets - AI shopping assistant / AI-enabled chatbots - collected 2026-10-06

**AI feature.** An AI shopping assistant in beta (Cooklist-powered per screening; live by May
2026) and AI-enabled chatbots on wegmans.com that help build shopping lists, find recipes and
answer product and service questions using third-party AI tools. Roster: NAICS 4451, rank 5,
main sample (private).

company: Wegmans Food Markets, Inc.
document_title: Terms of Use (wegmans.com/terms)
document_type: t1-governing-terms
url: https://www.wegmans.com/terms
retrieved: 2026-10-06
effective_or_revised: Last updated on October 5, 2025 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (chat, list and recipe help)
fetch_depth: full-fetch
clause_codes_present: B1 (generic: may refuse or cancel an Order for any reason, including errors in product or pricing information; pricing errors may occur), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/grocery/wegmans/wegmans_terms_RAW.html (+ .txt)

company: Wegmans Food Markets, Inc.
document_title: Privacy Policy ("Use of Chatbots and Other Artificial Intelligence Features")
document_type: privacy-notice
url: https://www.wegmans.com/privacypolicy
retrieved: 2026-10-06
effective_or_revised: updated as of October 29, 2025 (stated)
names_ai_feature: by category ("chatbots", "AI-enabled", "third-party AI tools")
fetch_depth: full-fetch
clause_codes_present: B10-adjacent (AI-specific: chatbot inputs processed by third-party AI tools; data used only for the stated purpose), advisory not-to-share-sensitive-information notice; no B11
files: mastersheet-sources/grocery/wegmans/wegmans_privacy-policy_RAW.html (+ .txt)

## Coding-relevant extract

**Terms: AI-silent, generic B1.** The October 2025 Terms of Use never mention AI or chatbots.
Generic clauses: pricing or availability errors may occur; Wegmans may refuse or cancel an Order
for any reason, including errors in product or pricing information (B1, generic); AS IS (B6);
damages limits (B2).

**Privacy policy has the only AI language.** A dedicated subsection says wegmans.com may use
chatbots, which "may be AI-enabled" and use third-party AI tools to understand inputs and
generate responses (shopping lists, recipes, product questions). Chat data is used only for the
stated purpose; users are advised not to submit sensitive information and to contact Customer
Care for detailed questions. No accuracy disclaimer, no reliance language.

## Coder note
1. **Locus 3 for liability (generic B1 reaching the AI's order flow); AI acknowledged only in
   privacy notice.** The privacy section is a disclosure, not a disclaimer.
2. **Vintage:** terms (Oct 5, 2025) and privacy (Oct 29, 2025) were revised weeks apart; only the
   privacy policy gained AI language. Same pattern as several pilot-corpus firms.
3. **Gaps:** assistant launch date and in-product microcopy not captured; Cooklist (vendor) terms
   deliberately not used (B2B).

---

<a name="gianteagle"></a>
## Giant Eagle - AI Recipe Generator (app) - collected 2026-10-06

**AI feature.** An AI Recipe Generator in the Giant Eagle app: users prompt it in free text
(e.g. a spicy, low-calorie shrimp dish using pantry items), save the recipe and add the
ingredients to their cart. It came out of an internal hackathon and was reported live in 2025
(Grocery Dive). Low-stakes advisory output with a cart-adding action. Roster: NAICS 4451, rank 7,
main sample (private).

company: Giant Eagle, Inc.
document_title: Terms of Use
document_type: t1-governing-terms (Sites and apps)
url: https://www.gianteagle.com/about-us/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated on August 26th, 2024 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (recipe generation) with add-to-cart
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (scripted fetch returns an empty JS shell)
clause_codes_present: B1-weak (generic: may change prices and offers at any time without notice or liability; no guarantee of availability), B6/B2 (generic)
files: mastersheet-sources/grocery/giant-eagle/gianteagle_terms-of-use_CAPTURE-NOTE.md

## Coding-relevant extract

The Terms of Use contain nothing about AI, generated recipes, or nutrition or allergen accuracy
of generated content. Generic clauses only: Giant Eagle may change goods, prices and offers at any
time without notice or liability and cannot guarantee availability (B1-weak); standard warranty
and damages disclaimers.

## Coder note
1. **Locus 5 (absent; generic clauses only).** For a recipe generator the obvious risk is
   allergen or dietary error; no document addresses it.
2. **Vintage:** terms (Aug 2024) predate the 2025 feature; not revised for it.
3. **Gaps:** no first-party announcement found (1 search); in-app microcopy not captured (app
   only); privacy notice not fetched.

---

<a name="mcdonalds"></a>
## McDonald's - "Archy" AI drive-thru voice ordering (ArchIQ, Google) - collected 2026-10-06

**AI feature.** Archy, a voice ordering assistant in the drive-thru, part of the ArchIQ operating
system built with Google. Pilot at five undisclosed US restaurants, reported 2026-06-05 (press);
English and Spanish; McDonald's reports more than one million transactions, about 90% completed
without human intervention. This is McDonald's second attempt: the IBM drive-thru test
(100+ restaurants) ended in 2024 after viral wrong-order incidents. Roster: NAICS 7225, rank 2,
main sample. **Cutoff flag:** the pilot was announced in early June 2026; confirm it was live to
customers by 2026-06-30.

company: McDonald's Corporation (McDonald's USA)
document_title: Terms & Conditions (online services)
document_type: t1-governing-terms (website and app only)
url: https://www.mcdonalds.com/us/en-us/terms-and-conditions.html
retrieved: 2026-10-06
effective_or_revised: Effective August 24, 2026 (stated) - after the cutoff and after the pilot announcement
names_ai_feature: no - zero AI-keyword hits
ai_vector: voice (drive-thru ordering)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B6 (generic: online services may include inaccuracies or errors; AS IS), B3 (generic: user assumes total responsibility for use of online services), B2 (generic). None reaches the drive-thru.
files: mastersheet-sources/restaurants/mcdonalds/mcdonalds_terms-and-conditions_CAPTURE-NOTE.md

## Coding-relevant extract

The Terms govern McDonald's "online services" (website and app). They concede the online services
may include inaccuracies or errors, disclaim warranties, and put total responsibility on the
user, but say nothing about AI and nothing about orders placed by voice at the drive-thru.

## Coder note
1. **Locus 5 (no consumer terms; operational control only).** The drive-thru customer sees no
   terms. Any error control is operational (order-confirmation screen, crew override), as with
   Wendy's in the pilot corpus.
2. **Assent: none** for the AI interaction.
3. **Vintage:** the Terms were revised on 2026-08-24, after the Archy pilot was announced, and
   still contain no AI language. That supports reading the silence as a choice, though the
   online terms would not reach the drive-thru in any case.
4. **Incident history (t6-incident, not separately captured):** the 2024 IBM test ended after
   widely reported erroneous orders (unwanted items added). A documented customer-facing AI
   error pattern for this firm.
5. **Gaps:** privacy statement not captured (403); no first-party Archy announcement fetched
   (press only); pilot liveness by cutoff to confirm.

---

<a name="chipotle"></a>
## Chipotle Mexican Grill - Pepper concierge chatbot and AI voice phone ordering - collected 2026-10-06

**AI feature.** (1) Pepper, an ordering and support "concierge bot" (launched on Facebook
Messenger in 2020, now also the support chat on Chipotle's website per 2026 coverage), built on
IPSoft/Amelia conversational AI. Customers describe orders in natural language. (2) AI voice
assistant for phone orders, piloted 2018 and rolled out to all restaurants in 2019. Roster:
NAICS 7225, rank 5, main sample. The Messenger channel is third-party and out of scope; the
website chat and phone ordering are Chipotle's own channels.

company: Chipotle Mexican Grill, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.chipotle.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated August 13, 2025 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: chat (ordering/support) + voice (phone ordering)
fetch_depth: full-fetch
clause_codes_present: B6 (generic: Services "as is, as available"), B2 (generic)
vendor: none named in terms (IPSoft/Amelia per press)
files: mastersheet-sources/restaurants/chipotle/chipotle_terms-of-use_RAW.html (+ .txt)

company: Chipotle (third-party coverage)
document_title: Should You Hijack a Corporate AI Chatbot for Free Tokens? (Gizmodo)
document_type: t6-incident
url: https://gizmodo.com/should-you-hijack-a-corporate-ai-chatbot-for-free-tokens-2000767595
retrieved: 2026-10-06
effective_or_revised: published June 4, 2026
names_ai_feature: yes (Pepper)
fetch_depth: full-fetch
files: mastersheet-sources/restaurants/chipotle/chipotle_TYPE6_incident-gizmodo_RAW.html (+ .txt)

## Coding-relevant extract

**Terms: AI-silent.** Nothing on chatbots, automated ordering, or AI output. Generic AS-IS and
damages limits only. No transaction-error clause found by keyword search.

**Incident (2026).** From March 2026, developers found Pepper would answer coding questions and
write Python; one reverse-engineered its backend to use it as a free LLM endpoint, and another
wrapped it into a branded coding assistant. Not a consumer-harm incident, but a documented case
of a customer-facing bot operating far outside its intended scope, which is the situation B9
(anti-jailbreak / misuse) clauses address. Chipotle's terms have no such clause.

## Coder note
1. **Locus 5 (absent).** For web chat: browsewrap terms with no AI language. For phone ordering:
   no terms presented at all (assent: none).
2. **Vintage:** terms updated Aug 2025, years after both AI channels launched; still silent.
3. **Say-do:** marketing has framed Pepper as letting customers order in natural language "as
   they would in-store"; nothing disclaims order errors.
4. **Gaps:** privacy policy not fetched; Pepper web-chat microcopy not captured; phone-ordering
   vendor and script not captured.

---

<a name="yum"></a>
## Yum! Brands (Taco Bell) - Voice AI drive-thru (Byte by Yum!) - collected 2026-10-06

**AI feature.** Voice AI taking drive-thru orders at Taco Bell: over 100 US drive-thrus in 13
states at the 2024 announcement, targeting hundreds by end of 2024, with plans for all Yum brands
globally. The release claims it improves "order accuracy". Roster: NAICS 7225, rank 6, main
sample (the firm is Yum! Brands; Taco Bell is the deploying brand).

company: Yum! Brands, Inc. (Taco Bell Corp.)
document_title: Taco Bell Terms of Use
document_type: t1-governing-terms (Platform: app and tacobell.com, plus loyalty program terms)
url: https://www.tacobell.com/legal/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last updated April 18, 2024 (stated)
names_ai_feature: no - zero AI hits
ai_vector: voice (drive-thru ordering)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (JS-rendered page)
clause_codes_present: B6 (generic: AS IS, WITH ALL FAULTS), B2 (generic); order-finality clause (app/web orders)
files: mastersheet-sources/restaurants/yum/tacobell_terms-of-use_CAPTURE-NOTE.md

company: Yum! Brands, Inc.
document_title: Yum! Brands to Expand Voice AI Technology to Hundreds of Taco Bell U.S. Drive-Thru Locations in 2024 ...
document_type: t6-marketing
url: https://investors.yum.com/news-events/financial-releases/news-details/2024/Yum-Brands-to-Expand-Voice-AI-Technology-to-Hundreds-of-Taco-Bell-U.S.-Drive-Thru-Locations-in-2024-with-a-Future-Vision-to-Bring-the-Technology-to-Its-Brands-Drive-Thrus-Around-the-World/
retrieved: 2026-10-06
effective_or_revised: 2024 (stated in URL path)
names_ai_feature: yes (Voice AI)
fetch_depth: full-fetch
files: mastersheet-sources/restaurants/yum/yum_TYPE6_voice-ai-release_RAW.html (+ .txt)

## Coding-relevant extract

The Taco Bell Terms of Use govern the app, website and loyalty program. They contain no AI
language. They do reach the drive-thru indirectly, through the loyalty program, and there they
assume a human: members must say their four-digit code to "the Taco Bell team member taking the
order". App and web orders are final once charged; drive-thru check-ins cannot be cancelled.

## Coder note
1. **Locus 5 (no consumer terms for the AI interaction).** The drive-thru customer sees no terms;
   assent: none. The only terms that touch the drive-thru describe a human order-taker, so the
   contract's picture of the interaction is out of date with the deployed system.
2. **Vintage:** terms April 2024, around the time of the 2024 voice-AI expansion; not revised in
   the 2.5 years since.
3. **Say-do:** release claims improved "order accuracy" and a "consistent, friendly experience";
   nothing addresses AI order errors.
4. **Gaps:** KFC and Pizza Hut voice-AI status not checked; Taco Bell privacy policy not captured
   (/legal/privacy 404); no in-lane disclosure captured (would need a site visit).

---

<a name="dominos"></a>
## Domino's Pizza - AI phone ordering agent / "Dom" voice ordering - collected 2026-10-06

**AI feature.** AI voice agents take phone orders at US stores (vendor ConverseNow per screening
evidence; trade press reports AI handles a large share of North American phone orders). Domino's
earlier "Dom" voice ordering assistant (2014 in-app; phone tests 2019) used Nuance. Phone channel.
Roster: NAICS 7225, rank 9, main sample.

company: Domino's Pizza, Inc. (Domino's Pizza LLC)
document_title: Terms of Use
document_type: t1-governing-terms (websites and apps)
url: https://www.dominos.com/content/terms-of-use
retrieved: 2026-10-06
effective_or_revised: updated as of March 06, 2017 (stated)
names_ai_feature: yes - by brand ("Dom", Voice Ordering in Mobile Apps), in a data-handling clause only
ai_vector: voice (phone and in-app ordering)
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: voice inputs recorded, sent to Nuance, retained to improve Dom), B6/B2 (generic)
vendor: Nuance Communications (named in terms, legacy in-app Dom); ConverseNow (phone AI, per screening; B2B, not used)
files: mastersheet-sources/restaurants/dominos/dominos_terms-of-use_RAW.html (+ .txt)

company: Domino's Pizza LLC
document_title: Privacy Policy
document_type: privacy-notice
url: https://www.dominos.com/content/privacy
retrieved: 2026-10-06
effective_or_revised: Effective Date August 2026 (stated)
names_ai_feature: no (covers orders "by phone"; voice data via voice skills)
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific, unusual: Domino's does not use personal data to train LLMs, but third parties it sells data to may train their own LLMs)
files: mastersheet-sources/restaurants/dominos/dominos_privacy_RAW.html (+ .txt)

## Coding-relevant extract

**Terms name the voice assistant but only for data.** A "Voice Ordering in Mobile Apps" clause
says using Dom is optional, that what you say is recorded and sent to Nuance to process the
request, and that voice data may be retained to improve Dom and other products (B10). Nothing on
accuracy, misheard orders, or who bears an ordering error. The Terms date from March 2017.

**Privacy policy (Aug 2026).** Covers information from orders placed "by phone". States Domino's
does not collect or use personal data to train large language models, but that third parties it
sells personal data to may use it to train their own. A rare explicit LLM-training disclosure,
aimed at data sale rather than at Domino's own AI.

## Coder note
1. **Locus 5 for the phone AI (no terms at the call; assent none).** The 2017 Dom clause names an
   AI by brand (rare in the corpus) but only for app voice ordering and only for data handling.
2. **Vintage:** a 2017 contract governing a channel now largely AI-operated; the Aug 2026 privacy
   revision added LLM language but not about phone ordering.
3. **Vendor rule:** ConverseNow's terms are B2B and not used (see CLAUDE.md hard rule).
4. **Gaps:** current phone-AI coverage and in-call disclosure not captured; the third-party
   wizcase article (screening evidence) timed out.

---

<a name="caseys"></a>
## Casey's General Stores - AI phone-ordering agents and "Darn-ell" chatbot - collected 2026-10-06

**AI feature.** (1) AI voice agents taking phone orders (pizza, food), deployed system-wide over
the past few years and in about 2,600 stores by April 2026 (vendor SoundHound/SYNQ3 per screening
evidence). (2) Darn-ell, a generative-AI "coffee roaster" chatbot on the campaign microsite
darngoodroast.com, launched 2025-03-06; it gave playful roasts and coffee recommendations and
handed out daily free-coffee redemption codes. The microsite no longer responds (likely retired
before the June 2026 cutoff). Roster: NAICS 4571, rank 5, main sample.

company: Casey's General Stores, Inc.
document_title: Website Terms and Conditions
document_type: t1-governing-terms (Sites and Services)
url: https://www.caseys.com/terms-and-conditions
retrieved: 2026-10-06
effective_or_revised: Last updated on March 1, 2026 (stated)
names_ai_feature: no - zero AI hits
ai_vector: voice (phone ordering); generative chat (campaign microsite)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B6 (generic AS IS), B2 (generic)
vendor: SoundHound/SYNQ3 (per screening; B2B, not used)
files: mastersheet-sources/gas-stations/caseys/caseys_terms-and-conditions_CAPTURE-NOTE.md

company: Casey's General Stores, Inc.
document_title: Darn-ell microsite (darngoodroast.com)
document_type: t4-in-product-microcopy
url: https://www.darngoodroast.com
retrieved: attempted 2026-10-06 (connection timed out)
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

The March 2026 Terms and Conditions contain no AI language. Generic AS-IS and damages clauses
cover the Sites and Services; phone orders are not obviously within them. The only "voice"
reference is TCPA consent to artificial or prerecorded voice in marketing texts and calls.

## Coder note
1. **Locus 5 (no consumer terms reach the AI).** Phone ordering: assent none. Darn-ell: governed,
   if at all, by microsite or sweepstakes rules that were not retrieved.
2. **Strong vintage finding:** terms revised 2026-03-01, after years of AI phone ordering and a
   year after Darn-ell, and still AI-silent.
3. **Darn-ell is transactional-adjacent:** it issued free-coffee codes, so a hallucinated or
   repeated code is a small-stakes honoring question. Its rules were not found.
4. **Gaps:** Darn-ell microsite and any official rules; privacy policy not captured; first-party
   release (investor site timed out; Business Wire copy exists).

---

<a name="ulta"></a>
## Ulta Beauty - Ulta AI (Gemini Enterprise for CX) - collected 2026-10-06

**AI feature.** Ulta AI, a generative chat shopping assistant on Ulta.com built with Google Gemini
Enterprise for Customer Experience, announced 2026-04-22, alongside "agentic commerce" in Google
AI Mode and the Gemini app (third-party surfaces, out of scope) and a ChatGPT experience
(third-party, out of scope). It recommends and compares products, explains ingredients, builds
routines and suggests gifts. Per Ulta's FAQ it cannot place orders or access accounts. Roster:
NAICS 4561, rank 2, main sample.

company: Ulta Beauty, Inc. (Ulta Salon, Cosmetics & Fragrance, Inc.)
document_title: Terms & Conditions
document_type: t1-governing-terms (Site plus "Third-Party Platform Experiences")
url: https://www.ulta.com/company/terms-and-conditions
retrieved: 2026-10-06
effective_or_revised: LAST UPDATED September 29th, 2026 (stated). NOTE: after the 2026-06-30 cutoff
names_ai_feature: yes - by brand ("Ulta(R) AI") and category ("AI-powered shopping assistants", "AI-generated recommendations")
ai_vector: generative (chat; recommendations)
fetch_depth: full-fetch
clause_codes_present: B1-analog (AI-specific: Ulta AI "not authorized to make any promises about Ulta Beauty or its products"), B6 (AI-specific: may provide untrue or inaccurate results; AS-IS), B4 (AI-specific: review and confirm validity), B2 (AI-specific: disclaims responsibility or liability for use of Ulta AI), not-professional-advice (AI-specific), B1 (generic: right to cancel orders containing errors), B8 (generic: relies on third-party manufacturer advice)
vendor: Google (Gemini Enterprise for CX), named in the release only
files: mastersheet-sources/health-personal-care/ulta/ulta_terms-and-conditions_RAW.html (+ .txt)

company: Ulta Beauty, Inc.
document_title: Ulta AI Chat (Guest Services page with FAQ)
document_type: t4-in-product-microcopy (help-center FAQ for the feature)
url: https://www.ulta.com/guestservices/ways-to-shop/ai-chat
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: yes (Ulta AI)
fetch_depth: full-fetch
clause_codes_present: B6, B4, B1-analog (same "not authorized to make any promises" wording), capability limits (cannot place orders, process returns or access accounts), not-professional-advice
files: mastersheet-sources/health-personal-care/ulta/ulta_ai-chat-page_RAW.html (+ .txt)

company: Ulta Beauty, Inc.
document_title: Privacy Policy (s.14 "AI Notice"; ADMT section)
document_type: privacy-notice
url: https://www.ulta.com/company/privacy
retrieved: 2026-10-06
effective_or_revised: LAST UPDATED September 30, 2026 (stated)
names_ai_feature: yes (Ulta(R) AI, third-party AI vendors)
fetch_depth: full-fetch
clause_codes_present: B11 (states no AI/ADMT used for profiling or significant decisions for consumers), B10-adjacent (third-party AI vendors may record and process chat data); employee AI notice (out of scope)
files: mastersheet-sources/health-personal-care/ulta/ulta_privacy_RAW.html (+ .txt)

company: Ulta Beauty, Inc.
document_title: Ulta Beauty and Google Introduce Gemini-Enabled Shopping Experiences ...
document_type: t6-marketing
url: https://www.ulta.com/investor/news-events/press-releases/detail/226/ulta-beauty-and-google-introduce-gemini-enabled-shopping
retrieved: 2026-10-06
effective_or_revised: April 22, 2026
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/health-personal-care/ulta/ulta_TYPE6_gemini-release_RAW.html (+ .txt)

## Coding-relevant extract

**Scope.** The T&C apply to the Site and to Ulta shopping experiences on third-party AI platforms
("Third-Party Platform Experiences"), so the firm extends its own contract into ChatGPT and Gemini
surfaces.

**The AI clause.** Paraphrased: Ulta AI and AI shopping experiences use generative AI that "may
provide untrue or inaccurate results" (B6); users should review and confirm (B4); Ulta AI and
AI shopping assistants "are not authorized to make any promises about Ulta Beauty or its
products" (B1-analog); use is AS-IS and Ulta disclaims responsibility or liability for it (B2/B6);
nothing generated is legal, professional, financial or medical advice. AI-generated
recommendations, comparisons and routines are folded into "Site Contents" for the all-caps
warranty disclaimer and are described as informational and for product discovery only.

**Why the authority clause matters.** *Moffatt* turned on the chatbot's statement being
attributed to the firm. Denying the AI any authority to make promises is the most direct
contractual answer to that reasoning in the v2 collection so far: it attacks attribution itself,
not just accuracy. It is repeated verbatim in the consumer-facing FAQ, so the same message reaches
the user at the point of use.

**Privacy s.14.** No AI/ADMT used for consumer profiling or significant decisions (B11, negative
disclosure); third-party AI vendors may record and process chat data.

## Coder note
1. **Locus 2 (AI language embedded in general terms), plus mirrored microcopy (locus 4).**
2. **Version problem (important).** T&C revised 2026-09-29 and privacy 2026-09-30, both after the
   cutoff and after Ulta AI's April 2026 launch. Whether the authority clause existed at
   2026-06-30 is unknown; the Internet Archive was unreachable from this machine on 2026-10-06.
   Retrieve the pre-cutoff version before coding this firm for the headline counts.
3. **Assent:** browsewrap on Ulta.com; the FAQ is a help page, not presented in the chat itself
   (in-chat text not captured).
4. **Say-do:** release and FAQ promise to help shoppers "shop with confidence" and "instantly
   recommend products"; terms deny any authority to promise.

---

<a name="bathbodyworks"></a>
## Bath & Body Works - Gingham Genius (generative fragrance finder) and AI chatbots - collected 2026-10-06

**AI feature.** Gingham Genius, an LLM-powered conversational fragrance finder in the app,
announced September 2024 and available to all customers by end of December 2024; plus
AI-facilitated customer-service chatbots run by service providers. Roster: NAICS 4561, rank 3,
main sample.

company: Bath & Body Works, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.bathandbodyworks.com/customer-care/terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: Last Updated January 31, 2025 (stated)
names_ai_feature: by category ("automated chatbots ... facilitated by artificial intelligence", "GenAI"); Gingham Genius not named
ai_vector: generative (chat; recommendations)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific: automated responses "could contain errors"), B4 (AI-specific, soft: read full product descriptions and reviews before purchasing), B10 (AI-specific: may develop, train and improve AI models, including third-party ones, with customer information), B1 (generic, strong: may revoke a stated price and correct errors "including after a purchase has been made", or cancel accepted orders), B2/B6 (generic)
vendor: unnamed "third-party service providers"
files: mastersheet-sources/health-personal-care/bath-body-works/bbw_terms-of-use_RAW.html (+ .txt)

company: Bath & Body Works (third-party coverage)
document_title: Bath & Body Works adds new features to mobile app (Yahoo Finance)
document_type: t6-marketing
url: https://finance.yahoo.com/news/bath-body-works-adds-features-111200530.html
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/health-personal-care/bath-body-works/bbw_TYPE6_gingham-genius-news_RAW.html (+ .txt)

## Coding-relevant extract

**s.5.D "Your Interactions with Us and Our Technologies (Including Artificial Intelligence)."**
Paraphrased: when you contact BBW you are also dealing with its service providers' technologies;
chatbots are run by providers that record and keep all chats; chatbot experiences are
facilitated by AI including GenAI; do not share confidential information; automated responses
"are informational only and could contain errors" (B6); read full product descriptions and
reviews before buying (soft B4); BBW may develop, train and improve AI tools and models,
including third-party ones, with customer information, e.g. to make product recommendations
through its chatbots (B10).

**Generic B1 (strong).** For pricing or specification errors, BBW may revoke any stated price and
correct the error "including after a purchase has been made", or refuse or cancel any order,
including accepted orders, in its sole discretion; it may modify or cancel orders for any reason.

## Coder note
1. **Locus 2 (AI subsection inside general terms).** Category-level, not brand-level.
2. **Vintage:** revised 2025-01-31, about a month after Gingham Genius reached all customers;
   plausibly drafted for it.
3. **Accuracy language is soft** ("informational only", "could contain errors"); no sole-
   responsibility shift. The heavy lifting against a wrong AI recommendation is the generic B1.
4. **Gaps:** privacy policy not fetched; first-party Gingham Genius announcement not fetched
   (third-party coverage used); in-app microcopy not captured.

---

<a name="kinney"></a>
## Kinney Drugs - Burt (AI refill voice/text assistant) and Ask Burt (vaccine-eligibility chat) - collected 2026-10-06

**AI feature.** (1) **Burt**, a generative-AI voice and text assistant for prescription refills,
reminders and pharmacy notifications, launched May 2026 (built by Synerio; piloted with
McKesson Pharmacy Systems). It calls customers and takes refill instructions by voice; it is
agentic (it places refill orders). (2) **Ask Burt**, a web chat that checks vaccine eligibility
(NY and VT) and schedules appointments, terms effective 2025-09-29. Roster: NAICS 4561, rank 8,
main sample (employee-owned).

company: Kinney Drugs, Inc.
document_title: Pharmacy Voice Calls and Text Messaging Communications Terms (Burt)
document_type: t3-dedicated-ai-doc (standalone terms for an AI-powered assistant)
url: https://www.kinneydrugs.com/kxterms/
retrieved: 2026-10-06
effective_or_revised: Effective Date August 18, 2025; Edited May 12, 2026 (stated) - edited the month Burt launched
names_ai_feature: yes - by brand ("Burt, our artificial intelligence ('AI') powered assistant")
ai_vector: generative voice + text; agentic (refills)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific, s.4.3 and s.8.2), B4 (AI-specific: use discretion in acting on Output), B3 (AI-specific, s.4.5: user solely responsible for managing medications; Kinney accepts no added responsibility), B10 (AI-specific: Inputs used to train and improve Burt), B8 (AI-specific: Outputs may come from manufacturers, drug databases, vendors and third-party AI models, not independently verified), B2 (AI-specific limitation of liability), arbitration + class waiver
vendor: unnamed "service providers" and "third-party AI models" (Synerio per press)
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_pharmacy-terms_RAW.html (+ .txt)

company: Kinney Drugs, Inc.
document_title: Kinney Drugs Vaccine Eligibility Assistant Terms of Use (Ask Burt)
document_type: t3-dedicated-ai-doc
url: https://www.kinneydrugs.com/burt-terms/
retrieved: 2026-10-06
effective_or_revised: Effective Date September 29, 2025 (stated)
names_ai_feature: yes - by brand
ai_vector: generative (chat); scheduling
fetch_depth: full-fetch
clause_codes_present: B1-analog (AI-specific, s.8: "No guarantee of eligibility, access or coverage of cost"; Burt cannot confirm insurance coverage), B6, B4 (confirm important information with a pharmacist), B3 (user responsible for use of Outputs), B2 (AI-specific; total liability capped at US$100), not-medical-advice, arbitration with 1-year claim bar
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_ask-burt-terms_RAW.html (+ .txt)

company: Kinney Drugs, Inc.
document_title: Ask Burt chat page (point-of-use notice)
document_type: t4-in-product-microcopy
url: https://www.kinneydrugs.com/burt/
retrieved: 2026-10-06
names_ai_feature: yes ("Kinney's AI vaccine assistant")
fetch_depth: full-fetch
clause_codes_present: assent notice at point of use ("by chatting with me, you're agreeing to Kinney's AI Terms of Use"), data-use limitation
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_TYPE6_ask-burt-page_RAW.html (+ .txt)

company: Kinney Drugs, Inc.
document_title: Notice of Privacy Practices
document_type: privacy-notice
url: https://www.kinneydrugs.com/contact-us/kd-npp/
retrieved: 2026-10-06
effective_or_revised: effective as of May 19, 2026 (stated) - one week after the Burt terms edit
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: PHI may be used in AI tools and models for treatment and to "run and improve our operations")
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_npp_RAW.html (+ .txt)

company: Kinney Drugs (third-party reporting)
document_title: A pharmacy chain in Vermont implemented AI for efficiency. It's led to delays, incorrect information and privacy concerns. (VTDigger)
document_type: t6-incident
url: https://vtdigger.org/2026/07/29/a-pharmacy-chain-in-vermont-implemented-ai-for-efficiency-its-led-to-delays-incorrect-information-and-privacy-concerns/
retrieved: 2026-10-06
effective_or_revised: July 29, 2026
fetch_depth: full-fetch
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_TYPE6_incident-vtdigger_RAW.html (+ .txt)

company: Kinney Drugs, Inc.
document_title: Terms & Conditions hub page
document_type: legal-hub-index
url: https://www.kinneydrugs.com/terms/
retrieved: 2026-10-06
fetch_depth: full-fetch (index page listing both Burt documents)
files: mastersheet-sources/health-personal-care/kinney-drugs/kinney_site-terms_RAW.html (+ .txt)

## Coding-relevant extract

**Assent by phone number.** The Burt terms open by saying that providing a phone number is
consent to automated AI calls and texts from Burt. Customers who gave a number years ago are
swept in; opt-out comes later. The incident report quotes customers who did not know they had
agreed.

**Burt terms, key clauses (paraphrased).** Burt gives notifications and facilitates refills and
"non-skilled" pharmacy tasks; it is not medical advice (s.4.1). Inputs may be used to train and
improve Burt (s.4.2, B10). Outputs may draw on manufacturers, drug databases, vendors and
third-party AI models and are not independently verified by Kinney (B8). "Due to the nature of
generative AI" Burt's responses may be inaccurate, incomplete, out of date or misleading, and Burt
may misunderstand the question and answer a different one; use discretion (s.4.3, B6/B4). The
customer remains "solely responsible" for managing medications, and Kinney accepts no added
responsibility by offering Burt (s.4.5, B3). AS IS; no guarantee of accuracy; damages excluded
(s.8, B6/B2). Mandatory individual arbitration.

**Ask Burt terms.** No guarantee of eligibility, access or coverage of cost (B1-analog: what the
bot says about eligibility does not bind Kinney); total liability capped at US$100; one-year
limit on claims.

**Incident (VTDigger, 2026-07-29).** Nearly a dozen customers in VT and NY report Burt placing
unrequested refills (one customer has four unused bottles after approving garbled refill calls),
wrong dosages, missed ready notices, failing to find long-time accounts, and no keypad
alternative. Kinney acknowledged rollout frustration. The article quotes the s.4.3 disclaimer.

## Coder note
1. **Locus 1 (dedicated standalone AI terms), twice.** Brand-named, generative-AI-specific,
   with every major family present. Corpus benchmark alongside Delta and Walmart.
2. **The cleanest say-do-harm triple in the collection:** marketed for efficiency ("handling those
   phone calls in such a nice manner"), contractually disclaimed in detail (s.4.3 predicts the
   exact failure, "may respond to a different question than asked"), and documented as causing
   wrong refills within two months.
3. **Assent mechanism is the weak point:** consent by having provided a phone number, for a
   voice channel where no terms are presented during the call. For Ask Burt, a sign-in-wrap style
   notice at the chat.
4. **Vintage:** Burt terms edited 2026-05-12 and NPP revised 2026-05-19, both timed to the May
   2026 launch; the documents were drafted for the AI, not inherited.

---

<a name="warbyparker"></a>
## Warby Parker - virtual agent chat and AI "Virtual Advisor" - collected 2026-10-06

**AI feature.** A customer-service virtual agent in chat (screening evidence; launch date not
stated) and a "Virtual Advisor" that combines a style quiz with Virtual Try-On and, optionally,
the customer's prescription to produce AI-curated frame recommendations. Roster: NAICS 4561,
rank 9, main sample.

company: Warby Parker Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.warbyparker.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Effective Date April 23, 2026 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: chat (support) + recommendation (Virtual Advisor)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/health-personal-care/warby-parker/warby_terms-of-use_RAW.html (+ .txt)

company: Warby Parker Inc.
document_title: Privacy Policy
document_type: privacy-notice
url: https://www.warbyparker.com/privacy-policy
retrieved: 2026-10-06
effective_or_revised: Effective Date June 17, 2026 (stated)
names_ai_feature: yes - "Virtual Advisor"; "in-house Artificial Intelligence Tools"
fetch_depth: full-fetch
clause_codes_present: disclosure only (AI tools use preferences and, optionally, prescription to curate frames); no B11
files: mastersheet-sources/health-personal-care/warby-parker/warby_privacy-policy_RAW.html (+ .txt)

## Coding-relevant extract

The April 2026 Terms of Use contain no AI language; only generic AS-IS and damages clauses
reach the chat agent and Virtual Advisor. Order clauses deal with backorders and prescriptions,
with no price-error non-honoring clause found. The June 2026 privacy policy describes the
Virtual Advisor and says in-house AI tools build a curated frame list from the user's preferences
and prescription. That is a disclosure, not a disclaimer.

## Coder note
1. **Locus 5 for liability; AI acknowledged only in the privacy policy.** Same split as Wegmans:
   two documents revised within two months of each other, only the privacy one names the AI.
2. **Vintage:** both documents are 2026 revisions; the AI-silent terms are recent, which makes the
   silence a stronger finding.
3. **Gaps:** virtual-agent launch date and vendor unknown; in-chat microcopy not captured.

---

<a name="att"></a>
## AT&T - generative AI assistant in the AT&T app - collected 2026-10-06

**AI feature.** A generative-AI assistant in the redesigned AT&T app (rollout began
2026-03-18) giving "faster answers" and advice on shopping and support; AT&T says it uses models
including Gemini and ChatGPT behind an AT&T-managed experience. Can act on account settings via
app controls (scope of AI actions unclear). Roster: NAICS 5171, rank 2, main sample. ("Ask AT&T"
is an employee tool and out of scope.)

company: AT&T Inc.
document_title: AT&T App End User License Agreement (Terms of Service)
document_type: t1-governing-terms (app)
url: https://www.att.com/legal/terms.AttappEULA.html
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (chat; support and shopping)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic), B10-generic (broad licence to use data derived from App use)
files: mastersheet-sources/telecom/att/att_app-eula_RAW.html (+ .txt)

company: AT&T Inc.
document_title: AT&T Website Terms of Use
document_type: t2-site-terms
url: https://www.att.com/legal/terms.attWebsiteTermsOfUse.html
retrieved: 2026-10-06
effective_or_revised: Effective January 2020 (stated)
names_ai_feature: no - zero AI-keyword hits
fetch_depth: full-fetch
clause_codes_present: B1 (generic: may cancel orders with an inaccurate price or description; user must notify AT&T of pricing errors and comply with corrective action), B6 (generic), B2 (generic)
files: mastersheet-sources/telecom/att/att_website-terms-of-use_RAW.html (+ .txt)

company: AT&T Inc.
document_title: AT&T Launches New App to Simplify Customers' Digital Experience
document_type: t6-marketing
url: https://about.att.com/story/2026/new-att-app.html
retrieved: attempted 2026-10-06 (HTTP 403)
fetch_depth: snippet-only (search results)
files: none

## Coding-relevant extract

Both documents that reach the app assistant are AI-silent. The app EULA has generic AS-IS and
damages terms and a broad licence over data derived from app use. The 2020 website terms disclaim
accuracy of site content and let AT&T cancel orders where a price or description is wrong; the
customer must report pricing errors and accept AT&T's correction (B1, generic). Neither mentions
the assistant.

## Coder note
1. **Locus 3 (generic B1) / 5 (no AI language).** The largest-revenue telecom in the v2 sample to
   launch a GenAI assistant in 2026 without any AI clause in the documents found.
2. **Vintage:** website terms Jan 2020; app EULA undated. Neither revised for the 2026 assistant.
3. **Gaps:** AT&T wireless Consumer Service Agreement (the main service contract) not fetched,
   which could contain AI or app-assistant language; release page 403 (snippet-only); in-app
   microcopy not captured.

---

<a name="tmobile"></a>
## T-Mobile US - Ask AI assistant (T-Life app) - collected 2026-10-06

**AI feature.** "Ask AI", an always-on AI assistant in the T-Life app, announced 2025-11-13. By
voice or text it helps customers upgrade devices, compare plans, and "finds promotions you're
eligible for". Promotion-eligibility statements are the *Moffatt* fact pattern: an AI telling a
customer what discount or deal the firm will honor. Conversations are stored (per third-party
coverage). Roster: NAICS 5171, rank 4, main sample.

company: T-Mobile US, Inc.
document_title: T-Mobile Terms & Conditions
document_type: t1-governing-terms (service contract)
url: https://www.t-mobile.com/responsibility/legal/terms-and-conditions
retrieved: 2026-10-06
effective_or_revised: Effective September 1, 2026 (stated) - after the cutoff; prior versions are archived by T-Mobile at dated URLs
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (voice/text; shopping and account help)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic); no price-error clause found by keyword search
files: mastersheet-sources/telecom/t-mobile/tmobile_terms-and-conditions_RAW.html (+ .txt)

company: T-Mobile US, Inc.
document_title: T-Life support page
document_type: t4-in-product-microcopy (help page describing the app onboarding)
url: https://www.t-mobile.com/support/plans-features/t-life
retrieved: 2026-10-06
names_ai_feature: no (describes the app; no AI mention)
fetch_depth: full-fetch
clause_codes_present: assent evidence: onboarding asks the user to "Review and agree to the terms & conditions" (clickwrap)
files: mastersheet-sources/telecom/t-mobile/tmobile_tlife-support-page_RAW.html (+ .txt)

company: T-Mobile US, Inc.
document_title: T-Life Lets You Connect to Your World, Effortlessly (newsroom)
document_type: t6-marketing
url: https://www.t-mobile.com/news/un-carrier/t-life-updates-one
retrieved: 2026-10-06
effective_or_revised: November 13, 2025
names_ai_feature: yes (Ask AI / AI assistant)
fetch_depth: full-fetch
files: mastersheet-sources/telecom/t-mobile/tmobile_TYPE6_tlife-ask-ai_RAW.html (+ .txt)

## Coding-relevant extract

The September 2026 Terms & Conditions are T-Mobile's main consumer service contract and reach
the app by incorporation. They contain no AI language and, on a keyword search, no clause about
honoring or correcting prices or promotions stated in error. Only generic AS-IS and damages
limits apply. T-Life onboarding has an explicit "review and agree" step (clickwrap), so assent is
strong, but what is agreed to says nothing about the AI.

## Coder note
1. **Locus 5 (no AI language), strong vintage finding.** Revised 2026-09-01, ten months after Ask
   AI launched, and still silent. Note it is after the cutoff: retrieve the version in force at
   2026-06-30 (T-Mobile keeps dated prior versions at t-mobile.com/responsibility/legal/...).
2. **Say-do:** marketing likens Ask AI to "shopping with a bestie" and says it finds promotions
   you are eligible for; no document disclaims eligibility statements.
3. **Gaps:** T-Life app terms (shown at onboarding) not separately located; T-Mobile privacy
   notice not fetched (AI conversation storage); in-app microcopy not captured.

---

<a name="cox"></a>
## Cox Communications - Oliver (chat) and Olive (voice) virtual assistants - collected 2026-10-06

**AI feature.** Oliver, an "automated live chat" on cox.com and in the app that shows balances,
takes bill payments in chat, troubleshoots, and "help[s] update your services and get you set up
with the right plan" (agentic: payments and plan changes); Olive is the voice counterpart
(screening evidence). In use before the Charter merger; the Oliver page now calls it "Spectrum's
Automated Live Chat" while the footer still reads Cox Communications. Roster: NAICS 5171, rank 7,
main sample (logged "stop" under v1; included in v2). **Identity flag:** confirm the
Charter-Cox merger status at the 2026-06-30 cutoff, since corporate identity is fixed then.

company: Cox Communications, Inc.
document_title: Residential Customer Service Agreement (v.7)
document_type: t1-governing-terms (service contract)
url: https://www.cox.com/aboutus/policies/customer-service-agreement.html
retrieved: 2026-10-06
effective_or_revised: Effective Date January 1, 2025 (v.7) (stated)
names_ai_feature: by category ("artificial intelligence (AI) technologies"); Oliver not named
ai_vector: chat + voice; transactional (payments, plan changes)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with the full AI clause + innerText SHA-256
clause_codes_present: AI-disclosure clause (AI-specific, no liability effect), B11-adjacent (names "automated decision-making tools" inside the contract), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/telecom/cox/cox_customer-service-agreement_CAPTURE-NOTE.md

company: Cox Communications, Inc.
document_title: About Oliver (Learn Center page)
document_type: t6-marketing
url: https://www.cox.com/residential/learn/oliver.html
retrieved: 2026-10-06
fetch_depth: full-fetch (browser read; summarized in the CAPTURE-NOTE)
files: mastersheet-sources/telecom/cox/cox_customer-service-agreement_CAPTURE-NOTE.md

## Coding-relevant extract

**s.10.G "Use of Artificial Intelligence."** In full, it says Cox may use AI to enhance services
and user experience, and that the AI may include machine learning, natural language processing
and automated decision-making tools. There is no accuracy disclaimer, no reliance language, and
no allocation of risk for AI errors. The AI shows up in a binding contract purely as a notice.

## Coder note
1. **New sub-type for the codebook: "AI-disclosure clause in binding terms."** AI-specific language
   with zero liability-shifting effect. Distinct from AI-silence and from a disclaimer. Locus 2 by
   position, but functionally closer to locus 5. Flag for the codebook discussion.
2. **Agentic exposure without B1 or B5:** Oliver takes payments and changes plans; nothing
   addresses a wrong plan change or wrong price quoted in chat.
3. **Vintage:** v.7 dated 2025-01-01, while Oliver predates it; the AI notice was likely added in
   v.7 (prior version not compared).
4. **Gaps:** privacy notice 403; Olive voice channel unverified; merger status at cutoff.

---

<a name="gap"></a>
## Gap Inc. - AI-powered customer care ("Chat with Us") - collected 2026-10-06

**AI feature.** A digital assistant in "Chat with Us" on all Gap Inc. brand sites (Gap, Old Navy,
Banana Republic, Athleta) and in the apps, which "helps customers manage returns, payments, order
tracking, and more". Announced 2025-11-25 with other AI shopping tools. Transactional (returns,
payments). Roster: NAICS 4581, rank 3, main sample.

company: Gap Inc.
document_title: Terms of Use (Gap brand site; shared across Gap Inc. brands)
document_type: t1-governing-terms
url: https://www.gap.com/customerService/info.do?cid=6754
retrieved: 2026-10-06
effective_or_revised: Last Revised February 3, 2025 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative chat; transactional (returns, payments)
fetch_depth: full-fetch
clause_codes_present: B1 (generic, strong: may correct errors in pricing, promotions, offers and availability and cancel orders "including after you have submitted your order"; may refuse any order), B2 (generic)
files: mastersheet-sources/clothing/gap/gap_terms-of-use_RAW.html (+ .txt)

company: Gap Inc.
document_title: Gap Inc. Is Using AI to Reimagine Retail, With New Innovations Launching in Time for Cyber Monday
document_type: t6-marketing
url: https://www.gapinc.com/en-us/articles/2025/11/gap-inc-is-using-ai-to-reimagine-retail,-with-new-
retrieved: 2026-10-06
effective_or_revised: November 25, 2025
names_ai_feature: yes ("AI-Powered Customer Care")
fetch_depth: full-fetch
files: mastersheet-sources/clothing/gap/gap_TYPE6_ai-retail-article_RAW.html (+ .txt)

## Coding-relevant extract

The Feb 2025 Terms of Use contain no AI language. The "Errors, Inaccuracies, and Omissions"
clause says site information may contain errors in descriptions, pricing, promotions, offers and
availability, and Gap may correct them and cancel orders at any time, including after an order is
submitted (B1, generic). Gap may also refuse any order. Nothing addresses an assistant that
handles returns or payments.

## Coder note
1. **Locus 3 (generic B1 reaching the AI's domain).**
2. **Vintage:** terms Feb 2025, AI care launched Nov 2025; not revised. The release says AI helps
   Gap "anticipate their needs" and "inspire confidence in every interaction".
3. **Gaps:** privacy policy not fetched; chat microcopy not captured; a 2026-10-05 Gap Inc. release
   on "the Next Era of AI-Powered Shopping" (after cutoff) not fetched.

---

<a name="americaneagle"></a>
## American Eagle Outfitters - AI chatbot (style recommendations, order tracking, returns) - collected 2026-10-06

**AI feature.** An AI chatbot on ae.com handling style recommendations, order tracking and returns
(screening evidence from a vendor case study; launch date not stated). Roster: NAICS 4581, rank 7,
main sample.

company: American Eagle Outfitters, Inc.
document_title: AEO US Terms of Use (PDF; linked as "Terms of Service")
document_type: t1-governing-terms
url: https://s7d2.scene7.com/is/content/aeo/Help/AEO_US_Terms_of_Use.pdf (linked from https://www.ae.com/us/en/content/help/terms-of-use, which blocks scripts with 403)
retrieved: 2026-10-06
effective_or_revised: Last Updated June 19, 2026 (stated) - eleven days before the cutoff
names_ai_feature: by category ("Artificial Intelligence 'AI' Chatbot")
ai_vector: generative chat; transactional-adjacent (returns, order tracking)
fetch_depth: full-fetch (PDF)
clause_codes_present: B6 (AI-specific: may give incomplete or inaccurate responses), B2 (AI-specific: "AEO is not liable for any errors or omissions in the information provided by the AI Chatbot"), B10 (AI-specific: conversations collected and analyzed to improve the chatbot; licence over interactions), no-endorsement (AI-specific), not-professional-advice; B1 (generic: correct errors and cancel orders "including after you have submitted your order"), B6/B2 (generic)
files: mastersheet-sources/clothing/american-eagle/ae_terms-of-use.pdf (+ .txt)

## Coding-relevant extract

**s.21 "AI Chatbot Disclosure."** By interacting with the AI Chatbot the user agrees that:
conversations may be collected, stored and analyzed by AEO and its vendors to improve the chatbot
(B10); the chatbot gives general information, not legal, medical or professional advice; it "may
occasionally provide incomplete or inaccurate responses" (B6), and **AEO is not liable for any
errors or omissions in the information it provides** (B2, AI-specific, an express no-liability
rule for chatbot statements); chatbot interactions are not an endorsement of products or
third-party content; prohibited uses apply; continued use of the chatbot is acceptance (B9-adjacent).

**Generic B1.** Site information may contain errors in pricing, promotions, offers and
availability; AEO may correct them and cancel orders at any time, including after submission.

## Coder note
1. **Locus 2 (dedicated AI section inside general terms).** The express "not liable for any errors
   or omissions" in chatbot information is the most direct AI-specific liability exclusion so far,
   short of Ulta's authority clause.
2. **Vintage:** revised 2026-06-19, inside the collection cutoff. Good timing for the headline counts.
3. **Assent:** browsewrap plus "continued use of the AI Chatbot constitutes ... acceptance".
4. **Gaps:** privacy notice not captured (403); chatbot launch date and in-chat microcopy unknown.

---

<a name="abercrombie"></a>
## Abercrombie & Fitch - AI Stylist (app) - collected 2026-10-06

**AI feature.** AI Stylist in the Abercrombie app, launched 2023: natural-language outfit
recommendations from prompts (e.g. an outfit for a bachelorette party in Nashville), described by
A&F's CDTO in an NRF interview (Feb 2024). Run through a third-party AI service. Roster: NAICS
4581, rank 8, main sample.

company: Abercrombie & Fitch Co.
document_title: Website/App Terms of Use ("AI Tools" section)
document_type: t1-governing-terms
url: https://www.abercrombie.com/shop/CustomerService?pageName=site-use&textKey=LEGAL_SITE_USE&storeId=10051&catalogId=10901&langId=-1
retrieved: 2026-10-06
effective_or_revised: Updated July 2023 (stated)
names_ai_feature: yes - by brand ("the AI Stylist") and category ("AI Tools")
ai_vector: generative (recommendations)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI section + innerText SHA-256 (JS-rendered page)
clause_codes_present: B1-analog (AI-specific: an AI Response "does not necessarily represent the opinion, comment, content, or recommendation of A&F"), B6 (AI-specific: may be inaccurate, inapplicable or inappropriate; no guarantee), B4 (AI-specific: suggestions only; exercise reasonable discretion before relying), B2/B8 (AI-specific: AI is a Third Party Service with no affiliation; A&F not responsible or liable for use of AI Tools or reliance on any AI Response), B3 (user bears risk of sharing personal information), B10-inverse (A&F claims no ownership of AI Responses; user's rights treated as User-Generated Content)
vendor: unnamed "Third Party Service"
files: mastersheet-sources/clothing/abercrombie/anf_website-terms-of-use_CAPTURE-NOTE.md

company: Abercrombie & Fitch (NRF interview)
document_title: Inside the digital transformation of Abercrombie & Fitch (NRF Retail Gets Real ep. 337)
document_type: t6-marketing
url: https://nrf.com/blog/inside-digital-transformation-abercrombie-fitch
retrieved: 2026-10-06
effective_or_revised: February 20, 2024
fetch_depth: full-fetch
files: mastersheet-sources/clothing/abercrombie/anf_TYPE6_nrf-blog_RAW.html (+ .txt)

## Coding-relevant extract

**AI Tools section.** Calls the AI Tools, "including ... the AI Stylist", "experimental" AI. Using
them is agreeing to additional terms: use responsibly; don't share personal information (at your
own risk if you do); using the tools means dealing with a third-party service unaffiliated with
A&F, subject to its terms, and **A&F is not responsible or liable for use of the AI Tools or
reliance on any AI Response** (B2/B8). AI Responses may be inaccurate or inappropriate, are
suggestions only, and require reasonable discretion before reliance (B6/B4). **An AI Response
does not necessarily represent A&F's opinion or recommendation**, a disclaimer of attribution
parallel to Ulta's "not authorized to make any promises" (B1-analog).

## Coder note
1. **Locus 2 (dedicated AI section inside site terms), brand-named.** Among the earliest in the
   corpus (July 2023, the year AI Stylist launched).
2. **Two anti-attribution moves.** (a) The AI is framed as a third-party service, not A&F;
   (b) its output "does not necessarily represent" A&F. Together they target the *Moffatt*
   holding that the chatbot is part of the firm's own website. Flag for the doctrinal section:
   courts may not accept that distinction when the tool is embedded in the firm's own app.
3. **Vintage:** July 2023, same year as launch: drafted for the AI.
4. **Gaps:** privacy policy not captured (JS shell); vendor identity; in-app microcopy.

---

<a name="jcrew"></a>
## J.Crew Group - AI Shopping Assistant (beta) - collected 2026-10-06

**AI feature.** An AI Shopping Assistant in beta on jcrew.com by 2025, described by J.Crew's CIO
(Forbes, 2025-11-18, screening evidence). Roster: NAICS 4581, rank 9, main sample (private).

company: J.Crew Group, LLC
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.jcrew.com/help/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated September 19, 2024 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (shopping assistant)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B3 (generic: user assumes all responsibility and risk for use of the Site), B6 (generic AS IS; information may contain inaccuracies and may be corrected without notice), B2 (generic)
files: mastersheet-sources/clothing/jcrew/jcrew_terms-of-use_CAPTURE-NOTE.md

## Coding-relevant extract

No AI language. Generic only: information on the Site may contain technical or factual
inaccuracies and may be corrected without notice; the user assumes all responsibility and risk;
the Site is AS IS. No express order-cancellation-for-price-error clause surfaced in the
keyword pass.

## Coder note
1. **Locus 5 (absent; generic only).** Terms predate the assistant beta and were not revised.
2. **Gaps:** first-party assistant announcement not located (Forbes interview only); privacy policy
   not captured; in-product microcopy not captured; beta liveness by 2026-06-30 assumed from
   screening.

---

<a name="bankofamerica"></a>
## Bank of America - Erica (virtual financial assistant) - collected 2026-10-06

**AI feature.** Erica, in the Mobile Banking app since 2018: voice and text assistant that
answers questions, gives proactive insights, and **acts**: initiates transfers, pays bills,
locks/unlocks cards. BofA states Erica uses NLP and machine learning to pick from pre-defined
answers and does **not** use generative AI or LLMs. Over 3 billion client interactions (2025
release). Roster: NAICS 5221, rank 2, main sample. Non-generative but agentic: in scope under the
consumer-interaction test.

company: Bank of America Corporation
document_title: Online Banking Service Agreement (section "Erica Bank of America's Virtual Financial Assistant")
document_type: t1-governing-terms
url: https://www.bankofamerica.com/online-banking/service-agreement.go
retrieved: 2026-10-06
effective_or_revised: EFFECTIVE OCTOBER 19, 2026 (stated) - the page already serves the next version; after the cutoff
names_ai_feature: yes - by brand (Erica) with an AI description
ai_vector: assistive NLP (non-generative, retrieval of pre-defined answers) + agentic (transfers, bill pay, card controls)
fetch_depth: full-fetch
clause_codes_present: B4 (AI-specific: user responsible for reviewing what Erica displays and confirming it matches the instruction), B6 (AI-specific: Erica may misunderstand, lack information, make a mistake, or fail), B3 (AI-specific: interactions via the device treated as authorized by the user even if another voice or person initiated them), B5-adjacent (Erica executes transactions; errors routed to the agreement's dispute terms), B10 (AI-specific: third-party voice provider; voice kept 90 days to refine listening; masked transcripts kept), plus generic B2/B6 for Online Banking
vendor: unnamed third-party voice provider
files: mastersheet-sources/banking/bank-of-america/bofa_online-banking-service-agreement_RAW.html (+ .txt)

company: Bank of America Corporation
document_title: Erica - Virtual Financial Assistant (product page and FAQ)
document_type: t6-marketing (with FAQ microcopy)
url: https://info.bankofamerica.com/en/digital-banking/erica
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: FAQ states Erica is "not an actual person" and not generative AI; "Erica does not provide investment advice"; chat may be recorded
files: mastersheet-sources/banking/bank-of-america/bofa_TYPE6_erica-page_RAW.html (+ .txt)

## Coding-relevant extract

**Erica section of the OBSA.** Erica is "a non-human, bot feature" of Digital Banking that can
obtain balances, initiate transfers and pay bills. It uses AI to understand intent and picks
from pre-defined answers; it does not use generative AI. The user must review what Erica shows
and confirm it reflects the request (B4); Erica may misunderstand, lack complete information,
make a mistake, or fail (B6); its insights are limited to BofA accounts. Anyone who can unlock
the app can use Erica, and BofA treats such interactions and transactions as authorized by the
customer "even if another voice or person initiated or completed them" (B3, AI-channel-specific
risk shift). Disputes about Erica transactions or information go through the general agreement's
dispute provisions; where agreements conflict, the Erica terms control for Erica. Third-party
voice processing; voice kept 90 days.

## Coder note
1. **Locus 2 (dedicated, brand-named section inside the governing agreement).** Matches Wells
   Fargo's Fargo pattern from the pilot corpus.
2. **The "non-generative" representation is itself a contract term.** It narrows the hallucination
   risk by design, and reallocates misunderstanding risk to the user through the review-and-confirm
   duty. Code the self-description as a separate feature (AI-type disclosure).
3. **No B1 for Erica-initiated transactions:** errors are handled as ordinary disputes (Reg E
   rights still apply by law), not refused in advance.
4. **Version problem:** captured version is effective 2026-10-19, after the cutoff. Retrieve the
   version in force at 2026-06-30 (BofA links prior versions from the page in some periods).
5. **Gaps:** BofA Online Privacy Notice not fetched (B11).

---

<a name="citi"></a>
## Citigroup - GenAI-powered Enhanced IVR (US Personal Banking) - collected 2026-10-06

**AI feature.** A generative-AI "Enhanced Interactive Voice Response" in US Personal Banking phone
service, launched as one of Citi's first business GenAI pilots (firm statement dated
2025-06-23): smarter call routing and self-service, alongside an employee-side Agent Assist (out
of scope). Voice. Roster: NAICS 5221, rank 3, main sample.

company: Citigroup Inc.
document_title: Strengthening Our Commitment to AI Innovation (Perspectives)
document_type: t6-marketing (firm statement; internal memo published externally)
url: https://www.citigroup.com/global/news/perspectives/2025/strengthening-commitment-ai-innovation
retrieved: 2026-10-06
effective_or_revised: June 23, 2025
names_ai_feature: yes (Enhanced IVR, GenAI pilot)
fetch_depth: full-fetch
files: mastersheet-sources/banking/citi/citi_TYPE6_ai-innovation_RAW.html (+ .txt)

company: Citigroup Inc.
document_title: Citi Online / Client Manual terms; Citi privacy notice
document_type: t1-governing-terms / privacy-notice
url: online.citi.com terms URL tried (404); www.citi.com/privacy (JS shell, 41 chars)
retrieved: attempted 2026-10-06
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

The only document captured is Citi's own statement: the GenAI IVR pilot is meant to "improve the
customer service experience and resolve client inquiries faster". No consumer document
addressing the IVR was located. Phone callers are not presented with terms during the call.

## Coder note
1. **Locus 5 (no consumer terms presented; assent none) for the voice channel**, provisionally.
   The Citi Client Manual (deposit agreement PDF) and Citi Online terms were not located within
   budget; they may contain generic telephone-banking clauses that would reach IVR instructions.
2. **Pilot liveness:** "pilot" as of June 2025; whether it reached real customers and remained live
   at 2026-06-30 is not established here (screening counted it).
3. **Gaps (honest):** governing terms and privacy notice not located (404 / JS shell). Re-try via
   browser in the version-check pass.

---

<a name="usbank"></a>
## U.S. Bancorp - U.S. Bank Smart Assistant - collected 2026-10-06

**AI feature.** U.S. Bank Smart Assistant (since 2020) in the mobile app, online banking and
usbank.com: voice or text, English and Spanish. It answers questions and **executes
transactions** ("Pay the statement balance on my credit card", "Send 200 bucks to Tony",
"Transfer $100 from savings to checking", lock a card). Roster: NAICS 5221, rank 5, main sample.

company: U.S. Bancorp (U.S. Bank N.A.)
document_title: Digital Services Agreement (Terms of Use for Digital Services)
document_type: t1-governing-terms
url: https://www.usbank.com/caas/digital-services-agreement.html
retrieved: 2026-10-06
effective_or_revised: not stated in captured text (date_basis: not-stated)
names_ai_feature: yes - by brand (Smart Assistant) and category ("artificial intelligence ('AI') technology", "AI powered chatbots")
ai_vector: assistive voice/text + agentic (payments, transfers, card lock); generative content named ("content generation")
fetch_depth: full-fetch
clause_codes_present: B2 (AI-specific, strong: "we expressly disclaim all liability for damages of any kind arising out of the use or reliance on the information provided by any AI tools"), B6 (AI-specific: AI output may not be error-free; no guarantee of accuracy or suitability), B10 (AI-specific: input data may be used to train or develop AI models and for offers and other business purposes), B11-adjacent (names "decision making" among AI functions), B3 (generic: user's sole responsibility for device security when the assistant is enabled), not-professional-advice
vendor: none named
files: mastersheet-sources/banking/us-bank/usbank_digital-services-agreement_RAW.html (+ .txt)

company: U.S. Bancorp
document_title: U.S. Bank Smart Assistant (product page)
document_type: t6-marketing
url: https://www.usbank.com/online-mobile-banking/smart-assistant.html
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/banking/us-bank/usbank_TYPE6_smart-assistant-page_RAW.html (+ .txt)

## Coding-relevant extract

**"Smart Assistant" subsection.** Voice or typed instructions let you view balances, pay bills and
initiate select transactions; the assistant "uses your prompts to perform actions or make
recommendations"; transcripts kept for quality, product improvement, compliance and business
purposes; be aware of surroundings when speaking commands.

**"Use of artificial intelligence" subsection.** Digital Services may include AI (e.g. the Smart
Assistant and automated chat) involving chatbots, automated responses, content generation, data
analysis and decision making. AI output may not be perfect or error-free, with no guarantee of
accuracy or suitability (B6). U.S. Bank is not responsible for, and "expressly disclaim[s] all
liability for, damages of any kind arising out of the use or reliance on the information provided
by any AI tools" (B2, AI-specific, the broadest AI-liability exclusion so far). Inputs may be used
to train or develop AI models and for offers and other business purposes (B10).

## Coder note
1. **Locus 2 (AI section inside the governing digital agreement), brand-named.**
2. **The exclusion is limited to "information provided by" AI tools,** not to transactions the
   assistant executes; those fall under the agreement's ordinary transfer and error terms (and
   Reg E). Read the B2 as an information-reliance exclusion.
3. **Say-do:** the product page calls the assistant "your trusted partner" and says information
   shared is "completely private"; the agreement reserves use of inputs for training and offers.
4. **Gaps:** no effective date in the captured text (check the PDF version linked from the
   online-banking dashboard); privacy notice not fetched.

---

<a name="truist"></a>
## Truist Financial - Truist Assist - collected 2026-10-06

**AI feature.** Truist Assist, an "AI-enhanced" virtual assistant in the mobile app and online
banking for personal and wealth clients, launched 2022-09-15. Uses NLP/NLU to answer 100+ common
support and digital-banking questions and hands off to contact-center staff. Informational
(the release does not describe transaction execution). Roster: NAICS 5221, rank 7, main sample
(logged "stop" under v1; included in v2).

company: Truist Financial Corporation (Truist Bank)
document_title: Truist Online and Mobile Banking Service Agreement
document_type: t1-governing-terms
url: https://www.truist.com/content/dam/truist-bank/us/en/documents/agreement/online-and-mobile-banking-service-agreement.pdf
retrieved: 2026-10-06
effective_or_revised: Effective as of 4/8/2026 (stated)
names_ai_feature: no - zero hits for AI terms, "Truist Assist", "virtual assistant", "chat"
ai_vector: assistive NLP (informational)
fetch_depth: full-fetch (PDF)
clause_codes_present: B6 (generic AS IS), B2 (generic), B3 (generic: user responsible for payments authorized even with wrong amount)
files: mastersheet-sources/banking/truist/truist_online-mobile-banking-agreement.pdf (+ .txt)

company: Truist Financial Corporation
document_title: Truist launches Truist Assist (press release)
document_type: t6-marketing
url: https://media.truist.com/2022-09-15-Truist-launches-Truist-Assist
retrieved: 2026-10-06
effective_or_revised: September 15, 2022
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/banking/truist/truist_TYPE6_assist-launch_RAW.html (+ .txt)

## Coding-relevant extract

The April 2026 agreement governs the app and online banking, where Truist Assist lives, and runs
to about 250,000 characters. It contains no reference to AI, the virtual assistant, or chat. Only
the generic AS-IS, limitation-of-liability, and payment-error allocation clauses reach it.

## Coder note
1. **Locus 5 (absent), strong vintage finding.** Revised April 2026, three and a half years after
   launch, and still silent, in contrast to peers (BofA, U.S. Bank) whose agreements carry
   dedicated assistant sections.
2. **Say-do:** release promises "detailed information to help empower clients to make financial
   decisions"; the agreement says nothing about that information.
3. **Gaps:** Bank Services Agreement and Privacy Notice (separate PDF) not fetched (B11 unchecked);
   in-app microcopy not captured.

---

<a name="dukeenergy"></a>
## Duke Energy - mobile-app AI chatbot and AI Bill Insights - collected 2026-10-06

**AI feature.** An AI chatbot in the Duke Energy app (about 280,000 interactions in its first three
months, per secondary sources and conference material) and "AI Bill Insights", plain-language
AI explanations of monthly bills for Carolinas customers (reported by Yahoo Finance). Billing and
outage domain: a wrong bill explanation is a classic *Moffatt*-type misstatement. Launch dates not
established. Roster: NAICS 2211, rank 1, main sample (regulated utility).

company: Duke Energy Corporation
document_title: Terms of Use (duke-energy.com)
document_type: t1-governing-terms (site and app)
url: https://www.duke-energy.com/legal/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last updated April 3, 2023 (stated)
names_ai_feature: no - only reference is "any chat functionality available through the Site" inside the user-submissions licence
ai_vector: generative/assistive chat; generative explanations (Bill Insights)
fetch_depth: full-fetch
clause_codes_present: B10 (generic but chat-reaching: royalty-free irrevocable licence to anything submitted via chat), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/electric-utilities/duke-energy/duke_terms-of-use_RAW.html (+ .txt)

company: Duke Energy (marketing / secondary)
document_title: AI Bill Insights coverage; chatbot interaction figures
document_type: t6-marketing
url: https://finance.yahoo.com/energy/articles/duke-energy-duk-launches-ai-150744199.html
retrieved: 2026-10-06 (search result)
fetch_depth: snippet-only
files: none

## Coding-relevant extract

The April 2023 Terms of Use contain no AI language. Chat is mentioned once: anything submitted
through "any chat functionality" is a "Comment" licensed to Duke royalty-free and irrevocably
(B10, generic). Otherwise only AS-IS and damages limits. Nothing addresses the accuracy of chatbot
answers or AI bill explanations.

## Coder note
1. **Locus 5 (no AI language).** Regulated utility: billing disputes go through state
   public-utility-commission rules and tariffs, which no website terms can override. The terms'
   silence may matter less than the tariff (record for the regulatory-intensity variable).
2. **Gaps:** first-party chatbot and Bill Insights announcements not fetched (snippet-only); privacy
   page was a 1.5k-char hub (dropped); tariff/rules of service not checked.

---

<a name="pge"></a>
## PG&E Corporation - "Peggy" conversational voice AI - collected 2026-10-06

**AI feature.** Peggy, PG&E's AI-powered voice assistant that replaced its traditional IVR on
customer service lines, described by PG&E's customer-service leaders as "the first
customer-facing conversational voice AI" at the company (Chartwell EMACS 2025 session). Voice;
billing, outage and account calls. Launch date not stated (by 2025). Roster: NAICS 2211, rank 6,
main sample (regulated utility).

company: PG&E Corporation (Pacific Gas and Electric Company)
document_title: AI in Action: PG&E's AI Voice Assistant Revolutionizing Customer Interactions (Chartwell EMACS 2025 session page)
document_type: t6-marketing (industry-conference abstract presented by PG&E staff; not a vendor case study)
url: https://chartwellinc.com/conferences/keynote-ai-in-action-pges-ai-voice-assistant-revolutionizing-customer-interactions/
retrieved: 2026-10-06
effective_or_revised: 2025 (EMACS 2025 agenda)
names_ai_feature: yes ("Peggy")
fetch_depth: full-fetch
files: mastersheet-sources/electric-utilities/pge/pge_TYPE6_peggy-chartwell_RAW.html (+ .txt)

company: PG&E Corporation
document_title: pge.com website terms of use
document_type: t2-site-terms
url: attempted https://www.pge.com/en/about/doing-business-with-pge/legal-notices/website-terms-of-use.html (404)
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

No consumer document addressing Peggy was located. Callers reach Peggy on the phone, where no
terms are presented. The conference abstract frames Peggy as replacing the IVR to streamline
service and improve satisfaction.

## Coder note
1. **Locus 5 (no consumer terms; assent none).** Website terms would not reach a phone call in any
   case; the binding rules for PG&E billing are CPUC-approved tariffs (electric/gas Rules), which
   were not checked. Record as regulated-utility, tariff-governed.
2. **Evidence tier:** conference session by PG&E employees; a first-party press release was not
   found within budget.
3. **Gaps:** website terms URL; CPUC tariff rules on customer communications.

---

<a name="exelon"></a>
## Exelon - utility chat assistant (six utilities) - collected 2026-10-06

**AI feature.** A chat assistant on the websites and apps of Exelon's six utilities (Atlantic
City Electric, BGE, ComEd, Delmarva Power, PECO, Pepco): shows balances, **pays bills**, reports
outages, **starts, stops or moves service**. Voice "if and when such may become available".
Agentic. Roster: NAICS 2211, rank 7, main sample (regulated utilities).

company: Exelon Corporation (operating utilities)
document_title: Chat Assistant Terms & Conditions (PDF: "Exelon Utilities Chat Bot Terms and Conditions")
document_type: t3-dedicated-ai-doc (standalone terms for the chat feature)
url: https://www.exeloncorp.com/content/dam/exelon/company/Documents/Exelon%20Utilities%20Chat%20Bot%20Terms%20and%20Conditions.pdf
retrieved: 2026-10-06
effective_or_revised: not stated (date_basis: not-stated)
names_ai_feature: by function ("the Chat", a chat assistant); the words "AI", "artificial intelligence" and "bot" do not appear in the body
ai_vector: assistive chat (voice planned) + agentic (payments, start/stop/move service)
fetch_depth: full-fetch (PDF)
clause_codes_present: B4 (chat-specific: user must review what the Chat displays and confirm it matches the request), B6 (chat-specific: may misunderstand, lack information, make a mistake, or fail), B3 (chat-specific: interactions by anyone with device access, or any voice, treated as authorized), B10 (interactions used to improve the service and personalize)
vendor: none named
files: mastersheet-sources/electric-utilities/exelon/exelon_chatbot-terms.pdf (+ .txt)

## Coding-relevant extract

Using the Chat means agreeing to these terms plus the site Privacy Policy and Terms of Use. The
Chat can take account actions, including bill payment and starting, stopping or moving service.
The user must review what the Chat displays and confirm it matches their instructions; the Chat
may misunderstand, lack complete information, make a mistake or not work (B4/B6). Interactions
by anyone with access to the account, or any voice in a voice session, are treated as authorized
by the customer (B3). Interactions may be used to improve the service.

## Coder note
1. **Locus 1 (dedicated standalone terms), but AI-unnamed.** A standalone instrument governing a
   conversational agent that never calls it AI. Code AI-specific by function (the clauses exist
   only because of the automated agent).
2. **Template diffusion (cross-firm finding).** Sections 2-3 track Bank of America's Erica terms
   almost word for word ("Please carefully execute and review interactions ... may misunderstand
   you at times, may not have complete information related to your request, may otherwise make a
   mistake ... or the technology may simply not work"; "We will treat these interactions as though
   you authorized them ... even if another voice or person initiated or completed them"). Likely a
   common vendor or drafting source. Worth a systematic sentence-level comparison across the
   corpus for the paper: clause language may spread through vendors, not through firms.
3. **Assent:** agreement by use of the chat; linked from the utility sites (incorporation status
   relative to the site terms not checked).
4. **Gaps:** no date; utility-specific tariffs govern billing and service changes.

---

<a name="edison"></a>
## Edison International (Southern California Edison) - AskSCE chatbot - collected 2026-10-06

**AI feature.** AskSCE, a 24/7 chatbot on sce.com for questions about payment methods, outages
and account help. AI status asserted by screening; launch date not stated. Roster: NAICS 2211,
rank 9, main sample (regulated utility).

company: Edison International (Southern California Edison Company)
document_title: SCE Website Terms of Use
document_type: t1-governing-terms (website)
url: https://www.sce.com/terms-conditions/website-terms-of-use
retrieved: 2026-10-06
effective_or_revised: updated on December 18, 2019 (stated)
names_ai_feature: no - "chat services" appear only in a list of site features
ai_vector: chat (support)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/electric-utilities/edison/sce_website-terms-of-use_RAW.html (+ .txt)

company: Edison International (SCE)
document_title: How do I contact SCE? (help-center page describing AskSCE)
document_type: t6-marketing
url: https://www.sce.com/customer-service-center/help-center/my-account/other/contact-sce
retrieved: 2026-10-06
names_ai_feature: yes ("AskSCE chatbot")
fetch_depth: full-fetch
files: mastersheet-sources/electric-utilities/edison/sce_contact-page_RAW.html (+ .txt)

company: Edison International (SCE)
document_title: Legal hub (sce.com/legal): 19 terms documents
document_type: legal-hub-index
url: https://www.sce.com/legal
retrieved: 2026-10-06 (browser read)
fetch_depth: full-fetch (browser; listing only, not saved)
files: none

## Coding-relevant extract

The 2019 Website Terms of Use say the site "may contain email and chat services" as part of
Website Content, with generic AS-IS and damages limits. Nothing about automated or AI responses.
The legal hub lists 19 sets of terms (online services, billing, alerts, programs), none for
AskSCE.

## Coder note
1. **Locus 5 (absent).** Terms predate the chatbot era and were not updated.
2. **Regulated utility:** billing and service governed by CPUC tariffs (not checked).
3. **Gaps:** AskSCE launch date and AI basis (vendor or generative) not verified from a firm
   source; "My Account Online Services" and "Online Services, Billing, Payment" terms not checked.

---

<a name="caesars"></a>
## Caesars Entertainment - Ivy (AI SMS concierge) - collected 2026-10-06

**AI feature.** Ivy, an AI text-message concierge for hotel guests (built by Go Moment, now part
of Revinate; earlier IBM Watson-powered). After check-in, guests who gave a mobile number get a
welcome text and can ask for recommendations, **dinner reservations**, housekeeping requests and
property information; unanswerable requests go to a human agent team. Rolled out across Caesars
Las Vegas resorts (6,000+ rooms) and other properties. SMS channel. Roster: NAICS 7211, rank 5,
main sample.

company: Caesars Entertainment, Inc.
document_title: Caesars Terms of Use (caesars.com/corporate/terms-of-use)
document_type: t1-governing-terms
url: https://www.caesars.com/corporate/terms-of-use
retrieved: attempted 2026-10-06
fetch_depth: referenced-not-located. Scripted fetch returned a Caesars Rewards login shell with no terms text; the built-in browser refuses caesars.com under a site safety restriction (gambling), so no browser capture was attempted further.
files: none

company: Caesars Entertainment, Inc.
document_title: Caesars Entertainment Las Vegas Resorts ... (investor release on Ivy; PDF)
document_type: t6-marketing
url: https://investor.caesars.com/static-files/8a650e6e-2e0e-4750-90b7-84356d69ca7c
retrieved: attempted 2026-10-06 (timed out)
fetch_depth: snippet-only (search results; trade press: Lodging Magazine, Hotel Business, Travel Weekly)
files: none

## Coding-relevant extract

No legal text was retrieved. From search snippets of firm and trade sources: Ivy is offered after
check-in to guests who gave a mobile number; it is optional; guests opt out by texting STOP.
No AI-specific terms were found in search results.

## Coder note
1. **Provisional coding:** assent by providing a phone number at booking (SMS consent), not a
   terms acceptance for the AI. Locus undetermined until the Terms of Use and any SMS terms are
   read.
2. **Retrieval route for later:** caesars.com is blocked in the built-in browser by policy; the
   user could open the page in their own browser, or the Terms could be retrieved from an archive
   once the Internet Archive is reachable.
3. **Liveness:** Ivy coverage is mostly 2018-2020; confirm it was still live at 2026-06-30.

---

<a name="hyatt"></a>
## Hyatt Hotels - generative natural-language (intent) search on Hyatt.com - collected 2026-10-06

**AI feature.** Hyatt rebuilt Hyatt.com search as a generative-AI interface where guests describe
trips in prose instead of city/date fields; the CEO reported conversion lift over several quarters
on the Feb 2026 earnings call (Skift, 2026-02-12). Hyatt also has a ChatGPT app (third-party
channel, out of scope). Roster: NAICS 7211, rank 7, main sample.

company: Hyatt Hotels Corporation
document_title: Hyatt Terms & Conditions
document_type: t1-governing-terms
url: https://www.hyatt.com/help/en-US/terms/hyatt (also /info/terms-of-use)
retrieved: attempted 2026-10-06
fetch_depth: snippet-only. Scripted fetch returned HTTP 403; the built-in browser rendered an empty page (0 chars) on both URLs (bot challenge).
names_ai_feature: unknown
clause_codes_present: B10 (generic, from search snippet: searches, questions, comments, chats and requests submitted to Hyatt are not confidential and Hyatt may use and disclose them freely)
files: none

company: Hyatt (trade press)
document_title: Hyatt CEO Sees Lift From AI Search; Reveals ChatGPT App (Skift)
document_type: t6-marketing
url: https://skift.com/2026/02/12/hyatt-ceo-sees-lift-from-ai-search-reveals-chatgpt-app/
retrieved: 2026-10-06
effective_or_revised: February 12, 2026
fetch_depth: full-fetch (paywalled page; opening paragraphs captured)
files: mastersheet-sources/hospitality/hyatt/hyatt_TYPE6_skift-ai-search_RAW.html (+ .txt)

## Coding-relevant extract

The Terms text could not be read. The search snippet shows a generic clause treating user
"searches ... chats, requests" as non-confidential communications Hyatt may use freely (B10,
generic; it would reach prompts typed into the AI search). Whether the Terms contain AI language
is unknown.

## Coder note
1. **Do not code locus or presence/absence for Hyatt yet.** Snippets can establish presence, not
   absence (CLAUDE.md rule).
2. **Scope note for the screen:** generative search that returns hotel results is at the edge of
   "converses with customers"; the screen accepted it.
3. **Retrieval route:** user's own browser, or an archived copy when the Internet Archive is
   reachable.

---

<a name="vanguard"></a>
## Vanguard - generative-AI Voicebot (proof-of-concept) and workplace bots - collected 2026-10-06

**AI feature.** (1) A generative-AI voicebot giving real-time answers that draw on the caller's
account information, run as a proof-of-concept with self-directed Personal Investor clients who
volunteered (terms effective 2026-02-23). Third-party AI models. (2) For workplace-plan
participants: 70+ "AI-powered bots", including transactional chatbots and a voice bot for address
changes. (The Digital Advisor gen-AI chat launched Sept 2026, after the cutoff, and is excluded.)
Roster: NAICS 5239, rank 3, main sample (client-owned).

company: The Vanguard Group, Inc.
document_title: Vanguard Voicebot Terms of Use (published within the Online Terms and Conditions page)
document_type: t3-dedicated-ai-doc
url: https://investor.vanguard.com/terms-conditions
retrieved: 2026-10-06
effective_or_revised: Effective date February 23rd, 2026 (stated)
names_ai_feature: yes - "Voicebot", expressly "generative AI-enabled"
ai_vector: generative voice; account-aware (uses non-public personal information)
fetch_depth: full-fetch (embedded in a 190k-char page that also holds the general online terms)
clause_codes_present: B1-analog (AI-specific: Output is informational only and "cannot be interpreted as an offer or indication to buy or sell securities"; Output "do[es] not represent the opinions, beliefs or assertions of Vanguard"), B3 (AI-specific: decisions based on Output are entirely the user's; Vanguard assumes no responsibility for consequences incl. errors and omissions), B6 (AI-specific: Output not reviewed for accuracy or timeliness; cannot be reviewed before receipt), B2 (AI-specific: no liability for reliance on Output), not-advice and not-fiduciary (AI-specific), B8/B10 (third-party AI models may receive Input and Output including NPI), B9 (no using Output to train AI tools or models)
vendor: unnamed "third-party provided AI models"
files: mastersheet-sources/investing/vanguard/vanguard_terms-conditions_RAW.html (+ .txt)

company: The Vanguard Group, Inc.
document_title: Innovation in action: how Vanguard is improving financial wellness outcomes (workplace blog)
document_type: t6-marketing
url: https://workplace.vanguard.com/insights-and-research/blog/innovation-in-action-how-vanguard-is-improving-financial-wellness-outcomes.html
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/investing/vanguard/vanguard_TYPE6_workplace-blog_RAW.html (+ .txt)

company: The Vanguard Group, Inc.
document_title: Vanguard Generative AI Features Terms of Use (published within the Online Terms and Conditions page) [added 2026-10-07 on full-read re-coding]
document_type: t3-dedicated-ai-doc
url: https://investor.vanguard.com/terms-conditions
retrieved: 2026-10-06
effective_or_revised: Effective date July 8, 2026 (stated)
names_ai_feature: category - "AI Features" (generative-AI chat, voice, web and public-facing "embedded GenAI agents")
ai_vector: generative chat/voice; account-aware; also public (no-login) AI interfaces
fetch_depth: full-fetch (same preserved page as the Voicebot terms; section headed "Vanguard Generative AI Features Terms of Use")
clause_codes_present: B2, B3, B4, B6, B7, B8, B9, B10 (all AI-specific); risk-factor section (contextual limits, inaccuracy, third-party model oversight, data-poisoning/adversarial attacks); anti-attribution ("do not necessarily represent the opinions... of Vanguard"); not-advice/not-fiduciary with carve-ins "except as expressly identified otherwise by Vanguard"
vendor: unnamed "third-party provided AI models"
files: mastersheet-sources/investing/vanguard/vanguard_terms-conditions_RAW.html (+ .txt)

company: The Vanguard Group, Inc.
document_title: Vanguard Terms & Conditions of Use (Online Terms; incorporated by both AI instruments) [added 2026-10-07 on full-read re-coding]
document_type: t2-site-terms
url: https://investor.vanguard.com/terms-conditions
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no
ai_vector: n/a (general site terms; AI-silent)
fetch_depth: full-fetch
clause_codes_present: B2, B3 (decisions based on Materials are the user's sole responsibility), B6, B7, B8, B10 (perpetual licence over User Content, into which both AI instruments route Input) - all generic
files: mastersheet-sources/investing/vanguard/vanguard_terms-conditions_RAW.html (+ .txt)

## Coding-relevant extract

**Scope and assent.** Users must accept the Terms to use the Voicebot; use is acceptance of these
terms plus the Online Terms and Privacy Notice. Access only for authorized volunteers after voice
verification. Explicit test framing: the PoC evaluates "accuracy, latency and other factors".

**Key provisions (paraphrased).** The Voicebot uses generative AI; the user is solely responsible
for Input and must not give account numbers or SSNs; Output will include the user's non-public
personal information and third-party AI providers may receive Inputs and Outputs; Output cannot
be reviewed before the user receives it and has not been checked for accuracy or timeliness
(B6). Decisions based on Output are the user's own, and Vanguard assumes no responsibility for
consequences, including errors or omissions (B3/B2). No legal, tax, financial or investment
advice; Vanguard is not a fiduciary by providing the Voicebot. Output is not an offer to buy or
sell securities, and Output's assertions "do not represent the opinions, beliefs or assertions of
Vanguard", which will not be liable for reliance on them (B1-analog, anti-attribution).

## Coder note
1. **Locus 1 (dedicated standalone AI terms), brand/function-named.** Third anti-attribution
   clause in the v2 collection (after Ulta and A&F) and the most explicit: it denies that the
   AI's statements are Vanguard's assertions at all.
2. **The "not a fiduciary" clause is sector-specific and new to the codebook:** a regulated
   adviser contracting out of fiduciary status for AI output. Flag for the doctrinal section
   (whether such a waiver is effective under the Advisers Act is doubtful).
3. **Assent is strong** (opt-in volunteers, explicit acceptance), unlike most voice deployments.
4. **Scope caveat:** a PoC limited to volunteers. Live to real customers, so it counts as launched
   under the protocol, but the population is tiny. The workplace bots (70+) are the broader
   deployment and are governed by separate plan documents not fetched.
5. **Vintage:** written at launch (Feb 2026).
6. **Added on full-read re-coding (2026-10-07):** the same page also carries a broader
   **Generative AI Features Terms of Use (eff. 2026-07-08)** covering all GenAI chat, voice and
   public-facing "embedded GenAI agents" - a later, more general instrument that reaches the
   voicebot (voice-based interface) and adds an "AI Features Risks" section (inaccuracy,
   third-party model oversight, data-poisoning and adversarial-attack risk) and carve-ins
   ("except as expressly identified otherwise by Vanguard") that reserve room for AI-delivered
   advice. Both AI instruments route user Input into the Online Terms' perpetual User Content
   licence (B10). Registered as VGD-03 (GenAI Features Terms) and VGD-04 (Online Terms).

---

<a name="wayfair"></a>
## Wayfair - customer-service Virtual Assistant and Muse (gen-AI inspiration) - collected 2026-10-06

**AI feature.** (1) An NLP Virtual Assistant for customer service (returns, delivery status,
damage reports), launched via A/B test in 2022 and built in-house. (2) Muse, a generative-AI room
inspiration tool. Roster: NAICS 4491, rank 1, main sample.

company: Wayfair Inc.
document_title: Terms of Use ("Chatbots and Use of Generative AI" section)
document_type: t1-governing-terms
url: https://www.wayfair.com/terms/
retrieved: 2026-10-06
effective_or_revised: Terms of Use Last Updated 28 January 2026 (stated)
names_ai_feature: by category ("AI Features", "Chatbots", "Generative AI"); Muse and the Virtual Assistant not named
ai_vector: chat (service) + generative content
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI section + textContent SHA-256 (storefront shell to scripts)
clause_codes_present: B1-analog (AI-specific: Output views "should not be attributed to Wayfair"), B4 (AI-specific, pricing-explicit: review all Outputs "including pricing information" before use), B6 (AI-specific: inaccurate/out-of-date; AS-IS; no warranties), B2 (AI-specific: no liability for "any inaccurate information generated by the AI Features"), B8 (AI-specific: Output may rest on suppliers, reviews, third-party AI models; not responsible for third-party services), B10 (AI-specific: Inputs, purchase history, promotion use and personal information used to improve AI and the underlying model; Inputs not confidential), B9 (AI-specific: no harmful or deceptive use; no copying AI features)
vendor: unnamed "third-party AI models" and service providers
files: mastersheet-sources/furniture/wayfair/wayfair_terms-of-use_CAPTURE-NOTE.md

company: Wayfair Inc.
document_title: Building Wayfair's First Virtual Assistant (tech blog)
document_type: t6-marketing
url: https://www.aboutwayfair.com/careers/tech-blog/building-wayfairs-first-virtual-assistant-automating-customer-service-by-text-based-intent-prediction
retrieved: 2026-10-06
effective_or_revised: September 1, 2022
fetch_depth: full-fetch
files: mastersheet-sources/furniture/wayfair/wayfair_TYPE6_va-blog_RAW.html (+ .txt)

## Coding-relevant extract

AI Features are "part of the Sites", so all site terms apply. Output may be inaccurate, incomplete,
out of date or unfit; AI may misunderstand Input; Wayfair takes no responsibility and disclaims
all warranties in Output (B6). Users must review all Output, **including pricing information**,
before relying on it (B4, aimed squarely at the *Moffatt* risk). Output may draw on third-party
sources and AI models (B8), and its views "should not be attributed to Wayfair" (B1-analog).
Wayfair is not liable for inaccurate AI-generated information (B2). Inputs, purchase history,
promotion use and personal data may train the AI and the underlying model (B10).

## Coder note
1. **Locus 2 (dedicated AI section inside general terms).** Fourth anti-attribution clause (Ulta,
   A&F, Vanguard, Wayfair) and the first to name pricing explicitly in the verification duty. An
   emerging drafting pattern in 2026 retail terms: deny attribution plus a verify-the-price duty,
   rather than a B1 non-honoring clause.
2. **Vintage:** Jan 2026, long after the 2022 VA and the 2023 Muse; revised for generative AI
   generally.
3. **Gaps:** in-chat microcopy not captured; privacy policy (30 Apr 2026, on the same page) not
   separately coded for B11.

---

<a name="williamssonoma"></a>
## Williams-Sonoma, Inc. - Olive / Otto AI assistants and Agentforce service agents - collected 2026-10-06

**AI feature.** Agentforce AI support agents across all brand websites (Williams Sonoma, Pottery
Barn, West Elm, ...), announced 2025-10-14 at Dreamforce, to give "accurate, personalized
responses without human intervention"; and "Olive", a sous-chef agent that plans menus, gives
recipes and builds shopping lists (Otto is a sibling assistant per screening). Roster: NAICS 4491,
rank 2, main sample.

company: Williams-Sonoma, Inc.
document_title: Legal Statement (site Terms of Use)
document_type: t1-governing-terms
url: https://www.williams-sonoma.com/customer-service/legal-statement.html
retrieved: 2026-10-06
effective_or_revised: Last Updated April 22, 2026 (stated)
names_ai_feature: no - AI appears only in restrictions on users (no training ML/AI models on site content)
ai_vector: generative + agentic (support resolution, shopping lists)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B9 (AI-specific, user-directed: no use of site data to train AI models), B1-soft (generic: may correct pricing errors even after order submission; customer offered cancellation or return), B6/B2/B3 (generic: AS IS; sole risk; no liability of any kind)
vendor: Salesforce (Agentforce), per the Salesforce release only
files: mastersheet-sources/furniture/williams-sonoma/wsi_legal-statement_CAPTURE-NOTE.md

company: Salesforce (about Williams-Sonoma)
document_title: Williams-Sonoma, Inc. Deploys Salesforce Agentforce 360 Across Its Brand Portfolio
document_type: t6-marketing (vendor release; joint announcement with WSI quotes)
url: https://www.salesforce.com/news/press-releases/2025/10/14/williams-sonoma-inc-agentforce-customer-support/
retrieved: 2026-10-06
effective_or_revised: October 14, 2025
fetch_depth: full-fetch
files: mastersheet-sources/furniture/williams-sonoma/wsi_TYPE6_agentforce-release_RAW.html (+ .txt)

## Coding-relevant extract

The April 2026 Legal Statement has no language about Williams-Sonoma's own AI agents. AI appears
only where users are forbidden to mine site content to build or train AI models. Generic clauses:
pricing and description errors may be corrected even after an order is submitted, with the
customer offered cancellation or return (a softer B1 than most retailers); site AS IS, use at sole
risk, no liability of any kind.

## Coder note
1. **Locus 5 for the deployed AI (the AI language is user-directed B9).** Same pattern as Anthem
   and eBay: the 2026 revision added AI restrictions on customers, not disclaimers for the firm's
   own agents.
2. **Vintage:** revised April 2026, six months after the Agentforce rollout; still silent on it.
3. **Say-do:** release promises "accurate, personalized responses without human intervention".
4. **Gaps:** privacy policy not captured; Olive liveness by cutoff ("will soon be able to" in Oct
   2025) to confirm; in-chat microcopy.

---

<a name="bobs"></a>
## Bob's Discount Furniture - BobBot conversational assistant - collected 2026-10-06

**AI feature.** BobBot, a post-order chatbot (web chat and SMS) that schedules and reschedules
deliveries automatically and hands off to agents, built on Quiq (the Quiq chat iframe is present
on mybobs.com). Agentic (delivery scheduling). Roster: NAICS 4491, rank 6, main sample
(private; S-1 filed 2026).

company: Bob's Discount Furniture, Inc.
document_title: Terms of Use (mybobs.com/terms-of-use)
document_type: t1-governing-terms
url: https://www.mybobs.com/terms-of-use
retrieved: attempted 2026-10-06
fetch_depth: referenced-not-located. Scripted fetch timed out (twice); the built-in browser loaded the page shell ("Home / Terms Of Use", 208 chars) but the terms body never rendered after 15 seconds. The page does embed the Quiq chat widget (bobs.quiq-api.com).
files: none

## Coding-relevant extract

None. Existence of the terms is confirmed (page and site-wide acceptance banner); content not
retrieved.

## Coder note
1. **Not coded.** No inference about presence or absence of AI language.
2. **Retrieval routes:** the S-1 (sec.gov, 2026) describes BobBot and may help with launch date;
   the terms may load in the user's own browser.

---

<a name="southwest"></a>
## Southwest Airlines - Southwest AI Assistant (Salesforce Agentforce) - collected 2026-10-06

**AI feature.** An always-on Agentforce (LLM) assistant in the Help Center on southwest.com and the
app, rolled out in phases from November 2025. It answers questions on "baggage limits, policies,
refunds, reservations, or the Rapid Rewards" program and brings in human reps when needed;
Southwest reports it resolves nearly half of eligible inquiries without a human. Roster: NAICS
4811, rank 4, main sample. This is the *Moffatt v. Air Canada* setting almost exactly: an
airline's website chatbot answering refund-policy questions.

company: Southwest Airlines Co.
document_title: Southwest.com Terms and Conditions
document_type: t1-governing-terms (website)
url: https://www.southwest.com/html/about-southwest/terms-and-conditions/index.html
retrieved: 2026-10-06
effective_or_revised: Last modified April 4, 2017 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative (LLM chat)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/airlines/southwest/southwest_terms-and-conditions_RAW.html (+ .txt)

company: Southwest Airlines Co.
document_title: Contract of Carriage (passenger)
document_type: contract-of-carriage
url: https://www.southwest.com/assets/pdfs/corporate-commitments/contract-of-carriage.pdf
retrieved: 2026-10-06
effective_or_revised: Effective Date 09/24/2026 (stated) - after the cutoff
names_ai_feature: no - zero AI-keyword hits
fetch_depth: full-fetch (PDF)
clause_codes_present: generic carrier limitations only; nothing on information given by automated agents
files: mastersheet-sources/airlines/southwest/southwest_contract-of-carriage.pdf (+ .txt)

company: Salesforce (about Southwest)
document_title: Southwest Airlines customer story: agentic self-service
document_type: t6-marketing (vendor case study with Southwest staff quotes)
url: https://www.salesforce.com/customer-stories/southwest-airlines/agentic-self-service/
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/airlines/southwest/southwest_TYPE6_agentforce-story_RAW.html (+ .txt)

## Coding-relevant extract

Neither the 2017 website terms nor the September 2026 Contract of Carriage mentions AI, the
assistant, or the status of information it gives. Only generic AS-IS and carrier-liability
limits apply. Southwest staff in the case study describe the rollout as its "first agentic AI
rollout" that "had to be perfect for customers".

## Coder note
1. **Locus 5 (absent) for the closest Moffatt analogue in the v2 sample.** Compare the pilot
   corpus: Delta (dedicated AI Terms), American (s.15 AI Tools), Frontier (AI clause), United
   (silent). Southwest joins United on the silent side.
2. **Strong vintage finding:** the Contract of Carriage was revised 2026-09-24, ten months after
   the AI launch, with nothing added. (After cutoff; the pre-cutoff COC should be retrieved for the
   headline count, though silence there is near-certain given silence now.)
3. **Gaps:** in-chat microcopy not captured; privacy notice not fetched; no first-party press
   release located (vendor case study used).

---

<a name="bestbuy"></a>
## Best Buy - generative-AI virtual assistant (web, app, phone) - collected 2026-10-06

**AI feature.** A gen-AI virtual assistant built with Google Cloud and Accenture, launched late
summer 2024 for US customers on BestBuy.com, the app and the support phone line. It troubleshoots
products, **changes delivery and scheduling**, and manages Geek Squad subscriptions and My Best Buy
memberships (agentic). Roster: NAICS 4492, rank 1, supplementary set.

company: Best Buy Co., Inc.
document_title: BestBuy.com Terms and Conditions
document_type: t1-governing-terms
url: https://www.bestbuy.com/site/help-topics/terms-and-conditions/pcmcat204400050067.c?id=pcmcat204400050067
retrieved: 2026-10-06
effective_or_revised: Last Updated September 25, 2026 (stated) - after the 2026-06-30 cutoff
names_ai_feature: by category ("artificial intelligence software ('AI')", "chat-based or conversation-based technologies")
ai_vector: generative chat + voice; agentic (delivery changes, subscriptions)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI passages + innerText SHA-256 (scripted fetch timed out)
clause_codes_present: B1 (AI-specific, the sharpest form: any AI/chat statement about Best Buy's terms, policies or practices that deviates or adds terms "shall be void and non-binding" and the actual terms control; plus generic: may cancel misstated or mispriced orders), B6 (AI-specific: AI content may not always be accurate; no warranty), B2 (AI-specific: no liability for indirect/consequential damages from "any inaccurate information generated by AI"), B5 (AI-specific, both directions: users' Digital Agents must self-identify and follow access rules, and purchases by a user's agent are deemed the user's own; Best Buy not responsible for agent errors)
vendor: none named in terms (Google Cloud, Accenture per release)
files: mastersheet-sources/electronics/best-buy/bestbuy_terms-and-conditions_CAPTURE-NOTE.md

company: Best Buy Co., Inc.
document_title: How Best Buy is using generative AI to create better customer support experiences
document_type: t6-marketing
url: https://corporate.bestbuy.com/2024/generative-ai-customer-support/
retrieved: 2026-10-06
effective_or_revised: April 9, 2024
fetch_depth: full-fetch
files: mastersheet-sources/electronics/best-buy/bestbuy_TYPE6_genai-support_RAW.html (+ .txt)

## Coding-relevant extract

**The anti-*Moffatt* clause.** Chat-delivered information may be AI-generated and "may not always
be accurate". Any AI or chat-based statement about Best Buy's terms, policies or practices is a
convenience only, and "any deviation, contradiction, additional, or different term provided shall
be void and non-binding", with the real terms, policy or practice controlling. This is the
*Moffatt* fact pattern (a chatbot misstating a refund or bereavement policy) answered in advance,
in the contract: the AI's version of the policy is void.

**Liability.** The damages exclusion expressly names "inaccurate information generated by AI".
Mispriced or misstated offers may be cancelled (generic B1).

**Digital Agents.** A full regime for customers' AI agents: identification string, single
logged-in customer, no human mimicry, no CAPTCHA defeat; purchases by a user's agent are the
user's own acts; Best Buy is not responsible for agent errors.

## Coder note
1. **Locus 2, with the corpus's first AI-specific B1.** In the pilot corpus the only B1 was
   Walmart's (AI pricing "does not constitute an offer"). Best Buy's is broader: it voids any
   AI-stated term or policy.
2. **Version problem (critical for the headline count).** This version is dated 2026-09-25,
   after the cutoff. Whether the void-and-non-binding sentence existed by 2026-06-30 is unknown.
   Retrieve the prior version before counting it; if it is new, it is still a powerful post-cutoff
   illustration of where drafting is heading.
3. **Doctrinal note for the paper:** whether a buried browsewrap clause can defeat a negligent
   misrepresentation claim like *Moffatt*'s is the open question (Moffatt was decided in tort; the
   tribunal said the firm is responsible for all information on its website, including the
   chatbot's).
4. **Assent:** browsewrap on the site; the phone channel has none.

---

<a name="newegg"></a>
## Newegg Commerce - AI Mode (newegg.com/ai) - collected 2026-10-06

**AI feature.** "AI Mode", a conversational AI shopping assistant for tech products at
newegg.com/ai (full launch 2026-06-26, inside the cutoff), plus an on-page assistant; earlier
ChatGPT-powered features since 2023. The landing screen greets with a named persona
("Hey, Celeste SM here") and deal prompts ("RTX 5000 series deals"). Roster: NAICS 4492, rank 5,
supplementary set.

company: Newegg Commerce, Inc.
document_title: Policy Agreement (Newegg Terms)
document_type: t1-governing-terms
url: https://kb.newegg.com/knowledge-base/policy-agreement/
retrieved: 2026-10-06
effective_or_revised: Updated Jul 21, 2026 (stated) - after the cutoff and 25 days after AI Mode launched
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative chat (shopping)
fetch_depth: full-fetch
clause_codes_present: B1 (generic: may accept, decline, cancel or limit any order for any reason after receipt), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/electronics/newegg/newegg_policy-agreement_RAW.html (+ .txt)

company: Newegg Commerce, Inc.
document_title: Newegg AI Mode landing screen
document_type: t4-in-product-microcopy
url: https://www.newegg.com/ai
retrieved: 2026-10-06 (browser read; 349 chars rendered; innerText SHA-256 0ef5dcdba0e5daac9bea37ea54d6c3c5299a82e506a379b340b6553347dd2b07)
names_ai_feature: yes ("AI Mode"; persona "Celeste")
fetch_depth: full-fetch (browser read; static shell from scripts is 56 chars, not kept)
clause_codes_present: none - no accuracy, verification or terms notice visible before a chat starts
files: none (recorded here)

## Coding-relevant extract

The July 2026 Policy Agreement does not mention AI, AI Mode or chat. Generic: Newegg may decline or
cancel any order after receipt for any reason (B1, generic), AS IS, damages limits. The AI Mode
entry screen shows a persona greeting, suggested prompts (including deal-seeking prompts) and a
sign-in nudge, with no "AI can make mistakes"-type notice and no link to terms.

## Coder note
1. **Locus 5 (absent) with a strong vintage finding:** a post-launch revision (21 days after the
   cutoff) still added nothing about AI. The pre-cutoff version would be older and presumably also
   silent.
2. **Persona + deal prompts + no disclaimer** is about the riskiest configuration for *Moffatt*:
   the AI is invited to discuss deals, with no qualification at all.
3. **Gaps:** in-chat microcopy after a conversation starts not captured (would require
   interaction); privacy policy not fetched.

---

<a name="dicks"></a>
## DICK'S Sporting Goods - Coach by DICK'S (agentic AI conversational coach) - collected 2026-10-06

**AI feature.** Coach by DICK'S, an "agentic AI-powered conversational Coach" (built on Adobe
Brand Concierge per screening), announced 2026-05-22 with rollout from June 2026: sport guidance,
gear recommendations, shopping help. Roster: NAICS 4591, rank 1, supplementary set.

company: DICK'S Sporting Goods, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.dickssportinggoods.com/s/policy/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Updated, posted and effective as of March 19, 2024 (stated)
names_ai_feature: no - zero AI hits
ai_vector: generative + agentic (shopping)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B1 (generic: may cancel orders on pricing error or discrepancy), B6 (generic: information may be inaccurate; AS IS; own risk), B2 (generic); human-agent no-authority clause (generic: employees cannot modify the Terms and are not acting as agents if they offer to)
files: mastersheet-sources/sporting-goods/dicks/dicks_terms-of-use_CAPTURE-NOTE.md

company: DICK'S Sporting Goods, Inc.
document_title: DICK'S Sporting Goods Introduces Coach by DICK'S, an Agentic AI Conversational Experience ...
document_type: t6-marketing
url: https://www.prnewswire.com/news-releases/dicks-sporting-goods-introduces-coach-by-dicks-an-agentic-ai-conversational-experience-to-support-athletes-at-every-stage-302780351.html
retrieved: 2026-10-06
effective_or_revised: May 22, 2026
fetch_depth: full-fetch
files: mastersheet-sources/sporting-goods/dicks/dicks_TYPE6_coach-release_RAW.html (+ .txt)

## Coding-relevant extract

No AI language. Two generic clauses matter for an AI coach: (1) s.7, site information may be
inaccurate, and orders may be cancelled for pricing errors (B1, generic); (2) s.1, employees
cannot modify the Terms orally or otherwise, and an employee who offers to "is not acting as an
agent for us or speaking on our behalf". That is an anti-apparent-authority clause written for
humans. It does not mention automated agents, so whether it reaches Coach is a question of
interpretation.

## Coder note
1. **Locus 5 for AI; but note the human no-authority clause.** Useful contrast for the paper:
   firms already disclaim human employees' authority to vary terms; only a few (Ulta, Best Buy)
   have extended that logic to AI. DICK'S has the human version only.
2. **Vintage:** terms March 2024; Coach launched May/June 2026; not revised.
3. **Gaps:** in-product microcopy for Coach; privacy policy not captured; rollout timing relative
   to the June 30 cutoff (rollout "starting June 2026") to confirm.

---

<a name="michaels"></a>
## Michaels Companies - Ask Mike (Gemini Enterprise for CX) - collected 2026-10-06

**AI feature.** Ask Mike, an AI shopping assistant on Michaels.com built with Google Cloud's Gemini
Enterprise for Customer Experience: shoppers describe a creative project and get product guidance
and recommendations "from inspiration to purchase". Released May 2026 (the July 21, 2026 release
says "Since its release in May, Ask Mike has generated strong engagement"), so it was live before the
cutoff. Roster: NAICS 4591, rank 4, supplementary set (private).

**Eligibility note.** An earlier draft of this entry flagged Ask Mike as post-cutoff based on the
July 21 release date; the same release confirms a May 2026 release. Eligible.

company: The Michaels Companies, Inc.
document_title: Terms & Conditions (combined page with Privacy Statement)
document_type: t1-governing-terms
url: https://www.michaels.com/lp/privacy-policy-terms-and-conditions
retrieved: 2026-10-06
effective_or_revised: Terms & Conditions Effective Date March 2025; Privacy Statement Last Updated December 31, 2025 (stated)
names_ai_feature: no - zero AI hits in either document
ai_vector: generative chat (shopping guidance)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (JS shell to scripts)
clause_codes_present: B1 (generic: order acknowledgement is not acceptance or price confirmation; items may be mispriced), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/sporting-goods/michaels/michaels_terms-privacy_CAPTURE-NOTE.md

company: The Michaels Companies, Inc.
document_title: Michaels Unveils 'Ask Mike' AI Assistant, Built With Google Cloud's Gemini Enterprise for Customer Experience
document_type: t6-marketing
url: https://www.michaelspressroom.com/news/detail/5064/michaels-unveils-ask-mike-ai-assistant-built-with
retrieved: 2026-10-06
effective_or_revised: July 21, 2026
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/sporting-goods/michaels/michaels_TYPE6_ask-mike-release_RAW.html (+ .txt)

## Coding-relevant extract

Both documents are AI-silent. Generic B1: acknowledging an order does not confirm price or
availability, and items may be mispriced; generic AS-IS and damages terms.

## Coder note
1. **Locus 5 (absent; generic B1 only).**
2. **Vintage:** T&C March 2025 and privacy December 2025, both before the May 2026 launch.
3. **Gaps:** in-product microcopy not captured.

---

<a name="intuit"></a>
## Intuit - Intuit Assist (TurboTax, Credit Karma) - collected 2026-10-06

**AI feature.** Intuit Assist, a generative-AI financial assistant across TurboTax, Credit Karma,
QuickBooks and Mailchimp (consumer GA January 2024). In TurboTax it builds a personalized tax
checklist, runs "realtime checks for accuracy", finds deductions and credits, and answers tax
questions as a "personalized assistant"; some Digital Assistants "perform functions or operations
on your behalf" (agentic). Roster: NAICS 5132, rank 1, supplementary set.

company: Intuit Inc.
document_title: Intuit Terms of Service for TurboTax Online Tax Preparation Services - Tax Year 2025 (General Terms, Section A, "Digital Assistants")
document_type: t1-governing-terms
url: https://www.intuit.com/legal/terms/en-us/turbotax/online-license/
retrieved: 2026-10-06
effective_or_revised: Version 02122026 (Feb 12, 2026), Tax Year 2025 (stated in document header)
names_ai_feature: by category ("Digital Assistants": "digital assistants, agents, avatars, chatbots ... powered by artificial intelligence"); "Intuit Assist" not named in the terms
ai_vector: generative chat + agentic functions; decisional-adjacent (deduction finding)
fetch_depth: full-fetch
clause_codes_present: B3 (AI-specific, strong: "solely responsible for actions or omissions caused by or resulting from your use or engagement with Digital Assistants"), B6 (AI-specific: may generate outputs that are inaccurate or inappropriate to your situation), B5 (AI-specific: Digital Assistants may act on your behalf; review their functionality and permissions), B10 (AI-specific: Content given to Digital Assistants used to personalize and to improve the Platform and AI), B9 (AI-specific: no training AI/ML on Platform-derived information), B6/B2 (generic AS IS, no accuracy warranty for the Platform); Accurate Calculation Guarantee (s.5.1) for calculation errors arising through the in-product interview
files: mastersheet-sources/software/intuit/turbotax_online-license-terms_RAW.html (+ .txt)

company: Intuit Inc.
document_title: What is Intuit Assist? (TurboTax Support)
document_type: t4-in-product-microcopy (help article for the feature)
url: https://ttlc.intuit.com/turbotax-support/en-us/help-article/data-privacy/intuit-assist/L8AA2pNTy_US_en_US
retrieved: 2026-10-06
effective_or_revised: Updated January 22, 2026
names_ai_feature: yes
fetch_depth: full-fetch
files: mastersheet-sources/software/intuit/turbotax_intuit-assist-help_RAW.html (+ .txt)

company: Intuit Inc.
document_title: Intuit Assist product page
document_type: t6-marketing
url: https://www.intuit.com/intuitassist/
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/software/intuit/intuit_TYPE6_intuit-assist-page_RAW.html (+ .txt)

## Coding-relevant extract

**"Digital Assistants."** Intuit may use AI digital assistants, agents, avatars and chatbots;
"these technologies are evolving and may have limitations". Their output may not be unique; Content
given to them is used to personalize and improve the Platform and AI (B10). Some may act on the
user's behalf, so users should review functionality and permissions (B5). Chatbots may generate
outputs "inaccurate or inappropriate to your situation" (B6), and the user is "solely responsible
for actions or omissions caused by or resulting from" using them (B3). Separately, users may not
train AI or ML models on Platform data (B9).

**The guarantee tension.** s.5.1 promises to pay IRS/state penalties and interest caused by
TurboTax calculation errors on returns prepared through the "in-product TurboTax interview
experience and guidance". The help page markets AI "realtime checks for accuracy" inside that same
experience. The Digital Assistants clause puts responsibility for AI-driven actions or omissions on
the user, while the guarantee keeps calculation risk with Intuit. Where an AI answer leads to a
wrong entry (not a wrong calculation), the AI clause, not the guarantee, governs.

## Coder note
1. **Locus 2 (dedicated AI section inside general terms).** Category-named.
2. **Notable interaction:** an express accuracy guarantee coexisting with an AI sole-responsibility
   clause. Good illustration for the paper of how firms ring-fence AI output from existing service
   promises.
3. **Vintage:** Feb 2026 version, after the 2024 GA; revised with AI language.
4. **Gaps:** Credit Karma's own terms not fetched (Intuit Assist also runs there); privacy
   statement not fetched.

---

<a name="ea"></a>
## Electronic Arts - EA Help AI chat - collected 2026-10-06

**AI feature.** An AI chat in EA Help (signed-in "Contact Us" flow) that takes the player's problem
description, offers possible solutions or FAQs, and only then exposes Live Chat with a human advisor.
It replaced the earlier contact form (player reports on EA Forums; screening evidence via a June 2026
archived help page). Mostly intake and triage; low transactional stakes but it gates access to human
support. Roster: NAICS 5132, rank 2, supplementary set.

company: Electronic Arts Inc.
document_title: EA User Agreement
document_type: t1-governing-terms
url: https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/
retrieved: 2026-10-06
effective_or_revised: Last Updated May 14, 2026 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: chat (support intake)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/software/electronic-arts/ea_user-agreement_RAW.html (+ .txt)

company: Electronic Arts (help site)
document_title: EA Help home page
document_type: t4-in-product-microcopy
url: https://help.ea.com/en/
retrieved: 2026-10-06 (scripted fetch and browser read; no AI text on the public page; bot is behind login)
fetch_depth: referenced-not-located (in-flow microcopy behind sign-in)
files: none

## Coding-relevant extract

The May 2026 User Agreement contains no AI language; only generic AS-IS and damages terms. The
public EA Help page shows no AI notice; the bot appears after sign-in.

## Coder note
1. **Locus 5 (absent).** Recently revised (May 2026) and silent.
2. **Evidence tier:** existence of the AI chat rests on player reports and an archived help page,
   not a first-party announcement. Acceptable under the protocol's evidence rules only if the
   archived page is first-party (it is: help.ea.com); flag as such.
3. **Gaps:** in-flow chat microcopy (login required); EA privacy and cookie policy not fetched.

---

<a name="roblox"></a>
## Roblox - Roblox Assistant, AI chat rephrasing, voice translation - collected 2026-10-06

**AI feature.** Roblox Assistant (Studio; agentic build/test since April 2026) for creators; AI
chat rephrasing of user messages (March 2026); real-time voice translation; AI moderation of voice
chat. Many users are minors. Roster: NAICS 5132, rank 4, supplementary set. Note: the Assistant is
a creator tool; the consumer-facing AI for ordinary players is mainly rephrasing, translation and
moderation (AI acting on their communications).

company: Roblox Corporation
document_title: Roblox Terms of Use ("AI Features" section)
document_type: t1-governing-terms
url: https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use
retrieved: 2026-10-06
effective_or_revised: Effective Date November 1, 2026 (stated) - future-dated version served on the page; after the cutoff
names_ai_feature: by category ("AI Features", "AI Tools for Creators")
ai_vector: generative (creator tools) + AI mediation of user chat and voice
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI section + innerText SHA-256 (scripted fetch timed out)
clause_codes_present: B3 (AI-specific: "You, not Roblox, are responsible for your use and interactions with AI Features ... and your use of Output"), B10 (AI-specific: perpetual licence to use Prompts, Outputs and interaction data incl. model training; UGC licence incl. ML training), B9 (AI-specific: no passing Output off as human; no stripping provenance tags; no using Virtual Content to train AI), B6 generic only (no AI-specific accuracy sentence found)
files: mastersheet-sources/software/roblox/roblox_terms-of-use_CAPTURE-NOTE.md

## Coding-relevant extract

The AI Features section defines optional AI features and creation tools, makes the user (not
Roblox) responsible for Prompts and Output (B3), grants Roblox a perpetual licence to use Prompts,
Outputs and interaction data, including for model training (B10), and bans deceptive use, passing
Output off as human, and removing provenance tags (B9). There is no AI-specific statement that
Output may be inaccurate. The terms also disclose AI moderation of voice chat.

## Coder note
1. **Locus 2 (dedicated AI section), responsibility-shift without accuracy disclaimer.** Unusual
   combination.
2. **Version problem:** captured version effective 2026-11-01. Retrieve the version in force at
   2026-06-30.
3. **Scope question for the screen:** is AI chat rephrasing "AI interacting with the consumer"? It
   rewrites the user's own messages (arguably acts on their behalf). Screen accepted Roblox; flag.
4. **Gaps:** Creator Terms (AI Tools section) not fetched; privacy policy not fetched.

---

<a name="gendigital"></a>
## Gen Digital - Norton Genie (AI scam-detection assistant) - collected 2026-10-06

**AI feature.** Norton Genie (since July 2023), an AI assistant that checks texts, emails, images,
links and (early access) YouTube videos for scams and gives "real-time tips"; built into Norton 360
plans since August 2025. Also Genie inside Norton Money (financial Q&A) and an OpenAI-powered "Smart
Chat" in Norton Private Browser. Stakes: a missed scam leads to direct financial loss. Roster: NAICS
5132, rank 5, supplementary set.

company: Gen Digital Inc.
document_title: Gen License and Services Agreement (Americas, English)
document_type: t1-governing-terms
url: https://us.norton.com/legal/lsa?lsar=americas&lsal=en
retrieved: 2026-10-06
effective_or_revised: document reference "GEN_LSA_January_2026_AMS" (January 2026)
names_ai_feature: yes - by brand ("Genie", "Virtual Advisor", "Smart Chat") in specific product clauses
ai_vector: generative chat (Genie, Smart Chat) + detection AI
fetch_depth: full-fetch
clause_codes_present: not-advice (AI-specific: Norton Money Genie responses are general, may be incomplete, not legal/tax/investment/financial advice; AI features incl. Genie and Virtual Advisor are not advice), not-fiduciary (AI-specific), B8 (AI-specific: Smart Chat governed by OpenAI's terms of use), B6-partial (AI-specific: Genie responses "may not constitute a comprehensive or complete statement"), B2 (generic, with stolen-identity insurance carve-out); no clause found on the accuracy of Genie's scam verdicts
files: mastersheet-sources/software/gen-digital/gen_lsa_RAW.html (+ .txt)

company: Gen Digital Inc.
document_title: Norton AI-powered Scam Protection / Genie product page
document_type: t6-marketing
url: https://us.norton.com/products/genie-scam-detector
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/software/gen-digital/norton_TYPE6_genie-page_RAW.html (+ .txt)

## Coding-relevant extract

The January 2026 LSA addresses Genie only where it gives financial information (Norton Money):
responses are general, may be incomplete, are not advice, and Gen is not a fiduciary by virtue of
reliance on them. Section 16 says AI features "including Genie and/or the Virtual Advisor" are not
legal, tax or financial advice. Smart Chat use is "subject to OpenAI's terms of use". A keyword search
found no clause on Genie's scam verdicts (no "may not detect all scams"-type sentence), the core
consumer use. Marketing claims "Advanced AI outsmarts online scams" and "up to 10x better scam
detection" (Norton internal testing).

## Coder note
1. **Locus 2-partial (brand-named AI clauses for financial Q&A only).** The highest-stakes AI
   output (telling a user a message is safe) is unaddressed in the captured agreement. Flag for
   checking product-specific terms or the help-center Genie FAQ.
2. **Vendor-terms pass-through:** Smart Chat binds the consumer to OpenAI's terms. This is the
   reverse of the B2B-vendor rule (here the deploying firm expressly imports a vendor's
   consumer terms). New codebook observation.
3. **Not-fiduciary language** recurs (Vanguard; now Gen for Norton Money).
4. **Gaps:** privacy notice; Genie in-app microcopy; LSA effective date beyond the document code.

---

<a name="campingworld"></a>
## Camping World Holdings - "Arvee" virtual agent (IBM watsonx Assistant) - collected 2026-10-06

**AI feature.** Arvee, a chat virtual agent on Camping World sites (IBM watsonx Assistant per
screening; by 2023), reachable via the "Chat" bubble alongside live agents. RV sales and service
questions. Roster: NAICS 4412, rank 1, supplementary set.

company: Camping World Holdings, Inc. (CWGS / FreedomRoads, LLC)
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.campingworld.com/helpcenter-ourpolicies/termsOfUse.html
retrieved: 2026-10-06
effective_or_revised: Last Updated 6/24/2025 (stated)
names_ai_feature: no - "chat area" appears only in the definition of "Public Forum"
ai_vector: chat (sales/service)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/rv-boat-dealers/camping-world/cw_terms-of-use_RAW.html (+ .txt)

company: Camping World Holdings, Inc.
document_title: AI Info - Official Information About Camping World ("Hey AI, Learn About Us")
document_type: t6-marketing (structured page addressed to LLMs and AI systems)
url: https://rv.campingworld.com/ai-information
retrieved: 2026-10-06
effective_or_revised: Last Updated April 8, 2026 (stated)
names_ai_feature: yes (says customers can chat with "Arvee" or a live agent)
fetch_depth: full-fetch
files: mastersheet-sources/rv-boat-dealers/camping-world/cw_ai-information_RAW.html (+ .txt)

## Coding-relevant extract

The June 2025 Terms of Use contain no AI language; "chat area" appears only in the definition of
user-content Public Forums. Generic AS-IS and damages terms only. The firm's only AI-oriented
document is an "AI Info" page meant to make external LLMs describe Camping World accurately ("the
authoritative source of structured information ... for Large Language Models"); it mentions Arvee
only as a support channel.

## Coder note
1. **Locus 5 (absent).**
2. **New observation (out-of-scope genre):** "AI Info" pages written for third-party LLMs (also seen
   at Wynn in screening). The firm worries about how outside AI represents it, not about its own
   AI's statements. Possibly worth a sentence in the paper.
3. **Gaps:** Arvee's in-chat microcopy; privacy policy not fetched; Arvee's generative status.

---

<a name="legalzoom"></a>
## LegalZoom - Doc Assist (GenAI legal-document summarizer) and other AI services - collected 2026-10-06

**AI feature.** Doc Assist, a free generative-AI summarizer for legal documents (overview, clause
summaries, Q&A), beta from 2023-09; also AI Business Name Generator, NAICS code search, expense
categorizer and search summaries. Advisory stakes (a misread contract). Roster: NAICS 5411, rank 2,
supplementary set.

company: LegalZoom.com, Inc.
document_title: AI Additional Terms
document_type: t3-dedicated-ai-doc
url: https://www.legalzoom.com/legal/general-terms/ai-additional-terms
retrieved: 2026-10-06
effective_or_revised: Last updated December 16, 2024 (stated)
names_ai_feature: yes - by brand (Doc Assist, Business Name Generator, NAICS Code Search, LZ Books Expense Categorizer)
ai_vector: generative (summaries, Q&A)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific: "as is"; no promise output is accurate, complete, error-free or fit for use), not-legal-advice (AI-specific), B9 (AI-specific: no harmful, deceptive or infringing use), use restrictions (no highly sensitive data, no minors' data, not for privileged material)
files: mastersheet-sources/legal-services/legalzoom/legalzoom_ai-additional-terms_RAW.html (+ .txt)

company: LegalZoom.com, Inc.
document_title: Terms of Service
document_type: t1-governing-terms
url: https://www.legalzoom.com/legal/general-terms/terms-of-service
retrieved: 2026-10-06
effective_or_revised: Updated September 4, 2026 (stated) - after the cutoff
names_ai_feature: category (s.35: "I acknowledge that LegalZoom may use artificial intelligence technology to provide me products and services")
fetch_depth: full-fetch
clause_codes_present: AI-disclosure acknowledgement (AI-specific, no liability effect), B2 (generic)
files: mastersheet-sources/legal-services/legalzoom/legalzoom_terms-of-service_RAW.html (+ .txt)

company: LegalZoom.com, Inc.
document_title: Terms of Use
document_type: t2-site-terms
url: https://www.legalzoom.com/legal/general-terms/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Updated April 21, 2026 (stated)
names_ai_feature: no (AI only in site navigation)
fetch_depth: full-fetch
clause_codes_present: B6/B2 (generic)
files: mastersheet-sources/legal-services/legalzoom/legalzoom_terms-of-use_RAW.html (+ .txt)

company: LegalZoom.com, Inc.
document_title: Doc Assist page (upload screen and FAQ)
document_type: t4-in-product-microcopy
url: https://www.legalzoom.com/ai/doc-assist
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: clickwrap at the point of use ("I agree to LegalZoom's Terms of Service, Privacy Policy, and AI Additional Terms"), B6 ("results may be incomplete or inaccurate"), not-legal-advice
files: mastersheet-sources/legal-services/legalzoom/legalzoom_doc-assist-page_RAW.html (+ .txt)

## Coding-relevant extract

**AI Additional Terms.** Apply on top of the Terms of Use and Terms of Service to every AI service
named on the site. 18+ only; no harmful, deceptive or infringing content; no highly sensitive or
minors' data. The services use "generative artificial intelligence, which is a new and rapidly
evolving technology"; provided "as is" with no promise of accuracy, completeness or fitness (B6);
not legal advice; not for privileged material.

**Point-of-use assent.** The Doc Assist upload screen shows an "I agree" line covering the AI
Additional Terms, plus microcopy that results "may be incomplete or inaccurate" and are not legal
advice. The Terms of Service (Sept 2026) add a bare acknowledgement that LegalZoom may use AI.

## Coder note
1. **Locus 1 (dedicated standalone AI terms) with clickwrap at the AI interaction.** One of the
   strongest assent mechanisms in the collection.
2. **No B3/B4/B2 AI-specific language:** the AI terms disclaim accuracy and advice but do not shift
   responsibility for actions taken or exclude liability for reliance. Moderate profile.
3. **Vintage:** AI terms Dec 2024 (after the 2023 beta); ToS Sept 2026 added an AI acknowledgement.
4. **Regulatory context:** unauthorized-practice-of-law rules shape the "not legal advice" language.

---

<a name="rocketlawyer"></a>
## Rocket Lawyer - Rocket Copilot (GenAI legal assistant) - collected 2026-10-06

**AI feature.** Rocket Copilot, an AI-powered legal-information assistant (launched 2023-12-21,
built with Google Cloud): contract review, Q&A, entity-name and logo generation. Advisory stakes.
Roster: NAICS 5411, rank 4, supplementary set (private).

company: Rocket Lawyer Incorporated
document_title: Terms of the Rocket Copilot Service
document_type: t3-dedicated-ai-doc
url: https://www.rocketlawyer.com/rocket-copilot-terms
retrieved: 2026-10-06
effective_or_revised: November 19, 2024 (stated)
names_ai_feature: yes - by brand
ai_vector: generative (legal information, contract review, name/logo generation)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim key passages + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B3 (AI-specific: "you assume the responsibility for such errors and inaccuracies"), B4 (AI-specific: user responsible for confirming accuracy, validity and legality; consult a Legal Pro before acting), B6 (AI-specific: experimental; not guaranteed error-free; AS-IS; output not reviewed for legal accuracy), B10 (AI-specific: Content used to develop and improve Copilot; Rocket Lawyer owns derived Metadata), not-legal-advice and no-privilege (AI-specific), IP non-vetting for generated names/logos; conflict clause (Copilot Terms control over General Terms)
files: mastersheet-sources/legal-services/rocket-lawyer/rocketlawyer_copilot-terms_CAPTURE-NOTE.md

company: Rocket Lawyer Incorporated
document_title: General Terms of Service
document_type: t1-governing-terms
url: https://www.rocketlawyer.com/general-terms-of-service
retrieved: 2026-10-06 (browser read; summarized in the CAPTURE-NOTE)
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch (browser read)
clause_codes_present: B6/B2 (generic)
files: mastersheet-sources/legal-services/rocket-lawyer/rocketlawyer_copilot-terms_CAPTURE-NOTE.md

## Coding-relevant extract

Using Copilot binds the user to the Copilot Terms plus the General Terms; the Copilot Terms prevail
on conflict. Copilot gives "legal information", not advice, and its output is not reviewed for
legal accuracy. The user must confirm accuracy, validity and legality and is urged to consult a
Legal Pro before acting (B4). Copilot is "experimental", not guaranteed accurate, AS-IS (B6); "you
assume the responsibility for such errors and inaccuracies" (B3). No privilege, no attorney-client
relationship. Generated names and logos may infringe. Content may be used to improve Copilot (B10).

## Coder note
1. **Locus 1 (dedicated standalone AI terms), brand-named.** With LegalZoom, both legal-services
   firms use dedicated AI terms. Sector pattern, likely driven by unauthorized-practice-of-law risk.
2. **Vintage:** Nov 2024, about a year after launch.
3. **Upsell structure:** the reliance remedy offered is a paid Legal Pro consult. The disclaimer
   doubles as a sales funnel (say-do note).
4. **Gaps:** in-product microcopy; privacy policy.

---

<a name="fidelity"></a>
## Fidelity Investments - Virtual Assistant - collected 2026-10-06

**AI feature.** Fidelity's Virtual Assistant on fidelity.com pages, which uses "advanced technology
and artificial intelligence" to answer FAQs, designed to be "anticipatory and responsive" using
search terms, user replies and **account information on file**. Cannot execute trades. Roster: NAICS
5231, rank 2, supplementary set (private).

company: FMR LLC (Fidelity Investments)
document_title: Fidelity Websites Terms of Use ("Virtual Assistant" section)
document_type: t1-governing-terms
url: https://www.fidelity.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated July 1, 2026 (stated) - one day after the cutoff
names_ai_feature: yes - "Fidelity's Virtual Assistant" (AI stated)
ai_vector: assistive/generative chat (account-aware)
fetch_depth: full-fetch
clause_codes_present: not-advice (AI-specific: responses general, not investment, legal or tax advice), capability limits (AI-specific: not designed to recommend securities; cannot judge suitability; cannot execute trades, so don't try to place orders through it), B10 (AI-specific: interactions recorded, shared with service providers, used for other business purposes; inputs retained and used per Privacy Policy), B6 (generic: accuracy and timeliness of content sections), B2 (generic)
files: mastersheet-sources/investing/fidelity/fidelity_terms-of-use_RAW.html (+ .txt)

company: FMR LLC (Fidelity Investments)
document_title: Customer Service - Contact us and virtual assistant ("Important Information" microcopy)
document_type: t4-in-product-microcopy
url: https://www.fidelity.com/customer-service/contact-us
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: B4 (review results carefully), B6 (Fidelity does not guarantee accuracy of results or suitability), data statement (inputs "not stored or reviewed for any purpose other than to provide search results")
files: mastersheet-sources/investing/fidelity/fidelity_contact-page_RAW.html (+ .txt)

## Coding-relevant extract

**Terms of Use, "Virtual Assistant."** The assistant uses AI and draws on the user's account
information. Interactions may be recorded and shared with service providers or "used for other
business purposes"; inputs may be retained and accessible to Fidelity staff (B10). It does not
recommend securities and cannot judge suitability; users must not try to place trades through it
(it cannot execute them). Responses are general and not investment, legal or tax advice. No AI
accuracy disclaimer in this section; accuracy is handled by the site-wide content clauses.

**Microcopy conflict.** The contact page calls the Virtual Assistant an "automated natural language
search engine", asks users not to enter personal or account information, and says inputs are "not
stored or reviewed for any purpose other than to provide search results". It also says Fidelity
does not guarantee accuracy or suitability and users should review results carefully (B4/B6). That
data statement contradicts the Terms of Use (recorded, shared, other business purposes, uses
account information).

## Coder note
1. **Locus 2 (dedicated section in general terms), brand-named; plus locus 4 microcopy.**
2. **Internal inconsistency between documents** (data use) is a reportable finding: two
   firm-authored descriptions of the same AI that disagree. Possibly a stale help page.
3. **Version:** Terms updated 2026-07-01, one day after the cutoff; the in-force version at
   2026-06-30 may differ. Retrieve the prior version.
4. **Gaps:** privacy policy; launch date of the AI-enabled assistant.

---

<a name="schwab"></a>
## Charles Schwab - Schwab Assistant - collected 2026-10-06

**AI feature.** Schwab Assistant, a virtual agent in the site's Support > Chat (page compliance code
1023, so by October 2023) that answers questions, gives general information and routes users to
pages. The firm's how-to video advises asking short questions "using any key words", which suggests
an intent/keyword bot rather than generative AI. (Schwab's "Charley" gen-AI launched October 2026,
after the cutoff, and is excluded.) Roster: NAICS 5231, rank 3, supplementary set.

company: The Charles Schwab Corporation
document_title: Schwab website Terms (schwab.com/legal/terms)
document_type: t1-governing-terms (site)
url: https://www.schwab.com/legal/terms
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: no - zero AI hits
ai_vector: chat (navigation/FAQ)
fetch_depth: full-fetch
clause_codes_present: B6 (generic: information may contain technical or factual inaccuracies; AS IS), B2 (generic)
files: mastersheet-sources/investing/schwab/schwab_terms_RAW.html (+ .txt)

company: The Charles Schwab Corporation
document_title: How to use Schwab Assistant (video transcript page)
document_type: t4-in-product-microcopy (help content)
url: https://www.schwab.com/content/how-to-use-schwab-assistant
retrieved: 2026-10-06
names_ai_feature: yes ("virtual agent")
fetch_depth: full-fetch
clause_codes_present: none (no accuracy or advice notice)
files: mastersheet-sources/investing/schwab/schwab_assistant-howto_RAW.html (+ .txt)

## Coding-relevant extract

The website terms have no AI or assistant language; only the generic statement that information may
contain inaccuracies and is provided AS IS. The help page describes the assistant without any
disclaimer.

## Coder note
1. **Locus 5 (absent).**
2. **Screen flag:** keyword-style guidance suggests a non-generative intent bot; the consumer-AI
   definition includes non-generative systems that converse, so it stays in, but note the AI basis
   is unverified.
3. **Gaps:** brokerage account agreement not checked; date of website terms.

---

<a name="equityresidential"></a>
## Equity Residential (Vivmark Residential) - "Ella" AI leasing assistant and digital resident-services agents - collected 2026-10-06

**AI feature.** Ella, an AI leasing assistant (by 2023), plus "digital leasing and resident-services
agents" and phone/website chatbots (per the firm's own terms and privacy notice). Leasing stakes:
rent, availability, fees, lease terms. Roster: NAICS 5311, rank 1, supplementary set. **Identity
note:** the terms and site now use the name "Vivmark Residential" ("About Vivmark"); confirm
whether this is a rebrand of Equity Residential and when, against the fixed-identity rule at cutoff.

company: Equity Residential (Vivmark Residential)
document_title: Vivmark Residential Terms of Use (equityapartments.com/terms; s.13 "Artificial Intelligence")
document_type: t1-governing-terms
url: https://www.equityapartments.com/terms
retrieved: 2026-10-06
effective_or_revised: Effective Date August 20, 2026 (stated) - after the cutoff
names_ai_feature: by category ("AI Technologies", "chatbots and digital leasing and resident-services agents"); Ella not named
ai_vector: generative chat + agentic (leasing and resident services)
fetch_depth: full-fetch
clause_codes_present: B2 (AI-specific, strong: not responsible or liable for any loss or damage caused by use of or reliance on any AI Technology), B6 (AI-specific: not responsible for accuracy of outputs; not reviewed; may be inaccurate, experimental, unsupervised), B4 (AI-specific: "required to confirm the accuracy and appropriateness of any solutions ... before use"), B3 (AI-specific: user "assume[s] all responsibilities and obligations" for results and output), B1-analog (AI-specific: output "does not represent our views"), B10 (AI-specific: inputs train the firm's own instance, not third-party LLMs), B8 (third-party AI vendors; waiver of claims against third-party services), B1 (generic: pricing/availability errors may be corrected)
vendor: unnamed "partners and vendors" (EliseAI per trade press for peers)
files: mastersheet-sources/apartment-reits/equity-residential/eqr_terms-of-use_RAW.html (+ .txt)

company: Equity Residential (Vivmark Residential)
document_title: Privacy Notice (s.6 "Social Features, Artificial Intelligence, and Other Third-Party Services")
document_type: privacy-notice
url: https://www.equityapartments.com/privacy
retrieved: 2026-10-06
effective_or_revised: Effective Date August 20, 2026 (stated)
names_ai_feature: category ("phone or website chatbot functionality and digital leasing and resident-services agents")
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: does not collect, use or sell personal information to train LLMs), B11 (no ADMT for legal or similarly significant decisions)
files: mastersheet-sources/apartment-reits/equity-residential/eqr_privacy_RAW.html (+ .txt)

## Coding-relevant extract

**s.13 "Artificial Intelligence."** The Service may use AI Technologies such as chatbots and digital
leasing and resident-services agents, including generative AI from third parties. To the fullest
extent permitted by law, the company is not responsible or liable for any loss or damage caused by
use of or reliance on any AI Technology (B2), and not responsible for the accuracy or appropriateness
of outputs, which are not reviewed (B6). Users are "required to confirm the accuracy and
appropriateness" of AI solutions before use (B4). AI is "experimental, unsupervised technology" that
may give inaccurate or offensive content that "does not represent our views" (B1-analog). The user
assumes all responsibility for results and output (B3). Inputs train the firm's own model instance
(B10). Phone chatbots are covered in the privacy notice, so the AI also takes calls.

## Coder note
1. **Locus 2 (dedicated AI section in general terms), among the broadest exclusions in the
   collection.** Housing context: leasing statements (rent, fees, concessions) are classic
   reliance facts, and Fair Housing exposure adds stakes.
2. **Version problem:** both documents dated 2026-08-20, after the cutoff and apparently tied to the
   Vivmark rebrand. Retrieve the pre-cutoff Equity Residential terms.
3. **Assent:** browsewrap on the site; phone agents have none.

---

<a name="avalonbay"></a>
## AvalonBay Communities - EliseAI leasing assistant - collected 2026-10-06

**AI feature.** An EliseAI-powered leasing assistant (chat/SMS/email/phone) answering prospects'
questions and scheduling tours. Roster: NAICS 5311, rank 2, supplementary set.

**Corporate identity.** AvalonBay and Equity Residential completed a merger of equals on
2026-08-17, forming **Vivmark Residential** (NYSE: VMRK from 2026-08-18). Under the protocol,
corporate identity is fixed at the 2026-06-30 cutoff, so AvalonBay and Equity Residential remain two
separate roster firms. But both sites now serve the merged company's documents, which postdate the
cutoff; the pre-merger AvalonBay terms are what should be coded.

company: AvalonBay Communities, Inc. (now Vivmark Residential)
document_title: Vivmark Residential Terms of Use (served at avaloncommunities.com/terms-of-use; s.13 "Artificial Intelligence")
document_type: t1-governing-terms
url: https://www.avaloncommunities.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Effective Date August 17, 2026 (stated) - merger closing date; after the cutoff
names_ai_feature: by category (same as EQR: "chatbots and digital leasing and resident-services agents")
ai_vector: generative chat + agentic (tour scheduling)
fetch_depth: full-fetch
clause_codes_present: identical to the EQR document (see #equityresidential): B1-analog:S, B2:S, B3:S, B4:S, B6:S, B8:S, B10:S, B1:G
files: mastersheet-sources/apartment-reits/avalonbay/avalon_terms-of-use_RAW.html (+ .txt)

company: AvalonBay Communities, Inc. (now Vivmark Residential)
document_title: Vivmark Privacy Notice (avaloncommunities.com)
document_type: privacy-notice
url: https://www.avaloncommunities.com/privacy-policy
retrieved: 2026-10-06
effective_or_revised: Effective Date August 17th, 2026 (stated)
fetch_depth: full-fetch
clause_codes_present: B10:S (no LLM training on personal info), B11:S (no ADMT)
files: mastersheet-sources/apartment-reits/avalonbay/avalon_privacy_RAW.html (+ .txt)

## Coding-relevant extract

The AvalonBay site serves Vivmark's August 17, 2026 Terms, whose s.13 "Artificial Intelligence" is
verbatim the same as the August 20 version on equityapartments.com: no liability for any loss from
reliance on AI; outputs unreviewed and possibly inaccurate; user must confirm accuracy; output does
not represent the company's views; user assumes all responsibility.

## Coder note
1. **Do not count this version for the headline.** It is a post-cutoff, post-merger document.
   Retrieve pre-merger AvalonBay and Equity Residential terms (both pre-2026-06-30).
2. **Useful for the paper anyway:** a merger produced a unified AI clause across two of the
   largest US apartment owners within days of closing.
3. **Vendor:** EliseAI's own terms are B2B and not used.

---

<a name="neighborly"></a>
## Neighborly (Molly Maid, Mr. Rooter, ...) - AI Receptionist (Vendasta) - collected 2026-10-06

**AI feature.** An AI Receptionist (Vendasta platform) on Molly Maid's website that captures leads,
**calculates price estimates** from square footage and room counts, pulls real-time availability
and **books appointments** through Neighborly's backend APIs, upsells recurring service, and closes
by showing the brand's "Done Right Promise" (vendor case study, 2025-08-20, reporting 55%
conversion). Live by August 2025. Transactional and price-quoting: a direct *Moffatt* risk.
Roster: NAICS 5617, rank 3, supplementary set (private franchisor).

company: Neighborly (Dwyer Group)
document_title: Neighborly Terms of Use (served on neighborly.com and on mollymaid.com)
document_type: t1-governing-terms
url: https://www.neighborly.com/terms-of-use (same document at https://www.mollymaid.com/terms-of-use/)
retrieved: 2026-10-06
effective_or_revised: Updated as of September 1, 2023 (stated)
names_ai_feature: no - zero AI-keyword hits
ai_vector: generative chat + agentic (estimates, booking)
fetch_depth: full-fetch (both URLs captured; identical text length, page-token differences only)
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/services-to-buildings/neighborly/neighborly_terms-of-use_RAW.html (+ .txt); mollymaid_terms-of-use_RAW.html (+ .txt)

company: Vendasta (about Molly Maid / Neighborly)
document_title: AI Receptionist Prompting: The Blueprint Behind a 55% Conversion Success Story
document_type: t6-marketing (vendor case study; last-resort evidence tier, flagged)
url: https://www.vendasta.com/blog/ai-receptionist-prompting/
retrieved: 2026-10-06
effective_or_revised: August 20, 2025
fetch_depth: full-fetch
files: mastersheet-sources/services-to-buildings/neighborly/neighborly_TYPE6_vendasta-case_RAW.html (+ .txt)

## Coding-relevant extract

The Neighborly Terms of Use (Sept 2023), which also govern mollymaid.com, contain no AI language
and no clause on estimates or quotes given online; only generic AS-IS and damages terms. The vendor
case study shows the AI quoting prices and booking jobs and being instructed to upsell and to
present the brand guarantee.

## Coder note
1. **Locus 5 (absent) for an agentic, price-quoting AI.** Among the highest-exposure configurations
   in the sample: the AI issues estimates and invokes a service guarantee, with no contractual
   qualification.
2. **Evidence tier:** vendor case study only (protocol last resort). Flag; seek first-party
   confirmation.
3. **Vintage:** terms 2023; AI live 2025; not revised.
4. **Franchise structure:** franchisees perform the service; whose representation the AI's quote
   is (franchisor vs franchisee) is an added doctrinal wrinkle.

---

<a name="synchrony"></a>
## Synchrony Financial - Sydney (intelligent virtual assistant) - collected 2026-10-06

**AI feature.** Sydney, an AI-enabled virtual assistant launched 2018 for Synchrony cardholders and
deployed by 20+ retail partners under partner-tuned tone and branding. It answers questions on
opening accounts, payment options, log-in issues and rewards (text, voice planned). Note: Synchrony
also uses ML for credit decisions (internal, out of scope; B11 context). Roster: NAICS 5222, rank 3,
supplementary set.

company: Synchrony Financial (Synchrony Bank)
document_title: Synchrony Terms of Use (synchrony.com/legal/terms-of-use)
document_type: t1-governing-terms (site)
url: https://www.synchrony.com/legal/terms-of-use
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: no - zero AI hits
ai_vector: chat (cardholder service)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/consumer-lending/synchrony/synchrony_terms-of-use_RAW.html (+ .txt)

company: Synchrony Bank
document_title: Synchrony Bank Online Credit Site Terms and Conditions (Website Usage Agreement, PDF)
document_type: t1-governing-terms (cardholder online account sites)
url: https://images.synchronycredit.com/assets/generic/en/website_usage_agreement.pdf
retrieved: 2026-10-06
effective_or_revised: Last updated 7/2021 (stated)
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch (PDF)
clause_codes_present: B6 (generic), B2 (generic)
files: mastersheet-sources/consumer-lending/synchrony/synchrony_credit-site-terms.pdf (+ .txt)

company: Synchrony Financial
document_title: Synchrony Harnesses AI to Transform Customer Experience (press release)
document_type: t6-marketing
url: https://www.synchrony.com/contenthub/newsroom/synchrony-harnesses-ai-to-transform-customer-experience.html
retrieved: 2026-10-06
effective_or_revised: October 22, 2018
fetch_depth: full-fetch
files: mastersheet-sources/consumer-lending/synchrony/synchrony_TYPE6_ai-cx_RAW.html (+ .txt)

## Coding-relevant extract

Neither the site terms nor the 2021 cardholder online-site terms mention AI, Sydney or chat. Generic
AS-IS and damages terms only. Sydney appears on partner-branded card sites, so the customer may not
even know the bot belongs to Synchrony.

## Coder note
1. **Locus 5 (absent).**
2. **White-label wrinkle:** Sydney is deployed under retailer brands with partner-matched tone.
   Attribution in a *Moffatt*-type dispute could point to the retailer or to Synchrony; neither
   document addresses it.
3. **Gaps:** cardholder agreements (per-card) not checked; privacy notice not fetched; Sydney's
   current (2026) status.

---

<a name="ally"></a>
## Ally Financial - Ally Assist - collected 2026-10-06

**AI feature.** Ally Assist, "the Ally Mobile app's built-in banking expert", a voice and text
assistant that answers questions and (per screening evidence) executes transfers. Roster: NAICS
5222, rank 4, supplementary set.

company: Ally Financial Inc. (Ally Bank)
document_title: Ally Bank Online Banking Services Agreement (OBSA, PDF)
document_type: t1-governing-terms (digital banking)
url: https://www.ally.com/content/dam/pdf/bank/ally-bank-obsa.pdf.coredownload.inline.pdf
retrieved: 2026-10-06
effective_or_revised: not stated in extracted text
names_ai_feature: no - zero hits for AI terms, "Ally Assist", "virtual assistant"; "Online Chat" appears only in a feature table
ai_vector: assistive voice/text + agentic (transfers)
fetch_depth: full-fetch (PDF, ~210k chars)
clause_codes_present: B6 (generic AS IS), B2 (generic), B3 (generic: credentials shared = authorized use)
files: mastersheet-sources/consumer-lending/ally/ally_bank-obsa.pdf (+ .txt)

company: Ally Financial Inc. (Ally Bank)
document_title: Ally Bank Deposit Agreement (PDF)
document_type: t1-governing-terms
url: https://www.ally.com/content/dam/pdf/bank/ally-bank-deposit-agreement.pdf.coredownload.inline.pdf
retrieved: 2026-10-06
effective_or_revised: Effective August 15, 2026 (stated) - after the cutoff
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch (PDF)
clause_codes_present: B2 (generic)
files: mastersheet-sources/consumer-lending/ally/ally_bank-deposit-agreement.pdf (+ .txt)

company: Ally Financial Inc.
document_title: Legal hub (ally.com/legal) and Online Banking product page
document_type: legal-hub-index / t6-marketing
url: https://www.ally.com/legal/ ; https://www.ally.com/bank/online-banking/
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/consumer-lending/ally/ally_legal-hub_RAW.html; ally_TYPE6_online-banking_RAW.html (+ .txt)

## Coding-relevant extract

Neither the OBSA nor the Deposit Agreement names Ally Assist or any AI. The legal hub lists no
assistant-specific terms (it lists co-browse, credit-score, debt-service and card terms). Generic
clauses only.

## Coder note
1. **Locus 5 (absent) for an agentic banking assistant.** Contrast with BofA and U.S. Bank, whose
   digital agreements have dedicated assistant sections.
2. **Vintage:** Deposit Agreement revised August 2026 (after cutoff) without AI language; OBSA undated.
3. **Gaps:** Ally Assist in-app terms or microcopy (app only); privacy notice; confirmation that
   Assist executes transfers (screening evidence; the product page says only that it answers questions).

---

<a name="rocket"></a>
## Rocket Companies - Rocket AI Agent on Rocket.com - collected 2026-10-06

**AI feature.** A "Rocket AI Agent" integrated into the Rocket.com home search, financing and
management site (launched 2025-01-22), plus an AI chat for hardship assistance (screening evidence).
Mortgage stakes: rates, eligibility, payments. Roster: NAICS 5222, rank 5, supplementary set.
Note: Redfin (pilot corpus) is a Rocket subsidiary since 2025; per the pilot crosswalk, Redfin's
documents were flagged for this firm. The group terms below now cover Redfin entities too.

company: Rocket Companies, Inc. (Rocket Limited Partnership subsidiaries; Redfin Corporation)
document_title: Terms of Use (linked from rocket.com footer; hosted at rocketmortgage.com)
document_type: t1-governing-terms (group-wide)
url: https://www.rocketmortgage.com/legal/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated 7/1/2025 (stated)
names_ai_feature: no - zero hits for AI, chatbot, generative, machine learning
ai_vector: generative chat + agentic (search, financing flows)
fetch_depth: full-fetch
clause_codes_present: B4 (generic, strong, model-specific: Estimated Home Value "generated by proprietary models" must not be relied on for loan origination, sale or any financial purpose), B6 (generic AS IS; information "deemed reliable but not guaranteed"), B8 (generic: MLS listing data from third parties), B2 (generic)
files: mastersheet-sources/consumer-lending/rocket-companies/rocketmortgage_terms-of-use_RAW.html (+ .txt)

company: Rocket Companies, Inc.
document_title: Rocket launches Rocket.com website ... (press release)
document_type: t6-marketing
url: https://www.rocketcompanies.com/press-release/rocket-launches-rocket-com-website-with-integrated-search-financing-and-management-tools/
retrieved: attempted 2026-10-06 (HTTP 403)
fetch_depth: snippet-only (screening evidence)
files: none

## Coding-relevant extract

The group Terms of Use (July 2025, after the January 2025 AI Agent launch) contain no AI language.
The closest clause is generic but model-specific: the Estimated Home Value comes from "proprietary
models", is not an appraisal, and "SHOULD NOT BE RELIED UPON" for loan origination, sale or any
financial purpose (B4). Listing data from MLS sources is not guaranteed (B8).

## Coder note
1. **Locus 5 for the conversational agent; generic model-output disclaimer exists for valuations.**
   Shows the firm knows how to disclaim model output but has not done so for its AI agent.
2. **Vintage:** revised July 2025, six months after the AI Agent launch; silent on it.
3. **Pilot-corpus link:** resolves the crosswalk "DECIDE" item for Redfin: Rocket collected fresh;
   Redfin's pilot documents remain supplementary.
4. **Gaps:** Rocket Mortgage loan disclosures; privacy policy (rocketaccount.com, JS app); AI Agent
   microcopy (behind account).

---

<a name="nisource"></a>
## NiSource - chatbot virtual assistant (Columbia Gas, NIPSCO) - collected 2026-10-06

**AI feature.** Chatbots on Columbia Gas and NIPSCO websites and apps (launched 2022-06-29), with
handoff to live chat: payment-plan enrollment, usage, outage reporting (NIPSCO), payment
locations, bill explanations, assistance options. Roster: NAICS 2212, rank 1, supplementary set
(regulated utility). AI basis not stated by the firm (screening counted it).

company: NiSource Inc. (Columbia Gas of Ohio, Inc.)
document_title: Terms of Use (Columbia Gas of Ohio)
document_type: t1-governing-terms
url: https://www.columbiagasohio.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Version October 6, 2025 (stated)
names_ai_feature: by category ("chat/chatbots", "chatbots") inside the definition of "Website"; no AI wording
ai_vector: chat (billing, payment plans, outages)
fetch_depth: full-fetch
clause_codes_present: B6 (generic, chatbot-reaching: AS IS; information may contain technical inaccuracies; not responsible for distorted transmissions affecting "chatbots"), B2 (generic)
files: mastersheet-sources/gas-utilities/nisource/columbiagas_terms-of-use_RAW.html (+ .txt)

company: NiSource Inc.
document_title: NiSource companies launch chatbots and live chat to provide an improved customer experience
document_type: t6-marketing
url: https://investors.nisource.com/financial-news/news-details/2022/NiSource-companies-launch-chatbots-and-live-chat-to-provide-an-improved-customer-experience/default.aspx
retrieved: 2026-10-06
effective_or_revised: June 29, 2022
fetch_depth: full-fetch
files: mastersheet-sources/gas-utilities/nisource/nisource_TYPE6_chatbot-launch_RAW.html (+ .txt)

## Coding-relevant extract

The Columbia Gas Terms of Use (Oct 2025) define the "Website" to include "information, surveys,
interactive forms or chat/chatbots", so the generic AS-IS, no-warranty, technical-inaccuracy and
damages clauses expressly reach the chatbot. A transmission-failure clause names chatbots. No AI
wording, no accuracy statement specific to chatbot answers, no clause on payment plans enrolled
through the bot.

## Coder note
1. **Locus 3 (generic clause expressly reaching a named chatbot category).** A clean example of the
   locus-3 type: the drafter knew the chatbot existed and swept it into the generic terms rather
   than writing AI-specific language.
2. **Vintage:** revised Oct 2025, three years after launch.
3. **Regulated utility:** payment plans and billing governed by state PUC tariffs.
4. **Gaps:** NIPSCO's own terms (Indiana) not fetched; privacy notice.

---

<a name="vailresorts"></a>
## Vail Resorts - My Epic Assistant (My Epic app) - collected 2026-10-06

**AI feature.** My Epic Assistant, an in-app guide "powered by advanced AI and resort experts"
(announced 2024-03-18, live for 2024/25 at Vail, Beaver Creek, Breckenridge, Keystone): answers on
grooming, conditions, ski school times, rentals, dining and parking, with handoff to live resort
experts; future plans for booking support. Roster: NAICS 7139, rank 1, supplementary set.

company: Vail Resorts, Inc.
document_title: Epic Pass Policies page (Website Terms and Conditions, Product Terms of Sale, Privacy Policy, EPIC Coverage terms)
document_type: t1-governing-terms (bundled policy page)
url: https://www.epicpass.com/policies.aspx
retrieved: 2026-10-06
effective_or_revised: coverage terms "Last Updated: March 3, 2026"; website terms tab date not isolated
names_ai_feature: no (only in navigation)
ai_vector: generative chat (resort information)
fetch_depth: full-fetch (browser, all tabs via textContent) - preservation: CAPTURE-NOTE + SHA-256 (JS shell to scripts)
clause_codes_present: generic only (not itemized; no AI clauses to code)
files: mastersheet-sources/amusement-recreation/vail-resorts/vail_policies_CAPTURE-NOTE.md

company: Vail Resorts, Inc.
document_title: Vail Resorts Announces "My Epic Assistant" ... (newsroom)
document_type: t6-marketing
url: https://news.vailresorts.com/2024-03-18-Vail-Resorts-Announces-My-Epic-Assistant-in-the-My-Epic-app-Powered-by-Advanced-AI-and-Resort-Experts
retrieved: 2026-10-06
effective_or_revised: March 18, 2024
fetch_depth: full-fetch
files: mastersheet-sources/amusement-recreation/vail-resorts/vail_TYPE6_my-epic-assistant_RAW.html (+ .txt)

## Coding-relevant extract

None of the legal documents on the Epic Pass policies page mention AI or the assistant. The app page
markets the assistant ("powered by AI and resort experts") with no qualification. Stakes are modest
(conditions, hours), but the assistant answers ski-school and rental questions that feed purchases,
and refund rules sit in the EPIC Coverage terms, which the AI could misstate.

## Coder note
1. **Locus 5 (absent).**
2. **"AI and resort experts" framing** implies human backing of AI answers, the opposite of a
   disclaimer (say-do).
3. **Gaps:** My Epic app EULA (app stores) not located; in-app microcopy.

---

<a name="lifetime"></a>
## Life Time Group Holdings - L•AI•C (AI health companion) and AI live-chat bots - collected 2026-10-06

**AI feature.** L•AI•C ("lay-see"), an AI "healthy way of life companion" in the Life Time app
(beta 2024-05-28; open to everyone 2025-07-29), built with Microsoft Azure AI Foundry: personalized
workouts, nutrition and **supplement recommendations**, recovery tips. Also AI chatbots in live chat.
Health-advisory stakes. Roster: NAICS 7139, rank 2, supplementary set.

company: Life Time Group Holdings, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.lifetime.life/policy/terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: Last Updated May 30, 2024 (stated) - two days after the L•AI•C beta
names_ai_feature: by category and vendor ("OpenAI GPT Model 3.5 and Microsoft Azure ... AI chatbots"); L•AI•C not named
ai_vector: generative (chat, health guidance)
fetch_depth: full-fetch
clause_codes_present: B2 (AI-specific: "not responsible for any incorrect or inaccurate information provided by the AI chatbots, nor for any consequences"), B3 (AI-specific: users "solely responsible for verifying the accuracy" and for actions taken), B6 (AI-specific: chatbots "not infallible"), B4 (AI-specific: review chat history; exercise caution before relying), B8-adjacent (names OpenAI/Azure), plus generic AS IS
files: mastersheet-sources/amusement-recreation/life-time/lifetime_terms-of-use_RAW.html (+ .txt)

company: Life Time Group Holdings, Inc.
document_title: Life Time Digital Membership Terms
document_type: t1-governing-terms (digital/app membership)
url: https://www.lifetime.life/policy/digital-membership-terms.html
retrieved: 2026-10-06
effective_or_revised: Last Modified November 18, 2020 (stated)
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch
clause_codes_present: generic only
files: mastersheet-sources/amusement-recreation/life-time/lifetime_digital-membership-terms_RAW.html (+ .txt)

company: Life Time Group Holdings, Inc.
document_title: Life Time Launches Complimentary AI Health Companion for Everyone: "Just Ask L•AI•C"
document_type: t6-marketing
url: https://news.lifetime.life/2025-07-29-Life-Time-Launches-Complimentary-AI-Health-Companion-for-Everyone-Just-Ask-LoAIoC
retrieved: 2026-10-06
effective_or_revised: July 29, 2025
fetch_depth: full-fetch
files: mastersheet-sources/amusement-recreation/life-time/lifetime_TYPE6_laic-launch_RAW.html (+ .txt)

## Coding-relevant extract

**AI chatbot paragraph (Terms of Use).** Life Time uses "OpenAI GPT Model 3.5 and Microsoft Azure"
for AI chatbots in live chat; they "are not infallible and may occasionally provide incorrect or
inaccurate information" (B6); users should review chat history and re-ask (B4); Life Time "is not
responsible for any incorrect or inaccurate information provided by the AI chatbots, nor for any
consequences" (B2); users are "solely responsible for verifying the accuracy" and for actions taken
(B3).

**Drafting oddity.** The sentences just before it address "the installation of the chat windows on
your website" and tell the reader to check that "the website appears and functions" correctly.
That is language for a business installing a chat widget, apparently carried over from a chat
vendor's B2B terms into consumer terms.

## Coder note
1. **Locus 2-lite (AI paragraph within general terms), vendor-named.** Covers chatbots; whether it
   reaches L•AI•C's health guidance is arguable (category language: "AI chatbots").
2. **Vintage:** May 30, 2024, coinciding with the L•AI•C beta, and not revised for the July 2025 full
   launch; the named model (GPT-3.5) is outdated relative to the Azure AI Foundry launch.
3. **Health stakes without a health disclaimer** for L•AI•C in the captured terms (supplement
   recommendations especially); the release calls it "science-backed guidance" and "your trusted AI
   companion" (say-do).
4. **Template diffusion again** (cf. Exelon/BofA): here from a B2B vendor into consumer terms.
5. **Full-read corrections (2026-10-08).** (a) The "Digital Membership Terms" capture is the
   **Ontario, Canada** agreement, not the US one. The contracting party is LTF Club Operations
   Company Canada, Inc.; it cites the Ontario Consumer Protection Act and selects Ontario law and
   Toronto courts, with "no representation that the Services are appropriate or available for use
   outside the province of Ontario". The row (LTH-02) is reclassified `out-non-us` /
   `structural-proxy`, and the US counterpart, which would govern the app and L•AI•C, is
   `referenced-not-located`. (b) Note 3 needs qualifying: the Terms of Use carry a *generic*
   health-information disclaimer ("should not be used in place of consultation with… your
   healthcare professionals"; coded B4 G). What is missing is an *AI-specific* health disclaimer.
   (c) The Terms of Use also contain a generic waiver of claims caused by Life Time's
   **negligence** (assumption-of-risk clause; B2/B3 G).

---

<a name="topgolf"></a>
## Topgolf - AI-Powered Player Assistant (Sierra) - collected 2026-10-06

**AI feature.** An AI-powered Player Assistant (Sierra) for reservations and questions, evidenced
by an archived Topgolf homepage from June 2026 (screening). Reservation stakes (bay bookings,
pricing, event packages). The assistant was not visible in a homepage text scan on 2026-10-06
(it may be a widget loaded on interaction). Roster: NAICS 7139, rank 4, supplementary set (private
since the Callaway separation).

company: Topgolf (Topgolf International, Inc.)
document_title: Terms & Conditions
document_type: t1-governing-terms
url: https://topgolf.com/us/company/terms-and-conditions/
retrieved: 2026-10-06
effective_or_revised: Updated Nov 3, 2023 (stated)
names_ai_feature: no - zero AI hits
ai_vector: generative chat (reservations)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/amusement-recreation/topgolf/topgolf_terms-and-conditions_RAW.html (+ .txt)

company: Topgolf
document_title: Privacy, Ad & Cookie Policies
document_type: privacy-notice
url: https://topgolf.com/us/company/privacy-policy/
retrieved: 2026-10-06
effective_or_revised: updated and effective October 5, 2026 (stated)
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch
files: mastersheet-sources/amusement-recreation/topgolf/topgolf_privacy_RAW.html (+ .txt)

## Coding-relevant extract

Neither document mentions AI, chat assistants or automated responses; generic AS-IS and damages
terms only. The privacy policy was revised the day before collection and still names no AI.

## Coder note
1. **Locus 5 (absent).**
2. **Vintage:** terms 2023, before the assistant; privacy revised 2026-10-05, after the assistant,
   still silent.
3. **Evidence flag:** AI assistant existence rests on an archived first-party page (June 2026);
   the live site did not show it in a text scan. Reconfirm liveness at cutoff.

---

<a name="macys"></a>
## Macy's - Ask Macy's (Gemini Enterprise for CX) - collected 2026-10-06

**AI feature.** Ask Macy's, a multimodal conversational AI shopping agent built on Google's Gemini
Enterprise for Customer Experience (piloted December 2025, launched March 2026) on macys.com and the
app: product discovery across 2.5M+ SKUs, personalized recommendations, virtual try-on. Google
reports 4.75x revenue per visit among users in beta. Roster: NAICS 4551, rank 1, supplementary set.

company: Macy's, Inc.
document_title: Macy's Terms of Use Legal Notice
document_type: t1-governing-terms
url: https://www.macys.com/customer-service/articles/legal-notice
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no - zero AI hits
ai_vector: generative (shopping agent)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256 (former customerservice-macys.com host no longer resolves)
clause_codes_present: B1 (generic: may correct pricing/availability errors "including after an order has been submitted" and cancel or refuse orders), B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/department-stores/macys/macys_legal-notice_CAPTURE-NOTE.md

company: Google Cloud (about Macy's)
document_title: A New Era for Online Shopping: How Macy's Built the 'Ask Macy's' AI Agent in 4 Weeks ...
document_type: t6-marketing (vendor release)
url: https://www.googlecloudpresscorner.com/2026-04-22-A-New-Era-for-Online-Shopping-How-Macys-Built-the-Ask-Macys-AI-Agent-in-4-Weeks-With-Gemini-Enterprise-for-Customer-Experience
retrieved: 2026-10-06 (search snippet)
fetch_depth: snippet-only
files: none

## Coding-relevant extract

The Terms of Use Legal Notice has no AI language. The generic errors clause lets Macy's correct
pricing and availability errors even after an order is submitted and cancel or refuse orders (B1).
AS-IS and damages terms otherwise.

## Coder note
1. **Locus 3 (generic B1 reaching the AI's domain) / no AI language.**
2. **Vintage:** undated; no evidence of revision for Ask Macy's.
3. **Gaps:** privacy notice not fetched; Ask Macy's in-app microcopy; first-party Macy's release
   (vendor and trade sources only).

---

<a name="nordstrom"></a>
## Nordstrom - natural-language (generative) search in the app - collected 2026-10-06

**AI feature.** Generative-AI natural-language search in the Nordstrom app (holiday 2024 app refresh,
per screening). Customers describe what they want in prose. Edge-of-scope (search, not a
conversational agent). Roster: NAICS 4551, rank 3, supplementary set (private since 2025).

company: Nordstrom, Inc.
document_title: Terms & Conditions
document_type: t1-governing-terms
url: https://www.nordstrom.com/browse/customer-service/policy/terms-conditions
retrieved: 2026-10-06
effective_or_revised: Last Updated May 27, 2026 (stated) - inside the cutoff
names_ai_feature: no (AI named only for generated product content)
ai_vector: generative search; generative product content
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256
clause_codes_present: B6 (AI-specific, content-level: product descriptions, specifications, dimensions, materials, "safety warnings, and usage guidelines" may be AI-generated and contain errors), B4 (review product details carefully; ask before buying), B1-soft (generic: may correct pricing even after order submission; customer may then withdraw), B2/B6 (generic)
files: mastersheet-sources/department-stores/nordstrom/nordstrom_terms-conditions_CAPTURE-NOTE.md

## Coding-relevant extract

The May 2026 Terms add an AI disclosure aimed at **AI-generated product content**: descriptions,
specifications and attributes, including dimensions, materials, safety warnings and usage
guidelines, "may be generated or enhanced using artificial intelligence and could contain errors,
omissions, or approximations"; customers should review details and ask questions before buying,
especially about safety, fit or performance. Generic errors clause: prices may be corrected even
after an order is placed. Nothing addresses the AI search feature.

## Coder note
1. **Locus 2-partial: AI-specific but aimed at generated content, not at the conversational/search
   AI.** A distinct sub-type (AI-generated product content disclaimers); Wayfair also disclaims
   AI-generated content. Note the safety-warning dimension, which raises product-liability issues
   beyond *Moffatt*.
2. **Vintage:** revised May 27, 2026, inside the cutoff.
3. **Gaps:** privacy notice; search-feature microcopy.

---

<a name="labcorp"></a>
## Labcorp - MyLabcorp app: AI explanations and Q&A on lab results - collected 2026-10-06

**AI feature.** The MyLabcorp app (launched 2026-05-20) gives AI-generated explanations of lab
results and answers patients' questions, built on OpenAI models (screening evidence). Health-
advisory stakes: a patient misreading results. Roster: NAICS 6215, rank 1, supplementary set.

company: Laboratory Corporation of America Holdings (Labcorp)
document_title: Labcorp Online Services User Agreement (Terms and Conditions)
document_type: t1-governing-terms (includes service-specific MyLabcorp section)
url: https://www.labcorp.com/terms-and-conditions
retrieved: 2026-10-06
effective_or_revised: last updated on July 22, 2026 (stated) - after the cutoff and two months after the MyLabcorp launch
names_ai_feature: by category ("artificial intelligence and large language models"); MyLabcorp has a service-specific section
ai_vector: generative (health information Q&A)
fetch_depth: full-fetch
clause_codes_present: B4 (AI-specific, strong: will not rely on AI output "as a source of truth or factual information, or as a substitute for professional advice"), B3 (AI-specific: use at "sole risk"; user responsible for evaluating accuracy; user solely responsible for User-Provided Content incl. AI inputs), B6 (AI-specific: output may be inaccurate, misleading, biased or offensive), B1-analog (AI-specific: output may not reflect and may be inconsistent with Labcorp's views), not-medical-advice / not for clinical decision-making (AI-specific), B10 (AI-specific: User-Provided Content used to develop and enhance AI features; HIPAA/NPP apply), B9 (AI-specific: no re-identification, no passing AI output off as human), B8 (output may be subject to third-party terms)
files: mastersheet-sources/medical-labs/labcorp/labcorp_terms_RAW.html (+ .txt)

company: Labcorp
document_title: Labcorp launches MyLabcorp, new AI-powered mobile app (investor release)
document_type: t6-marketing
url: https://ir.labcorp.com/news-releases/news-release-details/labcorp-launches-mylabcorptm-new-ai-powered-mobile-app-designed
retrieved: attempted 2026-10-06 (timed out)
fetch_depth: snippet-only (screening evidence; launch 2026-05-20)
files: none

## Coding-relevant extract

**s.6 "Use of Large Language Models and Artificial Intelligence."** AI output may be inaccurate,
misleading, biased or offensive, may differ between users, may lack IP protection, may be subject
to third-party terms, may not reflect Labcorp's views, and may reference third parties without
endorsement. Users are responsible for evaluating output. In capitals: use of AI output is at the
user's sole risk, and the user "WILL NOT RELY ON ANY AI-GENERATED OUTPUTS AS A SOURCE OF TRUTH OR
FACTUAL INFORMATION". AI features are not for clinical decision-making or medical, legal or financial
advice. Inputs, including when using AI features, are the user's sole responsibility and may be used
to develop AI features (B10), subject to HIPAA and the NPP.

## Coder note
1. **Locus 2 (dedicated AI section in a general user agreement), among the strongest anti-reliance
   wording in the collection** ("not a source of truth").
2. **Tension:** the product's point is to explain results; the contract says not to rely on the
   explanations as factual. Clear say-do gap in a health context.
3. **Version problem:** dated July 22, 2026, after the cutoff (MyLabcorp launched May 20, 2026).
   Retrieve the version in force at 2026-06-30.
4. **Gaps:** MyLabcorp in-app microcopy; release page (timed out).

---

<a name="quest"></a>
## Quest Diagnostics - Quest AI Companion (MyQuest) - collected 2026-10-06

**AI feature.** Quest AI Companion, a Gemini-based chat in the MyQuest app and portal (launched
2026-03-02, all adult users) that explains lab results and analyzes up to five years of a patient's
Quest results to "uncover potential health risks". Health-advisory stakes. Roster: NAICS 6215,
rank 2, supplementary set.

company: Quest Diagnostics Incorporated
document_title: Terms and Conditions (questdiagnostics.com; linked as "Terms" from MyQuest pages)
document_type: t1-governing-terms
url: https://www.questdiagnostics.com/home/privacy-policy/terms-conditions
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: no - zero AI hits in the body (AI words appear only in site navigation, e.g. the provider tool "Clinical Insights Companion")
ai_vector: generative (health Q&A)
fetch_depth: full-fetch
clause_codes_present: generic only (AS IS, damages limits not separately itemized)
files: mastersheet-sources/medical-labs/quest/quest_terms-conditions_RAW.html (+ .txt)

company: Quest Diagnostics Incorporated
document_title: MyQuest FAQ: How accurate is the Quest AI Companion?
document_type: t4-in-product-microcopy (help FAQ)
url: https://myquest.questdiagnostics.com/myquest-faq1/MyQuest/3113.htm
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch (browser) - CAPTURE-NOTE with complete verbatim text + SHA-256
clause_codes_present: B6 (AI-specific: "not a human or a doctor and may make mistakes"), B4 (AI-specific: "Always talk to your doctor about your results"), not-medical-advice (only a doctor can diagnose or suggest treatment); capability limit (sees only MyQuest results)
files: mastersheet-sources/medical-labs/quest/quest_ai-companion-faq_CAPTURE-NOTE.md

company: Quest Diagnostics
document_title: Quest Diagnostics Introduces AI Companion ... (newsroom); Quest AI Companion article (questhealth.com)
document_type: t6-marketing
url: https://newsroom.questdiagnostics.com/2026-03-02-Quest-Diagnostics-Introduces-AI-Companion-to-Help-Patients-Understand-and-Act-on-Lab-Test-Results ; https://www.questhealth.com/articles/ai-companion.html
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/medical-labs/quest/quest_TYPE6_ai-companion_RAW.html; quest_ai-companion-article_RAW.html (+ .txt)

## Coding-relevant extract

The Terms and Conditions body contains no AI language. The only AI disclaimer is a short MyQuest
FAQ: the Companion "has been tested, but it's not a human or a doctor and may make mistakes", sees
only MyQuest results, and only a doctor can diagnose or suggest treatment; "Always talk to your
doctor". Search-result snippets also cite a "do not start, stop or change treatment" instruction,
not captured here. Marketing: "personalized, easy-to-understand explanations" and identifying
"potential health risks".

## Coder note
1. **Locus 4 (microcopy-only).** Clean contrast with Labcorp (same industry, dedicated contract
   section).
2. **Health stakes, contract silence:** the binding document says nothing about an AI that
   interprets lab results.
3. **Gaps:** in-app Companion consent screen (snippets mention an opt-in and age 18+); MyQuest-
   specific terms if separate; Notice of Privacy Practices (HIPAA) for AI use.

### Full-read addendum (2026-10-08) - questhealth.com article registered as DGX-04

company: Quest Consumer Inc. / Quest Diagnostics
document_title: Quest AI Companion help article (questhealth.com)
document_type: t4-in-product-microcopy (public help article describing the in-product flow)
url: https://www.questhealth.com/articles/ai-companion.html
retrieved: 2026-10-07
effective_or_revised: not stated (cites sources accessed 2026-01-30)
names_ai_feature: yes (Quest AI Companion; "built in conjunction with a Google AI-powered chatbot")
ai_vector: generative (health Q&A)
fetch_depth: full-fetch
clause_codes_present: B4 S, B6 S, B10 S (AI-specific); vendor disclosure (Google), no carve-out
vendor: Google (model not named in the article; roster lists Gemini)
files: mastersheet-sources/medical-labs/quest/quest_ai-companion-article_RAW.html (+ .txt)

**Coding-relevant extract.** The article describes the in-product flow: the user opens the
Companion from a Results button, then must "Review the information. If you agree, click the I
consent button". So there is a click-through at the AI surface; what is agreed to was not
captured. It states that "Terms and Conditions apply and can be found while logged in on your
Account Settings page". The Companion "is not human and may make mistakes"; users should
always discuss results with a healthcare provider. Chat transcripts and ratings may be used "to
improve how Quest AI Companion works... but not for large language model training". One
passage says test results are never used to train any *public* LLM; another says *any* LLM.

**Coder note 4 (supersedes note 2).** The questdiagnostics.com Terms and Conditions (DGX-01)
say they apply only to www.QuestDiagnostics.com and that "other Web sites... are covered by
different terms of use". The Companion's governing terms are behind the MyQuest login and were
**not captured** (`referenced-not-located`; a logged-in capture is needed). Note 2 ("the binding
document says nothing") should be read as "the captured site terms say nothing; the binding
MyQuest terms are unseen". The in-product consent screen in gap 3 is confirmed to exist.

---

<a name="signet"></a>
## Signet Jewelers - chatbot on Kay/Zales/Jared sites (LivePerson) - collected 2026-10-06

**AI feature.** A LivePerson-powered chatbot on Signet banner sites (screening evidence: LivePerson
case material; launch not stated). Sales and service questions. Roster: NAICS 4583, rank 1,
supplementary set. Evidence tier: vendor material (flag).

company: Signet Jewelers Limited (US operations)
document_title: Signet Terms of Use (covers Kay.com, Jared.com, Zales.com, Banter, Rocksbox, Diamonds Direct and other banner sites)
document_type: t1-governing-terms
url: https://www.signetjewelers.com/terms-of-use/default.aspx
retrieved: 2026-10-06
effective_or_revised: Effective October 17, 2024 (stated)
names_ai_feature: no - zero AI-keyword hits (including "chat")
ai_vector: chat (sales/service)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic), arbitration
files: mastersheet-sources/jewelry/signet/signet_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

The group Terms of Use apply across all Signet banner sites and contain no AI or chat language;
generic AS-IS, damages limits and mandatory arbitration only.

## Coder note
1. **Locus 5 (absent).**
2. **Gaps:** first-party evidence of the chatbot and its AI basis (vendor material only); kay.com's
   own "legal disclaimers" page (kay.com/kay-legal-disclaimers) not separately fetched; privacy
   policy.

---

<a name="kendrascott"></a>
## Kendra Scott - generative-AI shopping assistant (iAdvize Copilot) - collected 2026-10-06

**AI feature.** A generative-AI shopping assistant for gifting and product advice (iAdvize Copilot;
by 2025, per Chain Store Age interview in screening). Roster: NAICS 4583, rank 2, supplementary
set (private).

company: Kendra Scott, LLC
document_title: Terms & Conditions (incl. returns, Club Kendra)
document_type: t1-governing-terms
url: https://www.kendrascott.com/terms-conditions.html
retrieved: 2026-10-06
effective_or_revised: Last Updated June 22, 2026 (stated; Club Kendra section updated June 23, 2026) - one week before the cutoff
names_ai_feature: no - "chat" appears only as a customer-service contact channel; no AI words
ai_vector: generative chat (shopping)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS); no AI clauses
files: mastersheet-sources/jewelry/kendra-scott/kendrascott_terms-conditions_RAW.html (+ .txt)

company: Kendra Scott, LLC
document_title: Privacy Policy
document_type: privacy-notice
url: https://www.kendrascott.com/privacy.html
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no ("virtual chat feature" listed as a customer-service channel)
fetch_depth: full-fetch
files: mastersheet-sources/jewelry/kendra-scott/kendrascott_privacy_RAW.html (+ .txt)

## Coding-relevant extract

Both documents treat chat as a customer-service channel; neither mentions AI or automated answers.
The Terms were revised June 22, 2026, a week before the cutoff, and still contain no AI language.

## Coder note
1. **Locus 5 (absent), strong vintage finding** (recent revision, still silent).
2. **Evidence tier:** AI assistant evidenced by a trade interview and vendor material (iAdvize).
   Flag for first-party confirmation.

---

<a name="tractorsupply"></a>
## Tractor Supply - AI assistant on tractorsupply.com (OpenAI) - collected 2026-10-06

**AI feature.** An AI chatbot/assistant on tractorsupply.com built with OpenAI technology (CIO Rob
Mills to Modern Retail, 2025; OpenAI chosen as primary AI partner early 2025). Also employee-facing
"Hey GURA" headsets and in-store computer vision (both out of scope). Roster: NAICS 4442, rank 1,
supplementary set.

company: Tractor Supply Company
document_title: Terms & Conditions (tractorsupply.com/tsc/cms/terms-conditions)
document_type: t1-governing-terms
url: https://www.tractorsupply.com/tsc/cms/terms-conditions
retrieved: attempted 2026-10-06
fetch_depth: referenced-not-located. Scripted fetch timed out; the built-in browser received an Akamai "Access Denied" page (225 chars).
files: none

company: Modern Retail (about Tractor Supply)
document_title: Tractor Supply bets on OpenAI as its primary AI partner
document_type: t6-marketing (trade press with firm CIO quotes)
url: https://www.modernretail.co/technology/tractor-supply-bets-on-openai-as-its-primary-ai-partner/
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/lawn-garden/tractor-supply/tsc_TYPE6_modernretail-openai_RAW.html (+ .txt)

company: CIO.com (about Tractor Supply)
document_title: Tractor Supply enlists AI to deliver 'legendary' customer service
document_type: t6-marketing (trade press; describes employee-facing tools)
url: https://www.cio.com/article/2088569/tractor-supply-enlists-ai-to-deliver-legendary-customer-service.html
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/lawn-garden/tractor-supply/tsc_TYPE6_cio-article_RAW.html (+ .txt)

## Coding-relevant extract

None from legal documents. Trade press confirms a customer-facing website chatbot built with OpenAI.
Note the screening evidence URL (CIO.com) describes only employee tools; the customer-facing claim
rests on the Modern Retail article.

## Coder note
1. **Not coded.**
2. **Screening evidence correction:** replace the CIO.com evidence URL with the Modern Retail article
   in the screening log.
3. **Retrieval route:** user's own browser; Akamai blocks both automated routes.

---

<a name="netflix"></a>
## Netflix - generative-AI conversational search (iOS opt-in beta) - collected 2026-10-06

**AI feature.** Generative-AI search on iOS (small opt-in beta announced 2025-05-07, OpenAI-powered
per screening) letting members search with natural phrases ("something funny and upbeat"). Low
stakes (title discovery). Roster: NAICS 5162, rank 1, supplementary set.

company: Netflix, Inc.
document_title: Netflix Terms of Use
document_type: t1-governing-terms
url: https://help.netflix.com/legal/termsofuse
retrieved: 2026-10-06
effective_or_revised: Last Updated April 10, 2026 (stated)
names_ai_feature: no (ML appears only in a user prohibition)
ai_vector: generative search
fetch_depth: full-fetch
clause_codes_present: B9 (AI-specific, user-directed: no use of the service in connection with prompting, fine-tuning, training or benchmarking ML models), B6/B2 (generic)
files: mastersheet-sources/streaming-social/netflix/netflix_terms-of-use_RAW.html (+ .txt)

company: Netflix, Inc.
document_title: Unveiling Our Innovative New TV Experience ... and a New Way to Search
document_type: t6-marketing
url: http://about.netflix.com/en/news/unveiling-our-innovative-new-tv-experience
retrieved: 2026-10-06
effective_or_revised: May 7, 2025
fetch_depth: full-fetch
files: mastersheet-sources/streaming-social/netflix/netflix_TYPE6_new-tv-experience_RAW.html (+ .txt)

## Coding-relevant extract

The April 2026 Terms of Use mention machine learning only to forbid users from using the service
to prompt, fine-tune, train or benchmark ML systems (B9, user-directed). Nothing on Netflix's own
generative search. Generic AS-IS and limitation terms.

## Coder note
1. **Locus 5 for the firm's AI; B9 user-directed only.** Same pattern as Anthem, eBay, WSI: 2026
   revisions add AI restrictions on users.
2. **Scope note:** an opt-in beta search feature; marginal under the consumer-interaction test
   (conversational query, but returns titles, not answers).
3. **Gaps:** beta-specific terms or consent screen (iOS, opt-in) not captured; whether the beta
   was still live at 2026-06-30.

---

<a name="snap"></a>
## Snap Inc. - My AI chatbot - collected 2026-10-06

**AI feature.** My AI, a generative chatbot inside Snapchat (Snapchat+ Feb 2023, all users
2023-04-19), plus other AI features (lenses, generated content). Many users are teens. Roster:
NAICS 5162, rank 2, supplementary set. (My AI uses third-party foundation models; Snap is a
deployer for this purpose.)

company: Snap Inc.
document_title: Snap Inc. Terms of Service (s.6 "AI Features")
document_type: t1-governing-terms
url: https://www.snap.com/terms
retrieved: 2026-10-06
effective_or_revised: Effective September 21, 2026 (stated) - after the cutoff
names_ai_feature: yes - "My AI" listed among the Services; s.6 "AI Features"
ai_vector: generative chat + generative content
fetch_depth: full-fetch (page contains US and UK/EU variants; AI text identical)
clause_codes_present: B1-analog (AI-specific: "Outputs are not Snap representations", stated twice; Outputs may not reflect Snap's view; no endorsement), B6 (AI-specific: Outputs not reviewed in advance; may be inaccurate, misleading, offensive, infringing, unlawful; as-is, no warranties), B4/B3 (AI-specific: use at your own risk; "should not rely on them for any purpose, including to make decisions or for professional, medical, legal, financial, educational or other advice"), B10 (AI-specific: Inputs/Outputs treated as content under the licences; used per Privacy Policy), B9 (AI-specific: no rights-violating Inputs; no removing watermarks; no circumventing safety)
files: mastersheet-sources/streaming-social/snap/snap_terms-of-service_RAW.html (+ .txt)

## Coding-relevant extract

**Summary box (top of Terms):** AI features generate outputs "which may not be accurate or
appropriate, so you use them at your own risk"; "Outputs of our AI-enabled features are not Snap
representations."

**s.6 AI Features:** Inputs and Outputs are content under the Terms (licences apply). Outputs may not
be reviewed in advance and may be inaccurate, incomplete, misleading, offensive, unlawful, or the
same as others' outputs; may not reflect Snap's view; Snap does not endorse them; references to
third parties imply no endorsement. AI Features and Outputs are as-is; use is at your own risk; do not
rely on them for any purpose, including decisions or professional, medical, legal, financial or
educational advice. "Outputs are not Snap representations." Prohibited: rights-violating Inputs,
removing watermarks or disclosures, circumventing safety.

## Coder note
1. **Locus 2 (dedicated AI section inside general terms), brand-named.** "Not Snap representations"
   is the purest anti-attribution formula in the collection, answering *Moffatt*'s attribution
   reasoning head-on (cf. Ulta, A&F, Vanguard, Wayfair, Labcorp, Vivmark).
2. **Version problem:** effective 2026-09-21, after the cutoff. The pre-cutoff Snap Terms are known
   to have had My AI language since 2023; retrieve the version in force at 2026-06-30 for coding.
3. **Minors:** the reliance waiver is aimed at a user base that includes teens; enforceability
   against minors is doubtful (doctrinal note).
4. **Gaps:** separate My AI support page and in-app disclaimer not captured (the 2023 "My AI
   Terms" URL now 404s).

---

<a name="roku"></a>
## Roku - AI-upgraded Roku Voice - collected 2026-10-06

**AI feature.** Roku Voice upgraded in October 2025 with in-house and commercial generative AI/LLMs
for conversational entertainment questions (e.g. about shows, actors, sports scores). Voice via
remote or app. Low stakes. Roster: NAICS 5162, rank 3, supplementary set.

company: Roku, Inc.
document_title: Roku Products Terms of Use
document_type: t1-governing-terms (devices/software)
url: https://docs.roku.com/published/deviceplayereula/en/us
retrieved: 2026-10-06
effective_or_revised: Effective October 17, 2020 (stated)
names_ai_feature: no (Voice Services clause; no AI wording)
ai_vector: generative voice Q&A
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with the voice clause + innerText SHA-256
clause_codes_present: B10-generic (voice inputs recorded, processed and stored by Roku and service providers)
files: mastersheet-sources/streaming-social/roku/roku_products-terms_CAPTURE-NOTE.md

company: Roku, Inc.
document_title: Roku Services Agreement (account/services terms)
document_type: t1-governing-terms
url: attempted https://docs.roku.com/published/userservicesterms/en/us (404 in browser)
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

The 2020 Products Terms of Use describe voice commands for search and control and authorize Roku and
its providers to record and store voice inputs. No AI, no accuracy language for conversational
answers. The account-level Services Agreement (which may carry newer AI language) was not located.

## Coder note
1. **Provisional locus 5**, pending the Roku Services Agreement.
2. **Vintage:** product terms from 2020 governing a 2025 generative upgrade.
3. **Gaps:** Roku Services Agreement URL; Roku privacy policy (voice/AI section).

---

<a name="pinterest"></a>
## Pinterest - Pinterest Assistant - collected 2026-10-06

**AI feature.** Pinterest Assistant (launched 2025-10-30, US beta, 18+), an "AI-powered, visual-first"
shopping collaborator by voice, text and image, drawing on users' saves and boards. Roster: NAICS
5162, rank 4, supplementary set.

**ELIGIBILITY FLAG (model-developer rule).** Pinterest's own "AI at Pinterest" help page says
Pinterest Assistant's conversational outputs are powered by **Navigator-1, "a multimodal foundation
model"**, and that **Pinterest Canvas** is Pinterest's "image generation foundation model", trained on
Pinterest data collected since 2009. The protocol excludes firms that develop their own foundation
models (Amazon was excluded for Nova). Recommend: mark Pinterest "exclude: model-developer" in the
screening log and let the next firm by revenue take the slot.

company: Pinterest, Inc.
document_title: Pinterest Terms of Service
document_type: t1-governing-terms
url: https://policy.pinterest.com/en/terms-of-service
retrieved: 2026-10-06
effective_or_revised: effective November 12, 2026 (stated; future-dated version served)
names_ai_feature: no - zero AI-keyword hits
fetch_depth: full-fetch
clause_codes_present: B6/B2 (generic)
files: mastersheet-sources/streaming-social/pinterest/pinterest_terms-of-service_RAW.html (+ .txt)

company: Pinterest, Inc.
document_title: AI at Pinterest (help article)
document_type: t4-in-product-microcopy (help content; model disclosures)
url: https://help.pinterest.com/en/article/ai-at-pinterest
retrieved: 2026-10-06
fetch_depth: full-fetch
clause_codes_present: AI-model disclosure (Navigator-1, Canvas; training data since 2009); controls to see fewer AI Pins
files: mastersheet-sources/streaming-social/pinterest/pinterest_ai-at-pinterest_RAW.html (+ .txt)

company: Pinterest, Inc.
document_title: Say hello to Pinterest Assistant (newsroom)
document_type: t6-marketing
url: https://newsroom.pinterest.com/news/pinterest-assistant-revolutionizing-the-way-you-shop-online/
retrieved: 2026-10-06
effective_or_revised: October 30, 2025
fetch_depth: full-fetch
files: mastersheet-sources/streaming-social/pinterest/pinterest_TYPE6_assistant-launch_RAW.html (+ .txt)

## Coding-relevant extract

The Terms of Service (even the November 2026 version) contain no AI language. The help article
discloses the in-house foundation models behind the Assistant and Canvas.

## Coder note
1. **Exclude from the sample (model developer)**, pending the user's confirmation. If retained,
   locus 5.
2. Pinterest's separate "Creative Generative AI Business Terms" are B2B (advertisers) and not used.

---

<a name="matchgroup"></a>
## Match Group - Hinge AI Prompt Feedback / Convo Starters; Tinder AI photo selector - collected 2026-10-06

**AI feature.** Hinge: AI "Prompt Feedback" coaching on profile answers and AI conversation starters
(2025). Tinder: AI photo selector choosing profile pictures (2025). The AI advises users on
self-presentation and generates content they post. Roster: NAICS 5162, rank 5, supplementary set.

company: Match Group, Inc. (Tinder)
document_title: Tinder Terms of Use
document_type: t1-governing-terms
url: https://policies.tinder.com/terms/us/en
retrieved: 2026-10-06
effective_or_revised: Effective on March 5, 2026 (stated)
names_ai_feature: by category ("AI Technology")
ai_vector: generative (profile content, photo selection)
fetch_depth: full-fetch
clause_codes_present: B3 (AI-specific: "solely responsible for any content generated by such AI Technology that you create, upload or share"; responsible for its accuracy and decisions based on it), B10 (AI-specific: licence to train and improve including through AI Technology; services "cannot thereafter 'unlearn'"; exclusive licence to AI-derived works), B9 (AI-specific: no third-party AI systems interacting with the service), B6/B2 (generic)
files: mastersheet-sources/streaming-social/match-group/tinder_terms_RAW.html (+ .txt)

company: Match Group, Inc. (Hinge)
document_title: Hinge Terms of Service
document_type: t1-governing-terms
url: https://hinge.co/terms
retrieved: 2026-10-06
effective_or_revised: Effective on August 25, 2025 (stated)
names_ai_feature: no (machine learning used on user content; no AI-feature clause)
fetch_depth: full-fetch
clause_codes_present: B10 (generic-ML: content incl. messages analyzed with ML to develop and improve services), B9 (no third-party AI systems), B6/B2 (generic)
files: mastersheet-sources/streaming-social/match-group/hinge_terms_RAW.html (+ .txt)

## Coding-relevant extract

**Tinder.** Tinder "may itself use or offer to You" AI Technology; the user is "solely responsible"
for AI-generated content they create, upload or share, including its accuracy and decisions based on
it (B3). Licence to user content covers training and improving services through AI; services
"cannot thereafter 'unlearn'"; Tinder holds an exclusive licence over derivative works created
through its AI (B10). Third-party AI tools may not interact with the service (B9).

**Hinge.** No AI-feature clause; messages and content may be analyzed with machine learning to
develop and personalize the service (B10, generic). Third-party AI systems banned (B9).

## Coder note
1. **Locus 2-lite (Tinder: AI definition plus responsibility shift), locus 5 (Hinge).** Same parent,
   different drafting maturity across brands.
2. **"Cannot unlearn"** is a notable, candid training disclosure (B10).
3. **Stakes are reputational and safety-related** (impersonation, misleading profiles); *Moffatt*-type
   transactional reliance is weak here.
4. **Gaps:** Hinge Prompt Feedback in-app microcopy; Match Group privacy policy.

---

<a name="1800flowers"></a>
## 1-800-Flowers.com - AI intelligent virtual assistant - collected 2026-10-06

**AI feature.** An AI intelligent virtual assistant working with human agents (by January 2020 per
firm release), following earlier GWYN (IBM Watson gift concierge, 2016) and a 2023 "MomVerse" GenAI
poem bot. Order and gift-delivery service. Roster: NAICS 4452, rank 1, supplementary set.

company: 1-800-FLOWERS.COM, Inc.
document_title: Terms of Use
document_type: t1-governing-terms
url: https://www.1800flowers.com/About-Us-Terms-of-Use
retrieved: 2026-10-06
effective_or_revised: Last updated June 20, 2025 (stated)
names_ai_feature: no - zero AI hits
ai_vector: chat (order service)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE + innerText SHA-256
clause_codes_present: B1-soft (generic: may correct errors and change information "including after you have submitted your order"), B6/B2 (generic)
files: mastersheet-sources/specialty-food/1800flowers/1800flowers_terms-of-use_CAPTURE-NOTE.md

## Coding-relevant extract

No AI language. Generic: information may contain errors, and the company may correct errors and
change information even after an order is submitted.

## Coder note
1. **Locus 5 (absent).**
2. **Vintage:** June 2025, years after the virtual assistant; not revised for it.
3. **Gaps:** current (2026) assistant status and AI basis; privacy notice; first-party release from
   2020 (screening evidence) not re-fetched.

---

<a name="hrblock"></a>
## H&R Block - AI Tax Assist (Azure OpenAI) - collected 2026-10-06

**AI feature.** AI Tax Assist, a generative-AI assistant in H&R Block's DIY online product
(launched 2023-12-14) answering free-form tax questions, explaining forms, deductions and credits,
and recent law changes. The firm's release says it delivers "real-time, reliable tax filing
assistance backed by H&R Block's 100% accuracy and maximum refund guarantees". Roster: NAICS 5412,
rank 1, supplementary set.

company: H&R Block, Inc.
document_title: H&R Block Terms of Use Agreement ("Artificial Intelligence and Automated Features")
document_type: t1-governing-terms (website; the DIY online license agreement was not reachable)
url: https://www.hrblock.com/universal/terms/
retrieved: 2026-10-06
effective_or_revised: not stated in rendered text
names_ai_feature: by category ("Automated Systems": digital assistants, chatbots, agents, avatars); AI Tax Assist not named
ai_vector: generative chat (tax Q&A)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with the complete AI section + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B3 (AI-specific: "solely responsible for verifying any information generated, for decisions you make, and for any actions or omissions"), B6 (AI-specific: may be incomplete, inaccurate or inappropriate; no warranty of accuracy), B2 (AI-specific: liability arising from use of AI features disclaimed), not-tax-advice (AI-specific)
files: mastersheet-sources/tax-prep/hr-block/hrblock_terms_CAPTURE-NOTE.md

company: H&R Block, Inc.
document_title: New H&R Block AI Tax Assist Provides DIY Tax Filers Instant, Unlimited Help ...
document_type: t6-marketing
url: https://www.hrblock.com/tax-center/newsroom/company-news/new-ai-tax-assist-diy/
retrieved: 2026-10-06 (search snippet; site returns 403 to scripts)
fetch_depth: snippet-only
files: none

company: H&R Block, Inc.
document_title: Digital/Online and Software License Agreement (DIY product terms; would carry the accuracy guarantee)
document_type: t1-governing-terms
url: attempted https://www.hrblock.com/universal/digital-online-and-software-license-agreement/ (403)
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

**AI section of the Terms of Use.** AI may "not always operate as intended". "Automated Systems"
(digital assistants, chatbots, agents, avatars) may give incomplete, inaccurate or inappropriate
responses; they are for information or convenience only and are not tax advice; the user remains
"solely responsible" for verifying information, decisions and resulting actions or omissions; no
warranties on AI output; liability arising from AI features disclaimed.

## Coder note
1. **Locus 2 (AI section inside general terms).**
2. **Sharpest say-do tension in the collection:** the launch release ties AI Tax Assist to the "100%
   accuracy and maximum refund guarantees", while the Terms of Use disclaim any liability from AI
   features and make users solely responsible. How the guarantee (in the DIY license agreement, not
   retrieved) treats AI-sourced errors is the key open question. Retrieve that agreement.
3. **Template diffusion (competitors):** the AI paragraph tracks Intuit's TurboTax "Digital
   Assistants" clause almost word for word ("digital assistants, ... agents, avatars, chatbots ...
   may not be unique ... inaccurate or inappropriate to your situation ... solely responsible for
   actions or omissions"). Add to the Exelon/BofA diffusion observation: shared drafting sources
   across rival firms.
4. **Gaps:** DIY license agreement and guarantee terms; release full text; date of Terms of Use.

---

<a name="avis"></a>
## Avis Budget Group - AI customer-support agent (Decagon) - collected 2026-10-06

**AI feature.** A Decagon-built AI customer-support agent (named in Decagon's 2026-01-28 funding
release as a customer). Rental support: reservations, changes, charges. Also ML-based biometric
identity verification for QuickPass/Avis First (decisional, consumer-affecting). Roster: NAICS 5321,
rank 2, supplementary set.

company: Avis Budget Group, Inc.
document_title: Avis Terms of Use
document_type: t1-governing-terms (website/app)
url: https://www.avis.com/en/legal-documents/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated December 4, 2023 (stated)
names_ai_feature: no - zero AI hits
ai_vector: generative/agentic chat (support)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/car-rental/avis-budget/avis_terms-of-use_RAW.html (+ .txt)

company: Avis Budget Group, Inc.
document_title: Avis Privacy Notice
document_type: privacy-notice
url: https://www.avis.com/en/legal-documents/privacy-notice
retrieved: 2026-10-06
effective_or_revised: Last Updated December 18, 2025 (stated)
names_ai_feature: no (discloses ML identity verification by vendors; session replay of chat text)
fetch_depth: full-fetch
clause_codes_present: B11-adjacent (ML + biometric facial comparison to verify identity for QuickPass/Avis First; a customer-affecting automated check), B10-adjacent (session-replay tools record text typed into chat features)
files: mastersheet-sources/car-rental/avis-budget/avis_privacy_RAW.html (+ .txt)

## Coding-relevant extract

The 2023 Terms of Use contain no AI language. The December 2025 privacy notice describes ML tools and
biometric facial comparison used by identity-verification vendors for QuickPass, and session-replay
tools that record text keyed into chat. Nothing on the AI support agent.

## Coder note
1. **Locus 5 for the support agent.**
2. **Decisional AI note:** QuickPass identity verification is consumer-facing in effect (it gates
   express rental); relevant to B11 coding even though it is not conversational.
3. **Evidence tier:** the support agent is evidenced by a vendor release (Decagon); flag for
   first-party confirmation and liveness at cutoff.
4. **Gaps:** rental agreement terms (counter/online rental agreement) not checked.

---

<a name="turo"></a>
## Turo - virtual agent / multilingual AI chatbot - collected 2026-10-06

**AI feature.** A virtual agent / multilingual AI chatbot for host and guest support (built on
Voiceflow per vendor case study). Peer-to-peer car rental: bookings, trip issues, claims. Roster:
NAICS 5321, rank 5, supplementary set (private).

company: Turo Inc.
document_title: Turo Terms of Service
document_type: t1-governing-terms
url: https://turo.com/us/en/policies/terms
retrieved: 2026-10-06
effective_or_revised: Last revised June 24, 2026 (stated) - inside the cutoff
names_ai_feature: no - zero AI hits
ai_vector: chat (support)
fetch_depth: full-fetch
clause_codes_present: B10-generic (web chat interactions monitored and recorded for quality control, training "or other purposes"; don't use chat if you object), B6/B2 (generic), B8 (marketplace: Turo not party to host-guest contract)
files: mastersheet-sources/car-rental/turo/turo_terms-of-service_RAW.html (+ .txt)

## Coding-relevant extract

The June 2026 Terms of Service mention web chat only to say interactions may be monitored or recorded
"for quality control, training, or other purposes"; no AI or chatbot language, no accuracy statement.
Generic AS-IS, damages, and marketplace terms.

## Coder note
1. **Locus 5 (absent), strong vintage finding:** revised six days before the cutoff, still silent.
2. **Evidence tier:** chatbot evidenced by vendor case study (Voiceflow); flag.
3. **Gaps:** Turo privacy policy; in-chat microcopy.

---

<a name="metropolis"></a>
## Metropolis Technologies (incl. SP+) - AI license-plate recognition that auto-charges - collected 2026-10-06

**AI feature.** Checkout-free parking: cameras read the plate on entry and exit and the card on
file is **charged automatically**, with no conversation. Included under the automated-transaction
rule adopted 2026-10-05 (an AI that bills the consumer). Also the "Metropolis Recognition Platform"
(facial recognition plus LPR) for hospitality (BLNQ) and security. Roster: NAICS 8129, rank 1,
supplementary set (private).

company: Metropolis Technologies, Inc.
document_title: Metropolis Terms of Service
document_type: t1-governing-terms
url: https://www.metropolis.io/terms
retrieved: 2026-10-06
effective_or_revised: Last updated July 16, 2026 (stated) - after the cutoff
names_ai_feature: yes - "Metropolis Recognition Platform (MRP) ... proprietary unified vision AI", LPR, BLNQ
ai_vector: decisional/transactional vision AI (auto-billing); biometric recognition
fetch_depth: full-fetch
clause_codes_present: payment authorization for any Transaction and future Transactions (consent to automated charging); refunds "case-by-case ... in its sole discretion" (anti-honoring of corrections, generic); detailed biometric consents (s.13); no clause on recognition errors, misreads or misattributed charges; generic B2/B6
files: mastersheet-sources/personal-services/metropolis/metropolis_terms_RAW.html (+ .txt)

company: Metropolis Technologies, Inc.
document_title: Metropolis Privacy Policy (with Supplemental ALPR Privacy Notice; MRP notice)
document_type: privacy-notice
url: https://www.metropolis.io/privacy
retrieved: 2026-10-06
effective_or_revised: Last updated August 20, 2026 (stated) - after the cutoff
names_ai_feature: yes (MRP, ALPR; technology from Oosto, a Metropolis subsidiary)
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: personal information used to "Train AI systems, including large language models and other machine learning systems"), B11-adjacent (automated identification and inferences, behavioral analytics)
files: mastersheet-sources/personal-services/metropolis/metropolis_privacy_RAW.html (+ .txt)

## Coding-relevant extract

The Terms define the recognition platform in detail and obtain consent to automated charging for any
transaction. Refunds are at Metropolis's "sole discretion", "case-by-case", and one refund creates no
obligation for the future. A keyword search found no clause addressing a misread plate, a wrongly
attributed charge, or a dispute process for recognition errors. The privacy policy states personal
information may be used to train AI systems including LLMs.

## Coder note
1. **Automated-transaction case (new class).** The AI does not speak; it bills. The relevant risk is
   a misread plate charging the wrong person. The contract's answer is discretionary refunds, the
   functional equivalent of a non-honoring position for AI errors (code as B1-analog, generic).
2. **Version problem:** both documents post-date the cutoff (July and August 2026). Retrieve
   pre-cutoff versions.
3. **Assent:** account/app sign-up for members; for drive-in non-members, assent is unclear
   (signage at the facility, not captured).

**Full-read addendum (2026-10-08).** Terms (MET-P-01) read in full. The AI-specific recognition-error disclaimer (Schedule C, C-7) and the MRP section 13 apply only to "Recognition Services" (BLNQ hospitality, Security Services). Checkout-free parking sits under an AI-silent Schedule A, so the disclaimer does not clearly reach a parking misread. MET-P-01 is coded locus none / generic only, with an alternative coding (locus 2, B2/B6/B11 S) logged for adjudication. Schedule A deems detection-triggered simultaneous-usage charges "valid" and pre-authorised. The privacy policy's ALPR exhibit (MET-P-02) promises a charge-dispute procedure for inaccurate charges, the only misread remedy in Metropolis's documents. See recollection/v2-coding-log.md.

---

<a name="odp"></a>
## ODP Corp (Office Depot, OfficeMax) - Oracle Digital Assistant chatbot - collected 2026-10-06

**AI feature.** An Oracle Digital Assistant chatbot in Office Depot's help chat (Oracle customer
material, screening evidence; the site links an Oracle Service Cloud chat launcher). ODP was acquired
by Atlas Holdings in 2025 (corporate identity fixed at cutoff). Roster: NAICS 4594, rank 1,
supplementary set.

company: The ODP Corporation (Office Depot, LLC)
document_title: Office Depot Terms of Use
document_type: t1-governing-terms
url: https://www.officedepot.com/cm/help/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Updated May 18, 2026 (stated) - inside the cutoff
names_ai_feature: no - zero AI hits ("Chat" only in a carrier name and a chat-launch link)
ai_vector: chat (support)
fetch_depth: full-fetch
clause_codes_present: B1 (generic: may refuse or cancel any order, including for inaccuracies or errors in product or pricing information), B6/B2 (generic)
files: mastersheet-sources/office-supplies/odp/officedepot_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

No AI language in the May 2026 Terms of Use. Generic: Office Depot may refuse or cancel any order for
any reason, including pricing or product-information errors.

## Coder note
1. **Locus 3/5 (generic B1; no AI language).** Revised inside the cutoff and still silent.
2. **Evidence tier:** chatbot's AI basis via vendor material (Oracle); flag.
3. **Gaps:** privacy policy; chat microcopy (custhelp.com launcher).

---

<a name="libertymedia"></a>
## Liberty Media (Formula One Group) - F1 fan companion agent on F1.com - collected 2026-10-06

**AI feature.** An Agentforce-powered "fan companion agent" on F1.com (launched 2026-03-03) answering
fans' questions about the 2026 technical regulations from F1 sources. Informational, very low
stakes. Roster: NAICS 7112, rank 2, supplementary set.

**Jurisdiction note.** Liberty Media is a US firm, but F1.com is operated by Formula One Digital Media
Limited (UK) and its Legal Notices are governed by the laws of England and Wales. The protocol's
home-market rule (collect US terms for US firms) has no US-specific F1.com terms to collect; the
global terms were used.

company: Liberty Media Corporation (Formula One Digital Media Limited)
document_title: Legal Notices (formula1.com terms of use)
document_type: t1-governing-terms
url: https://www.formula1.com/en/information/legal-notices.7egvZU48hzrypubGBNcQKt
retrieved: 2026-10-06 (browser read; innerText 22,642 chars; SHA-256 ccc064cafd6be68ca1b38498525c6cb42bdfce7a951c4f399184ce140bffc0ae)
effective_or_revised: not stated
names_ai_feature: no - zero AI hits (only a marketing tagline using "companion")
ai_vector: generative chat (informational)
fetch_depth: full-fetch (browser read; not saved as a capture note because there is no AI text to preserve; scripted fetch reset by host)
clause_codes_present: B6 (generic AS IS); English governing law
files: none (hash recorded here)

company: Salesforce (about Formula 1)
document_title: Formula 1 and Salesforce Deepen Partnership, Expanding Agentforce to Grow Fan Connection Worldwide
document_type: t6-marketing (vendor release)
url: https://www.salesforce.com/news/press-releases/2026/03/03/formula-1-agentforce-to-grow-fan-connection/
retrieved: 2026-10-06
effective_or_revised: March 3, 2026
fetch_depth: full-fetch
files: mastersheet-sources/spectator-sports/liberty-media/f1_TYPE6_agentforce-release_RAW.html (+ .txt)

## Coding-relevant extract

The F1.com Legal Notices contain no AI language. Generic AS-IS terms under English law.

## Coder note
1. **Locus 5 (absent).** Low-stakes informational agent.
2. **Scope question:** the deploying entity is a UK subsidiary of a US parent; flag for the
   jurisdiction rule and for whether Liberty Media belongs in the US sample at all for this feature.

---

<a name="sixflags"></a>
## Six Flags Entertainment Corp. - generative-AI virtual assistant - collected 2026-10-06

**AI feature.** A virtual assistant built on Google Cloud's Vertex AI Conversation, announced
2023-08-29 for the 2024 season, on the Six Flags app (day planning, personalized recommendations) and
park websites (answering customer queries in place of live agents). Six Flags merged with Cedar Fair
in 2024. Roster: NAICS 7131, rank 1, supplementary set.

company: Six Flags Entertainment Corporation
document_title: Six Flags Terms of Use
document_type: t1-governing-terms
url: https://www.sixflags.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last Updated October 28, 2025 (stated)
names_ai_feature: no - zero AI hits
ai_vector: generative chat (park information, ticket and pass questions)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/amusement-parks/six-flags/sixflags_terms-of-use_RAW.html (+ .txt)

company: Google Cloud / Six Flags
document_title: Six Flags to ... Launch a Cutting Edge Virtual Assistant Powered by Google Cloud's Generative AI
document_type: t6-marketing (joint release)
url: https://www.googlecloudpresscorner.com/2023-08-29-Six-Flags-to-Accelerate-Digital-Transformation-in-Amusement-Park-Industry-and-Launch-a-Cutting-Edge-Virtual-Assistant-Powered-by-Google-Clouds-Generative-AI
retrieved: 2026-10-06
effective_or_revised: August 29, 2023
fetch_depth: full-fetch
files: mastersheet-sources/amusement-parks/six-flags/sixflags_TYPE6_google-release_RAW.html (+ .txt)

## Coding-relevant extract

The October 2025 Terms of Use contain no AI language; generic AS-IS and damages terms only.

## Coder note
1. **Locus 5 (absent).** Terms revised after the merger (Oct 2025) without AI language.
2. **Gaps:** whether the assistant survived the Cedar Fair merger and was live at 2026-06-30;
   season-pass terms; privacy policy.

---

<a name="nerdy"></a>
## Nerdy (Varsity Tutors) - AI-enabled chat tutoring and Live+AI support - collected 2026-10-06

**AI feature.** AI chat tutoring (announced 2023-02) and "Live+AI" always-on AI support combined
with live tutors (2025), plus AI session summaries and AI education tools (ai.varsitytutors.com).
Educational-advisory stakes; many users are minors. Roster: NAICS 6116, rank 4, supplementary set.

company: Nerdy Inc. (Varsity Tutors LLC)
document_title: Varsity Tutors Terms of Use
document_type: t1-governing-terms
url: https://www.varsitytutors.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Updated October 8, 2025 (stated)
names_ai_feature: by category ("artificial intelligence or automated tools ... session summaries, chat interactions, and user support")
ai_vector: generative (tutoring chat, summaries, support)
fetch_depth: full-fetch
clause_codes_present: AI-disclosure + acknowledgement (AI-specific: tools "may operate without direct human oversight"; users agree to use the platform "with that understanding"), B6/B2 (generic AS IS, damages)
files: mastersheet-sources/tutoring/nerdy/varsitytutors_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

One AI paragraph: Varsity Tutors may use AI or automated tools for session summaries, chat
interactions and user support, under the Privacy Notice; users acknowledge such tools "may operate
without direct human oversight" and agree to use the platform on that understanding. No accuracy
disclaimer for AI tutoring content, no reliance language. Generic AS-IS and damages clauses.

## Coder note
1. **Locus 2-lite (AI disclosure/acknowledgement inside general terms).** Functionally an
   assumption-of-risk acknowledgement (no human oversight) rather than an output disclaimer. Similar
   in kind to Cox's disclosure clause; slightly stronger.
2. **Vintage:** Oct 2025, after both AI launches.
3. **Gaps:** separate terms for ai.varsitytutors.com tools (if any); privacy notice; minors' terms.

---

<a name="thredup"></a>
## ThredUp - Style Chat (GenAI outfit chatbot) and AI image search - collected 2026-10-06

**AI feature.** Style Chat, a generative-AI outfit assistant, and AI image search (launched
2024-08-05). Roster: NAICS 4595, rank 5, supplementary set.

company: ThredUp Inc.
document_title: ThredUp Terms of Use ("Artificial Intelligence ('AI') Features")
document_type: t1-governing-terms
url: https://www.thredup.com/legal/tou
retrieved: 2026-10-06
effective_or_revised: Last Updated July 14, 2025 (stated)
names_ai_feature: by category ("AI Features": LLMs, ML)
ai_vector: generative chat + image search
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI section + innerText SHA-256 (HTTP 403 to scripts)
clause_codes_present: B3/B4 (AI-specific: "solely responsible ... for evaluating the accuracy of any Output"), B6 (AI-specific: no guarantee of accuracy), B10 (AI-specific: Inputs used to improve AI; ThredUp owns all AI-Generated Content, incl. content trained on aggregated User Content; user assigns rights and waives compensation), B9 (AI-specific: no passing AI content off as human; no high-risk or unverified health/political advice uses; no scraping), B11-negative (AI not used for legal or significant decisions), B1 (generic: pricing/typographical errors)
files: mastersheet-sources/used-merchandise/thredup/thredup_tou_CAPTURE-NOTE.md

## Coding-relevant extract

The AI Features section defines AI Features (search, listings, recommendations), states they are not
used for significant decisions (B11-negative), makes the user solely responsible for evaluating
Output accuracy with no guarantee (B3/B4/B6), and claims exclusive ownership of AI-generated content,
including content created from aggregated user content, with users assigning rights and waiving
compensation (B10, aggressive). Prohibited uses include misrepresenting AI content as human-made.

## Coder note
1. **Locus 2 (dedicated AI section inside general terms).**
2. **Ownership grab** over AI-generated derivatives of user content is unusual and notable (B10).
3. **Vintage:** July 2025, about a year after the AI launch.
4. **Gaps:** privacy policy; Style Chat microcopy; release page (timed out).

---

<a name="paypal"></a>
## PayPal Holdings - PayPal Assistant (generative AI) - collected 2026-10-06

**AI feature.** PayPal Assistant, "our AI-powered digital assistant that helps you get answers, take
actions, and explore PayPal features" via the app's Search & Intelligence and the Message Center
(web and app); hands off to live agents. Agentic ("take actions"). Roster: NAICS 5223, rank 1,
supplementary set.

company: PayPal Holdings, Inc. (PayPal, Inc.)
document_title: PayPal User Agreement (full)
document_type: t1-governing-terms
url: https://www.paypal.com/us/legalhub/paypal/useragreement-full
retrieved: 2026-10-06
effective_or_revised: Last updated on September 14, 2026 (stated) - after the cutoff
names_ai_feature: no (one AI mention: arbitration filings)
ai_vector: generative chat + actions
fetch_depth: full-fetch
clause_codes_present: AI-in-procedure (any arbitration submission containing AI-generated content must be certified as personally verified); B1-generic (business users: 60 days to report pricing/fee errors or accept as accurate); B6/B2 (generic)
files: mastersheet-sources/payments-fintech/paypal/paypal_user-agreement_RAW.html (+ .txt)

company: PayPal Holdings, Inc.
document_title: What is PayPal Assistant and what can it do? (help article)
document_type: t4-in-product-microcopy (help article quoting the in-chat disclaimer)
url: https://www.paypal.com/us/cshelp/article/what-is-paypal-assistant-and-what-can-it-do-help1072
retrieved: 2026-10-06
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: B6/B4 (AI-specific, in-chat: "AI can make mistakes, so double-check responses"), B10 (chat may be recorded and used by PayPal)
files: mastersheet-sources/payments-fintech/paypal/paypal_assistant-help_RAW.html (+ .txt)

## Coding-relevant extract

The 175k-character User Agreement says nothing about PayPal Assistant. Its only AI language is
procedural: in arbitration, a party submitting AI-generated content must certify they verified its
accuracy. That is a verification duty imposed on customers' AI use in disputes, not on PayPal's AI.
The help article reports that each new chat opens with "AI can make mistakes, so double-check
responses. Your chat may be recorded and used by PayPal."

## Coder note
1. **Locus 4 (microcopy-only) for the assistant.** Asymmetry worth a line in the paper: PayPal's
   contract demands that customers verify AI output they submit in arbitration, while placing no
   contractual qualification on its own AI's statements to customers.
2. **Version:** Sept 2026 agreement (after cutoff); pre-cutoff version needed, though silence on the
   assistant likely holds.
3. **Gaps:** PayPal Assistant launch date; privacy statement (AI section).

**Full-read addendum (2026-10-08).** User Agreement read in full. It names no AI apart from the arbitration rule requiring AI-generated submissions to be certified. That sentence, plus the FRCP 68 and no-preclusion sentences, is identical to Metropolis's arbitration clause (shared template). A generic exclusion covers "errors, or inaccuracies of any kind" in the services "or in the information… obtained from them". Delegated-access clauses make the user responsible when someone given account access exceeds authority, and PayPal does not "Act as your agent", in tension with the Assistant's "take actions" positioning. The revision date (Sep 14 2026) is after the cutoff.

---

<a name="block"></a>
## Block, Inc. (Cash App) - Moneybot / AI-Powered Chat and Interfaces - collected 2026-10-06

**AI feature.** Moneybot, an agentic AI assistant in Cash App (announced in the Fall 2025 release;
integration "this winter"), plus AI-Powered Chat and AI-Powered Interfaces that suggest actions,
summarize usage and answer questions using account data. Financial stakes. Roster: NAICS 5223,
rank 2, supplementary set.

company: Block, Inc. (Cash App)
document_title: Cash App Terms of Service (incl. "AI-Powered Interactions", "Use of AI-Powered Features" and s.XXII "Generative AI Terms of Use")
document_type: t1-governing-terms (with an embedded dedicated AI terms part)
url: https://cash.app/legal/us/en-us/tos
retrieved: 2026-10-06
effective_or_revised: header shows "Effective: February 7, 2024", but the document contains AI-Powered sections that refer to later features; section-level revision dates not isolated (date_basis: stated, but likely stale for the AI sections; flag)
names_ai_feature: by category ("AI-Powered Chat", "AI-Powered Interfaces", "AI Products"); Moneybot not named
ai_vector: generative chat + agentic (suggested actions on payments/investing)
fetch_depth: full-fetch (~315k chars)
clause_codes_present: B5 (AI-specific, agentic guardrail: "no action will occur without your explicit confirmation"; user responsible for reviewing and confirming all actions before execution), not-advice and no-fiduciary-duty (AI-specific: outputs "do not create an advisory, brokerage, or fiduciary relationship"), B3/B4 (AI-specific: user bears "ultimate responsibility for evaluating the information"; not to be relied on as personalized advice), B6-partial (AI-specific: outputs automated and may not reflect full circumstances), B9 (AI-specific acceptable-use policy in s.XXII: no passing AI content as human, no misuse), B10-adjacent (AI processes account information, transaction history, balances within Cash App's architecture), Cash App Investing disclosures incorporated for AI Products
files: mastersheet-sources/payments-fintech/block/cashapp_terms-of-service_RAW.html (+ .txt)

## Coding-relevant extract

**"Use of AI-Powered Features."** AI chat and interfaces may display suggestions and potential
actions, answer questions, or route to app functions; informational only, not financial, investment,
legal or tax advice; the user reviews and confirms all actions, and "no action will occur without
your explicit confirmation" (B5).

**"AI-Powered Interactions."** Outputs are informational, automated and may not reflect the user's
full circumstances; they create no advisory, brokerage or fiduciary relationship; the user bears
"ultimate responsibility" for evaluating AI information and confirming any suggested action.

**s.XXII "Generative AI Terms of Use."** Using any AI Product means agreeing to these terms:
acceptable-use rules (no misleading use, no passing AI content off as human, no seeking or giving
specialized advice through AI Products, no reverse engineering). Cash App Investing disclosures apply
to AI Products that touch investing.

## Coder note
1. **Locus 1-in-2 (a dedicated "Generative AI Terms of Use" part embedded in the general terms) plus
   AI sections elsewhere.** The explicit-confirmation guardrail is the clearest agentic-AI clause in
   the collection (B5 as a design commitment, not just a disclaimer).
2. **Date problem:** header date (Feb 2024) predates Moneybot; the AI sections were evidently added
   later. Determine the true revision date of the AI sections, and the version in force at
   2026-06-30.
3. **No-fiduciary language** again (Vanguard, Gen Digital, Cash App): a pattern in finance-adjacent
   AI terms.

**Full-read addendum (2026-10-08).** ToS read in full (gray-box annotations are declared non-binding and were not coded). The coded date is "Last Updated Sep 11 2026", after the cutoff, so the AI clauses may post-date 2026-06-30. Confirmation-gating ("no transaction… will be executed solely on the basis of a conversational interaction") is coded B5 S and flagged as a channel-limitation device. Users are barred from using the AI to "Obtain… financial… advice". The AI-specific vendor pass-through ("your use is subject to the terms of those third parties") is coded B8 S, borderline.

---

<a name="remitly"></a>
## Remitly Global - AI-powered virtual support assistant - collected 2026-10-06

**AI feature.** An "AI-powered virtual support assistant" in the redesigned Help Center (announced
2024-07-31), in 18 languages, alongside AI search. Cross-border money transfers: stakes include
transfer status, fees and exchange rates. Roster: NAICS 5223, rank 5, supplementary set.

company: Remitly Global, Inc. (Remitly, Inc.)
document_title: Remitly User Agreement (US)
document_type: t1-governing-terms
url: https://www.remitly.com/us/en/home/agreement
retrieved: 2026-10-06
effective_or_revised: Effective Date February 23, 2026 (stated)
names_ai_feature: no - zero AI hits
ai_vector: chat (support)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic); transfer-error rights governed by federal remittance rules
files: mastersheet-sources/payments-fintech/remitly/remitly_user-agreement_RAW.html (+ .txt)

company: Remitly
document_title: Introducing the New and Improved Remitly Help Experience
document_type: t6-marketing
url: https://news.remitly.com/company-and-product-news/reintroducing-the-remitly-help-center/
retrieved: 2026-10-06
effective_or_revised: July 31, 2024
fetch_depth: full-fetch
files: mastersheet-sources/payments-fintech/remitly/remitly_TYPE6_help-center_RAW.html (+ .txt)

## Coding-relevant extract

The February 2026 User Agreement contains no AI language; only generic clauses (error resolution for
remittances follows federal remittance-transfer rules, which cap what a contract can disclaim).

## Coder note
1. **Locus 5 (absent).** Revised Feb 2026, 18 months after the assistant launched; still silent.
2. **Regulatory context:** CFPB Remittance Rule (Reg E subpart B) error-resolution rights apply
   regardless of contract silence.
3. **Gaps:** privacy notice; assistant microcopy.

---

<a name="royalcaribbean"></a>
## Royal Caribbean Group - virtual assistant in chat - collected 2026-10-06

**AI feature.** A virtual assistant in Royal Caribbean's website and app chat (screening evidence:
third-party guide describing the assistant as the first point of contact). Cruise booking and
pre-cruise questions. Roster: NAICS 4831, rank 2, supplementary set. Evidence tier weak (flag).

company: Royal Caribbean Cruises Ltd.
document_title: Digital Terms of Use and End User License Agreement
document_type: t1-governing-terms (website and apps)
url: https://www.royalcaribbean.com/terms-and-conditions/digital-terms-of-use-and-end-user-license-agreement
retrieved: 2026-10-06
effective_or_revised: Last Updated March 2023 (stated)
names_ai_feature: no - "Chat" refers only to guest-to-guest messaging onboard
ai_vector: chat (booking/support)
fetch_depth: full-fetch
clause_codes_present: B1 (generic, strong: not responsible for pricing or typographical errors; may "cancel without liability any bookings made at erroneous rates"; may cancel orders for pricing inaccuracies), B6/B2 (generic)
files: mastersheet-sources/cruise-lines/royal-caribbean/rcl_digital-terms-eula_RAW.html (+ .txt)

## Coding-relevant extract

No AI language in the March 2023 digital terms; "Chat" means onboard guest-to-guest messaging. Generic
B1: the company may cancel bookings made at erroneous rates without liability and may cancel orders
for pricing or availability errors.

## Coder note
1. **Locus 3 (generic B1) / no AI language.**
2. **Cruise contract** (guest-terms) not checked: it governs voyages and likely also AI-silent.
3. **Evidence:** customer-facing AI virtual assistant should be confirmed from a first-party source;
   the screening evidence is a third-party blog.

---

<a name="norwegian"></a>
## Norwegian Cruise Line Holdings - Nora (GenAI itinerary/booking assistant) - collected 2026-10-06

**AI feature.** Nora, a GenAI chatbot at ncl.com/ai-assistant (built with Slalom on OpenAI and AWS)
that recommends itineraries from guests' preferences, including price ("a family-friendly cruise ...
at a low price"); Slalom reports guests using Nora are 58% more likely to enter the booking funnel.
Roster: NAICS 4831, rank 3, supplementary set.

company: Norwegian Cruise Line Holdings Ltd.
document_title: NCL Terms & Conditions page (website terms, cookie policy, guest ticket contract and additional terms)
document_type: t1-governing-terms
url: https://www.ncl.com/terms
retrieved: 2026-10-06
effective_or_revised: Effective January 26, 2026 (stated)
names_ai_feature: no - zero AI hits across ~440k chars
ai_vector: generative chat (itinerary search; price-related answers)
fetch_depth: full-fetch
clause_codes_present: B1-weak (generic: not responsible for typographical errors, omissions or misprints; may correct website), B6/B2 (generic), carrier limits in ticket contract
files: mastersheet-sources/cruise-lines/norwegian/ncl_terms_RAW.html (+ .txt)

company: Slalom (about NCL)
document_title: GenAI guides guests to dream cruise vacations (customer story)
document_type: t6-marketing (vendor case study)
url: https://www.slalom.com/us/en/customer-stories/norwegian-cruise-line-generative-ai
retrieved: 2026-10-06
fetch_depth: full-fetch
files: mastersheet-sources/cruise-lines/norwegian/ncl_TYPE6_slalom-case_RAW.html (+ .txt)

company: Norwegian Cruise Line
document_title: Nora - NCL's AI Assistant page
document_type: t4-in-product-microcopy
url: https://www.ncl.com/ai-assistant
retrieved: 2026-10-06 (browser: content hidden behind a cookie-consent banner; consent not given, so page text beyond the banner was not read)
fetch_depth: referenced-not-located
files: none

## Coding-relevant extract

The January 2026 NCL terms page, which bundles website terms, cookie policy and the guest ticket
contract, contains no AI language. The only error language is generic (typographical errors,
omissions, misprints; right to correct).

## Coder note
1. **Locus 5 (absent).** Revised January 2026, after Nora launched (by 2025); silent.
2. **Moffatt relevance:** Nora answers price-sensitive itinerary questions on the booking path.
3. **Gaps:** Nora page microcopy (cookie wall; would need user consent choice); privacy policy.

**Full-read addendum (2026-10-08).** The ~445 KB hub (~20 sub-documents) was read in full after removing verified JSON-attribute duplicates (word 6-gram check: 14 of 31,549 unmatched, all markup). It contains no AI language. The website Legal Notice tells users to "verify information obtained from this site before you act upon it by calling NCL or your travel agent" (B4 G) and makes communications sent to the site usable for any purpose (B10 G). Bookings are governed by the Guest Ticket Contract, which is linked but **not captured** (gap). The provisional 1/26/2026 date was an air-policy date; the hub as a whole is undated.

---

<a name="barnesnoble"></a>
## Barnes & Noble - Ada AI support agent - collected 2026-10-06

**AI feature.** An Ada-powered AI support agent in the B&N help center (evidenced by an archived
help-center page, June 2026, in screening). Order and account support. Roster: NAICS 4592, rank 1,
supplementary set (private).

company: Barnes & Noble Booksellers, Inc.
document_title: Barnes & Noble Terms of Use
document_type: t1-governing-terms
url: https://www.barnesandnoble.com/terms/terms-of-use
retrieved: 2026-10-06
effective_or_revised: last revised on September 16, 2024 (stated)
names_ai_feature: no - zero AI hits
ai_vector: chat (support)
fetch_depth: full-fetch
clause_codes_present: B1 (generic: for incorrectly priced items B&N may contact the user, cancel the order, or "ship the item at the incorrect price to the benefit of the User", at its sole discretion), B6/B2 (generic)
files: mastersheet-sources/bookstores/barnes-noble/bn_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

No AI language. The pricing clause is notable for listing honoring the wrong price as one of B&N's
options (at its discretion), alongside cancellation.

## Coder note
1. **Locus 3/5 (generic B1; no AI language).**
2. **Vintage:** Sept 2024; AI agent status by 2026 rests on an archived help page (vendor Ada).
3. **Gaps:** help-center chat microcopy; privacy policy.

---

<a name="coursera"></a>
## Coursera (incl. Udemy since 2026-05-11) - Coursera Coach (GenAI tutor) - collected 2026-10-06

**AI feature.** Coursera Coach, a generative-AI tutor (Gemini) in courses (2023, expanded 2024-26);
Udemy's AI Assistant after the 2026 merger. Educational-advisory stakes. Roster: NAICS 6114, rank 1,
supplementary set.

company: Coursera, Inc.
document_title: Coursera Terms of Use (s.10 Disclaimers; AUP; Honor Code)
document_type: t1-governing-terms
url: https://www.coursera.org/about/terms
retrieved: 2026-10-06
effective_or_revised: Effective January 1, 2026 (stated)
names_ai_feature: by category ("Services that use AI", "AI-enhanced services", "AI outputs"); Coach not named
ai_vector: generative (tutoring)
fetch_depth: full-fetch
clause_codes_present: B6 (AI-specific: services using AI provided AS IS), B4 (AI-specific: "you must verify any AI outputs that you use in your coursework"), B2 (AI-specific: "Coursera is not responsible for inaccurate or incomplete AI outputs"), B9 (AI-specific: AUP; no claiming AI content as your own; no training AI on Coursera content; Honor Code bars unauthorized gen-AI tools in graded work), B10 (AI-modified derivative works excluded from User Content)
files: mastersheet-sources/online-training/coursera/coursera_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

s.10 (Disclaimers, in capitals): some Coursera services use AI and are provided "AS IS"; users "must
verify any AI outputs" used in coursework, and Coursera "is not responsible for inaccurate or
incomplete AI outputs"; AI use is subject to the Acceptable Use Policy; refers to an AI disclosure in
the privacy notice. Elsewhere: no presenting AI-generated content as one's own; no training AI on
Coursera content; the Honor Code counts unauthorized gen-AI tool use (e.g. ChatGPT) as misconduct,
which sits awkwardly with Coursera's own AI tutor.

## Coder note
1. **Locus 2 (AI language inside the disclaimers section).**
2. **Coursework framing:** the verification duty is tied to academic work, the main stakes.
3. **Gaps:** privacy notice AI disclosure (referenced, not fetched); Udemy terms after merger; Coach
   microcopy.

---

<a name="upbound"></a>
## Upbound Group (Rent-A-Center, Acima) - "Digital Assistant" chatbot - collected 2026-10-06

**AI feature.** An automated "Digital Assistant" chat on rentacenter.com that "may utilize artificial
intelligence" (Salesforce Einstein Bot per screening) and answers questions. Lease-to-own customers
are often credit-constrained; the privacy policy also discloses AI analytics predicting "potential
risks" from income, employment, payment history and biometric data. Roster: NAICS 5322, rank 1,
supplementary set.

company: Upbound Group, Inc.
document_title: Upbound Group, Inc. Privacy Policy (rentacenter.com)
document_type: privacy-notice
url: https://www.rentacenter.com/en-us/privacy-policy
retrieved: 2026-10-06
effective_or_revised: Last Updated September 29, 2026 (stated) - after the cutoff
names_ai_feature: yes - "Digital Assistant" (AI)
ai_vector: chat (support); decisional analytics (risk prediction)
fetch_depth: full-fetch (browser) - preservation: CAPTURE-NOTE with verbatim AI passages + innerText SHA-256
clause_codes_present: AI-disclosure (bot is automated, not a person; conversation recorded and shared with service provider), B11 (AI models predicting "potential risks" using income, employment, payment history, ID/biometric data; no AI decisions about children under 13)
files: mastersheet-sources/consumer-goods-rental/upbound/upbound_privacy_CAPTURE-NOTE.md

company: Upbound Group, Inc.
document_title: General website terms of use
document_type: t1-governing-terms
url: none linked (footer lists only ePay Terms and SMS/MMS Text Terms)
fetch_depth: referenced-not-located (no general terms found; ePay and SMS terms not fetched)
files: none

## Coding-relevant extract

The only AI language is in the privacy policy: the Digital Assistant is an automated program, not a
person; chats are recorded and shared with a vendor. The policy also discloses AI analytics that
predict "potential risks" using income, employment and biometric data, which is relevant to B11 given
the lease-to-own credit context. No document addresses accuracy of chatbot answers.

## Coder note
1. **Locus 4/5:** disclosure only; no binding terms reach the chatbot (no general terms of use found).
2. **Version:** privacy policy post-dates cutoff.
3. **Gaps:** ePay Terms and lease agreements (point-of-lease contracts) not checked; Acima terms.

---

<a name="livenation"></a>
## Live Nation Entertainment (Ticketmaster) - fan-support virtual assistant; Agentforce venue agents - collected 2026-10-06

**AI feature.** Ticketmaster's virtual assistant for fan support chat (by 2025) and Salesforce
Agentforce agents on 120 venue websites (screening evidence: Ticketmaster business blog). Ticketing
stakes: refunds, transfers, event changes. Roster: NAICS 7113, rank 1, supplementary set.

company: Live Nation Entertainment, Inc. (Ticketmaster L.L.C.)
document_title: Ticketmaster Terms of Use
document_type: t1-governing-terms
url: https://legal.ticketmaster.com/terms-of-use/
retrieved: 2026-10-06 (browser read; innerText 45,408 chars; SHA-256 0a2cb5dde84825adbfa66f4da3877d0dfead1a623177212ec99d68ecb9f72a84)
effective_or_revised: Effective Date August 12, 2025 (stated)
names_ai_feature: no - zero AI hits
ai_vector: chat (fan support) + venue agents
fetch_depth: full-fetch (browser read; scripted fetch returns an 896-char shell; hash recorded, no AI text to preserve)
clause_codes_present: generic only (no AI or error-honoring language surfaced)
files: none (hash recorded here)

## Coding-relevant extract

The August 2025 Ticketmaster Terms of Use contain no AI language. Ticket refund and exchange rules
live in the Purchase Policy (not fetched), which an AI assistant could misstate.

## Coder note
1. **Locus 5 (absent).**
2. **Gaps:** Ticketmaster Purchase Policy; the screening blog URL now 404s; venue-site Agentforce
   agents are on venues' own sites (separate terms per venue, not collected).

---

<a name="2u"></a>
## 2U (edX) - Xpert AI learning assistant - collected 2026-10-06

**AI feature.** Xpert, an OpenAI-based AI learning assistant on edX (launched 2023-05-12) that answers
learners' course questions and summarizes content. Educational-advisory stakes. Roster: NAICS 6117,
rank 1, supplementary set (private after the 2024 Chapter 11).

company: 2U, Inc. (edX LLC)
document_title: edX Terms of Service and Honor Code
document_type: t1-governing-terms
url: https://www.edx.org/edx-terms-service
retrieved: 2026-10-06
effective_or_revised: Last Updated November 3rd, 2025 (stated)
names_ai_feature: no - AI words appear only in site navigation (course catalog), not in the terms body
ai_vector: generative (learning Q&A)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/educational-support/2u/edx_terms-of-service_RAW.html (+ .txt)

## Coding-relevant extract

The November 2025 edX Terms of Service and Honor Code contain no AI language in the body (no
Xpert, no AI outputs, no Honor Code rule on generative AI). Generic AS-IS and damages clauses.

## Coder note
1. **Locus 5 (absent).** Contrast with Coursera (same sector), whose 2026 terms disclaim AI outputs
   and whose Honor Code addresses gen-AI tools.
2. **Vintage:** Nov 2025, 2.5 years after Xpert's launch.
3. **Gaps:** Xpert in-product microcopy; edX privacy policy.

---

<a name="lyft"></a>
## Lyft - customer care AI assistant - collected 2026-10-06

**AI feature.** A customer-care AI assistant built on Anthropic's Claude via Amazon Bedrock
(announced 2025-02-06): fast answers to common support issues, handoff to human specialists; Lyft
reports an 87% cut in average resolution time. Rider support: fares, charges, refunds, lost items.
Roster: NAICS 4853, rank 2, supplementary set.

company: Lyft, Inc.
document_title: Lyft Terms of Service
document_type: t1-governing-terms
url: https://www.lyft.com/terms
retrieved: 2026-10-06
effective_or_revised: Last Updated February 9, 2026 (stated)
names_ai_feature: by category only: "artificial intelligence tools" listed in the definition of the "Lyft Platform"
ai_vector: generative chat (support)
fetch_depth: full-fetch
clause_codes_present: generic clauses reaching AI tools by definition (B6 AS IS, B2 limitation, arbitration); no AI-specific accuracy or reliance clause
files: mastersheet-sources/ride-hailing/lyft/lyft_terms-of-service_RAW.html (+ .txt)

company: Lyft, Inc.
document_title: Lyft and Anthropic Team Up to Redefine Customer-Obsessed AI (Lyft blog)
document_type: t6-marketing
url: https://www.lyft.com/blog/posts/lyft-and-anthropic-team-up-to-redefine-customer-obsessed-ai
retrieved: 2026-10-06
effective_or_revised: February 6, 2025
fetch_depth: full-fetch
files: mastersheet-sources/ride-hailing/lyft/lyft_TYPE6_anthropic-blog_RAW.html (+ .txt)

## Coding-relevant extract

The February 2026 Terms define the "Lyft Platform" to include Lyft's "artificial intelligence tools",
so every generic platform clause (AS IS, damages limits, arbitration) expressly reaches the AI
assistant. There is no clause on AI accuracy, reliance, or the status of AI answers about fares and
refunds.

## Coder note
1. **Locus 3 (generic clauses expressly reaching AI by definition).** Same technique as Columbia
   Gas (chatbots in the "Website" definition).
2. **Vintage:** revised Feb 2026, a year after the assistant launched.
3. **Say-do:** Lyft promises the "character and human tone" of Claude and "empathetic" AI; no
   disclaimer of its answers.
4. **Gaps:** privacy notice; in-app microcopy.

---

<a name="ups"></a>
## UPS - UPS Virtual Assistant - collected 2026-10-06

**AI feature.** The UPS Virtual Assistant, an AI chatbot on ups.com (by 2023; vendor case study in
screening) handling tracking, delivery changes and shipping questions. Delivery-change actions are
agentic. Roster: NAICS 4921, rank 1, supplementary set.

company: United Parcel Service, Inc.
document_title: UPS Website Terms of Use (US)
document_type: t1-governing-terms (website)
url: https://www.ups.com/us/en/support/shipping-support/legal-terms-conditions/website-terms-of-use
retrieved: 2026-10-06 (browser read; innerText 21,079 chars; SHA-256 1b086c3415e30352a0b90804f9a292e9a5179ad59d0875ec41b5bf34a5fdc35a)
effective_or_revised: not stated in rendered text
names_ai_feature: no - zero AI hits
ai_vector: chat (tracking, delivery changes)
fetch_depth: full-fetch (browser read; scripted fetch returns a 193-char shell; no AI text to preserve, hash recorded)
clause_codes_present: generic only
files: none (hash recorded here)

## Coding-relevant extract

No AI language in the Website Terms of Use. Liability for shipments is governed by the UPS Tariff /
Terms and Conditions of Service (not fetched), which carry strict liability limits.

## Coder note
1. **Locus 5 (absent).**
2. **Gaps:** UPS Tariff/Terms and Conditions of Service; Virtual Assistant microcopy; first-party
   evidence of the assistant's AI basis (vendor case study only).

---

<a name="fedex"></a>
## FedEx - FedEx Virtual Assistant (AI chatbot; Nuance-based since 2017) - collected 2026-10-06

**AI feature.** FedEx Virtual Assistant, an AI chatbot on fedex.com (since 2017, originally
Nuance-based) for tracking, delivery and shipping questions; also AI customs tools. Roster: NAICS
4921, rank 2, supplementary set.

company: FedEx Corporation
document_title: FedEx.com Terms of Use (US)
document_type: t1-governing-terms (website)
url: https://www.fedex.com/en-us/terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: not stated in captured text
names_ai_feature: no - zero AI hits
ai_vector: chat (tracking/support)
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/couriers/fedex/fedex_terms-of-use_RAW.html (+ .txt)

## Coding-relevant extract

No AI language. Shipment liability sits in the FedEx Service Guide (not fetched), which caps carrier
liability regardless of what the assistant says.

## Coder note
1. **Locus 5 (absent).**
2. **Gaps:** FedEx Service Guide; Virtual Assistant microcopy; date of terms.

---

<a name="koa"></a>
## Kampgrounds of America (KOA) - KOA AI chatbot - collected 2026-10-06

**AI feature.** KOA AI, a generative chatbot embedded on KOA.com and trained on KOA.com content;
announced in open beta by a KOA blog post dated January 18, 2024. It answers questions about KOA and
camping, which puts it near reservations. Roster: NAICS 7212.

company: Kampgrounds of America, Inc.
document_title: Website Terms of Use
document_type: t1-governing-terms
url: https://koa.com/privacy/terms-of-use/
retrieved: 2026-10-06
effective_or_revised: Last updated September 12, 2011 (stated)
names_ai_feature: no (AI appears only in the site chrome and the embedded chat widget on the page, not in the terms text)
ai_vector: generative chat
fetch_depth: full-fetch
clause_codes_present: B1-weak (generic: site information may contain errors; KOA may correct errors and discontinue services), B6/B2 (generic)
files: mastersheet-sources/campgrounds/koa/koa_terms-of-use_RAW.html (+ .txt)

company: Kampgrounds of America, Inc.
document_title: KOA AI chat onboarding microcopy (embedded on every KOA.com page) + "Engage With KOA's AI Chatbot Feature Today" blog
document_type: t4-in-product-microcopy + t6-marketing
url: https://koa.com/blog/new-ai-chatbot-for-koa/
retrieved: 2026-10-06
effective_or_revised: blog dated January 18, 2024; widget text current
names_ai_feature: yes ("KOA AI")
fetch_depth: full-fetch
clause_codes_present: B6/B4 (AI-specific, in-product: "may occasionally generate incorrect or misleading information"; use the button to flag unhelpful responses), scope limit (only KOA and camping topics), B10 (flagged conversations reviewed to improve safety systems), incorporation notice ("your use of KOA AI is covered by our Terms of Service and Privacy Policy"), open-beta notice
files: mastersheet-sources/campgrounds/koa/koa_TYPE6_chatbot-blog_RAW.html (+ .txt)

## Coding-relevant extract

**In-product onboarding (verbatim key sentence):** KOA AI "uses the content on KOA.com to answer your
questions, but it may occasionally generate incorrect or misleading information." The widget states
the AI is in open beta, limited to KOA and camping topics, that flagged conversations are reviewed,
and that use "is covered by our Terms of Service and Privacy Policy".

**The Terms it points to** are dated September 12, 2011, more than a decade before generative AI,
and contain no AI language: generic errors, AS-IS and damages clauses only.

## Coder note
1. **Locus 4 (microcopy) with an incorporation pointer to stale terms.** A clean illustration that
   in-product notices can promise contractual coverage that the contract itself never addresses.
2. **Vintage:** the oldest governing document in the v2 collection (2011).
3. **Gaps:** franchisee campground terms; reservation terms; privacy policy.

**Full-read addendum (2026-10-08).** The KOA AI chat widget's onboarding text (rendered in the captured page HTML on both the Terms and blog pages) states that use of KOA AI "is covered by our Terms of Service". The governing instrument for a Jan 2024 generative chatbot is therefore *expressly* the Sep 12 2011 Website Terms, about 12 years older than the AI. The 2011 Terms say services will not necessarily be available "on the basis of any indicated terms or conditions" (B1 G), cap liability at $5, and assign to KOA all materials sent to KOA "or a third party provider on this Site" (B10 G).

---

<a name="greystar"></a>
## Greystar Real Estate Partners - AI leasing / resident chatbots - collected 2026-10-06

**AI feature.** Greystar-managed property websites and greystar.com offer AI chatbots, and Greystar
is a named EliseAI customer: an AI leasing and resident assistant that schedules tours, answers
questions and sends payment and renewal messages over web chat, SMS and email. Per Greystar's own
privacy statement, its site chatbot runs on Microsoft GPT models. Transaction stakes are high:
rent, fees, lease terms and renewals. Roster: NAICS 5313.

company: Greystar Real Estate Partners, LLC
document_title: Terms of Use (greystar.com)
document_type: t2-site-terms
url: https://www.greystar.com/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Last updated December 29, 2020 (stated)
names_ai_feature: no - zero AI hits
ai_vector: generative chat
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/real-estate/greystar/greystar_terms-of-use_RAW.html (+ .txt)

company: Greystar Real Estate Partners, LLC
document_title: Resident App Terms of Use
document_type: t1-governing-terms (resident app)
url: https://www.greystar.com/terms-of-use/resident-app-terms
retrieved: 2026-10-06
effective_or_revised: Last updated August 9, 2024 (stated)
names_ai_feature: no - zero AI hits
fetch_depth: full-fetch
clause_codes_present: B6, B2 (generic)
files: mastersheet-sources/real-estate/greystar/greystar_resident-app-terms_RAW.html (+ .txt)

company: Greystar Real Estate Partners, LLC
document_title: Global Privacy Statement - "AI tools" section
document_type: privacy-notice
url: https://www.greystar.com/privacy/global-privacy-policy
retrieved: 2026-10-06
effective_or_revised: no stated effective date; the text carries the dates June 23, 2026 and May 25, 2025 (context of the June date unconfirmed)
names_ai_feature: yes, generically ("AI chatbot", Microsoft GPT models)
fetch_depth: full-fetch
clause_codes_present: B10 (AI-specific: prompts may be used to improve chatbot responses; shared with Microsoft to provide the service), B11 (AI-specific negative ADM statement: chatbot not used for automated decision-making)
files: mastersheet-sources/real-estate/greystar/greystar_global-privacy_RAW.html (+ .txt)

company: Greystar Real Estate Partners, LLC
document_title: US State Law Privacy Notice
document_type: privacy-notice
url: https://www.greystar.com/privacy/us-state-law-privacy-notice
retrieved: 2026-10-06
effective_or_revised: Effective July 29, 2024 (stated)
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: none AI-relevant
files: mastersheet-sources/real-estate/greystar/greystar_us-state-privacy_RAW.html (+ .txt)

company: Greystar Real Estate Partners, LLC
document_title: "Are AI Chatbots Shaping the Future of Rental Housing Processes?" (blog)
document_type: t6-marketing
url: https://www.greystar.com/blog/are-ai-chatbots-shaping-the-future-of-rental-housing-processes
retrieved: 2026-10-06
effective_or_revised: published September 20, 2023
names_ai_feature: generic (chatbots on apartment websites)
fetch_depth: full-fetch
clause_codes_present: n/a ("say": AI chatbots give instant, accurate responses and can check availability and even reserve units)
files: mastersheet-sources/real-estate/greystar/greystar_TYPE6_ai-chatbots-blog_RAW.html (+ .txt)

company: Greystar Europe Holdings Limited (Chapter Living, UK)
document_title: Terms of Use for AI Assistant (January 2025)
document_type: structural-proxy (UK sister-entity dedicated AI terms) - NOT evidence for US Greystar
url: https://www.chapter-living.com/using-our-ai-assistant
retrieved: 2026-10-06
effective_or_revised: January 2025 (stated in title)
names_ai_feature: yes ("AI Assistant")
fetch_depth: full-fetch
clause_codes_present (proxy only): B1-analog (responses "should not be attributed to Greystar"), B4 (verify all information with on-site leasing team), B6, B3 (user responsible for decisions made on AI info), B2 (AI-specific LoL listing errors/inaccurate info), B7-lite (hold harmless re User Content), B10 (anonymised User Content to improve services); rent-quote disclaimer tied to tenancy agreement
files: mastersheet-sources/real-estate/greystar/greystar_PROXY-uk-chapter-ai-assistant_RAW.html (+ .txt)

## Coding-relevant extract

**US terms.** Both the 2020 site Terms and the August 2024 Resident App Terms are fully AI-silent,
even though Greystar was promoting generative chatbots in September 2023. That makes the app terms a
"recently updated, still AI-silent" finding.

**US privacy statement.** The "AI tools" section paraphrased:
- property and Greystar websites may offer AI chatbots built on Microsoft GPT models;
- prompts may be used to improve responses and are shared with Microsoft;
- the chatbot is "not used for the purpose of automated decision making."

These are data-handling disclosures only. The statement contains no accuracy disclaimer and no
anti-reliance language.

**UK proxy (Greystar Europe).** A full dedicated AI terms document from January 2025, which is
locus 1 for that entity. Paraphrased:
- responses are machine-generated and may be inaccurate;
- responses do not represent Greystar's views and "should not be attributed to Greystar";
- users should verify everything with the leasing team;
- an AI-specific limitation of liability covers inaccurate information.

This shows the corporate group *has* drafted an anti-attribution AI template, but deployed it only
where the EU/UK regime applies (the document has an "EU AI Act" heading).

## Coder note
1. **US locus 5 for liability language.** The only AI-specific US text is in the privacy statement
   (B10/B11), which is not a liability allocation. Exposure resembles Moffatt: the "say" (the blog
   claims instant, accurate responses and unit reservations) plus AI-silent terms.
2. **Jurisdictional asymmetry (strong comparative finding).** The same group has dedicated AI terms
   with anti-attribution language in the UK but none in the US. This supports the EU/UK matched
   expansion.
3. **Vendor:** EliseAI and Microsoft are vendors. Their B2B terms are not consumer evidence.
4. **Assent:** browsewrap for the site; the app terms are presumably accepted at app sign-up. No
   assent mechanism was observed for property-site chat or EliseAI SMS.
5. **Context (not an AI-chat incident):** RealPage algorithmic-pricing antitrust settlements (a
   multistate settlement of $7M; the NC AG announcement) and the FTC/Colorado hidden-fee suit. These
   involve decisional/pricing AI, not the customer chatbot, so they are out of scope as incidents and
   noted only as context.
6. **Gaps:**
   - in-chat microcopy on a US property site (the chat widget text was not observed);
   - EliseAI SMS disclosures;
   - lease-level electronic-communications clauses;
   - the meaning of the June 2026 date in the privacy statement.

**Full-read addendum (2026-10-08).** Greystar.com Terms (2020) govern only www.greystar.com, so chatbots on property-level sites are not reached and their terms were not captured. The Resident App terms are clickwrap, with an evaluation duty (B4 G) and a licence over uploaded information (B10 G). The Global Privacy Statement is dated "As of June 23, 2026", denies ADM for the chatbot, names Microsoft GPT models, and does not mention EliseAI. The UK Chapter Living AI Assistant Terms (structural proxy) show the group drafting a dedicated AI instrument abroad while the US surfaces have none (within-firm cross-jurisdiction drift).

---

<a name="cvs-health"></a>
## CVS Health (Aetna) - Aetna generative-AI conversational assistant - collected 2026-10-06

**AI feature.** Aetna's generative-AI "conversational navigation" assistant, embedded throughout the
Aetna website and the Aetna Health app. It answers coverage, prior-authorization, claims and
provider-search questions in plain language with generated UI cards. It entered beta in October
2025 and was announced on November 18, 2025, with rollout through 1H 2026 and voice planned for 2026.
CVS Health also markets AI in the CVS Health app and Health100 platform and uses AI pharmacy calls.
These are noted but secondary. Stakes are high: coverage and prior-authorization answers. Roster:
Insurance Agencies & Benefits vertical.

company: Aetna Inc. (a CVS Health company)
document_title: Aetna Digital Terms of Use (aetna.com + Aetna Health app); /legal-notices/disclaimer.html redirects here
document_type: t1-governing-terms
url: https://www.aetna.com/legal-notices/digital-terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: Last updated June 24, 2026 (stated), 6 days before the cutoff and 8 months after the AI beta
names_ai_feature: no - zero AI and zero "chat" hits
ai_vector: generative chat/search, embedded; voice planned
fetch_depth: full-fetch
clause_codes_present: B6 (generic AS IS), B2 (generic)
files: mastersheet-sources/insurance/cvs-health/cvs_aetna-web-mobile-terms_RAW.html (+ .txt)

company: Aetna Better Health / Aetna CVS Health (Medicaid)
document_title: Web and mobile terms of use (aetnacvshealth.com)
document_type: t1-governing-terms (Medicaid sites)
url: https://www.aetnacvshealth.com/legal-notices/disclaimer.html
retrieved: 2026-10-06
effective_or_revised: Last updated June 24, 2026 (stated)
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: B6, B2 (generic)
files: mastersheet-sources/insurance/cvs-health/cvs_aetnacvshealth-web-mobile-terms_RAW.html (+ .txt)

company: Aetna Inc.
document_title: Aetna Legal Notices index
document_type: legal-hub-index
url: https://www.aetna.com/legal-notices.html
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: none AI
files: mastersheet-sources/insurance/cvs-health/cvs_aetna-legal-notices_RAW.html (+ .txt)

company: CVS Health Corporation
document_title: CVS Health Terms of Use (cvshealth.com)
document_type: t2-site-terms
url: https://www.cvshealth.com/terms-of-use.html
retrieved: 2026-10-06
effective_or_revised: Last updated July 23, 2026 (stated; POST-cutoff - pre-cutoff version needed)
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: B6, B2 (generic)
files: mastersheet-sources/insurance/cvs-health/cvs_cvshealth-terms-of-use_RAW.html (+ .txt)

company: CVS Pharmacy, Inc.
document_title: CVS.com Terms of Use (website + CVS app)
document_type: t1-governing-terms (retail/pharmacy app)
url: https://www.cvs.com/help/terms_of_use.jsp
retrieved: 2026-10-06
effective_or_revised: Last updated September 4, 2026 (stated; POST-cutoff)
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: B6, B2 (generic); generic order-is-an-offer / refuse-orders language
files: mastersheet-sources/insurance/cvs-health/cvs_cvs-com-terms_RAW.html (+ .txt)

company: Aetna Inc.
document_title: "Aetna launches leading edge conversational AI navigation" (press release)
document_type: t6-marketing
url: https://www.aetna.com/insights/news/aetna-launches-leading-edge-conversational-ai-navigation.html
retrieved: 2026-10-06
effective_or_revised: November 18, 2025
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: n/a. The "say": immediate personalized answers on coverage; generative responses carry "clear designations"; complements human interactions.
files: mastersheet-sources/insurance/cvs-health/cvs_TYPE6_aetna-ai-launch_RAW.html (+ .txt)

company: Aetna Inc.
document_title: Live Chat chatbot AI clause (reported by search-engine summary only)
document_type: t4-in-product-microcopy or terms clause (unknown)
url: none verified
retrieved: 2026-10-06
effective_or_revised: unknown
names_ai_feature: "Live Chat" (reported)
fetch_depth: referenced-not-located
clause_codes_present: unverified. The summary claimed AI chatbot responses are general and may not be complete or current. The text was NOT found in any captured Aetna terms (the current Digital Terms, the Medicaid terms, and two co-brand JV terms were all checked and all were AI-silent). Do not code.

## Coding-relevant extract

The Aetna Digital Terms of Use cover aetna.com and the Aetna Health app and are accepted by clicking
"I Agree" in the app. They were revised on June 24, 2026, after the generative assistant had been
live for eight months. They contain no AI, chatbot or generated-content language: only generic
AS-IS and limitation-of-liability clauses. The CVS Health and CVS.com terms (both revised after the
cutoff, in July and September 2026) are likewise AI-silent.

The press release says the assistant labels when a response is generative. That would be T4 in-app
designation microcopy, but it sits behind member login and was not observed.

## Coder note
1. **Locus 5 in terms; possible locus 4 behind login.** The strongest kind of silence finding: a
   freshly revised governing document (June 2026), postdating the AI launch, with no AI language,
   for an assistant answering prior-authorization and coverage questions.
2. **Assent:** clickwrap in the Aetna Health app, a real assent moment that was not used for AI
   terms.
3. **Vintage:** the CVS Health and CVS.com captures are post-cutoff versions, so pre-cutoff versions
   are needed (the Internet Archive is blocked). The Aetna Digital Terms are pre-cutoff
   (June 24, 2026) and usable as-is.
4. **Gaps:**
   - in-app generative-response designation text (behind login);
   - verification of the unconfirmed "Live Chat" AI clause;
   - CVS Health app / Health100 AI terms;
   - AI pharmacy-call disclosures;
   - Aetna privacy-notice ADM section (not fetched within the query budget).

**Full-read addendum (2026-10-08).** Aetna Digital Terms (CVS-01) were read in full. A "new features… shall be subject to this Agreement" clause reaches the AI navigation, and the User-Generated Content definition expressly covers "participating in chats" and "navigating the Services" under a perpetual commercial licence (B10 G). Site modals say plan documents govern over site information. The aetnacvshealth.com terms (CVS-02) are verified identical to CVS-01. Their provisional "Medicaid" label is not supported by the captured text (the footer lists commercial Aetna Health entities). CVSHealth.com (CVS-04) and CVS.com (CVS-05) are CVS Pharmacy, Inc. terms for corporate and retail surfaces that **do not govern the Aetna AI surface** (reach flag; exclude from firm-level reach). The Legal Notices hub (CVS-03) lists no AI document.

---

<a name="cigna"></a>
## The Cigna Group (Cigna Healthcare) - myCigna AI Virtual Assistant - collected 2026-10-06

**AI feature.** The myCigna "AI-Powered Virtual Assistant", announced June 12, 2025. It is a
generative-AI tool in the myCigna portal and app that answers benefits-coverage, claims and
care-option questions and hands off to a human advocate when needed. The rollout is phased, with all
customers by 2026. Stakes are high: coverage and claims answers. Roster: Insurance Agencies &
Benefits vertical.

company: Cigna Corporate Services, LLC (Cigna Healthcare)
document_title: Terms of Use for Cigna Healthcare (Version 2.2)
document_type: t1-governing-terms (site + Portal clause reaching myCigna)
url: https://www.cigna.com/legal/compliance/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Version 2.2, June 04, 2026 (stated), about 12 months after the AI launch and 26 days before the cutoff
names_ai_feature: no. The only AI text is a prohibited-use item barring users from accessing the Site or processing its data with AI/LLM tools or for AI training.
ai_vector: generative chat (portal)
fetch_depth: full-fetch (browser innerText; fetch.py got a nav shell). Capture note with sha256.
clause_codes_present: B9-inbound (AI-specific, user-directed anti-scraping/anti-training: not about Cigna's AI), B6 (generic AS IS / no warranty that Site Content is accurate or reliable), B2 (generic LoL incl. communication errors), B7 (generic indemnity); Portal use subject to "Site-Specific Terms" (not located)
files: mastersheet-sources/insurance/cigna/cigna_terms-of-use_CAPTURE-NOTE.md

company: Cigna Healthcare
document_title: Cigna Access legal disclaimer (static.cigna.com)
document_type: t1-governing-terms (legacy app/site disclaimer)
url: https://static.cigna.com/assets/cignaaccess/en-us/html/legalDisclaimer.html
retrieved: 2026-10-06
effective_or_revised: Last revised 5/29/2020 (stated)
names_ai_feature: no
fetch_depth: full-fetch
clause_codes_present: B6, B2 (generic)
files: mastersheet-sources/insurance/cigna/cigna_cignaaccess-legal-disclaimer_RAW.html (+ .txt)

company: Cigna Healthcare
document_title: myCigna Site-Specific Terms (portal)
document_type: t1-governing-terms (portal supplement)
url: behind login (myCigna)
effective_or_revised: unknown
fetch_depth: referenced-not-located (the Terms of Use cross-reference Site-Specific Terms for Portals)
clause_codes_present: unknown

company: Cigna Healthcare
document_title: Product Disclosures
document_type: t1-adjacent disclaimer page
url: https://www.cigna.com/legal/compliance/disclosures
retrieved: 2026-10-06
effective_or_revised: not stated
names_ai_feature: no (the browser render showed only about 4.2k characters of index text)
fetch_depth: snippet-only. The search summary attributes generic coverage-non-guarantee language ("No benefits are guaranteed"; estimates not a guarantee of coverage) to Cigna disclosures. This is not verified on the rendered page. If confirmed, it would be a generic B1-analog (coverage representations not binding), not AI-specific.

company: The Cigna Group
document_title: "Cigna Healthcare Unveils Industry-Leading AI-Powered Digital Tools..." (press release)
document_type: t6-marketing
url: https://newsroom.cigna.com/cigna-healthcare-unveils-industry-leading-ai-powered-digital-tools
retrieved: 2026-10-06
effective_or_revised: June 12, 2025
names_ai_feature: yes
fetch_depth: full-fetch
clause_codes_present: n/a. The "say": "industry-first" generative AI giving clear, personalized answers on coverage and claims; built under an AI governance framework; title promises a "Simple and Reliable" experience.
files: mastersheet-sources/insurance/cigna/cigna_TYPE6_ai-tools-release_RAW.html (+ .txt)

## Coding-relevant extract

Cigna revised its Terms of Use in June 2026, a year after launching a generative assistant that
answers coverage and claims questions. The revision added AI language, but only to stop *users* from
running AI on Cigna's site or training models on its data. Nothing addresses the accuracy, reliance
or binding effect of Cigna's own assistant. The generic warranty disclaimer (Site Content not
warranted accurate or reliable) and the limitation of liability reach portal content generically.
Portal use is also subject to Site-Specific Terms that were not visible without login.

## Coder note
1. **Locus 5 for outbound AI (possibly 3, if the generic accuracy disclaimer is read as reaching
   assistant output).** Striking asymmetry: the June 2026 drafters thought about AI only as a threat
   to Cigna (scraping) and not as a source of Cigna's own liability. Strong "recently updated, still
   silent on own-AI" finding.
2. **Assent:** browsewrap on the site; myCigna registration likely adds clickwrap to Site-Specific
   Terms (not observed).
3. **Context (decisional AI, out of scope as a chatbot incident):** litigation alleging Cigna's PxDx
   algorithm auto-denied claims (Medscape coverage). This is relevant to B11/decisional vectors only.
4. **Gaps:**
   - myCigna Site-Specific Terms and in-assistant microcopy (behind login);
   - verification of the Product Disclosures coverage-non-guarantee language;
   - privacy-notice ADM section (not fetched within the budget).

**Full-read addendum (2026-10-08) - correction.** The "Cigna Access legal disclaimer" (CI-02) is, on full read, the legal disclaimer for **"Cigna's Online Portal for Employers and Plan Sponsors"**. It is a B2B instrument (site administration for plan sponsors; licences for certificates and SPDs), not consumer terms, and it does not govern the member-facing myCigna assistant. It is recoded as all na, and status adjudication proposes out-wrong-document. Consumer-side evidence for Cigna now rests on the Terms of Use v2.2 (CI-01, captured as an excerpt only and needing re-capture). The myCigna Site-Specific Terms remain referenced-not-located.

---

<a name="ehealth"></a>
## eHealth, Inc. - "Alice" AI voice agent - collected 2026-10-06

**AI feature.** Alice, an AI-powered, non-licensed voice agent on eHealth's inbound Medicare phone
lines. Its history:
- piloted in early 2025 and announced April 30, 2025, initially handling after-hours calls;
- tasks: starting intake, gathering personal information, checking initial eligibility and reading
  required disclosures;
- expanded November 12, 2025 to post-enrollment and general service calls for Medicare Advantage
  members.

Regal appears as the voice-AI vendor in a vendor case study; its terms are B2B and not consumer
evidence. Stakes are high: Medicare plan selection and enrollment, with a vulnerable population. The
modality is voice, the hardest case for assent. Roster: Insurance Agencies & Benefits vertical.

company: eHealthInsurance Services, Inc.
document_title: eHealth Terms of Use
document_type: t1-governing-terms (websites + agent services + "online chat and telephone call centers")
url: https://www.ehealthinsurance.com/about-ehealth/terms-of-use
retrieved: 2026-10-06
effective_or_revised: Updated Sep 25, 2025 (stated), about 5 months after the Alice launch
names_ai_feature: no - zero AI hits
ai_vector: voice (agentic intake)
fetch_depth: full-fetch (browser innerText; fetch.py 403). Capture note with sha256.
clause_codes_present: B6 (generic AS IS; no oral or written advice creates a warranty), B4 (generic: eHealth is not an insurer; don't cancel coverage until written insurer confirmation; informational/no medical advice), B2 (generic), arbitration; call-recording and autodialer/prerecorded-voice consent
files: mastersheet-sources/insurance/ehealth/ehealth_terms-of-use_CAPTURE-NOTE.md

company: eHealthInsurance Services, Inc.
document_title: eHealth Privacy Policy
document_type: privacy-notice
url: https://www.ehealthinsurance.com/about-ehealth/privacy-policy
retrieved: 2026-10-06
effective_or_revised: Effective January 5, 2023; Updated September 25, 2025 (stated)
names_ai_feature: no
fetch_depth: full-fetch (browser innerText; capture note)
clause_codes_present: none AI (no ADM/profiling/AI paragraphs)
files: mastersheet-sources/insurance/ehealth/ehealth_privacy_CAPTURE-NOTE.md

company: eHealth, Inc.
document_title: "eHealth Introduces AI Voice Agents..." (April 30, 2025) and "eHealth Advances its AI Strategy with Expanded Voice Agent Capabilities" (November 12, 2025)
document_type: t6-marketing (x2)
url: https://news.ehealthinsurance.com/news/ehealth-introduces-ai-voice-agents-to-enhance-customer-experience-in-health-plan-selection ; https://news.ehealthinsurance.com/news/ehealth-advances-its-ai-strategy-with-expanded-voice-agent-capabilities
retrieved: 2026-10-06
names_ai_feature: yes ("Alice")
fetch_depth: full-fetch
clause_codes_present: n/a. The "say": Alice eliminates wait times, outperforms human screeners at producing purchase interest, gathers personal information and delivers "necessary disclosures"; licensed agents remain the experts.
files: mastersheet-sources/insurance/ehealth/ehealth_TYPE6_ai-voice-launch_RAW.html, ehealth_TYPE6_ai-voice-expansion_RAW.html (+ .txt)

## Coding-relevant extract

The Terms of Use define the "Service" to include eHealth's agent services and telephone call
centers. That means the governing contract textually reaches calls that Alice answers, although the
Terms never mention AI or automated agents. The relevant clauses are generic:
- AS-IS;
- no oral or written advice creates a warranty;
- eHealth is not an insurer;
- don't cancel existing coverage until the new insurer confirms in writing.

These apply to Alice's statements only by reaching the phone channel generally. The Terms were
revised in September 2025, after Alice launched, and still contain no AI language. The privacy
policy, revised the same day, is also AI-silent even though Alice collects personal information.

## Coder note
1. **Locus 3 (generic clause reaching the AI channel).** This is the cleanest voice-channel example
   in the batch: the contract expressly names telephone call centers, and the "oral advice creates
   no warranty" clause is the generic anti-Moffatt tool. It is not AI-specific.
2. **Assent problem.** A caller to an after-hours Medicare line never clicks anything. The Terms
   claim assent "by otherwise using the Service", which is weak for a phone call. Whether Alice
   discloses that it is an AI, or references any terms, at call start is not documented. (The
   release says it communicates "necessary disclosures", likely CMS-required broker disclaimers, not
   AI terms.)
3. **Vintage:** both Terms and Privacy were revised September 25, 2025, post-launch and still
   AI-silent.
4. **Regulatory context:** CMS third-party marketing organization (TPMO) rules on call recording and
   disclaimers apply to Medicare broker calls. A possible future hook for AI-agent disclosure
   requirements; noted, not coded.
5. **Gaps:**
   - Alice call-opening script (T4 equivalent): not public;
   - Medicare.com / GoMediGap pages use the same Terms (they are listed in the Terms' scope);
   - no incidents located.

---
<a name="recapture-2026-10-09"></a>
## Re-capture pass (2026-10-09): full-text preservation

**Purpose.** Documents that were held only as AI-section excerpts (CAPTURE-NOTEs), read without being saved, or never located could not be coded from a full read. This pass preserves full text for them. **No coding is done here.** Codes follow from full reads logged in `recollection/v2-coding-log.md`.

**Method.** Bot-walled pages were rendered in the built-in browser pane. `document.body.innerText` was sent to a local receiver and saved verbatim as `<slug>.txt`, with a `[capture]` header (url, final_url, retrieved_utc, method, text_sha256, chars, client_sha_match). The SHA-256 computed in the browser matched the on-disk text for every file. Each page was also checked for large hidden DOM blocks (collapsed accordions or tabs). Where legal text was hidden, it was revealed and saved, and this is disclosed per document. Hidden blocks that were only navigation menus or cookie centres were ignored. Pages that a plain fetch could reach went through `_tools/fetch.py` (raw HTML or PDF plus text). Browser captures keep no raw HTML; the preserved artifact is the rendered text.

### A. Previously excerpt-only or read-but-unsaved: now full text

| doc_id | file | retrieved (UTC) | chars | text SHA-256 (16) |
|---|---|---|---|---|
| BJS-01 | `retail/bjs/bjs_terms-of-use.txt` | 2026-10-09T18:43:54Z | 62994 | 0477d30f83d716a7 |
| KMX-01 | `auto-dealers/carmax/carmax_terms-of-use.txt` | 2026-10-09T18:44:39Z | 63456 | 9ae5d93a2353bfa4 |
| GE-01 | `grocery/giant-eagle/gianteagle_terms-of-use.txt` | 2026-10-09T18:44:54Z | 82563 | 01706bfd19c2952f |
| MCD-01 | `restaurants/mcdonalds/mcdonalds_terms-and-conditions.txt` | 2026-10-09T18:45:04Z | 79751 | e093cccb3fb55e1c |
| YUM-01 | `restaurants/yum/tacobell_terms-of-use.txt` | 2026-10-09T18:45:18Z | 91957 | 78baa36071a840cb |
| CASY-01 | `gas-stations/caseys/caseys_terms-and-conditions.txt` | 2026-10-09T18:47:19Z | 58994 | 531d50ebb357b990 |
| ANF-01 | `clothing/abercrombie/anf_website-terms-of-use.txt` | 2026-10-09T18:46:11Z | 41124 | 7ab75cafb0867efb |
| JCR-01 | `clothing/jcrew/jcrew_terms-of-use.txt` | 2026-10-09T18:46:29Z | 45668 | 2d7ea3e12285e984 |
| W-01 | `furniture/wayfair/wayfair_terms-of-use.txt` | 2026-10-09T19:39:47Z | 64782 | f3870ec2d47c11b8 |
| WSM-01 | `furniture/williams-sonoma/wsi_legal-statement.txt` | 2026-10-09T18:48:04Z | 89765 | a28357246dfb2344 |
| BBY-01 | `electronics/best-buy/bestbuy_terms-and-conditions.txt` | 2026-10-09T18:48:23Z | 45227 | 32144d8d1c717435 |
| DKS-01 | `sporting-goods/dicks/dicks_terms-of-use.txt` | 2026-10-09T18:48:52Z | 55150 | 04657364896b9140 |
| MIK-01 | `sporting-goods/michaels/michaels_terms-privacy.txt` | 2026-10-09T18:51:18Z | 110859 | bba8862d8aad0497 |
| RBLX-01 | `software/roblox/roblox_terms-of-use.txt` | 2026-10-09T18:51:31Z | 229976 | 5397a22cf29cd551 |
| RL-01 | `legal-services/rocket-lawyer/rocketlawyer_copilot-terms.txt` | 2026-10-09T18:51:45Z | 9994 | ea4804155b5991b8 |
| RL-02 | `legal-services/rocket-lawyer/rocketlawyer_general-terms-of-service.txt` | 2026-10-09T18:51:58Z | 54722 | 85b4af13fa8b2e06 |
| MTN-01 | `amusement-recreation/vail-resorts/vail_policies.txt` | 2026-10-09T18:52:38Z | 223038 | ebe34928c6dedd46 |
| MTN-01 (tabs) | `amusement-recreation/vail-resorts/vail_policies_hidden-tabs.txt` | 2026-10-09T18:54:04Z | 151994 | 34f15eef13c65165 |
| M-01 | `department-stores/macys/macys_legal-notice.txt` | 2026-10-09T18:52:52Z | 14442 | 6922ac2b67e95131 |
| JWN-01 | `department-stores/nordstrom/nordstrom_terms-conditions.txt` | 2026-10-09T18:53:04Z | 51330 | 98c9db6feff941c9 |
| ROKU-01 | `streaming-social/roku/roku_products-terms.txt` | 2026-10-09T18:53:16Z | 9168 | 702e06b0bd8307b3 |
| FLWS-01 | `specialty-food/1800flowers/1800flowers_terms-of-use.txt` | 2026-10-09T18:53:32Z | 42611 | ae4714324a64e9bd |
| HRB-01 | `tax-prep/hr-block/hrblock_terms.txt` | 2026-10-09T18:54:31Z | 27887 | 6a2dc82d53047171 |
| TDUP-01 | `used-merchandise/thredup/thredup_tou.txt` | 2026-10-09T18:54:45Z | 71814 | 4ee62386d5a5ea09 |
| UPBD-01 | `consumer-goods-rental/upbound/upbound_privacy.txt` | 2026-10-09T18:55:00Z | 43982 | 73f732da96caba1c |
| CI-01 | `insurance/cigna/cigna_terms-of-use.txt` | 2026-10-09T18:55:13Z | 35728 | 4abef78f15609737 |
| EH-01 | `insurance/ehealth/ehealth_terms-of-use.txt` | 2026-10-09T18:55:40Z | 38032 | 4521492b70c110df |
| EH-02 | `insurance/ehealth/ehealth_privacy.txt` | 2026-10-09T18:55:54Z | 33924 | c4a7a2c131a66a15 |
| EIX-03 | `electric-utilities/edison/sce_legal-hub.txt` | 2026-10-09T19:32:37Z | 4349 | 47a32ac8f8091a13 |
| NEGG-02 | `electronics/newegg/newegg_ai-mode-landing.txt` | 2026-10-09T19:32:51Z | 360 | a10ff59295fd7eef |
| FWON-01 | `spectator-sports/liberty-media/f1_legal-notices.txt` | 2026-10-09T19:33:03Z | 22976 | ecccaeea6e358981 |
| LYV-01 | `event-promoters/live-nation/ticketmaster_terms-of-use.txt` | 2026-10-09T19:33:36Z | 46355 | 7c01a44192480e7e |
| UPS-01 | `couriers/ups/ups_website-terms-of-use.txt` | 2026-10-09T19:33:49Z | 21753 | 3f3dc77eea30003b |

Disclosed capture caveats:
- **W-01 Wayfair:** the Terms of Use are a collapsed accordion. Only that section was revealed and saved (it begins "Last Updated: 28 January 2026"). A visible-text-only save would have missed the terms body. One later visit got a bot-challenge page; no challenge was solved, and the capture comes from a visit where the page rendered normally.
- **MTN-01 Vail:** the Terms of Sale, Privacy Policy and Website T&C tabs are hidden at load. They were revealed and saved separately, with markers.
- **CI-04 Cigna Product Disclosures:** collapsed accordions (396 elements) were revealed and the text of `<main>` was saved.

### B. Newly located or captured documents (previously referenced-not-located or snippet-only)

company: Citigroup Inc.
doc_id: C-02
document_title: Citi Online User Agreement (Citi Online / Citi Mobile)
document_type: governing digital-banking terms
url: https://www.citi.com/tandc/view-printable-version
retrieved: 2026-10-09
effective_or_revised: not stated in triage; check on full read
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch (direct; raw HTML kept)
clause_codes_present: not yet coded (full read pending)
file: `banking/citi/citi_online-mobile-terms.txt`

company: PG&E Corporation
doc_id: PCG-02
document_title: pge.com website terms of use ("Disclosure" page; the old URL is a 404)
document_type: site terms
url: https://www.pge.com/en/privacy-center/disclosure.html
retrieved: 2026-10-09
effective_or_revised: not stated in triage; check on full read
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser
clause_codes_present: not yet coded (full read pending)
file: `electric-utilities/pge/pge_website-terms-disclosure.txt`

company: Caesars Entertainment, Inc.
doc_id: CZR-01
document_title: Caesars Terms of Service (non-gaming sites incl. caesars.com and the Caesars Rewards app)
document_type: governing site/app terms
url: https://www.caesars.com/corporate/terms-of-service
retrieved: 2026-10-09
effective_or_revised: stated "Effective Date: March 1, 2018 (Last updated: July 2, 2025)"
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch (direct; raw HTML kept). /terms-of-use only gave a login shell, and the browser refuses caesars.com (gambling restriction)
clause_codes_present: not yet coded (full read pending)
file: `hospitality/caesars/caesars_terms-of-service.txt`

company: Tractor Supply Company
doc_id: TSCO-01
document_title: Terms and Conditions of Use (the old /tsc/cms/terms-conditions path is now a 404)
document_type: governing site terms
url: https://www.tractorsupply.com/tsc/cms/policies-information/customer-solutions/terms-and-conditions-of-use
retrieved: 2026-10-09
effective_or_revised: stated "Last Updated: February 19, 2026"
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser
clause_codes_present: not yet coded (full read pending)
file: `lawn-garden/tractor-supply/tsco_terms-and-conditions-of-use.txt`

company: Roku, Inc.
doc_id: ROKU-02
document_title: Roku Account Terms (US). This is the account/services document the "Roku Services Agreement" reference points to; the old userservicesterms path is a 404
document_type: governing account/services terms
url: https://docs.roku.com/api/v1/published/usertermsandconditions/en/us/text
retrieved: 2026-10-09
effective_or_revised: stated "Effective: October 17, 2020"
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch (direct, plain-text API)
clause_codes_present: not yet coded (full read pending)
file: `streaming-social/roku/roku_account-terms.txt`

company: H&R Block, Inc.
doc_id: HRB-03
document_title: H&R Block Online Services Agreement (PDF; the DIY product terms)
document_type: governing product terms
url: https://www.hrblock.com/pdf/HRBlock-Online-Services-Agreement.pdf
retrieved: 2026-10-09
effective_or_revised: stated "Last Updated 09/18/2026" (post-cutoff). Keyword triage shows 24 AI hits: likely an AI-specific locus, to be confirmed by full read
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch (direct PDF)
clause_codes_present: not yet coded (full read pending)
file: `tax-prep/hr-block/hrblock_online-services-agreement.txt (+ .pdf)`

company: Upbound Group, Inc.
doc_id: UPBD-02
document_title: There is no general website ToU: the rentacenter.com footer links only "ePay Terms" and "SMS/MMS Text Terms", and both were captured. The SMS Terms of Service arbitration clause reaches disputes "related to the use of Company services, including any websites, mobile applications, and communication services"
document_type: nearest governing terms (reach to be assessed)
url: https://www.rentacenter.com/terms-of-service ; https://www.rentacenter.com/terms-and-conditions
retrieved: 2026-10-09
effective_or_revised: not stated in triage; check on full read
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser
clause_codes_present: not yet coded (full read pending)
file: `consumer-goods-rental/upbound/rentacenter_sms-terms-of-service.txt ; rentacenter_epay-terms.txt`

company: Casey's General Stores, Inc.
doc_id: CASY-02
document_title: darngoodroast.com now redirects to caseys.com/darn-good-coffee, so the Darn-ell campaign microsite is retired
document_type: t4 surface (successor page)
url: https://www.darngoodroast.com -> https://www.caseys.com/darn-good-coffee
retrieved: 2026-10-09
effective_or_revised: n-a
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser
clause_codes_present: not yet coded (full read pending)
file: `gas-stations/caseys/caseys_darn-good-coffee-page.txt`

company: The Cigna Group
doc_id: CI-04
document_title: Product Disclosures (accordion content revealed)
document_type: product disclosures
url: https://www.cigna.com/legal/compliance/disclosures
retrieved: 2026-10-09
effective_or_revised: not stated in triage; the earlier search-summary attribution can now be checked against the full text
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser (revealed accordions)
clause_codes_present: not yet coded (full read pending)
file: `insurance/cigna/cigna_product-disclosures.txt`

company: Cox Communications
doc_id: COX-01 (context)
document_title: Spectrum Residential General Terms and Conditions of Service: the current redirect target of the Cox CSA URL; plus the "Cox is now Spectrum" notice
document_type: possible successor governing terms
url: https://www.cox.com/aboutus/policies/customer-service-agreement.html -> https://www.spectrum.com/policies/residential-general-terms-and-conditions-of-service
retrieved: 2026-10-09
effective_or_revised: not stated in triage. The Cox CSA v.7 full text is lost (only the 2026-10-06 excerpts survive). Adjudication item
names_ai_feature: to be determined by full read
ai_vector: per roster
fetch_depth: full-fetch-browser
clause_codes_present: not yet coded (full read pending)
file: `telecom/cox/cox_redirect-spectrum-residential-general-terms.txt ; cox_cox-is-now-spectrum.txt`

### C. Still not captured (honest gaps, as of 2026-10-09)

- **H-01 Hyatt T&C:** HTTP 403 to scripted fetch; the browser renders an empty page (bot challenge) on both URLs. Remains snippet-only.
- **BOB-01 Bob's Terms of Use:** the page shell loads, but the terms body never renders (also true of /terms-of-sale). Remains referenced-not-located.
- **NCLH-03 Nora page:** after non-essential cookies were declined (privacy-preserving choice), the page body renders empty (140 chars); a scripted fetch returns a 25-char shell. Remains referenced-not-located.
- **CVS-07 Aetna Live Chat AI clause:** the Medicare Terms of Use URL in search results now redirects to the Aetna Digital Terms of Use (Last updated 24 June 2026 = CVS-01). With accordions revealed, that page has no "Live Chat", "chatbot" or "artificial intelligence" text. The search-summary clause cannot be verified on any current page; it is probably from a superseded Medicare terms version. Remains unverified; **do not code from it.**
- **EA-02 (EA Help AI microcopy) and CI-03 (myCigna Site-Specific Terms):** behind sign-in. Not attempted (no logging in).
- **COX-01:** the Cox CSA v.7 full text is no longer served (see above).

## Coder note
1. These captures are the evidence base for the next full-read coding batch. Until those reads are logged, the PROVISIONAL codes on these rows still stand and must not be cited.
2. Two re-captures change the document-identification picture rather than just the depth: **Cox** (the governing URL now serves Spectrum's terms) and **H&R Block** (an Online Services Agreement revised 09/18/2026 with many AI hits, which likely moves HRB's locus). **Upbound** is confirmed to have no general website terms, which supports the 'AI disclosed only in privacy policy' finding.
3. Keyword counts above are triage, used only to prioritise reading. They are not findings (see the full-reads rule).


---
<a name="gapfill-2026-10-09"></a>
## Gap-fill pass 2 (2026-10-09): legal hub, binding status, vintage, full text

**Scope.** This pass completes four steps, in order, for every in-sample non-t6 document (262 rows):
1. legal-hub completion;
2. binding status;
3. vintage;
4. full-text capture.

No B1-B11 coding is done here; that still requires the full reads logged in `recollection/v2-coding-log.md`.

### 1. Legal hub
- **Verizon** (previously microcopy + privacy only). Added:
  - VZ-04 Verizon Online Web Site Use Agreement (2010; a legacy portal and the wrong surface);
  - VZ-05 My Verizon Terms & Conditions;
  - VZ-06 My Verizon app EULA (7/23/2026; click-accept);
  - VZ-07 Mobile Customer Agreement (6/16/2026).
- **Comcast.** Added:
  - CMX-03 Xfinity Web Services Terms of Service (2/13/2024; covers Xfinity apps);
  - CMX-04 Residential Services Agreement (excludes websites and apps that do not link to it);
  - CMX-05 policies hub.
- **Chime.** Added CHM-03 Chime User Agreement (effective 08/2025), the governing app/website terms. Previously only the disclosures page was on file.
- Every roster firm now has at least one terms document on file.

### 2. Binding status (new columns `binding_v2`, `binding_basis`)
- **Method.** For each document with full text:
  - read the scope/applicability clauses, the incorporation and conflict clauses, and every AI/chat line;
  - record the category with line citations.
  - Helper scripts: `scope.py` (evidence) and `bind_decisions.py` (decisions), in the session scratchpad.
- **Categories:**
  - governs-ai-expressly
  - governs-surface (AI not named)
  - governs-surface-partial
  - adjacent-not-governing
  - no-reach
  - in-flow-microcopy
  - info-not-terms
  - notice-not-contract
  - hub-index
  - needs-text
- **Consistency rule.** An express statement in the governing document that AI features are part of, or used to provide, the Services counts as governs-ai-expressly (eBay, LegalZoom, Home Depot treated alike).
- **Document counts:**

| Category | Documents |
|---|---|
| governs-surface | 74 |
| governs-ai-expressly | 55 |
| notice-not-contract | 47 |
| info-not-terms | 20 |
| governs-surface-partial | 16 |
| no-reach | 15 |
| needs-text (gaps) | 11 |
| in-flow-microcopy | 9 |
| adjacent-not-governing | 9 |
| hub-index | 6 |

- **Firm-level finding.** Six firms have no captured consumer document that reaches the AI channel at all: Citi, Domino's, McDonald's, PG&E, Quest, Yum. These are mostly phone, IVR and drive-thru AI that website terms do not cover, and there is no assent moment.

### 3. Vintage (new column `vintage_check_v2`)
- Every document with full text was searched for date statements (effective / last updated / revised). Footer copyright years were ignored.
- Many carry-over rows had been left "not-stated" although the text states a date; these were corrected.
- Post-cutoff dates found:
  - H&R Block Online Services Agreement 9/18/2026;
  - Delta Contract of Carriage 8/18/2026;
  - Chegg Terms 9/22/2026;
  - Chegg Privacy 9/9/2026;
  - Hims Privacy 9/17/2026.

### 4. Full text: new captures (browser innerText with SHA check, unless noted)
- **Marriott**
  - Terms of Use: sections revealed; "Ask Bonvoy" is defined as an AI search engine.
  - Homes & Villas Terms: AI tool section.
  - Global Privacy Statement.
- **Hilton**
  - Site Usage Agreement: AI-silent.
  - Global Privacy Statement.
  - AI Terms: the only public host is the Hilton Grand Vacations legal page, a separate company. Nine candidate hilton.com URLs return 404, so this is coded as no-reach for hilton.com.
- **Expedia:** AI Terms; Privacy Statement.
- **Booking.com:** Terms.
- **Booking.com privacy (BKG-02 replaced).** The previously held Booking Holdings corporate notice was the wrong document. It is replaced by the Booking.com Privacy Notice, which has an AI / automated-decisions section.
- **Tripadvisor:** Terms (disclaimer reaches services "created or powered by AI"); Privacy.
- **Airbnb:** US Terms of Service and Privacy.
  - FLAG: the current ToS (2/5/2026) contains zero AI mentions; the v1 "AI-generated Content (Sec 9)" claim is unsupported.
- **Chegg:** Terms ("AI-Assisted Features"); Privacy.
- **Hims & Hers:** Terms (clickwrap; AI in support and clinical care); Privacy.
- **Zillow:** Terms; Privacy (direct fetch).
- **Lowe's:** full Terms (previously 51% partial verbatim).
- **Home Depot**
  - Full Terms: extracted from the embedded page-JSON markdown, because the body is lazy-rendered.
  - Magic Apron "More information" modal (in-flow): verify responses; do not rely for professional advice; reviews not screened.
- **Delta:** Contract of Carriage (PDF, 8/18/2026).
- **American:** Conditions of Carriage; AAdvantage Terms.
- **Alaska:** AI Destination Search page with in-flow microcopy ("can make mistakes. Consider checking important information").
- **DoorDash:** Privacy Policy.
- **Verizon:** chatbot support page ("Generated by AI. Verify if needed."); Full Privacy Policy.
- **Comcast:** live Xfinity Assistant entry text ("Responses may be AI-generated... By continuing, you agree to our Privacy Policy"), an assent-by-continuing to the privacy policy, not the terms; Xfinity Privacy Policy.
- **Chime:** disclosures (FLAG: no AI / no-advice language, so the v1 snippet claim is unsupported); Privacy Notice; User Agreement.
- **Aetna Live Chat clause (CVS-07): VERIFIED via a Wayback Machine snapshot (2026-05-12).**
  - The Aetna Medicare Terms of Use carried an AI Live Chat clause: automated assistance using AI; responses general and possibly incomplete; consent to recording and to insecure-channel risk.
  - The live URL now redirects to the Aetna Digital Terms of Use (6/24/2026), which lack it. The clause was removed or superseded between May and October 2026.
- **Wells Fargo:** Fargo landing/FAQ page only (the in-app disclosure is not public).

### Remaining gaps (11, each documented in `binding_basis`)
- **Login required:** WMT-03 Sparky, EA-02, CI-03 myCigna.
- **App / SMS / in-hotel only:** UAL-04, MAR-05 RENAI, COF-07 (dealer-hosted).
- **B2B / not public:** COF-06.
- **Blocked:** H-01 Hyatt, BOB-01 Bob's, NCLH-03 Nora. Live pages render empty; the Wayback Machine renders empty or rate-limits.
- **Gone:** COX-01 Cox CSA. The URL now serves Spectrum terms; only the 2026-10-06 excerpts survive.

## Coder note
1. Binding status and vintage are now recorded for every document with full text. They feed, and must be confirmed by, the clause-level full reads.
2. Three v1 claims are contradicted by current full text and must be re-coded before citing: Airbnb ABB-01 (AI clause absent), Chime CHM-01 (AI language absent), and Booking BKG-02 (wrong document).
   - **Correction (2026-10-09, Batch 11 full read):** the Airbnb part of this note is wrong. It came from a keyword scan; the full read found the s.9 generated-content clause (ToS L242). See [Batch 11–12 correction 1](#fullread-batch11-12-2026-10-09). The Chime and Booking parts stand.
3. The Aetna Live Chat clause is historical evidence. It is a rare documented case of an AI clause disappearing from a consumer document.


---
<a name="fulltext-pass3-2026-10-09"></a>
## Full-text pass 3 (2026-10-09): remaining public documents

**Goal.** Capture full text for every in-sample document still held only as snippets or excerpts, including the t6 marketing/incident documents (not coded, but needed for say-vs-do comparison).

**Captured.** Browser innerText with a SHA-256 check, or direct fetch:
- **Lowe's:** "AI at Lowe's" Mylow page (LOW-03).
- **Marriott:** Ask Bonvoy launch release, 6/16/2026 (MAR-04).
- **Hilton:** AI Planner launch release (HIL-03).
- **Verizon:** Pivot-to-AI chatbot incident coverage (VZ-03).
- **Tripadvisor:** Futurism AI review-summary incident article (TRP-02).
- **Hims & Hers:** FTC + states press release, 7/29/2026 (HIM-02).
- **AT&T:** new-app release (T-03).
- **Cox:** "About Oliver" page (COX-02). The page is now titled "Spectrum's Automated Live Chat", which corroborates the Cox to Spectrum transition.
- **Duke:** AI Bill Insights coverage, Yahoo Finance (DUK-02).
- **Caesars:** Ivy release (CZR-02), via the PR Newswire mirror. investor.caesars.com is blocked to scripts and refused by the browser (gambling restriction); this is the same 2018 release.
- **Rocket:** Rocket.com launch release (RKT-02).
- **Macy's:** Google Cloud press piece on building Ask Macy's (M-02).
- **Labcorp:** MyLabcorp launch release (LH-02).
- **H&R Block:** AI Tax Assist release (HRB-02).
- **Quest:** MyQuest FAQ "How accurate is the Quest AI Companion?" as a full page (DGX-02; previously excerpt only).
- **State Farm (STF-02):** the actual Notice of Privacy Policy, last updated 9/11/2026, with no AI/chat language. This replaces the wrong hub page.

**Full-text coverage now:**
- 327/339 in-sample documents (96%).
- 250/262 codable documents (95%).

**The 11 remaining are non-public, blocked or gone:**
- Login: WMT-03, EA-02, CI-03.
- App / SMS / hotel only: UAL-04, MAR-05, COF-07.
- B2B: COF-06.
- Blocked: H-01, BOB-01, NCLH-03.
- Gone: COX-01.

GRY-P1 is a deliberately held structural proxy, not a gap.


---
<a name="usersupplied-2026-10-09"></a>
## User-supplied captures + scope decision (2026-10-09)

company: Hyatt Hotels Corporation
doc_id: H-01
document_title: Hyatt Terms & Conditions of Use for the Site
document_type: governing site/app terms
url: https://www.hyatt.com/help/terms
retrieved: 2026-10-09
effective_or_revised: not stated in text
names_ai_feature: no
ai_vector: per roster
fetch_depth: full-fetch (user-supplied paste)
clause_codes_present: not yet coded (full read pending)
file: `hospitality/hyatt/hyatt_terms-and-conditions_USER-SUPPLIED.txt`

**Capture method.** The researcher copied the text from the live page in a normal browser; automated capture was blocked by a bot wall. SHA-256 is recorded in the file header.

**Binding.**
- Scope: "Site" covers Hyatt.com and any app or platform displaying the terms, including chat rooms.
- AI: not mentioned anywhere.
- Errors clause: Hyatt may decline to honor reservations affected by errors, even after confirmation. This is B1-relevant and still to be coded.
- Chats: submitted chats are non-confidential and carry an irrevocable licence to Hyatt.

company: Bob's Discount Furniture, LLC
doc_id: BOB-01
document_title: Terms of Use
document_type: governing site/app terms
url: https://www.mybobs.com/terms-of-use
retrieved: 2026-10-09
effective_or_revised: February 19, 2026 (s.28)
names_ai_feature: yes (generic): s.19 "Use of AI" names chatbot use in customer communications
ai_vector: per roster
fetch_depth: full-fetch (user-supplied paste)
clause_codes_present: not yet coded (full read pending)
file: `furniture/bobs-discount/bobs_terms-of-use_USER-SUPPLIED.txt`

**Binding.**
- Scope: Website plus mobile apps.
- s.19: AI trained on Personal Information and Submitted Content; used "to support communications with customers (such as a chatbot)".
- Conflicts: the Terms of Sale control (s.27).

**Scope decision (researcher, 2026-10-09).** App-only and in-product microcopy documents are out of capture scope and disclosed as unreachable:
- WMT-03 Sparky disclaimer;
- UAL-04 delay messages;
- COF-07 Chat Concierge;
- MAR-05 RENAI;
- EA-02 EA help chat;
- NCLH-03 Nora page.

They are marked `binding_v2 = unreachable-disclosed`.

**Remaining genuine gaps (3):**
- CI-03 myCigna Site-Specific Terms: needs a member login.
- COF-06 Capital One dealer-side agreements: B2B, not public.
- COX-01 Cox CSA v.7: no longer served; only the 2026-10-06 excerpts survive.


---
<a name="fullread-batch11-12-2026-10-09"></a>
## Full-read coding, Batches 11–12 (2026-10-09): carry-over, provisional and newly captured rows

**What this is.** This addendum records the clause-level full reads that close out v2 coding. The audit trail is `recollection/v2-coding-log.md` (headers "# Batch 11" and "# Batch 12"). There, every code is cited to a line number of the preserved `.txt` in `mastersheet-sources/`. This addendum summarises the batches and is not a substitute for the log.

**Method.**
- Every non-blank line of the preserved full text was read with the chunked reader (`rd.py`). Over-long lines were re-printed in full.
- Navigation-only regions were verified mechanically (no line over 60 characters) before being skipped.
- Non-US regional appendices were read but not coded.
- Superseded historical versions kept on the same page (e.g. prior-season Vail EPIC Coverage, the eBay February 2026 version) were checked only for vintage.
- An **A** is recorded only after a full read; untested codes stay **U**.

**Scale.**

| Batch | Rows coded | U codes filled | Prior (v1/provisional) codes changed | Field changes (locus / names_ai / ai_language) |
|---|---|---|---|---|
| 11 | 82 | 211 | 114 (incl. privacy-notice na → coded B10/B11 under the privacy convention) | 29 |
| 12 | 45 (44 + STF-02; COX-01 partial) | 360 | 8 | 8 |

**Status after Batch 12.** 226/230 terms and privacy documents are fully read and coded. Not fully coded:
- COF-06 and CI-03: no text exists (disclosed gaps).
- COX-01: coded from verbatim excerpts only (see below).

The 32 in-product microcopy rows (26 recorded, 6 app-only and disclosed unreachable) and the 77 t6 marketing/incident rows are outside the coding count by design.

### Corrections to earlier archive statements (read before citing older entries)

1. **Airbnb (entry 42 and Gap-fill pass 2, coder note 2): the "AI clause absent" flag is WRONG.**
   - The 2026-10-09 binding pass relied on a keyword scan for "AI" and reported zero mentions.
   - The full read of the US Terms of Service (Last Updated 2026-02-05, `travel-ota/airbnb/airbnb_terms-of-service.txt` L242, s.9 Content) found a generated-content clause. Airbnb does not guarantee the accuracy of generated Content or translations, and Members must confirm that accuracy.
   - The clause names generation tools, not "AI" (names_ai category). It is coded B4 S and B6 S, locus 2.
   - The original entry 42 ("disclaimer not located", snippet-only) is superseded. The 2026-09-23 "warned (integrated)" note was correct.
   - Lesson for the method: keyword scans miss clauses that avoid the word "AI". This is why coding requires full reads.
2. **Chime CHM-01:** the v1 snippet ("informational purposes only…", "humans stay in the loop") is not on the current Disclosures page, and its source is unidentified. The claim is withdrawn. Chime's governing document is the User Agreement (CHM-03).
3. **Cigna CI-04:** the v1 attribution of AI-assistant language to the Product Disclosures page is unsupported. The page's only AI text concerns an internal claims-review tool with human determinations, which is out of scope.
4. **Verizon VZ-01:** "Generated by AI. Verify if needed." labels an AI summary of a support video, not the chatbot's answers. The scope was corrected (B6 S → A, B3 S → A).
5. **Hilton HIL-01:** this is Hilton Grand Vacations, a separate licensee. Its AI Terms are evidence for HGV only and must be excluded from the Hilton firm roll-up.
6. **State Farm STF-02:** the earlier capture was the Contact Us page (redirect). It is replaced by the Notice of Privacy Policy (09/11/2026): AI-silent, B10 G, B11 A.
7. **Aetna CVS-07:** the Live Chat AI clause (Wayback, 2026-05-12) is absent from the live Aetna Digital Terms (2026-06-24). It is historical evidence of an AI clause being withdrawn.

### Principal findings surfaced in these batches (detail and line cites in the log)

- **Sharpest anti-Moffatt clause found:** Best Buy BBY-01 (B1 S). Statements by the AI that deviate from the terms or policies are void and non-binding. Locus corrected 3 → 2.
- **First AI-honouring clause:** H&R Block HRB-03. The accuracy guarantee covers incorrect advice in the AI Tax Assist chat transcript (penalties and interest up to $10k). It runs in the opposite direction to every other B1 finding.
- **AI expressly inside a pricing-error clause:**
  - Tripadvisor TRP-01: information "created or powered by AI" may contain pricing errors, which may be corrected (B1 S, locus 3).
  - Nordstrom JWN-01 was coded S in the full read, but adjudication (ruling 2) returned it to **G**: its correction right links back to non-AI text as well. Tripadvisor remains the only express AI pricing-error clause.
- **Generic clauses that reach AI channels without naming them:**
  - eHealth EH-01: the Service includes telephone call centres, so the terms reach the Alice voice agent.
  - Casey's CASY-01 and Williams-Sonoma WSM-01: offline-reach clauses.
  - United UAL-02: no liability for misstatements about delays, and no representative's statement binds United.
  - Vail MTN-01: no representative may modify the Terms "verbally or in writing".
  - These generic anti-attribution devices are the main contractual answer to a Moffatt-type claim among AI-silent firms.
- **Recently revised documents that are still AI-silent** (vintage flag; stronger than an old silent document):
  - Tractor Supply TSCO-01 (Feb 2026);
  - Michaels MIK-01 (predates Ask Mike);
  - Cigna CI-01 (Jun 2026; its only AI language bars users' AI);
  - Vail MTN-01 (four documents revised Mar–Jul 2026);
  - State Farm STF-02 (Sep 2026);
  - DoorDash DD-03 (no AI section, although the help article names this policy as governing the Assistant).
- **Restrictive-only AI language (B5 S, locus none)**, where the firm's only AI clause bars customers' AI agents:
  - Booking BKG-01;
  - Cigna CI-01;
  - Comcast CMX-04.
- **Dedicated AI sections with full allocation (locus 2):**
  - Walmart WMT-01 (s.16.J);
  - Chegg CHG-01 (B2 S, "not liable for your use of the chat bot");
  - Hims & Hers HIM-01 (AI not used for clinical decisions, B11 A);
  - Roblox RBLX-01 (creators must tell users "AI is not human"; captured text likely the Nov 1 2026 post-cutoff version);
  - Williams-Sonoma WSM-01 (locus corrected none → 2).

### COX-01 — excerpt-preserved, partially coded (final status)

- The Cox Residential Customer Service Agreement v.7 (Jan 1 2025) was read in full in the browser on 2026-10-06. Only the s.10.G AI section (verbatim) and the AS-IS summary were saved.
- Since around Oct 7–9 2026 the URL has redirected to Spectrum's Residential General Terms (the Cox–Spectrum transition).
- Recovery attempts on 2026-10-09 all failed:
  - Wayback Machine: snapshot renders an error page; CDX and raw-snapshot requests returned HTTP 429.
  - archive.today: holds only a 2017 snapshot.
  - Likely PDF paths in the cox.com document library: nothing.
  - One web search: no alternate copy found.
- Coded: B6 G (AS IS) and B11 S ("automated decision-making tools" disclosed in the contract). B1–B5 and B7–B10 remain **U** (untested), not A. The row is excluded from the full-read re-apply script.
- The Spectrum successor terms are post-cutoff and not coded for this row.
- Retry the Wayback raw snapshot when the rate limit clears.

### Adjudication (resolved 2026-10-09; PI to confirm)
`recollection/v2-adjudication-batch11-12.md` holds 10 rulings. Four of them set standing conventions:
- privacy notice as a liability vehicle;
- B1–AI linkage;
- the B5 boundary categories, including the new finding flag "ungoverned agentic capability";
- locus as container type, independent of binding.

Two codes changed: JWN-01 B1 S → G and UPBD-01 B11 S → G (same-system rule). The other rulings confirm existing codes.

## Coder note
Batches 11–12 complete the full-read coding of every terms and privacy document for which text exists. Codes from earlier provisional or v1 passes that were not confirmed by a full read must not be cited. Use the `documents.csv` row as updated by these batches, with the line cites in the coding log.

---
<a name="privacy-fallback-2026-10-14"></a>
## Privacy-notice fallback pass (2026-10-14): Silent main-sample firms

**Purpose.** The collection protocol reads types 1-3 (governing terms, site terms, dedicated AI terms) for every firm and, where none carries AI-specific language, also reads the firm's privacy notice in full, because some firms put their only AI language there (Frontier). An audit on 2026-10-13 found 18 main-sample firms whose t1-t3 documents were AI-silent and whose privacy notice had never been collected. This pass collects and codes those notices. Line-by-line codes are in `recollection/v2-coding-log.md`, Batch 13.

**Capture.** All 18 captured in full: 8 by `fetch.py` (incl. the Albertsons PDF, URL supplied by the researcher after albertsonscompanies.com showed a Cloudflare human-verification page), 9 in the built-in browser through the capture receiver (each with a matching client hash), and Hyatt as a researcher-supplied paste (Kasada bot protection).

company: AT&T Inc.
document_title: AT&T Privacy Notice
document_type: privacy-notice
url: https://about.att.com/privacy/privacy-notice.html
retrieved: 2026-10-14
effective_or_revised: LAST UPDATED May 27, 2026 (stated)
names_ai_feature: no
ai_vector: generative (GenAI assistant in AT&T app)
fetch_depth: full-fetch-browser
clause_codes_present: B10 G; B11 A (AI mentioned only for internal ad personalization)
files: mastersheet-sources/telecom/att/att_privacy-notice.txt

company: Caesars Entertainment, Inc.
document_title: Caesars Entertainment U.S. Privacy Policy
document_type: privacy-notice
url: https://www.caesars.com/corporate/privacy
retrieved: 2026-10-14
effective_or_revised: REVISED April 2, 2026 (stated)
names_ai_feature: no
ai_vector: generative (Ivy text concierge)
fetch_depth: full-fetch
clause_codes_present: B10 G; B11 A; states it creates no contractual obligation
files: mastersheet-sources/hospitality/caesars/caesars_privacy-policy.txt (+ _RAW.html)

company: Casey's General Stores, Inc.
document_title: Casey's Privacy Policy
document_type: privacy-notice
url: https://www.caseys.com/privacy-policy
retrieved: 2026-10-14
effective_or_revised: effective December 2, 2019; last updated January 1, 2026 (stated)
names_ai_feature: no
ai_vector: generative (AI phone ordering + Darn-ell chatbot)
fetch_depth: full-fetch-browser
clause_codes_present: B10 G; B11 A (express denial)
files: mastersheet-sources/gas-stations/caseys/caseys_privacy-policy.txt

company: Chipotle Mexican Grill, Inc.
document_title: Chipotle U.S. Privacy Policy, including California Privacy Rights
document_type: privacy-notice
url: https://www.chipotle.com/privacy-policy
retrieved: 2026-10-14
effective_or_revised: LAST UPDATED April 8, 2026 (stated)
names_ai_feature: yes, by brand ("our AI powered chat bot, Pepper")
ai_vector: generative (Pepper chatbot + AI phone ordering)
fetch_depth: full-fetch
clause_codes_present: B10 G; B11 A; consent-by-use to chat recording (data handling, no liability language)
files: mastersheet-sources/restaurants/chipotle/chipotle_privacy-policy.txt (+ _RAW.html)

company: Citigroup Inc.
document_title: Citi U.S. Privacy Notice for Consumers
document_type: privacy-notice
url: https://online.citi.com/US/JRS/portal/template.do?ID=Privacy (redirects to citi.com/policies/us-privacy-notice-for-consumers)
retrieved: 2026-10-14
effective_or_revised: LAST UPDATED October 8, 2026 (stated)
names_ai_feature: no
ai_vector: generative (GenAI enhanced IVR, phone pilot)
fetch_depth: full-fetch-browser
clause_codes_present: B10 G; B11 A; browsewrap to the notice
files: mastersheet-sources/banking/citi/citi_privacy-notice.txt

company: Duke Energy Corporation
document_title: Duke Energy Digital Privacy Policy
document_type: privacy-notice
url: https://www.duke-energy.com/legal/privacy-policy
retrieved: 2026-10-14
effective_or_revised: Last updated October 7, 2026 (stated)
names_ai_feature: partially, by category ("automated chat feature")
ai_vector: generative (app AI chatbot + AI Bill Insights)
fetch_depth: full-fetch-browser
clause_codes_present: B10 G; B11 A
files: mastersheet-sources/electric-utilities/duke-energy/duke_privacy-policy.txt

company: Edison International (Southern California Edison)
document_title: SCE Website Privacy Notice
document_type: privacy-notice
url: https://www.sce.com/privacy-notice/website-privacy-notice
retrieved: 2026-10-14
effective_or_revised: Updated December 30, 2020 (stated; pre-ChatGPT)
names_ai_feature: no
ai_vector: generative (AskSCE chatbot)
fetch_depth: full-fetch
clause_codes_present: B10 G; B11 A; browsewrap acceptance of the notice
files: mastersheet-sources/electric-utilities/edison/sce_website-privacy-notice.txt (+ _RAW.html)

company: The Gap, Inc.
document_title: The Gap Inc. Privacy Policy
document_type: privacy-notice
url: https://www.gapinc.com/en-us/consumer-privacy-policy
retrieved: 2026-10-14
effective_or_revised: Last updated June 22, 2026 (stated)
names_ai_feature: partially, by category ("AI and machine-learning based tools")
ai_vector: generative (AI customer-care assistant)
fetch_depth: full-fetch-browser
clause_codes_present: B10 S (inputs to AI tools may train generative AI and LLMs); B11 A (denial)
files: mastersheet-sources/clothing/gap/gap_consumer-privacy-policy.txt

company: Giant Eagle, Inc.
document_title: Giant Eagle Privacy Notice
document_type: privacy-notice
url: https://www.gianteagle.com/privacy-notice
retrieved: 2026-10-14
effective_or_revised: effective October 13, 2025 (stated)
names_ai_feature: partially, by category (website chatbot "may rely on embedded and/or third-party generative AI")
ai_vector: generative (AI Recipe Generator)
fetch_depth: full-fetch-browser
clause_codes_present: B10 S (chatbot inputs used for training, consent by use); B11 A
files: mastersheet-sources/grocery/giant-eagle/gianteagle_privacy-notice.txt

company: J.Crew Group, LLC
document_title: J.Crew Group Privacy Policy
document_type: privacy-notice
url: https://www.jcrew.com/help/privacy-policy
retrieved: 2026-10-14
effective_or_revised: Last updated September 2, 2026 (stated)
names_ai_feature: partially, by category ("chatbot")
ai_vector: generative (AI Shopping Assistant, beta)
fetch_depth: full-fetch-browser
clause_codes_present: B10 G; B11 A
files: mastersheet-sources/clothing/jcrew/jcrew_privacy-policy.txt

company: McDonald's Corporation / McDonald's USA, LLC
document_title: McDonald's Global Customer Privacy Statement (with U.S. addendum)
document_type: privacy-notice
url: https://www.mcdonalds.com/us/en-us/privacy.html
retrieved: 2026-10-14
effective_or_revised: Last updated July 1, 2026 (stated, global and U.S.)
names_ai_feature: partially, by category ("AI models"); drive-thru audio processing described without naming AI
ai_vector: generative (Archy AI drive-thru voice ordering, pilot)
fetch_depth: full-fetch-browser
clause_codes_present: B10 S (training of AI models; drive-thru audio used to improve technologies); B11 A (denial)
files: mastersheet-sources/restaurants/mcdonalds/mcdonalds_privacy-statement.txt

company: PG&E Corporation (Pacific Gas and Electric Company)
document_title: PG&E Privacy Policy
document_type: privacy-notice
url: https://www.pge.com/en/privacy-center/privacy-policy.html
retrieved: 2026-10-14
effective_or_revised: Effective July 1, 2026 (stated)
names_ai_feature: no
ai_vector: generative (Peggy AI voice assistant)
fetch_depth: full-fetch
clause_codes_present: B10 G; B11 A
files: mastersheet-sources/electric-utilities/pge/pge_privacy-policy.txt (+ _RAW.html)

company: Southwest Airlines Co.
document_title: Southwest Airlines Privacy Policy & Data Options
document_type: privacy-notice
url: https://www.southwest.com/about-southwest/terms-and-conditions/privacy-policy/
retrieved: 2026-10-14
effective_or_revised: Last Updated March 30, 2026 (stated)
names_ai_feature: partially, by category ("chatbot technology")
ai_vector: generative-agentic (Agentforce AI assistant)
fetch_depth: full-fetch
clause_codes_present: B10 S (training of AI systems); B11 A; states it is not a contract
files: mastersheet-sources/airlines/southwest/southwest_privacy-policy.txt (+ _RAW.html)

company: T-Mobile US, Inc.
document_title: T-Mobile Privacy Notice
document_type: privacy-notice
url: https://www.t-mobile.com/privacy-center/privacy-notices/t-mobile-privacy-notice
retrieved: 2026-10-14
effective_or_revised: Last updated June 26, 2026 (stated)
names_ai_feature: partially, by category ("artificial intelligence models")
ai_vector: generative (Ask AI in T-Life)
fetch_depth: full-fetch
clause_codes_present: B10 S (training of AI models, including for customer service); B11 A
files: mastersheet-sources/telecom/t-mobile/tmobile_privacy-notice.txt (+ _RAW.html)

company: Truist Financial Corporation
document_title: Truist Privacy page (Statement of Online Privacy Practices; Consumer Privacy Notice; CCPA Notice at Collection)
document_type: privacy-notice
url: https://www.truist.com/privacy
retrieved: 2026-10-14
effective_or_revised: Online Practices and CCPA Notice updated January 2026; Consumer Privacy Notice Rev. 01/2025 (stated)
names_ai_feature: no (Truist Assist appears only as a footer link)
ai_vector: generative-agentic (Truist Assist)
fetch_depth: full-fetch
clause_codes_present: B10 G; B11 A (ADMT opt-out concerns credit decisions)
files: mastersheet-sources/banking/truist/truist_privacy.txt (+ _RAW.html)

company: Yum! Brands, Inc.
document_title: Yum! Brands Privacy Policy (Taco Bell US Privacy Center)
document_type: privacy-notice
url: https://privacy.tacobell.com/ (redirects to /policies)
retrieved: 2026-10-14
effective_or_revised: Last modified September 1, 2026 (stated)
names_ai_feature: partially, by category (AI at the drive-thru and in chatbots)
ai_vector: generative (Byte by Yum voice AI drive-thru)
fetch_depth: full-fetch-browser
clause_codes_present: B10 S (drive-thru voice orders and chats used to train AI); B11 A; browsewrap; franchisee interactions outside the policy
files: mastersheet-sources/restaurants/yum/tacobell_privacy-policy.txt


company: Albertsons Companies, Inc.
document_title: Albertsons Companies Privacy Policy (with U.S. State Privacy Rights Supplement)
document_type: privacy-notice
url: https://s29.q4cdn.com/239956855/files/doc_downloads/2026/09/2026.09.16-PDF-Version-Privacy-Policy.pdf
retrieved: 2026-10-14
effective_or_revised: effective January 1, 2023; last updated September 16, 2026 (stated)
names_ai_feature: partially, by category ("our chatbot is AI-powered"; third-party AI services such as ChatGPT)
ai_vector: generative-agentic (Albertsons AI / Safeway AI shopping assistant)
fetch_depth: full-fetch (PDF; URL supplied by the researcher)
clause_codes_present: B10 S (AI training among data uses); B11 A
files: mastersheet-sources/grocery/albertsons/albertsons_privacy-policy_2026-09-16.pdf (+ .txt)

company: Hyatt Hotels Corporation
document_title: Hyatt Privacy Policy for Guests
document_type: privacy-notice
url: https://world.hyatt.com/content/gp/en/privacy/guest-policy.html
retrieved: 2026-10-14
effective_or_revised: Last Updated July 2025 (stated)
names_ai_feature: no
ai_vector: generative (natural-language search)
fetch_depth: full-fetch (user-supplied paste; automated capture blocked by Kasada)
clause_codes_present: B10 G; B11 A
files: mastersheet-sources/hospitality/hyatt/hyatt_privacy-policy-for-guests_USER-SUPPLIED.txt
## Coding-relevant extract

None of the 18 notices contains liability, accuracy, reliance or warranty language about the AI. Every firm therefore stays Silent on locus, and no headline figure changes. What the notices add is disclosure:
- Chipotle names "Pepper" as its AI-powered chatbot and obtains consent to recording by use.
- Duke, J.Crew and Southwest name a chatbot or "automated chat feature" by category.
- Six firms state that customer inputs or interactions may train AI: Gap, Giant Eagle (website chatbot built on generative AI), McDonald's, Southwest, T-Mobile and Yum.
- Yum describes drive-thru voice recording "including AI training"; McDonald's describes using drive-thru audio "to receive and process orders". Both notices reach a drive-thru channel that the firms' website terms do not.

## Coder note
1. **Disclosure axis.** Ten main-sample firms move from 0 to 1 (Albertsons, Chipotle, Duke, Gap, Giant Eagle, J.Crew, McDonald's, Southwest, T-Mobile, Yum). Locus, clusters and the headline counts are unchanged; Figure 1 positions change.
2. **Paper correction.** §5.1 says no consumer document reaches the AI for McDonald's and Yum. Their privacy notices now do (non-binding), so the sentence must say no *binding* document reaches the AI.
3. **Non-contract statements.** Caesars (L43) and Southwest (L99-100) expressly say their privacy notices are not contracts; Citi, SCE and Yum assert browsewrap acceptance of the notice only. Consistent with coding all 16 as notice-not-contract.
4. **Vintage.** SCE's notice dates from December 2020 and is the only pre-ChatGPT document in this pass. Citi (October 8, 2026) and Duke (October 7, 2026) were revised in the past week and remain silent about their assistants.
5. **Albertsons and Hyatt (added later the same day).** Albertsons' policy (September 16, 2026) calls its chatbot "AI-powered", has a section on third-party AI services such as ChatGPT, and lists AI training among its data uses (B10 S); no liability language, so Albertsons stays Silent and becomes the tenth firm to disclose its AI outside the contract. Hyatt's policy (July 2025) is AI-silent (B10 G). Remaining uncertainty: Giant Eagle's notice does not say whether its chatbot is the AI Recipe Generator.
