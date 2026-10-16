"""File researcher-saved Wayback pages (previous-tos/_manual-inbox/*.htm*) as Nov-2022 baselines.

Each page saved from Chrome ("Webpage, HTML only") carries a "saved from url=" comment holding the snapshot
address https://web.archive.org/web/<timestamp>/<original-url>. The Wayback banner comment ("FILE ARCHIVED
ON ...") is a fallback. The original URL is matched to v2-baseline-worklist.csv. The Wayback toolbar and
URL rewriting are stripped. The file is saved with the same naming and provenance header as the scripted
fetcher, and a manifest row and fetch-log rows are appended (method = manual browser save). Processed inbox
files move to _manual-inbox/processed/.
Run from the project root: python previous-tos/_tools/v2-ingest-manual.py"""
import csv, datetime, glob, hashlib, html, json, os, re, shutil

PT = "previous-tos"
INBOX = f"{PT}/_manual-inbox"
TARGET = 20221130235959
W = list(csv.DictReader(open(f"{PT}/v2-baseline-worklist.csv", encoding="utf-8")))


def norm(u):
    u = html.unescape(u).strip()
    u = re.sub(r"^https?://", "", u, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I).split("#")[0].rstrip("/")
    host, _, rest = u.partition("/")
    return host.lower() + "/" + rest


def nopath_q(u):
    return norm(u).split("?")[0]


by_url, by_path = {}, {}
for w in W:
    by_url.setdefault(norm(w["url"]), []).append(w)
    by_path.setdefault(nopath_q(w["url"]), []).append(w)


def snapshot(raw):
    m = re.search(r"saved from url=\(\d+\)(\S+?)\s*-->", raw[:3000])
    if m:
        s = re.search(r"web\.archive\.org/web/(\d{14})[a-z_]*/(.+)", m.group(1))
        if s:
            return s.group(1), s.group(2)
    w = re.search(r"__wm\.wombat\(\s*[\"'](https?://[^\"']+)[\"']\s*,\s*[\"'](\d{14})[\"']", raw)
    if w:  # Wayback's page-init call names the archived URL and timestamp exactly
        return w.group(2), w.group(1)
    m = re.search(r"FILE ARCHIVED ON (\d\d:\d\d:\d\d) (\w{3} \d\d?, \d{4})", raw)
    o = re.search(r"<input[^>]+name=[\"']?url[\"']?[^>]+value=[\"'](https?://[^\"']+)", raw)  # toolbar URL box
    if m and o:
        ts = datetime.datetime.strptime(m.group(2) + " " + m.group(1), "%b %d, %Y %H:%M:%S").strftime("%Y%m%d%H%M%S")
        return ts, o.group(1)
    return None, None


def clean(raw):
    raw = re.sub(r"(?s)<!-- BEGIN WAYBACK TOOLBAR INSERT -->.*?<!-- END WAYBACK TOOLBAR INSERT -->", " ", raw)
    raw = re.sub(r"(?s)<!--\s*FILE ARCHIVED ON.*?-->", " ", raw)
    raw = re.sub(r"https?://web\.archive\.org/web/\d{14}[a-z_]*/", "", raw)
    return re.sub(r"(?s)<script[^>]*archive\.org[^>]*>.*?</script>", " ", raw)


def detag(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?is)<br\s*/?>|</(p|div|li|tr|h[1-6])>", "\n", t)
    t = html.unescape(re.sub(r"(?s)<[^>]+>", " ", t))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()


def method_of(raw):
    m = re.search(r"<!-- capture-method: (.*?) -->", raw[:4000])
    return m.group(1) if m else "researcher browser save (Ctrl+S)"


