"""v2 baseline fetcher, playback route (no CDX API).

Used after the Wayback CDX index endpoint began returning HTTP 429 to this machine while ordinary page
playback still worked (verified 2026-10-10). For each worklist document still lacking a baseline:
  GET https://web.archive.org/web/20221130235959/<url>
Wayback redirects (inside the archive) to the snapshot CLOSEST to that time, which is the pilot's selection
rule (closest either side; side recorded). Redirects are followed by hand. Any redirect that leaves
web.archive.org is rejected (an archived redirect replayed to the live site must never be saved as 2022).
Accepted only if the snapshot is within 2021-01-01 .. 2023-06-01; otherwise logged NO-SNAPSHOT-IN-WINDOW
with the nearest timestamp. The page is written to previous-tos/_manual-inbox/<doc_id>.html with its
snapshot address; v2-ingest-manual.py then strips the toolbar and rewriting and files it.
Pacing: >= 20 s between requests, one process, STOP at the first 429.
Run from the project root: python previous-tos/_tools/v2-baseline-fetch-playback.py"""
import csv, gzip, os, re, sys, time, urllib.error, urllib.parse, urllib.request, zlib

PT = "previous-tos"
INBOX = f"{PT}/_manual-inbox"
LOG = f"{PT}/v2-baseline-fetch-log.csv"
UA = "Mozilla/5.0 (research; AI-ToS liability dataset; slow-paced)"
GAP = 30
LO, HI, TARGET = 20210101000000, 20230601000000, 20221130235959
_last = [0.0]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def get(url):
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    try:
        r = OPENER.open(req, timeout=120)
        st, hdr, body = r.status, r.headers, r.read()
    except urllib.error.HTTPError as e:
        st, hdr, body = e.code, e.headers, e.read() if e.code < 300 or e.code >= 400 else b""
    except Exception as e:
        return "NET", None, repr(e).encode()
    enc = (hdr.get("Content-Encoding") or "").lower() if hdr else ""
    if body[:2] == b"\x1f\x8b" or enc == "gzip":
        try: body = gzip.decompress(body)
        except Exception: pass
    elif enc == "deflate":
        try: body = zlib.decompress(body)
        except Exception: pass
    return st, hdr, body


def resolve(url):
    cur = "https://web.archive.org/web/20221130235959/" + url
    for _ in range(6):
        st, hdr, body = get(cur)
        if st == 429:
            return "STOP", None, None, None
        if st in (301, 302, 303, 307, 308):
            nxt = urllib.parse.urljoin(cur, hdr.get("Location", ""))
            if urllib.parse.urlparse(nxt).hostname != "web.archive.org":
                return "LEFT-ARCHIVE", None, None, nxt
            cur = nxt
            continue
        if st == 404:
            return "NOT-ARCHIVED", None, None, None
        if st != 200:
            return f"HTTP-{st}", None, None, None
        m = re.search(r"/web/(\d{14})[a-z_]*/(.+)$", cur)
        if not m:
            return "NO-TS", None, None, cur
        return "OK", m.group(1), m.group(2), body
    return "TOO-MANY-REDIRECTS", None, None, None


def main():
    work = [w for w in csv.DictReader(open(f"{PT}/v2-baseline-worklist.csv", encoding="utf-8")) if w["action"] == "fetch"]
    final = {"OK", "OK-THIN", "NO-SNAPSHOT-IN-WINDOW", "NOT-ARCHIVED"}
    done = set()
    for r in csv.reader(open(LOG, encoding="utf-8")):
        if len(r) > 3 and r[3] in final:
            done.add(r[0])
    os.makedirs(INBOX, exist_ok=True)
    pending = {os.path.splitext(f)[0] for f in os.listdir(INBOX) if f.endswith(".html")}
    by_url = {}
    for w in work:
        by_url.setdefault(w["url"], []).append(w)
    lw = csv.writer(open(LOG, "a", encoding="utf-8", newline=""))
    for url, ws in by_url.items():
        ids = [w["doc_id"] for w in ws]
        if all(d in done for d in ids) or any(d in pending for d in ids):
            continue
        print(f"{', '.join(ids)} {ws[0]['company']} {url}", flush=True)
        res, ts, orig, body = resolve(url)
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        if res == "STOP":
            print("  HTTP 429 - stopping (no retry)", flush=True)
            break
        if res == "OK" and not (LO <= int(ts) <= HI):
            res = "NO-SNAPSHOT-IN-WINDOW"
        if res != "OK":
            for w in ws:
                lw.writerow([w["doc_id"], w["company"], url, res, ts or "", "", "", "", stamp])
            print(f"  {res}" + (f" (nearest {ts})" if ts else "") + (f" -> {orig}" if res == "LEFT-ARCHIVE" else ""), flush=True)
            continue
        snap = f"https://web.archive.org/web/{ts}/{orig}"
        html = body.decode("utf-8", errors="replace")
        open(f"{INBOX}/{ws[0]['doc_id']}.html", "w", encoding="utf-8").write(
            f"<!-- saved from url=({len(snap):04d}){snap} -->\n" + html)
        side = "on-or-before" if int(ts) <= TARGET else "after"
        print(f"  saved ts={ts} ({side}) bytes={len(body)}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
