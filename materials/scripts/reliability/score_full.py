"""Score the full-corpus GPT recode against the dataset: validation/full-recode/RESULTS-full.md.

Run from the project root after merge_full.py:  python validation/full-recode/score_full.py
Reports agreement overall and by coder setup (Codex / ChatGPT), per clause family, binding status, repeat-coding
consistency, and lists every cell where the GPT coder disagrees with an AI-specific (S) code in the dataset.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
C = [f"B{i}" for i in range(1, 12)]
BIND = {"governs-ai-expressly", "governs-surface", "governs-surface-partial"}
D = {r["doc_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "documents.csv"), encoding="utf-8"))}
G = list(csv.DictReader(open(os.path.join(HERE, "gpt-full-sheet.csv"), encoding="utf-8")))
norm = lambda v: {"S": "S", "G": "G", "A": "A", "NA": "A", "N/A": "A", "": "A"}.get((v or "").strip().upper(), None)


def kappa(pairs):
    pairs = [p for p in pairs if None not in p]
    n = len(pairs)
    if not n:
        return float("nan"), 0, float("nan")
    po = sum(a == b for a, b in pairs) / n
    cats = {x for p in pairs for x in p}
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return (1.0 if pe == 1 else (po - pe) / (1 - pe)), n, po


def block(rows, label):
    s = [(norm(r[c]) == "S", norm(D[r["doc_id"]][c]) == "S") for r in rows for c in C]
    p = [(norm(r[c]) != "A", norm(D[r["doc_id"]][c]) != "A") for r in rows for c in C]
    b1 = [(norm(r["B1"]) == "S", norm(D[r["doc_id"]]["B1"]) == "S") for r in rows]
    bd = [(r["binding_status"] in BIND, D[r["doc_id"]]["binding_v2"] in BIND) for r in rows]
    be = [(r["binding_status"], D[r["doc_id"]]["binding_v2"]) for r in rows]
    out = []
    for name, pairs in (("AI-specific tag (S vs not), all cells", s), ("Presence, all cells", p),
                        ("B1, AI-specific (S vs not)", b1), ("Binding vs not binding", bd), ("Binding, exact category", be)):
        k, n, po = kappa(pairs)
        out.append(f"| {label} | {name} | {k:.2f} | {n} | {po:.1%} |")
    return out


lines = ["# Full-corpus GPT recode vs dataset", "",
         f"Documents: {len(G)} ({sum(r['setup'] == 'codex' for r in G)} Codex, {sum(r['setup'] == 'chatgpt' for r in G)} ChatGPT). "
         "Pre-adjudication. Dataset `na` cells are treated as A.", "",
         "| Setup | Measure | κ | n | % agree |", "|---|---|---|---|---|"]
for label, rows in (("All", G), ("Codex", [r for r in G if r["setup"] == "codex"]), ("ChatGPT", [r for r in G if r["setup"] == "chatgpt"])):
    lines += block(rows, label)

lines += ["", "## Per clause family (all 264 documents)", "", "| Family | κ S-tag | κ presence | % agree presence | dataset S | GPT S | dataset present | GPT present |", "|---|---|---|---|---|---|---|---|"]
for c in C:
    ks = kappa([(norm(r[c]) == "S", norm(D[r["doc_id"]][c]) == "S") for r in G])
    kp = kappa([(norm(r[c]) != "A", norm(D[r["doc_id"]][c]) != "A") for r in G])
    lines.append(f"| {c} | {ks[0]:.2f} | {kp[0]:.2f} | {kp[2]:.1%} | {sum(norm(D[r['doc_id']][c]) == 'S' for r in G)} | {sum(norm(r[c]) == 'S' for r in G)} | "
                 f"{sum(norm(D[r['doc_id']][c]) != 'A' for r in G)} | {sum(norm(r[c]) != 'A' for r in G)} |")

# Generic-mispricing B1: dataset G vs GPT A.
g1 = Counter((norm(D[r["doc_id"]]["B1"]), norm(r["B1"])) for r in G)
lines += ["", "## B1 cross-tab (dataset → GPT)", "", "| dataset | GPT | n |", "|---|---|---|"] + [f"| {a} | {b} | {n} |" for (a, b), n in sorted(g1.items())]

# Repeat-coding consistency: Codex batch 06 vs the ChatGPT coding of the same documents.
R = {r["doc_id"]: r for r in csv.DictReader(open(os.path.join(HERE, "retest_codex06.csv"), encoding="utf-8"))}
Gi = {r["doc_id"]: r for r in G}
both = [d for d in R if d in Gi]
rs = kappa([(norm(R[d][c]) == "S", norm(Gi[d][c]) == "S") for d in both for c in C])
rp = kappa([(norm(R[d][c]) != "A", norm(Gi[d][c]) != "A") for d in both for c in C])
lines += ["", "## Repeat coding: Codex batch 06 vs ChatGPT, same documents", "",
          f"{len(both)} documents coded independently by both GPT setups. AI-specific tag κ {rs[0]:.2f} ({rs[2]:.1%}); presence κ {rp[0]:.2f} ({rp[2]:.1%})."]

# Every cell where the dataset says S and GPT does not, or GPT says S and the dataset does not.
lines += ["", "## AI-specific disagreements (for adjudication)", "", "| doc_id | company | code | dataset | GPT | GPT source |", "|---|---|---|---|---|---|"]
n_s = 0
for r in G:
    for c in C:
        a, b = norm(D[r["doc_id"]][c]), norm(r[c])
        if (a == "S") != (b == "S"):
            n_s += 1
            lines.append(f"| {r['doc_id']} | {D[r['doc_id']]['company']} | {c} | {a} | {b} | {r['source']} |")
lines.insert(4, f"AI-specific disagreements to adjudicate: {n_s} cells (listed at the end).")
open(os.path.join(HERE, "RESULTS-full.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(l for l in lines if not l.startswith("| ") or "| All |" in l or "| Codex |" in l or "| ChatGPT |" in l or l.startswith("| B")))
