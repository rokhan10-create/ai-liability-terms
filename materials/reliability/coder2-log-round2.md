# Independent second-coder log — IRR Round 2

I coded this corpus blind from the raw documents, using only `CODING-MANUAL.md` as the methodological instrument. I did not open the primary coder archive, datasets, analysis directory, round-1 IRR outputs, gap registers, retrieval queues, governing-terms tables, explorer pages, or neighboring coder-note files. Where bracketed annotations appeared inside the American, United, Gopuff, or Lowe's source captures, I disregarded them and coded only the operative prose. The Alaska Inspires capture was only a JavaScript/client challenge and was recorded `referenced-not-located`; the short Capital One privacy text was a navigation/landing capture, so B10 was left untested (the listed PDF sibling was inspected only to characterize the linked privacy notice). All listed PDFs were text-extracted and read through their complete page ranges. RAW HTML duplicates were not opened.

## Document entries

- **Alaska/Hawaiian — Website terms.** Governs the Sites by browsewrap and generically supplies B1/B2/B4/B5/B7; no AI wording. The broad anti-reliance sentence is directive-leaning.
- **Alaska/Hawaiian — Contract of Carriage.** Fails the governance gate: transportation contract, not AI-use terms.
- **Alaska/Hawaiian — Inspires page.** Bot/client challenge only; unreadable gap, no confirmed absence.
- **Alaska/Hawaiian — Privacy Notice.** Readable privacy document, but no named feature or qualifying in-scope ADM; attachment to the AI surface is contested.
- **American — Platform terms.** Attached AI section yields B1/B2/B3/B4/B7/B9/B11 as AI-specific, B5 generic, and a weak B8 based on third-party AI providers. Category naming only.
- **American — Privacy policy.** Reaches interactive services generally but contains no feature-specific liability clause or qualifying ADM disclosure.
- **Delta — AI Terms.** Dedicated, comprehensive B1/B2/B3/B4/B5/B7/B8/B9 language; directive verification duty. Orphaned because the general site terms do not route users to it.
- **Delta — Site Terms.** Generic B1/B4/B5/B7 reach site services; no AI-specific language.
- **Delta — Privacy and Security.** No output-liability code or in-scope ADM disclosure; relationship to AI terms is privacy-only.
- **Frontier — Terms of Use.** Generic website B1 and B4 only.
- **Frontier — Privacy Notice.** AI-assisted chat disclosure contains B1, hedged B2, and B3. Liability wording in a privacy container makes attachment contested.
- **Frontier — Contract of Carriage.** Fails governance gate; carriage only.
- **Frontier — Legal hub.** Index/signposting only, no governing AI terms.
- **United — Legal terms.** Generic B1/B4/B5/B7; AI-silent. Human forums/chat were ignored as directed.
- **United — Contract of Carriage.** Fails governance gate.
- **United — Privacy Policy.** No named AI feature or qualifying same-system ADM.
- **Capital One — Website terms.** Generic B1/B4/B5/B8. The AI link is a compelled training-data disclosure, not voluntary risk shifting.
- **Capital One — Important Disclosures.** Generic B1/B8 for third-party tools; compelled AI link only. Whether it reaches Eno is contested.
- **Capital One — GAI disclosure.** Fails the consumer-feature governance gate; statutory model-training transparency only.
- **Capital One — Privacy.** Landing capture was not the full policy; treated as a gap and B10 untested.
- **Dave — Terms.** Generic B1/B4/B5/B7/B8 reach the service; no AI naming.
- **Dave — Privacy.** No feature-specific AI or qualifying ADM.
- **Wells Fargo — General Terms.** Chat/Chatbot section supplies thin AI-specific B1; generic B4/B5. Electronic-record language is a channel limitation, not B6.
- **Wells Fargo — Online Access Agreement.** Affirmative enrollment and a live chat/virtual-assistant definition attach the document; generic B4 and the no-trade-instructions channel limitation apply.
- **Wells Fargo — Consumer Privacy Notice.** Full three-page notice; no in-scope B10.
- **DoorDash — Consumer Terms.** Generic B1/B4/B5/B7/B8/B9, with an AI-content disclosure tied to merchant listings but no assistant-output term.
- **DoorDash — AI Assistant article.** B1 plus directive B2 for health, packaging, and cart verification; help-article locus and contested attachment.
- **Gopuff — Terms.** Generic B1/B4/B5/B8; no AI naming. Embedded coder annotations were ignored.
- **Gopuff — Privacy Notice.** Read in full; B10 confirmed absent.
- **Instacart — Terms.** Dedicated AI section and agent rules produce AI-specific B1/B2/B3/B7/B9/B11; generic B4/B5 and a close B8.
- **Instacart — Privacy.** No qualifying same-system ADM.
- **Instacart — Cart Assistant article.** Named feature with B1/B2; informational, not proven incorporated.
- **Instacart — Food-search article.** Named AI search with B1/B2; informational and contested attachment.
- **Uber — General Terms.** AI-enhanced interactions are acknowledged, but the separate AI page is merely signposted. Generic B1/B4/B5/B7/B8 reach the Services.
- **Uber — Privacy Notice.** B10 coded for automated decision-making in the consumer-service ecosystem; direct tie to the generative feature is uncertain.
- **Uber — Generative AI page.** B1/B2 plus `near-B6` for estimated pricing and checkout redirection. Signposting rather than incorporation makes attachment contested.
- **Amazon — Conditions of Use.** Generic B1/B4/B5/B7/B8 reach Amazon Services; AI unnamed. Current preserved capture appeared substantive enough for full-fetch.
- **Amazon — Privacy Notice.** B10 coded for automated decision-making/profiling; direct linkage to Rufus is uncertain.
- **Amazon — Generative AI disclosure.** Compelled/model-development transparency, not consumer liability terms; gates out.
- **Home Depot — Terms.** Generic B1/B4/B5/B7/B8 reach the Site; no Magic Apron naming.
- **Home Depot — Privacy Statement.** No named AI or qualifying in-scope ADM.
- **Home Depot — Magic Apron surface.** Short but genuine microcopy: AI-content disclosure only. I did not infer B1 from “AI-generated.”
- **Lowe's — Terms.** Generic B1/B4/B5/B7/B8 reach Mylow; no AI naming. Anti-bot language is not B11.
- **Lowe's — Privacy Statement.** Complete PDF; no same-system ADM disclosure.
- **Target — Privacy Policy.** Agentic Commerce Agent clause is B3+B11, but privacy-policy placement leaves contractual attachment contested.
- **Walmart — Terms.** Attached AI section: B1/B2/B3/B6/B8/B9 AI-specific; B4/B7 generic-reaching. Clean B6 and directive B2. Category named, not Sparky.
- **Walmart — Privacy Notice.** B10 coded, with uncertainty about whether the automated-processing disclosure maps specifically to Sparky.

