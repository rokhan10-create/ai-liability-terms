"""Clause-level Nov-2022 -> current diffs for the v2 corpus.

Pairs come from previous-tos/v2-baseline-worklist.csv (current = the v2 full-read capture) plus the
fetch log (baseline = the Wayback capture saved by v2-baseline-fetch.py, or a reused pilot baseline).
Outputs (previous-tos/clause-diff-results-v2/):
  <doc_id>.txt|.json          per-document diff (clause-diff.py report)
  SUMMARY-v2.csv              document-level churn + AI-sentence classes per document
  CODED-CLAUSES-v2.csv        every S/G code in documents.csv joined to its clause-family continuity
Run from the project root: python previous-tos/_tools/v2-run-diffs.py
"""
import contextlib, csv, importlib.util, io, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cd", os.path.join(HERE, "clause-diff.py"))
cd = importlib.util.module_from_spec(spec); spec.loader.exec_module(cd)
# v2: widen the legal-sentence filter. The pilot filter dropped operative clauses phrased without
# "you/we/terms" (e.g. Elevance's AI-agent access ban, "unless expressly authorized by us"; found 2026-10-09).
cd.LEGAL = re.compile(cd.LEGAL.pattern + r"|\bus\b|\bmust\b|\bunless\b|authori[sz]|prohibit|artificial intelligence|\bAI\b", re.I)

OUT = "previous-tos/clause-diff-results-v2"
CLEAN = "previous-tos/_v2-current-clean"
os.makedirs(OUT, exist_ok=True); os.makedirs(CLEAN, exist_ok=True)
WEAK_AI = re.compile(r"automated (?:system|tool|technolog)\w*|concierge", re.I)


def ai_strict(s):
    """AI tag for v2: drop hits that rest only on 'automated system/tool/technology' or 'concierge'
    (anti-robot clauses, autodialer consent, generic algorithms) - verified 2026-10-09 on ACI-01/02, CVNA-01, WMT-01."""
    return bool(cd.AI.search(WEAK_AI.sub(" ", s)))


FAM = {"B1": "B1 txn-error non-honoring", "B2": "B2 limitation of liability", "B3": "B3 user-responsibility",
       "B4": "B4 anti-reliance", "B5": "B5 agentic / agent", "B6": "B6 accuracy / no-warranty",
       "B7": "B7 indemnification", "B8": "B8 third-party carve-out", "B9": "B9 anti-scrape / no-training",
       "B10": "B10 IP over inputs / training", "B11": "B11 automated decisions"}


def clean_current(w):
    """Return a path to an annotation-free text of the v2 current document, or (None, reason)."""
    f = w["current_file"]
    if f.lower().endswith(".pdf"):
        f = f[:-4] + ".txt"
        if not os.path.exists(f):
            return None, "pdf without .txt sibling"
    raw = open(f, encoding="utf-8-sig", errors="replace").read()
    dst = f"{CLEAN}/{w['doc_id']}.txt"
    if raw.startswith("SOURCE CAPTURE") or "FULL DOCUMENT TEXT" in raw[:20000]:
        r = subprocess.run([sys.executable, os.path.join(HERE, "strip-annotations.py"), f, dst],
                           capture_output=True, text=True)
        return (dst, "stripped annotations") if r.returncode == 0 else (None, r.stdout + r.stderr)
    body = raw
    while body.startswith("[capture]") or body.startswith("[derived"):
        body = body.split("\n", 1)[1] if "\n" in body else ""
    if re.search(r"SOURCE CAPTURE|CODER NOTE|COVERAGE STATEMENT", body[:200000]):
        return None, "contains coder annotations"
    open(dst, "w", encoding="utf-8").write(f"# V2 CURRENT (capture header removed)\n# source_file: {f}\n\n" + body)
    return dst, "ok"


def baseline_for(w, fetched):
    if w["action"] == "reuse":
        return w["baseline"], "pilot baseline (reused)"
    r = fetched.get(w["doc_id"])
    if not r or r["result"] not in ("OK", "OK-THIN"):
        return None, (r["result"] if r else "not fetched yet")
    raw = r["file"]
    # thin plaintext: feed the RAW html so clause-diff can recover JSON-embedded text
    if raw.endswith(".txt"):  # text-only capture (raw not retained)
        return raw, f"wayback {r['snapshot_ts']} ({r['side']}), text-only"
    return (raw if r["result"] == "OK-THIN" else raw[:-len("_RAW.html")] + ".txt"), f"wayback {r['snapshot_ts']} ({r['side']})"


