"""Build previous-tos/v2-baseline-worklist.csv from documents.csv (v2 full-read, baseline-able documents).
Run from the project root: python previous-tos/_tools/v2-build-worklist.py"""
import collections, csv, glob, os, re

R = list(csv.DictReader(open("documents.csv", encoding="utf-8")))
OK = ("governs-ai-expressly", "governs-surface", "governs-surface-partial", "notice-not-contract",
      "adjacent-not-governing", "no-reach")
TYPES = ("t1-governing-terms", "t2-site-terms", "privacy-notice", "contract-of-carriage", "t3-dedicated-ai-doc")
W = [r for r in R if r["status_v2"] == "new-v2-fullread" and r["binding_v2"] in OK
     and r["url"].startswith("http") and r["doc_type"] in TYPES]
# pilot baselines already on disk for the same document (verified by firm + document identity)
REUSE = {
    "WMT-01": "retail/walmart/walmart_terms-of-use_20221130080639",
    "HD-06": "retail/homedepot/homedepot_terms-of-use_20221130131408",
    "LOW-01": "retail/lowes/lowes_terms-and-conditions_20221130195140",
    "TGT-01": "retail/target/target_terms-conditions_20221128074519",
    "DAL-02": "airlines/delta/delta_site-terms-of-use_20221126120150",
    "DAL-03": "airlines/delta/delta_privacy-policy_20221130032232",
    "AAL-01": "airlines/american/american_legal-information_20221017155337",
    "FRO-01": "airlines/frontier/frontier_terms-of-use_20221102020018",
    "FRO-02": "airlines/frontier/frontier_privacy-policy_20221116203715",
    "INS-01": "food-delivery/instacart/instacart_terms-of-service_20221129223743",
    "UBR-01": "food-delivery/ubereats/uber_general-terms-of-use-US_20220626175240",
    "WFC-01": "banking/wells-fargo/wellsfargo_online-access-agreement_20221201101257",
    "WFC-02": "banking/wells-fargo/wellsfargo_general-terms-of-use_20221124062825",
    "MAR-01": "hospitality/marriott/marriott_terms-of-use_20221126200132",
    "HIL-02": "hospitality/hilton/hilton_site-usage-agreement_20221126182440",
    "UAL-01": "airlines/united/united_legal-terms-conditions-notices_20221220171554",
}
for v in REUSE.values():
    assert os.path.exists(f"previous-tos/{v}.txt"), v
PRI = {"governs-ai-expressly": 0, "governs-surface": 0, "governs-surface-partial": 1,
       "notice-not-contract": 2, "adjacent-not-governing": 3, "no-reach": 4}
W.sort(key=lambda r: (r["sample_group_v2"] != "main", PRI[r["binding_v2"]], r["company"], r["doc_id"]))
sl = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
out = []
for r in W:
    f = r["file"]
    txt = f[:-len("_RAW.html")] + ".txt" if f.endswith("_RAW.html") else f
    hits = glob.glob(f"mastersheet-sources/**/{glob.escape(txt)}", recursive=True) if txt else []
    out.append(dict(
        doc_id=r["doc_id"], company=r["company"], company_slug=sl(r["company"]), vertical=sl(r["vertical"]),
        slug=sl(r["doc_id"] + "_" + r["doc_title"])[:70], url=r["url"], doc_type=r["doc_type"],
        binding_v2=r["binding_v2"], sample_group=r["sample_group_v2"],
        current_file=hits[0].replace(os.sep, "/") if hits else "NOT-FOUND:" + f,
        action="reuse" if r["doc_id"] in REUSE else "fetch",
        baseline=f"previous-tos/{REUSE[r['doc_id']]}.txt" if r["doc_id"] in REUSE else ""))
with open("previous-tos/v2-baseline-worklist.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print(len(out), collections.Counter((o["sample_group"], o["action"]) for o in out))
print("current not found:", [o["doc_id"] + " " + o["current_file"] for o in out if o["current_file"].startswith("NOT")])
