#!/usr/bin/env bash
# Binary-search Wayback snapshots for the FIRST appearance of a keyword in a document.
# Distinguishes fetch failure / unrendered JS shell (exit 2) from genuine absence.
# Usage: wb-birthdate.sh <url> <keyword> [from YYYYMMDD]
set -u
URL="$1"; KW="$2"; FROM="${3:-20221101}"; TMP="$USERPROFILE/AppData/Local/Temp/wb-birthdate-$$"; mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT
rc(){ local i=0; while [ $i -lt 6 ]; do
    curl -sL --compressed --max-time 90 -A "Mozilla/5.0 (research)" "$1" -o "$2" 2>/dev/null
    if [ -s "$2" ] && ! head -c 400 "$2" | grep -qi "Temporarily Offline\|504 Gateway"; then return 0; fi
    i=$((i+1)); sleep $((i*7)); done; return 1; }
rc "http://web.archive.org/cdx/search/cdx?url=${URL#http*://}&from=${FROM}&output=json&fl=timestamp&collapse=digest&filter=statuscode:200" "$TMP/cdx.json" || { echo "CDX-FAIL"; exit 2; }
# tr -d '\r': Windows Python emits CRLF, and mapfile keeps the CR, corrupting every snapshot URL
mapfile -t TS < <(python -c "import json;print('\n'.join(x[0] for x in json.load(open(r'$TMP/cdx.json'))[1:]))" | tr -d '\r')
N=${#TS[@]}; [ "$N" -eq 0 ] && { echo "NO-SNAPSHOTS"; exit 2; }
echo "snapshots(distinct-digest,200) = $N   range ${TS[0]} .. ${TS[$((N-1))]}"
# returns 0=present 1=absent 2=unreadable (fetch failed, or an empty JS shell)
# Unreadable = thin plaintext AND no legal vocabulary in the RAW html. Pages whose text is JSON-embedded
# in <script> (thin plaintext, but legal words present in raw) are still searched.
has(){ rc "http://web.archive.org/web/${1}id_/$URL" "$TMP/s.html" || { echo "    !! fetch failed at $1" >&2; return 2; }
       local verdict; verdict=$(python -c "
import re,html
raw=open(r'$TMP/s.html',encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',raw); t=re.sub(r'(?s)<[^>]+>',' ',t)
chars=len(re.sub(r'\s+',' ',html.unescape(t)))
legal=sum(raw.lower().count(w) for w in ('liabilit','warrant','arbitrat','indemn'))
print('shell' if chars<3000 and legal<3 else 'ok', chars, legal)" | tr -d '\r')
       [ "${verdict%% *}" = "shell" ] && { echo "    !! empty shell at $1 ($verdict) - treating as unreadable" >&2; return 2; }
       grep -qia "$KW" "$TMP/s.html"; }
# walk back from the latest until a readable snapshot is found
while :; do has "${TS[$((N-1))]}"; r=$?; [ $r -ne 2 ] && break; TS=("${TS[@]:0:$((N-1))}"); N=$((N-1)); [ $N -eq 0 ] && { echo "no readable snapshot"; exit 2; }; done
[ $r -ne 0 ] && { echo "ABSENT even in latest readable snapshot ${TS[$((N-1))]}"; exit 0; }
while :; do has "${TS[0]}"; r=$?; [ $r -ne 2 ] && break; TS=("${TS[@]:1}"); N=$((N-1)); [ $N -le 1 ] && { echo "no readable early snapshot"; exit 2; }; done
[ $r -eq 0 ] && { echo "PRESENT already in earliest readable snapshot ${TS[0]}"; exit 0; }
lo=0; hi=$((N-1)); p=0
while [ $((hi-lo)) -gt 1 ]; do
  mid=$(((lo+hi)/2)); p=$((p+1)); has "${TS[$mid]}"; r=$?
  if [ $r -eq 2 ]; then echo "  probe$p ${TS[$mid]} UNREADABLE - dropped"; TS=("${TS[@]:0:$mid}" "${TS[@]:$((mid+1))}"); hi=$((hi-1)); continue; fi
  if [ $r -eq 0 ]; then hi=$mid; else lo=$mid; fi
  echo "  probe$p ${TS[$mid]} -> $([ $r -eq 0 ] && echo PRESENT || echo absent) | window ${TS[$lo]}..${TS[$hi]}"
done
echo "FIRST-APPEARANCE of '$KW': absent ${TS[$lo]} -> present ${TS[$hi]}"