def file_pdfs():
    """PDF captures from the browser receiver: <doc>.pdf + <doc>.pdf.json {ts, orig, doc_ids}."""
    from pypdf import PdfReader
    n = 0
    for meta in sorted(glob.glob(f"{INBOX}/*.pdf.json")):
        info = json.load(open(meta, encoding="utf-8")); pdf = meta[:-5]
        ws = [w for w in W if w["doc_id"] in info["doc_ids"]]
        if not ws or not os.path.exists(pdf):
            print(f"??  {os.path.basename(meta)}: no matching worklist doc or missing PDF"); continue
        ts, w = info["ts"], ws[0]
        side = "on-or-before" if int(ts) <= TARGET else "after"
        out = f"{PT}/{w['vertical']}/{w['company_slug']}"; os.makedirs(out, exist_ok=True)
        base = f"{w['slug']}_{ts}"
        data = open(pdf, "rb").read()
        try:
            txt = "\n\n".join((p.extract_text() or "") for p in PdfReader(pdf).pages).strip()
        except Exception as e:
            print(f"??  {os.path.basename(pdf)}: not a readable PDF ({e!r}) - kept in inbox"); continue
        shutil.copy(pdf, f"{out}/{base}.pdf")
        open(f"{out}/{base}.txt", "w", encoding="utf-8").write(
            f"# WAYBACK CAPTURE\n# source_url: {w['url']}\n# snapshot_ts: {ts}\n"
            f"# snapshot_url: https://web.archive.org/web/{ts}id_/{info['orig']}\n"
            f"# method: browser-session capture of archived PDF closest to 2022-11-30 (side={side}); text via pypdf; "
            f"v2 doc(s) {', '.join(x['doc_id'] for x in ws)}\n\n" + txt)
        sha = hashlib.sha256(data).hexdigest()
        with open(f"{PT}/WAYBACK-MANIFEST.csv", "a", encoding="utf-8", newline="") as mf:
            csv.writer(mf, quoting=csv.QUOTE_ALL).writerow([w["vertical"], w["company_slug"], base + ".pdf", w["url"], ts, len(data), sha])
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(f"{PT}/v2-baseline-fetch-log.csv", "a", encoding="utf-8", newline="") as lf:
            for x in ws:
                csv.writer(lf).writerow([x["doc_id"], x["company"], x["url"], "OK" if len(txt) >= 3000 else "OK-THIN", ts, side,
                                         f"{out}/{base}.txt", len(txt), stamp])
        shutil.move(pdf, f"{INBOX}/processed/{os.path.basename(pdf)}")
        shutil.move(meta, f"{INBOX}/processed/{os.path.basename(meta)}")
        n += 1
        print(f"OK  {', '.join(x['doc_id'] for x in ws):18s} ts={ts} ({side}) PDF chars={len(txt)}" + ("  THIN" if len(txt) < 3000 else ""))
    return n


def file_texts():
    """Text-only captures from v2-browser-receiver.py: <doc>.txt with a '# saved-from:' header; raw not retained."""
    n = 0
    for f in sorted(glob.glob(f"{INBOX}/*.txt")):
        t = open(f, encoding="utf-8").read()
        hdr, _, body = t.partition("\n\n")
        meta = dict(re.findall(r"^# ([\w-]+): (.*)$", hdr, re.M))
        s = re.search(r"/web/(\d{14})[a-z_]*/(.+)$", meta.get("saved-from", ""))
        ids = [x for x in meta.get("doc_ids", "").split(",") if x]
        ws = [w for w in W if w["doc_id"] in ids]
        if not s or not ws:
            print(f"??  {os.path.basename(f)}: missing saved-from / doc_ids header"); continue
        ts, orig, w = s.group(1), s.group(2), ws[0]
        side = "on-or-before" if int(ts) <= TARGET else "after"
        out = f"{PT}/{w['vertical']}/{w['company_slug']}"; os.makedirs(out, exist_ok=True)
        base = f"{w['slug']}_{ts}"
        open(f"{out}/{base}.txt", "w", encoding="utf-8").write(
            f"# WAYBACK CAPTURE\n# source_url: {w['url']}\n# snapshot_ts: {ts}\n"
            f"# snapshot_url: https://web.archive.org/web/{ts}id_/{orig}\n"
            f"# method: {meta.get('capture-method', 'browser-session capture')} of Wayback copy closest to 2022-11-30 "
            f"(side={side}); TEXT-ONLY (raw {meta.get('raw_type', '?')} not retained; raw_sha256 {meta.get('raw_sha256', '?')}, "
            f"{meta.get('raw_bytes', '?')} bytes); v2 doc(s) {', '.join(x['doc_id'] for x in ws)}\n\n" + body)
        with open(f"{PT}/WAYBACK-MANIFEST.csv", "a", encoding="utf-8", newline="") as mf:
            csv.writer(mf, quoting=csv.QUOTE_ALL).writerow([w["vertical"], w["company_slug"], base + ".txt", w["url"], ts,
                                                            meta.get("raw_bytes", ""), meta.get("raw_sha256", "")])
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        thin = len(body) < 3000
        with open(f"{PT}/v2-baseline-fetch-log.csv", "a", encoding="utf-8", newline="") as lf:
            for x in ws:
                csv.writer(lf).writerow([x["doc_id"], x["company"], x["url"], "OK-THIN" if thin else "OK", ts, side,
                                         f"{out}/{base}.txt", len(body), stamp])
        shutil.move(f, f"{INBOX}/processed/{os.path.basename(f)}")
        n += 1
        print(f"OK  {', '.join(x['doc_id'] for x in ws):18s} ts={ts} ({side}) TEXT chars={len(body)}" + ("  THIN" if thin else ""))
    return n


