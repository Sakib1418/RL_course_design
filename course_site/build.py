#!/usr/bin/env python3
"""Build the ChemE x AI course site.

specs/*.md (registry in front matter) + content/**/*.md  ->  _site/ (static HTML, relative links)

Usage:  python build.py            # builds into _site/
"""
from __future__ import annotations

import datetime as dt
import html
import re
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

ROOT = Path(__file__).resolve().parent
CONTENT, SPECS, ASSETS, OUT = ROOT / "content", ROOT / "specs", ROOT / "assets", ROOT / "_site"
TEMPLATE = (ROOT / "templates" / "base.html").read_text(encoding="utf-8")

SITE = {
    "name": "ChemE × AI Course Series",
    "url": "https://sakib1418.github.io/RL_course_design/",
    "email": "ferdous1418@gmail.com",
    "author": "Sakib Ferdous, Ph.D.",
    "description": "Three seven-week, hands-on courses in reinforcement learning, digital twins and agentic AI "
                   "for chemical and process engineers with no coding background.",
}
SESSION_TYPES = ["Concept", "Studio", "Lab"]
MD_EXT = ["extra", "sane_lists", "smarty", "toc"]


# ---------------------------------------------------------------- helpers
def split_fm(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, text)


def md(text: str) -> str:
    out = markdown.markdown(text, extensions=MD_EXT, output_format="html5")
    # ```mermaid fences -> <pre class="mermaid"> (mermaid decodes the entities itself)
    out = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                 r'<div class="figure-diagram"><pre class="mermaid">\1</pre></div>', out, flags=re.S)
    # wrap tables so they scroll on phones
    out = re.sub(r"(<table>.*?</table>)", r'<div class="table-wrap">\1</div>', out, flags=re.S)
    return out


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def mailto(subject: str) -> str:
    return f"mailto:{SITE['email']}?subject={quote(subject)}"


def put_token(page: str, token: str, value: str) -> str:
    page = re.sub(r"<p>\s*\{\{" + token + r"\}\}\s*</p>", lambda _: value, page)
    return page.replace("{{" + token + "}}", value)


def load_courses() -> dict:
    courses = {}
    for p in SPECS.glob("*.md"):
        fm, _ = split_fm(p.read_text(encoding="utf-8"))
        courses[fm["slug"]] = fm
    return dict(sorted(courses.items(), key=lambda kv: kv[1]["number"]))


COURSES = load_courses()


def partial(name: str, root: str) -> str:
    p = CONTENT / "_partials" / f"{name}.md"
    return md(p.read_text(encoding="utf-8").replace("{{root}}", root)) if p.exists() else ""


# ---------------------------------------------------------------- generated components
def phase_bar(c: dict) -> str:
    segs = "".join(f'<span class="seg ph-{w["phase"].lower()}" title="Week {w["n"]} · {esc(w["phase"])}"></span>'
                   for w in c["weeks"])
    return f'<div class="phase-bar" aria-hidden="true">{segs}</div>'


def week_grid(c: dict, prefix: str = "") -> str:
    cards = []
    for w in c["weeks"]:
        cards.append(
            f'<a class="week-card ph-{w["phase"].lower()}" href="{prefix}week-{w["n"]}.html">'
            f'<span class="wk-top"><span class="wk-no">Week {w["n"]}</span>'
            f'<span class="phase-tag ph-{w["phase"].lower()}">{esc(w["phase"])}</span></span>'
            f'<strong>{esc(w["title"])}</strong><span class="wk-sum">{esc(w["summary"])}</span>'
            f'<span class="wk-go">3 sessions &rarr;</span></a>')
    cards.append(f'<a class="week-card cap" href="{prefix}syllabus.html"><span class="wk-top"><span class="wk-no">Outcome</span></span>'
                 f'<strong>Capstone</strong><span class="wk-sum">{esc(c["capstone"])}</span><span class="wk-go">Full syllabus &rarr;</span></a>')
    return f'<div class="week-grid">{"".join(cards)}</div>'


