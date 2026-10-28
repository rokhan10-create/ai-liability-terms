"""Score the human validation against the dataset (paper §2.3). Pre-adjudication; dataset na/U cells are scored as A.

Paper set: the 30 documents with in_paper_set = 1, i.e. positions 1-29 except WSM-01, plus CMX-01 (position 39).
Run from the project root: python validation/human/score_human.py
Writes validation/human/human-coder-codings.csv (the 30 paper-set documents).
"""
import csv, random

FAM = [f"B{i}" for i in range(1, 12)]
BIND = ("governs-ai-expressly", "governs-surface", "governs-surface-partial")
PAPER_DROP, PAPER_ADD = {"WSM-01"}, {"CMX-01"}
D = {r["doc_id"]: r for r in csv.DictReader(open("documents.csv", encoding="utf-8"))}
H = [r for r in csv.DictReader(open("validation/human/coding-sheet-completed.csv", encoding="utf-8-sig")) if r["B1"]]
in_paper = lambda r: (int(r["position"]) <= 29 and r["doc_id"] not in PAPER_DROP) or r["doc_id"] in PAPER_ADD
norm = lambda v: "A" if v.strip().lower() in ("na", "n-a", "", "u") else v.strip()


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    cats = {x for p in pairs for x in p}
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


MEASURES = {
    "AI-specific tag (S vs not S)": lambda R: [(norm(r[f]) == "S", norm(D[r["doc_id"]][f]) == "S") for r in R for f in FAM],
    "Clause presence (S or G vs A)": lambda R: [(norm(r[f]) != "A", norm(D[r["doc_id"]][f]) != "A") for r in R for f in FAM],
    "Full S / G / A": lambda R: [(norm(r[f]), norm(D[r["doc_id"]][f])) for r in R for f in FAM],
    "B1 (S / G / A)": lambda R: [(norm(r["B1"]), norm(D[r["doc_id"]]["B1"])) for r in R],
    "Incorporation (binding vs not)": lambda R: [(r["binding_status"] == "binding", D[r["doc_id"]]["binding_v2"] in BIND) for r in R],
}


def report(rows, label, ci=False):
    print(f"\n== {label}: {len(rows)} documents, {len({r['company'] for r in rows})} firms")
    rng = random.Random(20261020)
    for name, fn in MEASURES.items():
        po, k = kappa(fn(rows))
        line = f"  {name:32s} kappa {k:.2f}  agree {po:.1%}  n={len(fn(rows))}"
        if ci:  # 95% CI from 5,000 bootstrap resamples of documents
            bs = []
            for _ in range(5000):
                try:
                    bs.append(kappa(fn([rng.choice(rows) for _ in rows]))[1])
                except ZeroDivisionError:
                    pass
            bs.sort()
            line += f"  CI {bs[int(0.025 * len(bs))]:.2f}-{bs[int(0.975 * len(bs)) - 1]:.2f}"
        print(line)


P = [r for r in H if in_paper(r)]
report(P, "Paper set", ci=True)
cols = ["position", "doc_id", "company", "doc_type", "url", "binding_status"] + FAM + ["minutes_spent"]
with open("validation/human/human-coder-codings.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in sorted(P, key=lambda r: int(r["position"])):
        w.writerow([r[c] for c in cols])
