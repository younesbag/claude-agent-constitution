"""Build index.html from src/index.template.html and the prompt files.

The prompt text lives in exactly one place (prompt/ar.md, prompt/en.md); this script
injects it into the page so the page and the files can never drift apart.

    python build.py          # write index.html
    python build.py --check  # exit 1 if index.html is out of date (used in CI)
"""
import html
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent
SITE_URL = "https://younesbag.github.io/claude-agent-constitution/"
REPO_URL = "https://github.com/younesbag/claude-agent-constitution"
VERSION = "1.0.0"
VERSION_AR = "١٫٠"
DATE = "2026-09-24"
DATE_AR = "٢٤ سبتمبر ٢٠٢٦"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


LATIN = re.compile(r"[A-Za-z]")
TOKEN = re.compile(r"[^\s()،؛]+")
ARABIC_LEAD = re.compile(r"[؀-ۿ]*")


def isolate_ltr(text: str) -> str:
    """Escape text for <pre>, wrapping path-like Latin runs (~/.claude/x.md) in LTR spans.

    Inside right-to-left text, the leading dots and tildes of paths jump to the wrong side.
    The spans add markup only: the element's textContent, and therefore what the copy
    button copies, stays byte-identical to the source file.
    """
    out, pos = [], 0
    for m in TOKEN.finditer(text):
        tok = m.group(0)
        lead = ARABIC_LEAD.match(tok).group(0)  # an attached «و» stays outside the LTR run
        tok = tok[len(lead):]
        while tok and tok[-1] in ".,:":
            tok = tok[:-1]
        if not (LATIN.search(tok) and ("/" in tok or tok[:1] in ".~" or tok.endswith(".md"))):
            continue
        start = m.start() + len(lead)
        out.append(html.escape(text[pos:start], quote=False))
        out.append('<span dir="ltr">' + html.escape(tok, quote=False) + "</span>")
        pos = start + len(tok)
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def build() -> str:
    page = read("src/index.template.html")
    values = {
        "SITE_URL": SITE_URL,
        "SITE_URL_ENC": urllib.parse.quote(SITE_URL, safe=""),
        "REPO_URL": REPO_URL,
        "VERSION": VERSION,
        "VERSION_AR": VERSION_AR,
        "DATE": DATE,
        "DATE_AR": DATE_AR,
        # prompts go inside <pre>: escape markup characters, keep text byte-for-byte otherwise
        "PROMPT_AR": isolate_ltr(read("prompt/ar.md").rstrip("\n")),
        "PROMPT_EN": html.escape(read("prompt/en.md").rstrip("\n"), quote=False),
    }
    for key, value in values.items():
        page = page.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if leftover:
        sys.exit(f"unreplaced placeholders: {sorted(set(leftover))}")
    return page


def main() -> None:
    out = build()
    target = ROOT / "index.html"
    if "--check" in sys.argv:
        current = target.read_text(encoding="utf-8").replace("\r\n", "\n") if target.exists() else ""
        if current != out:
            sys.exit("index.html is out of date — run: python build.py")
        print("index.html is up to date with prompt/*.md")
        return
    target.write_text(out, encoding="utf-8", newline="\n")
    print(f"wrote index.html ({len(out.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
