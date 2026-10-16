"""Append a non-OK baseline result for one or more doc_ids to previous-tos/v2-baseline-fetch-log.csv.
Usage (project root):
  python previous-tos/_tools/v2-log-result.py <RESULT> <ts-or-''> <doc_id> [doc_id ...]
RESULT is one of: NOT-ARCHIVED | NO-SNAPSHOT-IN-WINDOW | LEFT-ARCHIVE | ARCHIVED-HTTP-<code> |
ARCHIVED-UNUSABLE-<reason> (copy exists but is a captcha/bot wall/empty script shell) | CAPTURE-FAILED
(the last is NOT final: the document stays in the queue)."""
import csv, datetime, sys

OKS = {"NOT-ARCHIVED", "NO-SNAPSHOT-IN-WINDOW", "LEFT-ARCHIVE", "CAPTURE-FAILED"}
res, ts, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
assert ids and (res in OKS or res.startswith("ARCHIVED-")), "bad result or no doc_ids"
assert ts == "" or (ts.isdigit() and len(ts) == 14), "ts must be 14 digits or ''"
W = {w["doc_id"]: w for w in csv.DictReader(open("previous-tos/v2-baseline-worklist.csv", encoding="utf-8"))}
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open("previous-tos/v2-baseline-fetch-log.csv", "a", encoding="utf-8", newline="") as f:
    for d in ids:
        w = W[d]
        csv.writer(f).writerow([d, w["company"], w["url"], res, ts, "", "", "", stamp])
print("logged", res, ts, ids)
