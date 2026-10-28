"""List every codable document for the full second coding (Codex), ordered by firm.

Run once from the project root:  python validation/full-recode/build_full_sheet.py
Scope: status_v2 new-v2-fullread or carry-over, full-text fetch, excluding t6 (marketing / incident / regulatory),
legal-hub indexes and structural proxies. Writes validation/full-recode/sheet.csv (no codes), the input to
validation/build_coding_tool.py.
"""
import csv, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "validation", "full-recode")
docs = [r for r in csv.DictReader(open(os.path.join(ROOT, "documents.csv"), encoding="utf-8"))
        if r["status_v2"] in ("new-v2-fullread", "carry-over")
        and r["fetch_depth"].startswith("full-fetch")
        and not r["doc_type"].startswith("t6") and r["doc_type"] not in ("legal-hub-index", "structural-proxy")]
index = {}
for p in glob.glob(os.path.join(ROOT, "mastersheet-sources", "**", "*"), recursive=True):
    index.setdefault(os.path.basename(p), os.path.relpath(p, ROOT))
missing = [r["doc_id"] for r in docs if os.path.basename(r["file"]) not in index]
assert not missing, missing
docs.sort(key=lambda r: (r["company"].lower(), r["doc_id"]))  # a firm's documents stay together in one batch
with open(os.path.join(OUT, "sheet.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["position", "doc_id", "company", "doc_type", "url", "local_file"])
    for pos, r in enumerate(docs, 1):
        w.writerow([pos, r["doc_id"], r["company"], r["doc_type"], r["url"], index[os.path.basename(r["file"])]])
print(f"{len(docs)} documents from {len({r['company'] for r in docs})} firms -> validation/full-recode/sheet.csv")
