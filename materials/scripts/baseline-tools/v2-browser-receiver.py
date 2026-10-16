"""Local receiver for browser-session Wayback captures (one page at a time). TEXT-ONLY storage.

The browser POSTs {doc_ids:[...], url, company, ts, orig, method, result, html | b64(pdf)}.
For result == "OK" the receiver extracts the document TEXT (HTML: scripts/styles dropped, block breaks kept,
with JSON-embedded text recovered for script-rendered pages; PDF: pypdf), computes the SHA-256 and size of
the raw bytes it received, and writes ONLY previous-tos/_manual-inbox/<doc_id>.txt with a provenance header.
Raw HTML/PDF bytes are never written to disk. v2-ingest-manual.py files the .txt as the baseline.
Other results are appended to v2-baseline-fetch-log.csv.
Run from the project root: python previous-tos/_tools/v2-browser-receiver.py   (127.0.0.1:8766)"""
import base64, csv, datetime, hashlib, html as H_, http.server, io, json, os, re

INBOX = os.path.abspath("previous-tos/_manual-inbox")
LOG = os.path.abspath("previous-tos/v2-baseline-fetch-log.csv")
os.makedirs(INBOX, exist_ok=True)


def html_text(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?is)<br\s*/?>|</(p|div|li|tr|h[1-6]|section|article)>", "\n", t)
    t = H_.unescape(re.sub(r"(?s)<[^>]+>", " ", t))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()
    if len(t.split()) < 1500:  # script-rendered page: text may sit in <script> JSON (see previous-tos/README.md)
        body = raw.replace("\\n", "\n").replace('\\"', '"').replace("\\u0026", "&")
        alt = H_.unescape(re.sub(r"(?s)<[^>]+>", " ", body))
        alt = re.sub(r"[#*_`\[\]]+|\(https?://[^)]*\)", " ", alt)
        alt = re.sub(r"[ \t\xa0]+", " ", alt)
        if len(alt.split()) > 2 * len(t.split()):
            t = t + "\n\n# --- text recovered from embedded script data (JSON-rendered page) ---\n\n" + alt.strip()
    return t


def pdf_text(data):
    from pypdf import PdfReader
    return "\n\n".join((p.extract_text() or "") for p in PdfReader(io.BytesIO(data)).pages).strip()


class H(http.server.BaseHTTPRequestHandler):
    def cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_OPTIONS(self):
        self.send_response(204); self.cors(); self.end_headers()

    def do_POST(self):
        d = json.loads(self.rfile.read(int(self.headers["Content-Length"])).decode("utf-8"))
        ids = [re.sub(r"[^A-Za-z0-9-]", "", x) for x in d["doc_ids"]]
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        reply = {"ok": 1}
        if d["result"] == "OK":
            assert re.fullmatch(r"\d{14}", d["ts"])
            if d.get("b64"):
                raw, kind = base64.b64decode(d["b64"]), "pdf"
                text = pdf_text(raw)
            else:
                raw, kind = d["html"].encode("utf-8"), "html"
                text = html_text(d["html"])
            method = re.sub(r"[^\w .;:()/=-]", "", d.get("method", "browser-session capture"))[:200]
            snap = f"https://web.archive.org/web/{d['ts']}/{d['orig']}"
            open(os.path.join(INBOX, ids[0] + ".txt"), "w", encoding="utf-8").write(
                f"# saved-from: {snap}\n# capture-method: {method}\n# raw_type: {kind}\n"
                f"# raw_sha256: {hashlib.sha256(raw).hexdigest()}\n# raw_bytes: {len(raw)}\n"
                f"# raw_retained: no (text-only capture)\n# doc_ids: {','.join(ids)}\n# received_utc: {stamp}\n\n" + text)
            reply.update(words=len(text.split()))
        else:
            with open(LOG, "a", encoding="utf-8", newline="") as f:
                w = csv.writer(f)
                for i in ids:
                    w.writerow([i, d.get("company", ""), d["url"], d["result"], d.get("ts", ""), "", "", "", stamp])
        print(stamp, d["result"], ",".join(ids), d.get("ts", ""), reply.get("words", ""), flush=True)
        self.send_response(200); self.cors(); self.end_headers()
        self.wfile.write(json.dumps(reply).encode())

    def log_message(self, *a):
        pass


http.server.ThreadingHTTPServer(("127.0.0.1", 8766), H).serve_forever()
