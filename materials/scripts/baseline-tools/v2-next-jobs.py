"""Print the next N v2 baseline jobs as JSON: one entry per distinct URL still lacking a Nov-2022 copy.
A document counts as finished when the fetch log has OK / OK-THIN / NOT-ARCHIVED / NO-SNAPSHOT-IN-WINDOW /
ARCHIVED-HTTP-xxx for it, or when it is waiting in previous-tos/_manual-inbox/. Order: main sample first,
binding terms before privacy notices (worklist order). PDFs are flagged; they need the PDF path in the skill.
Usage (project root): python previous-tos/_tools/v2-next-jobs.py [N]   (default 10)"""
import csv, json, os, re, sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
W = list(csv.DictReader(open("previous-tos/v2-baseline-worklist.csv", encoding="utf-8")))
st = {}
for r in csv.reader(open("previous-tos/v2-baseline-fetch-log.csv", encoding="utf-8")):
    if len(r) > 3 and r[0] != "doc_id" and st.get(r[0]) not in ("OK", "OK-THIN"):
        st[r[0]] = r[3]
final = lambda s: s in ("OK", "OK-THIN", "NOT-ARCHIVED", "NO-SNAPSHOT-IN-WINDOW", "LEFT-ARCHIVE") \
    or (s or "").startswith("ARCHIVED-")
inbox = "previous-tos/_manual-inbox"
pending = {os.path.splitext(f)[0] for f in os.listdir(inbox)} if os.path.isdir(inbox) else set()
jobs = {}
for w in W:
    if w["action"] == "reuse" or final(st.get(w["doc_id"])) or w["doc_id"] in pending:
        continue
    j = jobs.setdefault(w["url"], {"url": w["url"], "company": w["company"], "group": w["sample_group"], "ids": [],
                                   "pdf": bool(re.search(r"\.pdf($|[?#%])|coredownload|CoC%20English", w["url"], re.I))})
    j["ids"].append(w["doc_id"])
J = list(jobs.values())
print(json.dumps({"remaining_urls": len(J), "remaining_docs": sum(len(j["ids"]) for j in J), "next": J[:N]}, indent=1))
