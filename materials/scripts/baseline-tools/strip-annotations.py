"""Derive a clean document text from an annotated mastersheet capture.
Keeps only the span between "FULL DOCUMENT TEXT" and "END OF DOCUMENT", removes every [bracketed coder
note or section tag] and the ----- / ===== rule lines. Refuses files without those markers, or files that
declare themselves excerpts. Usage: python strip-annotations.py <annotated.txt> <clean_out.txt>"""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="replace").read()
if re.search(r"COVERAGE STATEMENT|characters \d[\d,]* ?- ?\d[\d,]* of|omitted portion", t, re.I):
    sys.exit(f"REFUSED: {src} is an excerpt, not the full document")
a, b = t.find("FULL DOCUMENT TEXT"), t.find("END OF DOCUMENT")
if a < 0 or b < 0:
    sys.exit(f"REFUSED: {src} has no FULL DOCUMENT TEXT / END OF DOCUMENT markers")
body = t[a + len("FULL DOCUMENT TEXT"):b]
body = re.sub(r"\[[^\]]*\]", " ", body)                     # coder notes + section tags
body = re.sub(r"^\s*[-=]{5,}\s*$", "", body, flags=re.M)     # rule lines
body = re.sub(r"[ \t]+\n", "\n", body)
open(dst, "w", encoding="utf-8").write(
    f"# CLEANED FROM ANNOTATED CAPTURE\n# source_file: {src}\n# method: strip-annotations.py "
    f"(span between FULL DOCUMENT TEXT/END OF DOCUMENT markers; [bracketed] notes removed)\n\n" + body.strip() + "\n")
print(f"OK {dst}: {len(body.split())} words")
