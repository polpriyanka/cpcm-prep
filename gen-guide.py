#!/usr/bin/env python3
"""Convert STUDY-GUIDE.md -> study-guide.js (window.STUDY_GUIDE_HTML + section index).
Re-run this whenever STUDY-GUIDE.md changes. Handles the markdown subset the guide uses:
h1/h2/h3, tables, ordered/unordered lists, bold, italic, inline code, hr, paragraphs."""
import re, html as _html, json, sys

SRC = "/Users/priyanka/projects/cpcm-prep/STUDY-GUIDE.md"
OUT = "/Users/priyanka/projects/cpcm-prep/study-guide.js"

def esc(s):
    return _html.escape(s, quote=False)

def inline(s):
    # protect inline code first
    codes = []
    def stash(m):
        codes.append(m.group(1)); return "\x00%d\x00" % (len(codes)-1)
    s = re.sub(r"`([^`]+)`", stash, s)
    s = esc(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    # restore code
    s = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % esc(codes[int(m.group(1))]), s)
    return s

def main():
    lines = open(SRC).read().split("\n")
    out = []          # html chunks
    sections = []     # (id, title) for the first-level (# ) headings -> TOC
    i = 0
    n = len(lines)
    sec_idx = 0
    while i < n:
        line = lines[i]
        # horizontal rule / section divider
        if re.match(r"^---+\s*$", line):
            i += 1; continue
        # headings
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            level = len(m.group(1)); text = m.group(2).strip()
            if level == 1:
                sid = "gsec-%d" % sec_idx
                sections.append((sid, text))
                sec_idx += 1
                out.append('<h2 class="g-h1" id="%s">%s</h2>' % (sid, inline(text)))
            elif level == 2:
                out.append('<h3 class="g-h2">%s</h3>' % inline(text))
            else:
                out.append('<h4 class="g-h3">%s</h4>' % inline(text))
            i += 1; continue
        # table: a line starting with | followed by a |---| separator line
        if line.lstrip().startswith("|") and i+1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i+1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ['<div class="g-tablewrap"><table class="g-table"><thead><tr>']
            t += ["<th>%s</th>" % inline(c) for c in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t)); continue
        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(inline(re.sub(r"^\s*[-*]\s+", "", lines[i])))
                i += 1
            out.append("<ul class='g-ul'>" + "".join("<li>%s</li>" % it for it in items) + "</ul>")
            continue
        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(inline(re.sub(r"^\s*\d+\.\s+", "", lines[i])))
                i += 1
            out.append("<ol class='g-ol'>" + "".join("<li>%s</li>" % it for it in items) + "</ol>")
            continue
        # blank line
        if line.strip() == "":
            i += 1; continue
        # paragraph: gather consecutive non-blank, non-structural lines
        para = [line]
        i += 1
        while i < n and lines[i].strip() != "" and not re.match(r"^(#{1,3}\s|---+\s*$|\s*[-*]\s|\s*\d+\.\s)", lines[i]) and not lines[i].lstrip().startswith("|"):
            para.append(lines[i]); i += 1
        text = " ".join(p.strip() for p in para)
        cls = ' class="g-lede"' if text.startswith("*") and text.endswith("*") and text.count("*")==2 else ""
        out.append("<p%s>%s</p>" % (cls, inline(text)))

    body = "\n".join(out)
    js = ("/* Auto-generated from STUDY-GUIDE.md by gen-guide.py — do not edit by hand.\n"
          "   Re-run gen-guide.py after editing the study guide. */\n"
          "window.STUDY_GUIDE_HTML = " + json.dumps(body, ensure_ascii=False) + ";\n"
          "window.STUDY_GUIDE_TOC = " + json.dumps([{"id": s, "title": t} for s, t in sections], ensure_ascii=False) + ";\n")
    open(OUT, "w").write(js)
    print("wrote study-guide.js: %d sections, %d bytes html, %d words" % (len(sections), len(body), len(body.split())))

if __name__ == "__main__":
    main()
