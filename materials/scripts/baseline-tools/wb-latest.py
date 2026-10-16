"""Print the timestamp of the most recent HTTP-200 Wayback capture of a URL (retries on archive errors).
Usage: python wb-latest.py <url> [from YYYY]"""
import json, sys, time, urllib.parse, urllib.request

url, frm = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "2026")
q = urllib.parse.urlencode({"url": url.split("://", 1)[-1], "output": "json", "filter": "statuscode:200",
                            "from": frm, "collapse": "digest", "fl": "timestamp"})
for attempt in range(6):
    try:
        with urllib.request.urlopen(f"http://web.archive.org/cdx/search/cdx?{q}", timeout=90) as r:
            rows = json.loads(r.read() or b"[]")
        print(rows[-1][0] if len(rows) > 1 else "")
        sys.exit(0)
    except Exception as e:
        print(f"retry {attempt + 1}: {e}", file=sys.stderr)
        time.sleep(8 * (attempt + 1))
sys.exit(1)