os.makedirs(f"{INBOX}/processed", exist_ok=True)
files = sorted(glob.glob(f"{INBOX}/*.htm*"))
ok, bad = 0, []
for f in files:
    raw = open(f, encoding="utf-8", errors="replace").read()
    ts, orig = snapshot(raw)
    if not ts:
        bad.append((f, "no snapshot address in file - re-save from the Wayback page with Ctrl+S")); continue
    stem = os.path.splitext(os.path.basename(f))[0]
    named = [w for w in W if w["doc_id"] == stem]  # fetcher-saved files are named <doc_id>.html
    ws = ([w for w in W if w["url"] == named[0]["url"]] if named else None) \
        or by_url.get(norm(orig)) or by_path.get(nopath_q(orig))
    if not ws:
        bad.append((f, f"snapshot URL not in worklist: {orig}")); continue
    body = clean(raw)
    txt = detag(body)
    side = "on-or-before" if int(ts) <= TARGET else "after"
    w = ws[0]
    out = f"{PT}/{w['vertical']}/{w['company_slug']}"
    os.makedirs(out, exist_ok=True)
    base = f"{w['slug']}_{ts}"
    open(f"{out}/{base}_RAW.html", "w", encoding="utf-8").write(body)
    open(f"{out}/{base}.txt", "w", encoding="utf-8").write(
        f"# WAYBACK CAPTURE\n# source_url: {w['url']}\n# snapshot_ts: {ts}\n"
        f"# snapshot_url: https://web.archive.org/web/{ts}/{orig}\n"
        f"# method: {method_of(raw)} of Wayback page closest to 2022-11-30 (side={side}); "
        f"toolbar and URL rewriting stripped by v2-ingest-manual.py; v2 doc(s) {', '.join(x['doc_id'] for x in ws)}\n\n" + txt)
    sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
    with open(f"{PT}/WAYBACK-MANIFEST.csv", "a", encoding="utf-8", newline="") as mf:
        csv.writer(mf, quoting=csv.QUOTE_ALL).writerow([w["vertical"], w["company_slug"], base + "_RAW.html", w["url"], ts,
                                                        len(body.encode("utf-8")), sha])
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(f"{PT}/v2-baseline-fetch-log.csv", "a", encoding="utf-8", newline="") as lf:
        for x in ws:
            csv.writer(lf).writerow([x["doc_id"], x["company"], x["url"], "OK" if len(txt) >= 3000 else "OK-THIN", ts, side,
                                     f"{out}/{base}_RAW.html", len(txt), stamp])
    shutil.move(f, f"{INBOX}/processed/{os.path.basename(f)}")
    ok += 1
    print(f"OK  {', '.join(x['doc_id'] for x in ws):18s} ts={ts} ({side}) chars={len(txt)}" + ("  THIN" if len(txt) < 3000 else ""))
for f, why in bad:
    print(f"??  {os.path.basename(f)}: {why}")
print(f"filed {ok} of {len(files)} saved pages; PDFs filed: {file_pdfs()}; text-only captures filed: {file_texts()}")
