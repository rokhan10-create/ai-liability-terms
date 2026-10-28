"""Clause-level diff between a Nov-2022 baseline and a current version of the same governing document.

Answers: (1) how much of the legal text changed at all, and (2) for each clause family we code,
whether the current language is verbatim from 2022, edited from a 2022 sentence, or new.

Usage: python clause-diff.py <baseline(.txt|_RAW.html)> <current(.txt|_RAW.html)> [--json out.json]
"""
import difflib, html, json, re, sys

UNCHANGED, EDITED = 0.90, 0.60   # similarity thresholds against the best-matching 2022 sentence

LEGAL = re.compile(r"liabil|warrant|indemn|arbitrat|agree|terms|shall|may not|responsib|rights?\b|"
                   r"license|damages|consent|content|service|you |we |our |your ", re.I)
AI = re.compile(r"artificial intelligence|generative|\bA\.?I\.?\b|AI[- ]powered|chatbot|virtual assistant|"
                r"machine learning|large language|\bLLMs?\b|\bAI agents?\b|agentic|autonomous|ask bonvoy|rufus|"
                r"magic apron|concierge|automated (?:system|tool|technolog)", re.I)
FAMILIES = {  # current CLAUDE.md codebook numbering
    "B1 txn-error non-honoring": r"\bhono(u)?r|typographical|mispric|pricing error|error.{0,40}(cancel|correct)",
    "B2 limitation of liability": r"limitation of liability|consequential|in no event|not be liable|no liability",
    "B3 user-responsibility": r"you (are|shall be|will be) (solely )?responsible|at your (own|sole) risk",
    "B4 anti-reliance": r"\brel(y|ies|iance)\b|\bverify\b|independently (confirm|verify)|consult a",
    "B5 agentic / agent": r"agentic|autonomous|\bAI agents?\b|agent terms|\ban agent\b(?! of)|acting on your behalf",
    "B6 accuracy / no-warranty": r"as is|as available|without warrant|accura|error[- ]free",
    "B7 indemnification": r"indemnif|hold harmless",
    "B8 third-party carve-out": r"third[- ]part(y|ies)",
    "B9 anti-scrape / no-training": r"reverse engineer|scrap(e|ing)|data mining|\brobots?\b|spider|"
                                    r"circumvent|(develop|train|improve).{0,40}(model|machine learning)",
    "B10 IP over inputs / training": r"perpetual|royalty[- ]free|irrevocable|training data|to train",
    "B11 automated decisions": r"automated decision|profiling|solely automated",
}


def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    if re.search(r"SOURCE CAPTURE|CODER NOTE|COVERAGE STATEMENT", raw[:200000]):
        raise SystemExit(f"REFUSED: {path} contains project annotations (coder notes/provenance header); "
                         "diff against a clean capture instead")
    if raw.startswith("# "):  # provenance header block (WAYBACK / LIVE CAPTURE): drop up to first blank line
        raw = raw.split("\n\n", 1)[1] if "\n\n" in raw else ""
    if path.lower().endswith(".html"):
        stripped = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
        text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", stripped))
        if len(text.split()) < 1500:  # JSON-embedded page: keep <script> content too (see README)
            body = raw.replace("\\n", "\n").replace('\\"', '"').replace("\\u0026", "&")
            text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", body))
            text = re.sub(r"[#*_`\[\]]+|\(https?://[^)]*\)", " ", text)
        return text
    return raw


def sentences(text):
    text = re.sub(r"[‘’“”]", "'", text).replace("–", "-").replace("—", "-")
    parts = re.split(r"(?<=[.;!?])\s+|\n{2,}", text)
    out = []
    for p in parts:
        p = re.sub(r"\s+", " ", p).strip()
        if len(p.split()) >= 10 and LEGAL.search(p) and not re.search(r"[{}]|function\(|var |=>", p):
            out.append(p)
    return list(dict.fromkeys(out))


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower()).split()


def best_match(sent, pool):
    a = norm(sent)
    best, best_s = 0.0, ""
    sm = difflib.SequenceMatcher(autojunk=False)
    sm.set_seq2(a)
    for cand, b in pool:
        if not b or min(len(a), len(b)) / max(len(a), len(b)) < best * 0.9:
            continue
        sm.set_seq1(b)
        if sm.real_quick_ratio() <= best or sm.quick_ratio() <= best:
            continue
        r = sm.ratio()
        if r > best:
            best, best_s = r, cand
            if r == 1.0:
                break
    return best, best_s


def status(r):
    return "unchanged" if r >= UNCHANGED else "edited" if r >= EDITED else "new"


def ai_kind(x):
    """PRE-EXISTING only if the matched 2022 sentence itself carries the AI wording; else RETROFIT/NEW."""
    if x["ratio"] >= 0.5 and AI.search(x["match_2022"] or ""):
        return "PRE-EXISTING (already in 2022)"
    return "RETROFIT (AI words added to a 2022 sentence)" if x["ratio"] >= 0.5 else "NEW TEXT"


def run(base_path, cur_path):
    base = sentences(load(base_path))
    cur = sentences(load(cur_path))
    pool = [(s, norm(s)) for s in base]
    rows = []
    for s in cur:
        r, m = best_match(s, pool)
        fams = [f for f, pat in FAMILIES.items() if re.search(pat, s, re.I)]
        rows.append({"sentence": s, "ratio": round(r, 3), "status": status(r), "match_2022": m,
                     "families": fams, "ai": bool(AI.search(s))})
    cur_pool = [(s, norm(s)) for s in cur]
    removed = [s for s in base if best_match(s, cur_pool)[0] < EDITED]
    return base, rows, removed


def report(base_path, cur_path, json_out=None):
    base, rows, removed = run(base_path, cur_path)
    n = len(rows)
    cnt = {k: sum(1 for x in rows if x["status"] == k) for k in ("unchanged", "edited", "new")}
    print(f"baseline: {base_path}\ncurrent:  {cur_path}")
    print(f"legal sentences: 2022={len(base)}  current={n}")
    if n:
        print("document level: " + "  ".join(f"{k} {v} ({v / n:.0%})" for k, v in cnt.items())
              + f"  | 2022 sentences removed: {len(removed)}")
    print("\nclause families (current sentences): unchanged / edited / new")
    fam_summary = {}
    for f in FAMILIES:
        sel = [x for x in rows if f in x["families"]]
        if not sel:
            continue
        c = {k: sum(1 for x in sel if x["status"] == k) for k in ("unchanged", "edited", "new")}
        fam_summary[f] = c
        print(f"  {f:32s} {c['unchanged']:3d} / {c['edited']:3d} / {c['new']:3d}")
    ai_rows = [x for x in rows if x["ai"]]
    print(f"\nAI-mentioning current sentences: {len(ai_rows)}")
    for x in ai_rows:
        kind = ai_kind(x)
        print(f"  [{kind}] r={x['ratio']}  {x['sentence'][:180]}")
        if kind.startswith("RETROFIT"):
            print(f"      2022: {x['match_2022'][:180]}")
    if json_out:
        json.dump({"baseline": base_path, "current": cur_path, "n_2022": len(base), "n_current": n,
                   "doc_level": cnt, "removed_2022": len(removed), "families": fam_summary, "rows": rows,
                   "removed": removed}, open(json_out, "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    args = sys.argv[1:]
    out = None
    if "--json" in args:
        i = args.index("--json"); out = args[i + 1]; del args[i:i + 2]
    report(args[0], args[1], out)
