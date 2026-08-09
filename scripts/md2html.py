#!/usr/bin/env python3
"""
md2html.py — canonical, mechanical Markdown -> HTML renderer for Store Leads review docs.

WHY THIS EXISTS (Marina S22 / lesson S18): Marina reads HTML; the agent works in MD.
To keep the two surfaces from ever diverging, MD is the ONLY canonical source and the
HTML is GENERATED from it — never hand-edited. Edit the .md, re-run this, get the .html.

Deliberately small + deterministic. Handles the subset used in these docs:
  ATX headers (#..######), GFM pipe tables, blockquotes (>), unordered lists (-, *, •),
  ordered lists (1.), fenced code (```), horizontal rules (---), inline **bold** *italic*
  `code`, links [t](u), and paragraphs. Anything else passes through as text.

Usage:  python3 scripts/md2html.py <in.md> <out.html> ["Optional Title"]
"""
import sys, re, html, os


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def inline(s: str) -> str:
    """Inline markdown -> HTML. Order matters (code first so its contents aren't touched)."""
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == '`':  # inline code — verbatim, no further parsing inside
            j = s.find('`', i + 1)
            if j != -1:
                out.append('<code>' + esc(s[i + 1:j]) + '</code>')
                i = j + 1
                continue
        if c == '[':  # link [text](url)
            m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', s[i:])
            if m:
                out.append(f'<a href="{esc(m.group(2))}">{esc(m.group(1))}</a>')
                i += m.end()
                continue
        if s.startswith('**', i):
            j = s.find('**', i + 2)
            if j != -1:
                out.append('<strong>' + inline(s[i + 2:j]) + '</strong>')
                i = j + 2
                continue
        if c == '*':
            j = s.find('*', i + 1)
            if j != -1:
                out.append('<em>' + inline(s[i + 1:j]) + '</em>')
                i = j + 1
                continue
        out.append(esc(c))
        i += 1
    return ''.join(out)


def is_table_sep(line: str) -> bool:
    return bool(re.match(r'^\s*\|?[\s:|-]+\|[\s:|-]*$', line)) and '-' in line