## Manual issues for adjudication

1. **`governs_ai` versus privacy scope.** The manual says to stop when a document does not govern the feature, yet separately authorizes privacy-notice loci and B10. I used `contested` when a privacy notice governed data processing across the service but did not clearly govern AI-output liability.
2. **B8 breadth.** The rule includes generic marketplace-seller disclaimers, but its definition speaks of output/content drawing on unverified third-party sources. I therefore coded broad third-party-material/source clauses when they plausibly reached the feature, while flagging American and Instacart as close calls.
3. **B10 same-system linkage.** Privacy notices often describe automated decisions or profiling at company/service level without tying them to the marketed assistant. I coded B10 for Uber, Amazon, and Walmart but marked the system identity uncertainty; stricter identity proof would change those cells.
4. **Assent tokens conflict.** Section 4 permits `none-at-AI-surface` while the requested output brief asks for `none`; I used the manual's more specific `none-at-AI-surface` where a real AI/privacy/help surface lacked assent, and `none` only for documents that failed the governance gate.
5. **Attachment `none`.** Section 8 lists attached/orphaned/contested, while the output brief adds `none`. I used `none` only for gate-outs.
6. **Locus for AI-silent privacy notices.** The manual defines a privacy-notice extension but does not say whether every privacy notice gets that locus when it contains no AI language. I used `privacy-notice` to describe the container and preserved uncertainty through `governs_ai`/`attachment`.
7. **Microcopy disclosure versus B1.** Home Depot says only “AI-generated responses.” Because B1 requires inaccuracy/no-warranty language, I recorded `AI-content-disclosure` without B1.
8. **Current Amazon capture versus manual example.** The manual cites Amazon Conditions as historically snippet-only/robots-blocked. The listed current capture contains substantive terms. I followed the actual source and treated it as full-fetch, noting the conflict rather than copying the historical depth.
9. **Partial source captures labeled complete.** Lowe's states that 51% of the page contains the entire substantive contract and that omitted rewards appendices contain no relevant material. I treated the target terms as full-fetch but this is not literally the whole webpage; the manual does not define this case.
10. **B2 “should” register.** Alaska's generic clause says material “should not be relied upon,” which is directive-leaning under Section 11, though it lacks an express verification verb. I coded B2 directive.
11. **B7 content-license reach.** Whether a generic submissions/content license captures chat prompts depends on whether prompts qualify as submitted content. I applied the manual's generic-reaching convention uniformly, but this legal reach can be contested document by document.
