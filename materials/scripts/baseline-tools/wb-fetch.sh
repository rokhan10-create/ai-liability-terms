#!/usr/bin/env bash
# wb-fetch.sh — Wayback Machine snapshot fetcher for the AI-ToS Liability Dataset
# Finds the snapshot closest to a target date, saves RAW html + plaintext, records SHA-256.
# Usage: wb-fetch.sh <url> <company-dir> <slug> <target-ts YYYYMMDD> [vertical]
set -u
ROOT="./previous-tos"
URL="$1"; COMPANY="$2"; SLUG="$3"; TARGET="${4:-20221130}"; VERTICAL="${5:-airlines}"
OUT="$ROOT/$VERTICAL/$COMPANY"; mkdir -p "$OUT"

# --- retrying curl (IA returns 504 / "Temporarily Offline" under load) ---
rc() { local i=0; local out
  while [ $i -lt 6 ]; do
    out=$(curl -sL --compressed --max-time 90 -A "Mozilla/5.0 (research; AI-ToS liability dataset)" "$1" 2>/dev/null)
    if [ -n "$out" ] && ! grep -qi "Temporarily Offline\|504 Gateway" <<<"${out:0:600}"; then printf '%s' "$out"; return 0; fi
    i=$((i+1)); sleep $((i*8))
  done; return 1; }

CDX="http://web.archive.org/cdx/search/cdx?url=${URL#http*://}&from=20220601&to=20230601&output=json&fl=timestamp,statuscode,digest,length&collapse=digest&filter=statuscode:200"
J=$(rc "$CDX") || { echo "CDX-FAIL|$URL"; exit 2; }
[ "$(tr -d '[:space:]' <<<"$J")" = "[]" ] && { echo "NO-SNAPSHOT|$URL"; exit 3; }

# closest timestamp to TARGET
TS=$(python -c "
import json,sys
rows=json.loads(sys.stdin.read())[1:]
t=int('$TARGET'+'000000')
print(min(rows,key=lambda r:abs(int(r[0])-t))[0])
" <<<"$J") || { echo "PICK-FAIL|$URL"; exit 4; }

SNAP="http://web.archive.org/web/${TS}id_/$URL"
HTML=$(rc "$SNAP") || { echo "FETCH-FAIL|$URL|$TS"; exit 5; }
printf '%s' "$HTML" > "$OUT/${SLUG}_${TS}_RAW.html"
python - "$OUT/${SLUG}_${TS}_RAW.html" "$OUT/${SLUG}_${TS}.txt" "$URL" "$TS" <<'PY'
import re,sys,html
raw=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',raw)
t=re.sub(r'(?is)<br\s*/?>|</(p|div|li|tr|h[1-6])>','\n',t)
t=re.sub(r'(?s)<[^>]+>',' ',t); t=html.unescape(t)
t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n\s*\n+','\n\n',t)
open(sys.argv[2],'w',encoding='utf-8').write(
 f"# WAYBACK CAPTURE\n# source_url: {sys.argv[3]}\n# snapshot_ts: {sys.argv[4]}\n"
 f"# snapshot_url: http://web.archive.org/web/{sys.argv[4]}id_/{sys.argv[3]}\n# method: CDX closest-to-target, id_ raw modifier\n\n"+t.strip())
PY
SHA=$(sha256sum "$OUT/${SLUG}_${TS}_RAW.html" | cut -d' ' -f1)
BY=$(wc -c < "$OUT/${SLUG}_${TS}_RAW.html")
TXTCHARS=$(wc -m < "$OUT/${SLUG}_${TS}.txt")
echo "\"$VERTICAL\",\"$COMPANY\",\"${SLUG}_${TS}_RAW.html\",\"$URL\",\"$TS\",\"$BY\",\"$SHA\"" >> "$ROOT/WAYBACK-MANIFEST.csv"
if [ "$TXTCHARS" -lt 3000 ]; then
  echo "WARN-THIN-CAPTURE|$COMPANY|$SLUG|ts=$TS|plaintext_chars=$TXTCHARS - either an empty JS shell OR content embedded as JSON in <script> (which the .txt strips). Keyword-scan the _RAW.html before citing any result." >&2
fi
echo "OK|$COMPANY|$SLUG|ts=$TS|bytes=$BY|plaintext_chars=$TXTCHARS"