def split_row(line: str):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def render(md: str) -> str:
    lines = md.split('\n')
    html_out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]

        # fenced code block
        if line.strip().startswith('```'):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            html_out.append('<pre><code>' + esc('\n'.join(buf)) + '</code></pre>')
            continue

        # blank line
        if not line.strip():
            i += 1
            continue

        # horizontal rule
        if re.match(r'^\s*---+\s*$', line):
            html_out.append('<hr>')
            i += 1
            continue

        # header
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            lvl = len(m.group(1))
            html_out.append(f'<h{lvl}>{inline(m.group(2).rstrip())}</h{lvl}>')
            i += 1
            continue

        # table: current line has a pipe and next line is a separator
        if '|' in line and i + 1 < n and is_table_sep(lines[i + 1]):
            header = split_row(line)
            i += 2  # skip header + separator
            rows = []
            while i < n and '|' in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            t = ['<table><thead><tr>'] + [f'<th>{inline(c)}</th>' for c in header] + ['</tr></thead><tbody>']
            for r in rows:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table>')
            html_out.append(''.join(t))
            continue

        # blockquote (consecutive > lines)
        if line.lstrip().startswith('>'):
            buf = []
            while i < n and lines[i].lstrip().startswith('>'):
                buf.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            html_out.append('<blockquote>' + '<br>'.join(inline(b) if b.strip() else '' for b in buf) + '</blockquote>')
            continue

        # unordered list (-, *, •) possibly nested by indentation
        if re.match(r'^\s*[-*•]\s+', line):
            buf = []
            while i < n and re.match(r'^\s*[-*•]\s+', lines[i]):
                indent = len(lines[i]) - len(lines[i].lstrip())
                item = re.sub(r'^\s*[-*•]\s+', '', lines[i])
                buf.append((indent, inline(item)))
                i += 1
            html_out.append(render_list(buf))
            continue

        # ordered list
        if re.match(r'^\s*\d+\.\s+', line):
            buf = []
            while i < n and re.match(r'^\s*\d+\.\s+', lines[i]):
                item = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                buf.append(inline(item))
                i += 1
            html_out.append('<ol>' + ''.join(f'<li>{b}</li>' for b in buf) + '</ol>')
            continue

        # paragraph (gather consecutive non-structural lines)
        buf = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r'^(\s*[-*•]\s+|\s*\d+\.\s+|#{1,6}\s|\s*>|```|\s*---+\s*$)', lines[i]) \
                and not ('|' in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
            buf.append(lines[i])
            i += 1
        html_out.append('<p>' + '<br>'.join(inline(b) for b in buf) + '</p>')

    return '\n'.join(html_out)


def render_list(items):
    """Two-level unordered list by indentation."""
    out, open_sub = ['<ul>'], False
    base = min(ind for ind, _ in items) if items else 0
    for ind, txt in items:
        if ind > base:
            if not open_sub:
                out.append('<ul>')
                open_sub = True
            out.append(f'<li>{txt}</li>')
        else:
            if open_sub:
                out.append('</ul>')
                open_sub = False
            out.append(f'<li>{txt}</li>')
    if open_sub:
        out.append('</ul>')
    out.append('</ul>')
    return ''.join(out)


CSS = """
:root{color-scheme:light dark}
*{box-sizing:border-box}
body{margin:0;padding:2.2rem 1rem 6rem;font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 background:#fbfbfa;color:#1c1c1c}
main{max-width:900px;margin:0 auto}
h1,h2,h3,h4,h5,h6{line-height:1.28;margin:1.9em 0 .55em;font-weight:700}
h1{font-size:1.85rem;margin-top:.2em;border-bottom:2px solid #e6e6e3;padding-bottom:.35em}
h2{font-size:1.4rem;border-bottom:1px solid #ececea;padding-bottom:.28em}
h3{font-size:1.16rem}h4{font-size:1.02rem}
p{margin:.7em 0}
a{color:#2b6cb0;text-decoration:none}a:hover{text-decoration:underline}
strong{font-weight:700}
code{background:#f0f0ee;border-radius:4px;padding:.08em .38em;font:.86em ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:#f6f6f4;border:1px solid #e6e6e3;border-radius:8px;padding:.9rem 1rem;overflow-x:auto}
pre code{background:none;padding:0;font-size:.82rem;line-height:1.5}
blockquote{margin:.9em 0;padding:.5em .95em;border-left:3px solid #cfcfca;background:#f4f4f1;border-radius:0 6px 6px 0;color:#333}
hr{border:0;border-top:1px solid #e6e6e3;margin:2em 0}
ul,ol{margin:.6em 0;padding-left:1.5em}li{margin:.25em 0}
ul ul{margin:.2em 0}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.93rem;display:block;overflow-x:auto}
th,td{border:1px solid #e2e2df;padding:.42em .7em;text-align:left;vertical-align:top}
th{background:#f2f2ef;font-weight:700}
tr:nth-child(even) td{background:#fafaf8}
.meta{color:#8a8a86;font-size:.8rem;margin-top:0}
@media (prefers-color-scheme:dark){
 body{background:#1a1a1a;color:#e4e4e2}
 h1{border-color:#333}h2{border-color:#2c2c2c}
 a{color:#7db3e8}
 code{background:#2a2a2a}pre{background:#222;border-color:#333}pre code{background:none}
 blockquote{background:#242424;border-left-color:#444;color:#cfcfcd}
 hr{border-top-color:#333}
 th{background:#262626}td,th{border-color:#333}tr:nth-child(even) td{background:#1f1f1f}
 .meta{color:#777}
}
"""


def main():
    if len(sys.argv) < 3:
        print("usage: md2html.py <in.md> <out.html> [title]", file=sys.stderr)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding='utf-8') as f:
        md = f.read()
    title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(src)
    body = render(md)
    import datetime
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    page = (f"<!doctype html><html lang='ru'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{esc(title)}</title><style>{CSS}</style></head><body><main>"
            f"<p class='meta'>⚙ Сгенерировано механически из {esc(os.path.basename(src))} · {stamp} · руками не править</p>"
            f"{body}</main></body></html>")
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"OK → {dst} ({len(page)} bytes, from {os.path.basename(src)})")


if __name__ == '__main__':
    main()
