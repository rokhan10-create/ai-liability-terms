"""Build previous-tos/v2-manual-checklist.html: a click-through list of every v2 document that still needs a
Nov-2022 baseline. The researcher opens each link in their own browser (normal manual browsing), checks the
Wayback date bar, and saves the page with Ctrl+S ("Webpage, HTML only") into previous-tos/_manual-inbox/.
v2-ingest-manual.py then files each saved page as a baseline. Run from the project root."""
import csv, html, os

W = list(csv.DictReader(open("previous-tos/v2-baseline-worklist.csv", encoding="utf-8")))
done = set()
if os.path.exists("previous-tos/v2-baseline-fetch-log.csv"):
    for r in csv.reader(open("previous-tos/v2-baseline-fetch-log.csv", encoding="utf-8")):
        if len(r) > 3 and r[3] in ("OK", "OK-THIN", "NO-SNAPSHOT"):
            done.add(r[0])
todo = [w for w in W if w["action"] == "fetch" and w["doc_id"] not in done]
seen, rows = {}, []
for w in todo:  # one link per distinct URL; several doc_ids can share a URL
    seen.setdefault(w["url"], []).append(w)
for i, (url, ws) in enumerate(seen.items(), 1):
    w = ws[0]
    ids = ", ".join(x["doc_id"] for x in ws)
    link = "https://web.archive.org/web/20221130235959/" + url
    rows.append(f"<tr><td class=n>{i}</td><td><label><input type=checkbox> {html.escape(w['company'])}</label>"
                f"<div class=m>{html.escape(ids)} · {html.escape(w['doc_type'])} · {html.escape(w['sample_group'])}</div></td>"
                f"<td><a href=\"{html.escape(link)}\" target=_blank rel=noopener>open Nov-2022 copy</a>"
                f"<div class=m>{html.escape(url[:90])}</div></td></tr>")
page = f"""<!doctype html><meta charset=utf-8><title>Nov-2022 baseline checklist</title>
<style>
:root{{--ink:#1d232b;--mute:#5f6b78;--line:#d9dee4;--bg:#f7f8fa;--acc:#1f5fa8}}
body{{font:14px/1.45 system-ui,sans-serif;color:var(--ink);background:var(--bg);margin:0;padding:24px 16px}}
main{{max-width:980px;margin:0 auto}} h1{{font-size:20px;margin:0 0 4px}} .m{{color:var(--mute);font-size:12px}}
ol{{padding-left:20px}} table{{width:100%;border-collapse:collapse;background:#fff}}
td{{border-top:1px solid var(--line);padding:8px;vertical-align:top}} td.n{{color:var(--mute);width:2.5em;text-align:right}}
a{{color:var(--acc)}} input:checked+*,label:has(input:checked){{color:var(--mute);text-decoration:line-through}}
.box{{background:#fff;border:1px solid var(--line);padding:12px 16px;margin:12px 0}}
</style><main>
<h1>Nov-2022 baseline checklist</h1>
<div class=m>{len(rows)} pages · {len(todo)} documents · main-sample firms first</div>
<div class=box><b>For each row</b><ol>
<li>Click <i>open Nov-2022 copy</i>. Wayback jumps to the snapshot closest to 30 Nov 2022. Its date is in the bar at the top. Any date is fine; the date is recorded automatically.</li>
<li>If the page shows the legal text: press <b>Ctrl+S</b>, choose <b>"Webpage, HTML only"</b>, and save into<br><code>OneDrive\\TOS AI audit\\previous-tos\\_manual-inbox</code>. The filename doesn't matter.</li>
<li>If Wayback says it has no copy, or the page is blank or an error, skip it. Gaps are logged automatically.</li>
<li>Tick the box and move on. Tell Claude when you've done a batch; nothing else is needed.</li></ol>
<div class=m>Go at a normal browsing pace. Chrome writes the snapshot address into the saved file, which is how each page is matched back to its document.</div></div>
<table>{''.join(rows)}</table></main>"""
open("previous-tos/v2-manual-checklist.html", "w", encoding="utf-8").write(page)
os.makedirs("previous-tos/_manual-inbox", exist_ok=True)
print(len(rows), "links for", len(todo), "documents")
