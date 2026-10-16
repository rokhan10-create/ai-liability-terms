#!/usr/bin/env bash
# Save an EXACT Wayback snapshot (RAW + plaintext + manifest row). Usage: wb-save.sh <url> <company> <slug> <timestamp> [vertical]
set -u
ROOT="./previous-tos"
URL="$1"; CO="$2"; SLUG="$3"; TS="$4"; VERTICAL="${5:-airlines}"; OUT="$ROOT/$VERTICAL/$CO"; mkdir -p "$OUT"
curl -sL --compressed --max-time 120 -A "Mozilla/5.0 (research)" "http://web.archive.org/web/${TS}id_/$URL" -o "$OUT/${SLUG}_${TS}_RAW.html" || exit 1
python - "$OUT/${SLUG}_${TS}_RAW.html" "$OUT/${SLUG}_${TS}.txt" "$URL" "$TS" <<'PY'
import re,sys,html
raw=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',raw)
t=re.sub(r'(?is)<br\s*/?>|</(p|div|li|tr|h[1-6])>','\n',t)
t=re.sub(r'(?s)<[^>]+>',' ',t); t=html.unescape(t)
t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n\s*\n+','\n\n',t)
open(sys.argv[2],'w',encoding='utf-8').write(
 f"# WAYBACK CAPTURE\n# source_url: {sys.argv[3]}\n# snapshot_ts: {sys.argv[4]}\n"
 f"# snapshot_url: http://web.archive.org/web/{sys.argv[4]}id_/{sys.argv[3]}\n# method: exact-timestamp capture, id_ raw modifier\n\n"+t.strip())
PY
SHA=$(sha256sum "$OUT/${SLUG}_${TS}_RAW.html" | cut -d' ' -f1); BY=$(wc -c < "$OUT/${SLUG}_${TS}_RAW.html")
TXTCHARS=$(wc -m < "$OUT/${SLUG}_${TS}.txt")
echo "\"$VERTICAL\",\"$CO\",\"${SLUG}_${TS}_RAW.html\",\"$URL\",\"$TS\",\"$BY\",\"$SHA\"" >> "$ROOT/WAYBACK-MANIFEST.csv"
if [ "$TXTCHARS" -lt 3000 ]; then
  echo "WARN-THIN-CAPTURE|$CO|$SLUG|ts=$TS|plaintext_chars=$TXTCHARS - either an empty JS shell OR content embedded as JSON in <script> (which the .txt strips). Keyword-scan the _RAW.html before citing any result." >&2
fi
echo "OK|$CO|$SLUG|$TS|$BY bytes|plaintext_chars=$TXTCHARS"