def main():
    W = list(csv.DictReader(open("previous-tos/v2-baseline-worklist.csv", encoding="utf-8")))
    fetched = {}
    if os.path.exists("previous-tos/v2-baseline-fetch-log.csv"):
        K = ["doc_id", "company", "url", "result", "snapshot_ts", "side", "file", "plaintext_chars", "logged_utc"]
        for row in csv.reader(open("previous-tos/v2-baseline-fetch-log.csv", encoding="utf-8")):
            if row and row[0] != "doc_id":
                r = dict(zip(K, row))
                if r["doc_id"] not in fetched or r["result"] in ("OK", "OK-THIN"):
                    fetched[r["doc_id"]] = r  # an OK row is never overwritten by a later failure
    docs = {r["doc_id"]: r for r in csv.DictReader(open("documents.csv", encoding="utf-8"))}
    summary, coded, status = [], [], []
    for w in W:
        base, bwhy = baseline_for(w, fetched)
        cur, cwhy = clean_current(w)
        st = {"doc_id": w["doc_id"], "company": w["company"], "sample_group": w["sample_group"],
              "binding_v2": w["binding_v2"], "baseline": base or "", "baseline_note": bwhy, "current_note": cwhy}
        if not base or not cur:
            st["diffed"] = "no"; status.append(st); continue
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                cd.report(base, cur, f"{OUT}/{w['doc_id']}.json")
        except SystemExit as e:
            st["diffed"] = f"refused: {e}"; status.append(st); continue
        open(f"{OUT}/{w['doc_id']}.txt", "w", encoding="utf-8").write(buf.getvalue())
        d = json.load(open(f"{OUT}/{w['doc_id']}.json", encoding="utf-8"))
        for x in d["rows"]:
            x["ai"] = ai_strict(x["sentence"])
        json.dump(d, open(f"{OUT}/{w['doc_id']}.json", "w", encoding="utf-8"), indent=1)
        n = d["n_current"] or 1
        kinds = {"pre": 0, "retro": 0, "new": 0}
        for x in d["rows"]:
            if x["ai"]:
                k = cd.ai_kind(x)
                kinds["pre" if k.startswith("PRE") else "retro" if k.startswith("RETRO") else "new"] += 1
        thin = d["n_2022"] < 15
        st["diffed"] = "yes" + (" (THIN baseline: <15 legal sentences - check for empty shell)" if thin else "")
        status.append(st)
        summary.append({"doc_id": w["doc_id"], "company": w["company"], "sample_group": w["sample_group"],
                        "doc_type": w["doc_type"], "binding_v2": w["binding_v2"], "baseline_note": bwhy,
                        "sent_2022": d["n_2022"], "sent_current": d["n_current"],
                        "pct_unchanged": round(100 * d["doc_level"]["unchanged"] / n),
                        "pct_edited": round(100 * d["doc_level"]["edited"] / n),
                        "pct_new": round(100 * d["doc_level"]["new"] / n), "removed_2022": d["removed_2022"],
                        "ai_sents": sum(kinds.values()), "ai_preexisting": kinds["pre"],
                        "ai_retrofit": kinds["retro"], "ai_new": kinds["new"], "thin_baseline": thin})
        row = docs[w["doc_id"]]
        for code, fam in FAM.items():
            if row[code] not in ("S", "G"):
                continue
            sel = [x for x in d["rows"] if fam in x["families"]]
            u = sum(x["status"] == "unchanged" for x in sel); e = sum(x["status"] == "edited" for x in sel)
            nw = sum(x["status"] == "new" for x in sel); tot = len(sel)
            if row[code] == "S":
                ai_f = [x for x in sel if x["ai"]]
                basis = ai_f or [x for x in d["rows"] if x["ai"]]
                kinds = [cd.ai_kind(x)[:3] for x in basis]  # PRE / RET / NEW
                if not basis:
                    verdict = "S: NO AI SENTENCE LOCATED - manual"
                elif "PRE" in kinds:
                    verdict = "S: AI TEXT ALREADY IN 2022"
                elif "RET" in kinds:
                    verdict = "S: RETROFIT (AI words added to 2022 clause)"
                else:
                    verdict = "S: NEW AI TEXT"
                verdict += "" if ai_f else " (document-level)"
            elif tot == 0:
                verdict = "NOT LOCATED BY PATTERN"
            elif u / tot >= 0.75 and nw == 0:
                verdict = "CARRIED OVER"
            elif (e + nw) / tot >= 0.75:
                verdict = "NEW OR REWRITTEN"
            else:
                verdict = "MIXED"
            coded.append({"doc_id": w["doc_id"], "company": w["company"], "sample_group": w["sample_group"],
                          "code": code, "coded_as": row[code], "sents": tot, "unchanged": u, "edited": e, "new": nw,
                          "verdict": verdict, "thin_baseline": thin,
                          "flag": "CHECK" if verdict.startswith("S: AI TEXT ALREADY") or "manual" in verdict else ""})
    for name, rows in (("SUMMARY-v2.csv", summary), ("CODED-CLAUSES-v2.csv", coded), ("STATUS-v2.csv", status)):
        if rows:
            with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8") as fh:
                wr = csv.DictWriter(fh, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
    print(f"diffed {len(summary)} / {len(W)} documents; coded clauses joined: {len(coded)}")
    for s in summary:
        print(f"{s['doc_id']:8s} {s['company'][:18]:18s} unch {s['pct_unchanged']:3d}% edit {s['pct_edited']:3d}% "
              f"new {s['pct_new']:3d}%  AI pre/retro/new {s['ai_preexisting']}/{s['ai_retrofit']}/{s['ai_new']}"
              + ("  THIN" if s["thin_baseline"] else ""))


if __name__ == "__main__":
    main()
