"""v2 pre-ChatGPT baseline fetcher (extends the pilot baselines to the full v2 corpus).

For every v2 document in previous-tos/v2-baseline-worklist.csv that has no baseline yet:
  1. CDX query (2021-01-01 .. 2023-06-01, status 200, collapse=digest) for the document URL,
     trying www/non-www variants.
  2. Pick the LATEST snapshot on or before 2022-11-30 (pre-ChatGPT). If none exists, take the
     EARLIEST snapshot up to 2023-06-01 and flag side=after (still near-baseline, disclosed).
  3. Fetch the raw bytes with the id_ modifier, save _RAW.html + de-tagged .txt with a provenance
     header (same format as wb-fetch.sh), append WAYBACK-MANIFEST.csv, record SHA-256.
Pacing is deliberately slow (Wayback rate-limits by IP): >= 12 s between requests; the run STOPS at the
first HTTP 429 rather than retrying. Resumable: documents already OK in v2-baseline-fetch-log.csv are skipped.
Run from the project root: python previous-tos/_tools/v2-baseline-fetch.py
"""
import csv, gzip, hashlib, html, json, os, re, sys, time, urllib.error, urllib.request, zlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PT = os.path.join(ROOT, "previous-tos")
WORK = os.path.join(PT, "v2-baseline-worklist.csv")
LOG = os.path.join(PT, "v2-baseline-fetch-log.csv")
MAN = os.path.join(PT, "WAYBACK-MANIFEST.csv")
TARGET = 20221130235959
UA = "Mozilla/5.0 (research; AI-ToS liability dataset; slow-paced)"
GAP, PAUSE_429, MAX_429 = 25, 900, 0  # MAX_429=0: stop at the first 429 (respect the Archive's limit)
_last = [0.0]


def get(url):
    """Paced GET returning (status, bytes). Handles gzip; waits out 429s."""
    n429 = 0
    while True:
        wait = GAP - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
                enc = (r.headers.get("Content-Encoding") or "").lower()
                if enc == "gzip" or body[:2] == b"\x1f\x8b":
                    body = gzip.decompress(body)
                elif enc == "deflate":
                    body = zlib.decompress(body)
                return r.status, body
        except urllib.error.HTTPError as e:
            if e.code == 429:
                n429 += 1
                print(f"  429 (#{n429})", flush=True)
                if n429 > MAX_429:
                    return 429, b""
                time.sleep(PAUSE_429)
                continue
            if e.code in (502, 503, 504):
                time.sleep(60)
                continue
            return e.code, b""
        except Exception as e:  # timeouts, resets
            print(f"  net error {e!r} - retry in 60 s", flush=True)
            time.sleep(60)


def cdx(url):
    rows = []
    bare = re.sub(r"^https?://", "", url).split("#")[0]
    variants = [bare]
    if bare.startswith("www."):
        variants.append(bare[4:])
    else:
        variants.append("www." + bare)
    for v in variants:
        q = ("http://web.archive.org/cdx/search/cdx?url=" + urllib.request.quote(v, safe="/:?=&.-_~")
             + "&from=20210101&to=20230601&output=json&fl=timestamp,statuscode,digest,length"
             + "&collapse=digest&filter=statuscode:200")
        st, body = get(q)
        if st == 429:
            return None, "CDX-429"
        if st != 200:
            return [], f"CDX-ERR-{st}"  # not evidence of absence; retried on the next run
        try:
            js = json.loads(body.decode("utf-8") or "[]")
        except ValueError:
            continue
        rows = [(int(r[0]), v) for r in js[1:]]
        if rows:
            return rows, "ok"
    return [], "NO-SNAPSHOT"


def detag(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?is)<br\s*/?>|</(p|div|li|tr|h[1-6])>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()


def main():
    work = list(csv.DictReader(open(WORK, encoding="utf-8")))
    done = set()
    if os.path.exists(LOG):
        for r in csv.reader(open(LOG, encoding="utf-8")):  # tolerant of a stray header row
            if len(r) > 3 and r[3] in ("OK", "OK-THIN", "NO-SNAPSHOT", "REUSED"):
                done.add(r[0])
    newlog = not os.path.exists(LOG) or os.path.getsize(LOG) == 0
    logf = open(LOG, "a", encoding="utf-8", newline="")
    lw = csv.DictWriter(logf, fieldnames=["doc_id", "company", "url", "result", "snapshot_ts", "side",
                                          "file", "plaintext_chars", "logged_utc"])
    if newlog:
        lw.writeheader()
    for w in work:
        d = w["doc_id"]
        if d in done or w["action"] != "fetch":
            continue
        print(f"{d} {w['company']} {w['url']}", flush=True)
        rows, why = cdx(w["url"])
        rec = dict(doc_id=d, company=w["company"], url=w["url"], snapshot_ts="", side="", file="",
                   plaintext_chars="", logged_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        if rows is None:
            rec["result"] = why
            lw.writerow(rec); logf.flush()
            print("  stopping: Wayback still rate-limiting after repeated pauses", flush=True)
            break
        if not rows:
            rec["result"] = why
            lw.writerow(rec); logf.flush()
            continue
        before = [r for r in rows if r[0] <= TARGET]
        ts, variant = (max(before) if before else min(rows))
        side = "on-or-before" if before else "after"
        st, body = get(f"http://web.archive.org/web/{ts}id_/http://{variant}")
        if st != 200 or not body:
            rec.update(result=f"FETCH-{st}", snapshot_ts=ts, side=side)
            lw.writerow(rec); logf.flush()
            if st == 429:
                print("  stopping: HTTP 429 from Wayback", flush=True)
                break
            continue
        out = os.path.join(PT, w["vertical"], w["company_slug"])
        os.makedirs(out, exist_ok=True)
        base = f"{w['slug']}_{ts}"
        rawp = os.path.join(out, base + "_RAW.html")
        open(rawp, "wb").write(body)
        raw = body.decode("utf-8", errors="replace")
        txt = detag(raw)
        open(os.path.join(out, base + ".txt"), "w", encoding="utf-8").write(
            f"# WAYBACK CAPTURE\n# source_url: {w['url']}\n# snapshot_ts: {ts}\n"
            f"# snapshot_url: http://web.archive.org/web/{ts}id_/http://{variant}\n"
            f"# method: CDX latest-on-or-before 2022-11-30 (side={side}), id_ raw modifier; v2 doc {d}\n\n" + txt)
        sha = hashlib.sha256(body).hexdigest()
        with open(MAN, "a", encoding="utf-8", newline="") as mf:
            csv.writer(mf, quoting=csv.QUOTE_ALL).writerow(
                [w["vertical"], w["company_slug"], base + "_RAW.html", w["url"], ts, len(body), sha])
        rec.update(result="OK" if len(txt) >= 3000 else "OK-THIN", snapshot_ts=ts, side=side,
                   file=os.path.relpath(rawp, ROOT).replace("\\", "/"), plaintext_chars=len(txt))
        lw.writerow(rec); logf.flush()
        print(f"  {rec['result']} ts={ts} side={side} chars={len(txt)}", flush=True)
    logf.close()
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