def schedule(c: dict) -> str:
    head = "".join(f"<th>Session {i + 1} · {t}</th>" for i, t in enumerate(SESSION_TYPES))
    rows = []
    for w in c["weeks"]:
        cells = "".join(f"<td>{esc(s)}</td>" for s in w["sessions"])
        rows.append(f'<tr><th scope="row"><a href="week-{w["n"]}.html">Week {w["n"]}</a>'
                    f'<span class="phase-tag ph-{w["phase"].lower()}">{esc(w["phase"])}</span>'
                    f'<span class="row-title">{esc(w["title"])}</span></th>{cells}</tr>')
    return (f'<div class="table-wrap"><table class="schedule"><thead><tr><th>Week</th>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def course_cards(root: str) -> str:
    out = []
    for c in COURSES.values():
        base = f'{root}{c["slug"]}/'
        out.append(f'''
<article class="course-card accent-{c["accent"]}">
  <div class="cc-top"><span class="cc-no">0{c["number"]}</span><span class="status s-{c["status"].lower()}">{esc(c["status"])}</span></div>
  <h3><a href="{base}index.html">{esc(c["title"])}</a></h3>
  <p class="cc-sub">{esc(c["subtitle"])}</p>
  <p class="cc-text">{esc(c["card"])}</p>
  {phase_bar(c)}
  <ul class="cc-meta"><li>7 weeks · 21 sessions</li><li>{esc(c["level"])}</li></ul>
  <div class="cc-actions"><a class="btn small primary" href="{base}index.html">Course overview</a>
  <a class="btn small ghost" href="{base}syllabus.html">Syllabus</a></div>
</article>''')
    return f'<div class="course-grid">{"".join(out)}</div>'


def nav(root: str, current: str | None) -> str:
    links = "".join(
        f'<a class="{"active" if c["slug"] == current else ""}" href="{root}{c["slug"]}/index.html">'
        f'<span class="n">0{c["number"]}</span>{esc(c["nav"])}</a>' for c in COURSES.values())
    return f'''
<header class="topbar"><div class="wrap topbar-in">
  <a class="brand" href="{root}index.html"><img src="{root}assets/img/favicon.svg" alt="" width="30" height="30">
    <span><strong>ChemE × AI</strong><em>Course Series</em></span></a>
  <nav class="nav-links" aria-label="Courses">{links}<a href="{root}index.html#instructor">Instructor</a></nav>
  <a class="btn small primary nav-cta" href="{mailto("Course materials request")}">Request materials</a>
</div></header>'''


def footer(root: str) -> str:
    year = dt.date.today().year
    links = "".join(f'<li><a href="{root}{c["slug"]}/index.html">{esc(c["title"])}</a></li>' for c in COURSES.values())
    return f'''
<footer class="site-footer"><div class="wrap foot-grid">
  <div><p class="foot-brand">ChemE × AI Course Series</p>
  <p>Three seven-week courses for chemical and process engineers. Designed by Sakib Ferdous, Ph.D.; co-developed with Dr. Nigel F. Reuel, Iowa State University.</p></div>
  <div><p class="foot-h">Courses</p><ul>{links}</ul></div>
  <div><p class="foot-h">Contact</p><ul>
    <li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
    <li><a href="tel:+15156867280">+1 515 686 7280</a></li>
    <li><a href="https://www.linkedin.com/in/sakib-ferdous">LinkedIn</a> · <a href="https://scholar.google.com/citations?user=LM1_PDYAAAAJ">Google Scholar</a></li>
    <li><a href="https://orcid.org/0000-0001-7396-9830">ORCID</a> · <a href="https://github.com/Sakib1418">GitHub</a></li></ul></div>
</div><div class="wrap foot-base">© {year} Sakib Ferdous · Full slide decks, notebooks and instructor guides available on request · Built with AI-assisted (vibe) coding</div></footer>'''


def course_hero(c: dict, root: str) -> str:
    return f'''
<section class="course-hero accent-{c["accent"]}"><div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="crumbs"><a href="{root}index.html">Course series</a> / Course {c["number"]}</p>
    <p class="kicker">Course 0{c["number"]} <span class="status s-{c["status"].lower()}">{esc(c["status"])}</span></p>
    <h1>{esc(c["title"])}</h1>
    <p class="subtitle">{esc(c["subtitle"])}</p>
    <p class="lede">{esc(c["tagline"])}</p>
    <ul class="hero-meta"><li><strong>7</strong> weeks</li><li><strong>21</strong> hands-on sessions</li><li><strong>3 × 1 h</strong> per week</li><li><strong>0</strong> prior coding</li></ul>
    <div class="actions"><a class="btn light" href="syllabus.html">View the syllabus</a>
      <a class="btn outline-light" href="week-1.html">Start at Week 1</a></div>
  </div>
  <figure class="hero-art"><img src="{root}assets/img/{c["hero"]}" alt="{esc(c["title"])} overview diagram"></figure>
</div>
<div class="wrap hero-facts">
  <div><span>Level</span>{esc(c["level"])}</div>
  <div><span>Prerequisites</span>{esc(c["prereq"])}</div>
  <div><span>Capstone</span>{esc(c["capstone"])}</div>
</div></section>'''


def sub_header(c: dict, root: str, kicker: str, title: str, lede: str, phase: str | None = None) -> str:
    tag = f'<span class="phase-tag ph-{phase.lower()}">{esc(phase)}</span>' if phase else ""
    return f'''
<section class="sub-hero accent-{c["accent"]}"><div class="wrap">
  <p class="crumbs"><a href="{root}index.html">Course series</a> / <a href="index.html">{esc(c["short"])}</a> / {esc(kicker)}</p>
  <p class="kicker">{esc(kicker)} {tag}</p>
  <h1>{esc(title)}</h1>
  <p class="lede">{esc(lede)}</p>
</div></section>'''


def sidebar(c: dict, current: str) -> str:
    items = [f'<a class="{"active" if current == "syllabus" else ""}" href="syllabus.html">Syllabus &amp; schedule</a>']
    for w in c["weeks"]:
        act = "active" if current == f'week-{w["n"]}' else ""
        items.append(f'<a class="{act}" href="week-{w["n"]}.html"><span class="dot ph-{w["phase"].lower()}"></span>'
                     f'<span><small>Week {w["n"]} · {esc(w["phase"])}</small>{esc(w["title"])}</span></a>')
    return f'''
<aside class="sidebar"><div class="side-in">
  <a class="side-course" href="index.html">0{c["number"]} · {esc(c["short"])}</a>
  <nav>{"".join(items)}</nav>
  <div class="side-cta"><p>Slides, notebooks and the instructor guide for this course are available on request.</p>
  <a class="btn small primary" href="{mailto("Materials request: " + c["short"])}">Request materials</a></div>
</div></aside>'''


def pager(c: dict, n: int) -> str:
    prev_ = (f'<a class="prev" href="week-{n - 1}.html"><small>&larr; Week {n - 1}</small>{esc(c["weeks"][n - 2]["title"])}</a>'
             if n > 1 else '<a class="prev" href="syllabus.html"><small>&larr; Syllabus</small>Course schedule</a>')
    next_ = (f'<a class="next" href="week-{n + 1}.html"><small>Week {n + 1} &rarr;</small>{esc(c["weeks"][n]["title"])}</a>'
             if n < len(c["weeks"]) else '<a class="next" href="index.html"><small>Course overview &rarr;</small>Capstone and outcomes</a>')
    return f'<nav class="pager">{prev_}{next_}</nav>'


def request_band(root: str, c: dict | None = None) -> str:
    return f'<section class="band request-band" id="request"><div class="wrap">{partial("request", root)}</div></section>'.replace(
        "{{mailto}}", mailto("Materials request: " + (c["short"] if c else "ChemE × AI course series")))


def instructor_band(root: str) -> str:
    return f'<section class="band instructor-band" id="instructor"><div class="wrap">{partial("instructor", root)}</div></section>'


# ---------------------------------------------------------------- pages
def render_page(src: Path) -> None:
    rel = src.relative_to(CONTENT)
    depth = len(rel.parts) - 1
    root = "../" * depth
    fm, body = split_fm(src.read_text(encoding="utf-8"))
    layout = fm.get("layout", "page")
    c = COURSES.get(fm.get("course", ""))
    body_html = md(body.replace("{{root}}", root))
    if c:
        body_html = put_token(body_html, "week_grid", week_grid(c))
        body_html = put_token(body_html, "schedule", schedule(c))
    body_html = put_token(body_html, "course_cards", course_cards(root))

    accent = f'accent-{c["accent"]}' if c else "accent-rl"
    if layout == "home":
        title = SITE["name"] + " · AI for chemical and process engineers"
        desc = SITE["description"]
        main = f'<main class="home">{body_html}</main>{instructor_band(root)}{request_band(root)}'
    elif layout == "course":
        title = f'{c["title"]}: {c["subtitle"]} · {SITE["name"]}'
        desc = c["tagline"]
        main = (f'{course_hero(c, root)}<main class="wrap prose-wide course-body">{body_html}</main>'
                f'{instructor_band(root)}{request_band(root, c)}')
    elif layout in ("syllabus", "week"):
        if layout == "syllabus":
            head = sub_header(c, root, "Syllabus", f'{c["title"]}: syllabus and schedule',
                              "Seven weeks, three one-hour sessions a week. Every session is hands-on.")
            title, desc, cur, tail = f'Syllabus · {c["title"]}', f'Syllabus for {c["title"]}', "syllabus", ""
        else:
            n = int(fm["week"])
            w = c["weeks"][n - 1]
            head = sub_header(c, root, f"Week {n}", w["title"], w["summary"], w["phase"])
            title, desc, cur, tail = f'Week {n}: {w["title"]} · {c["short"]}', w["summary"], f"week-{n}", pager(c, n)
        main = (f'{head}<div class="wrap doc-grid">{sidebar(c, cur)}'
                f'<main class="prose">{body_html}{tail}</main></div>{request_band(root, c)}')
    else:
        title, desc, main = fm.get("title", SITE["name"]), SITE["description"], f'<main class="wrap prose">{body_html}</main>'

    page = TEMPLATE
    for k, v in {"title": esc(title), "description": esc(desc), "root": root, "body_class": accent,
                 "og_image": SITE["url"] + "assets/img/preview.png", "url": SITE["url"] + rel.with_suffix(".html").as_posix(),
                 "nav": nav(root, c["slug"] if c else None), "footer": footer(root)}.items():
        page = page.replace("{{" + k + "}}", v)
    page = page.replace("{{content}}", main)

    dest = OUT / rel.with_suffix(".html")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for child in OUT.iterdir():  # empty, don't delete: a local preview server may hold the folder open
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    shutil.copytree(ASSETS, OUT / "assets")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    pages = [p for p in CONTENT.rglob("*.md") if "_partials" not in p.parts]
    for p in sorted(pages):
        render_page(p)
    missing = [f"{s}/{f}" for s in COURSES for f in ["index.md", "syllabus.md", *[f"week-{i}.md" for i in range(1, 8)]]
               if not (CONTENT / s / f).exists()]
    print(f"Built {len(pages)} pages into {OUT}")
    if missing:
        print("Missing pages:", ", ".join(missing))


if __name__ == "__main__":
    main()
