"""Merge the full-corpus GPT recode into one sheet: validation/full-recode/gpt-full-sheet.csv.

Run from the project root:  python validation/full-recode/merge_full.py

Sources (one row per document; a document is taken from exactly one source):
- Codex batches 01-05 and 11 (validation/full-recode/codex/batch-NN.csv), setup "codex"
- ChatGPT chats 01-29 (validation/full-recode/chatgpt/chat-NN.csv), setup "chatgpt"
Codex batch 06 (30 of its 34 documents, run before credits ran out) overlaps ChatGPT chats; it is kept out of
the merged sheet and used only as a repeat-coding check (retest_codex06.csv is written for that).
"""
import csv, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
C = [f"B{i}" for i in range(1, 12)]
H = ("position,doc_id,company,binding_status," + ",".join(C) + ",names_ai,b4_register,special_flags,trigger_quotes,notes").split(",")


def load(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    return [{k.strip(): (v or "").strip() for k, v in r.items() if k} for r in rows]


rows, src = {}, {}
for n in ("01", "02", "03", "04", "05", "11"):
    for r in load(os.path.join(HERE, "codex", f"batch-{n}.csv")):
        rows[r["doc_id"]] = r
        src[r["doc_id"]] = f"codex batch-{n}"
for f in sorted(glob.glob(os.path.join(HERE, "chatgpt", "chat-*.csv"))):
    tag = re.search(r"chat-\d+", f)[0]
    for r in load(f):
        assert r["doc_id"] not in rows, f"{r['doc_id']} coded twice ({src[r['doc_id']]} and {tag})"
        rows[r["doc_id"]] = r
        src[r["doc_id"]] = f"chatgpt {tag}"

expected = {r["doc_id"] for r in csv.DictReader(open(os.path.join(HERE, "sheet.csv"), encoding="utf-8"))}
missing, extra = sorted(expected - set(rows)), sorted(set(rows) - expected)
bad = [(d, c, r[c]) for d, r in rows.items() for c in C if r.get(c) not in ("S", "G", "A", "U")]
assert not missing and not extra and not bad, (missing, extra, bad)

out = sorted(rows.values(), key=lambda r: int(r["position"]))
with open(os.path.join(HERE, "gpt-full-sheet.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=H + ["setup", "source"])
    w.writeheader()
    for r in out:
        w.writerow({**{k: r.get(k, "") for k in H}, "setup": src[r["doc_id"]].split()[0], "source": src[r["doc_id"]]})
print(f"{len(out)} documents: {sum(s.startswith('codex') for s in src.values())} Codex, {sum(s.startswith('chatgpt') for s in src.values())} ChatGPT")

# Codex batch 06 as a repeat-coding check against the ChatGPT codings of the same documents.
with open(os.path.join(HERE, "retest_codex06.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=H)
    w.writeheader()
    for r in load(os.path.join(HERE, "codex", "batch-06.csv")):
        w.writerow({k: r.get(k, "") for k in H})
