# Lightweight Markdown -> PDF (Cyrillic-safe via Arial Unicode; strips emoji glyphs).
# Usage: python3 md_to_pdf.py <input.md> [output.pdf]
import sys, os, re
from fpdf import FPDF

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
lines = open(src, encoding="utf-8").read().split("\n")

FONTS = ["/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
         "/Library/Fonts/Arial Unicode.ttf"]
fp = next((p for p in FONTS if os.path.exists(p)), None)

def clean(s):
    # keep Cyrillic, dashes, arrows (<0x2500); drop emoji/symbol glyphs the font lacks
    return "".join(ch for ch in s if ord(ch) < 0x2500).rstrip()

pdf = FPDF(format="A4")
pdf.set_auto_page_break(True, margin=15)
pdf.add_page()
if fp:
    pdf.add_font("U", "", fp); pdf.add_font("U", "B", fp); F = "U"
else:
    F = "Helvetica"
EPW = pdf.epw

def text_block(s, size=10, bold=False, gray=False, indent=0, gap=1.4):
    pdf.set_font(F, "B" if bold else "", size)
    pdf.set_text_color(110,110,110) if gray else pdf.set_text_color(20,20,20)
    if indent: pdf.set_x(pdf.l_margin + indent)
    pdf.multi_cell(EPW - indent, size*0.52, clean(s), markdown=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(gap)

i = 0
while i < len(lines):
    ln = lines[i].rstrip()
    s = ln.strip()
    if not s:
        pdf.ln(2); i += 1; continue
    # table block
    if s.startswith("|"):
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not re.match(r"^[-:\s]+$", "".join(row)):  # skip |---| separator
                block.append(row)
            i += 1
        if block:
            ncol = max(len(r) for r in block)
            pdf.set_font(F, "", 8)
            with pdf.table(col_widths=tuple([14,12,46,28][:ncol] or [100]),
                           text_align="LEFT", first_row_as_headings=True,
                           line_height=4.2, padding=1) as tbl:
                for ri, row in enumerate(block):
                    row = (row + [""]*ncol)[:ncol]
                    tr = tbl.row()
                    for cell in row:
                        tr.cell(clean(re.sub(r"\*\*", "", cell)))
        pdf.ln(2); continue
    if s.startswith("# "):
        pdf.ln(1); text_block(s[2:], 16, bold=True, gap=1.5)
    elif s.startswith("## "):
        pdf.ln(2); text_block(s[3:], 13, bold=True, gap=1.2)
    elif s.startswith("### "):
        text_block(s[4:], 11, bold=True, gap=1)
    elif s.startswith("_") and s.endswith("_"):
        text_block(s.strip("_"), 8.5, gray=True, gap=1.2)
    elif s.startswith("- "):
        text_block("•  " + s[2:], 9.5, indent=3, gap=0.8)
    else:
        text_block(s, 10, gap=1.2)
    i += 1

pdf.output(dst)
print("PDF:", dst, "| font:", fp or "core")
