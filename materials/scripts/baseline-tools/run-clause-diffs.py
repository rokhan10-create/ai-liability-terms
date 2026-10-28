"""Run clause-diff.py over every pair in previous-tos/clause-diff-pairs.csv.
Writes previous-tos/clause-diff-results/<firm>_<doc>.txt|.json and a summary CSV.
Run from the project root: python previous-tos/_tools/run-clause-diffs.py"""
import contextlib, csv, glob, importlib.util, io, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cd", os.path.join(HERE, "clause-diff.py"))
cd = importlib.util.module_from_spec(spec); spec.loader.exec_module(cd)

OUT = "previous-tos/clause-diff-results"
os.makedirs(OUT, exist_ok=True)
summary = []
for p in csv.DictReader(open("previous-tos/clause-diff-pairs.csv", encoding="utf-8")):
    slug = re.sub(r"[^a-z0-9]+", "-", f"{p['firm']}_{p['document']}".lower()).strip("-")
    if "*" in p["current"]:  # comparator file named by capture timestamp; take the newest
        hits = sorted(glob.glob(p["current"]))
        if hits:
            p["current"] = hits[-1]
    missing = [f for f in (p["baseline"], p["current"]) if not os.path.exists(f)]
    if missing:
        print(f"SKIP {slug}: missing {missing}"); continue
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cd.report(p["baseline"], p["current"], f"{OUT}/{slug}.json")
    open(f"{OUT}/{slug}.txt", "w", encoding="utf-8").write(buf.getvalue())
    d = json.load(open(f"{OUT}/{slug}.json", encoding="utf-8"))
    n = d["n_current"] or 1
    ai = [r for r in d["rows"] if r["ai"]]
    kinds = {"pre-existing": 0, "retrofit": 0, "new": 0}
    for r in ai:
        k = cd.ai_kind(r)
        kinds["pre-existing" if k.startswith("PRE") else "retrofit" if k.startswith("RETRO") else "new"] += 1
    coded = [r for r in d["rows"] if r["families"]]
    summary.append({
        "vertical": p["vertical"], "firm": p["firm"], "document": p["document"], "current_source": p["current_source"],
        "sent_2022": d["n_2022"], "sent_current": d["n_current"],
        "pct_unchanged": round(100 * d["doc_level"]["unchanged"] / n), "pct_edited": round(100 * d["doc_level"]["edited"] / n),
        "pct_new": round(100 * d["doc_level"]["new"] / n), "removed_2022": d["removed_2022"],
        "clause_sents": len(coded),
        "clause_unchanged": sum(r["status"] == "unchanged" for r in coded),
        "clause_edited": sum(r["status"] == "edited" for r in coded),
        "clause_new": sum(r["status"] == "new" for r in coded),
        "ai_preexisting": kinds["pre-existing"], "ai_retrofit": kinds["retrofit"], "ai_new": kinds["new"],
    })
    s = summary[-1]
    print(f"{p['firm']:12s} {p['document'][:28]:28s} unchanged {s['pct_unchanged']:3d}%  edited {s['pct_edited']:3d}%  "
          f"new {s['pct_new']:3d}%  | clause sents {s['clause_sents']:3d}: {s['clause_unchanged']}/{s['clause_edited']}/{s['clause_new']}"
          f"  | AI sents pre/retro/new {kinds['pre-existing']}/{kinds['retrofit']}/{kinds['new']}")
with open(f"{OUT}/SUMMARY.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0])); w.writeheader(); w.writerows(summary)
