# SYSTEM — ChemE × AI Course Series (GitHub Pages front face)

> **Master document.** Everything else is generated from here:
> `SYSTEM.md` → 3 course specs (`specs/*.md`) → a series of markdown pages per course (`content/<slug>/*.md`) → `build.py` → static HTML (`_site/`) → GitHub Pages (`gh-pages` branch).
> **Resumable:** read §8 *Status*, do the first unchecked step, tick it, move on.

## 1 · Purpose
- A professional, public **front face** for three 7-week courses, shown at **AIChE 2026** (faculty poster, Sun 8 Nov; Talk 217c, Mon 9 Nov) via a QR code and a screenshot on the slides.
- Goal of the visitor's first 10 seconds: *"These courses are designed, they are valuable, and this instructor is the right person."*
- **Showmanship, not depth.** Pages are complete-looking, specific and polished, but shallow: no slide content, no notebooks. Every page ends with *"full materials on request"* → contact.

## 2 · The series (from the poster's *Courses* strip; all co-developed with Dr. Nigel F. Reuel)
| # | Slug | Course | Poster status | One line |
|---|---|---|---|---|
| 1 | `rl-vibe-coding` | Reinforcement Learning for Chemical Engineers: Vignettes & Vibe Coding | Built | Fed-batch controller, from a no-code game to tested code |
| 2 | `digital-twins` | Digital Twins for Process Engineering | Designed | Hybrid twin with learned parts bounded by balances |
| 3 | `agentic-ai` | Agentic AI for Process Operations (graduate) | Designed | AI agents whose actions are checked on a twin first |

**Common format:** 7 weeks (half semester) · 3 × 1-hour sessions per week = 21 sessions · hands-on every session.
**Audience:** ChemE undergraduates and graduate students; practicing engineers and leaders with **no coding or AI background**.
**Promise:** from the inception of a process idea to a deployed AI tool, using a vibe-coding environment (Claude, or any AI coding assistant). Browser-only setup; no command line or version control needed (one gentle introduction in Week 7).
**Pedagogy spine (poster):** PLAY → BUILD → VERIFY → DEPLOY. Weekly rhythm: **Concept · Studio · Lab** (session 1 · 2 · 3).
**Hook (poster):** *"If AI is replacing software engineers, who designs and deploys the systems? Process engineers do."*

## 3 · Instructor facts (CV wins any conflict)
Sakib Ferdous, Ph.D. — Ph.D. ChemE, Iowa State (2025, advisor N. F. Reuel) · M.Sc. AI, Iowa State (2023, first graduate of the program) · B.Sc. ChemE, BUET (2018). Postdoc, AI in Plant Breeding, Corteva Agriscience (Feb 2025–) — company-wide “virtual breeder” on Docker/Kubernetes. Head of Bioprocess Automation, Craft BioSolutions (Oct 2025–) — physics-based twin, device-to-cloud. MIT Initiative for New Manufacturing, from Jan 2027 (planned, per poster). Game of Cells digital twin; RL for CAR T-cell expansion (Biotechnol Bioeng 2024, 1st author); RL for fed-batch enzyme production (Biotechnol Bioeng 2026); FEM tip-sonication (AIChE J 2021, 1st author). NSF I-Corps Entrepreneurial Lead. APEX & WiSE AI-in-ChemE workshops. CEGSO President, GPSS Senator.
**Contact (CV):** ferdous1418@gmail.com · +1 515 686 7280 · linkedin.com/in/sakib-ferdous · github.com/Sakib1418 · ORCID 0000-0001-7396-9830 · Scholar `LM1_PDYAAAAJ`.
Avoid publication/patent counts (poster and CV disagree). No Corteva data, crops, metrics.

## 4 · Architecture
```
course_site/
  SYSTEM.md                 ← this file (master)
  specs/<slug>.md           ← layer 2: YAML registry (weeks, sessions) + writer brief
  content/index.md          ← hub landing (3 courses)
  content/_partials/*.md    ← instructor bio, request-materials CTA (injected by build)
  content/<slug>/index.md   ← course landing
  content/<slug>/syllabus.md
  content/<slug>/week-1..7.md
  templates/base.html       ← one HTML shell
  assets/{css,js,img}/      ← design system + SVG figures
  build.py                  ← md → _site/ (relative links; works on file:// and Pages)
  publish.sh                ← _site/ → gh-pages branch → https://sakib1418.github.io/RL_course_design/
  presentation/             ← QR code + front-page screenshot for the slides
```
**Single source of truth:** course titles, week titles, phases and session titles live only in the spec front matter. `build.py` generates nav, hero, sidebar, pager, the 21-session schedule table and the week grid from it.

## 5 · Design system
Matches the poster: MIT maroon `#750014` (course 1), navy `#1F3A52` (course 2), olive `#565029` (course 3), sand `#EAE8DA`, paper `#F7F6F0`, ink `#212326`. Headings *Source Serif 4*, body *Inter*. Swiss-modern: generous white space, thin rules, numbered sections, one accent per page.

## 6 · Page contract (for writers)
Markdown + `md_in_html`. Front matter: `layout` (`home|course|syllabus|week`), `course: <slug>`, `week: n`. Do **not** write the page hero/title, sidebar, pager, bio or CTA — build adds them.
Tokens: `{{week_grid}}` (7 linked week cards) · `{{schedule}}` (21-session table) · `{{root}}` (relative path to site root).
Components:
- `<div class="cards" markdown="1">` holding `<div class="card" markdown="1">…</div>` (2–4 per row)
- `<div class="callout" markdown="1">` (accent note) · `<div class="callout tip" markdown="1">`
- `<div class="session" markdown="1">` — one per session on week pages, starts with `### Session n · Concept|Studio|Lab — Title`
- `<span class="chip">text</span>` · numbered outcome lists: wrap the `1.` list in `<div class="outcomes" markdown="1">…</div>`
- ` ```mermaid ` fenced blocks for flowcharts (`flowchart LR`, ≤ 8 nodes, short labels)
- Images: `![alt]({{root}}assets/img/<file>)`
Voice: confident, concrete, ChemE-native (balances, kinetics, fed-batch, CSTR, P&ID, SOP), plain English, no hype words, no emojis.

## 7 · Orchestration
1. Orchestrator writes this file, the 3 specs, the design system, templates, build, hub and partials.
2. Three writer agents run **in parallel**, one per spec, each writing only `content/<slug>/` (9 pages).
3. Orchestrator builds, screenshots, fixes, publishes, makes the QR code.

## 8 · Status (tick as you go)
- [x] S1 Read poster, CV, course-1 materials
- [x] S2 SYSTEM.md
- [x] S3 Specs ×3
- [x] S4 Design system, template, build.py, SVG figures, hub, partials
- [x] S5 Writers ×3 (parallel) → content/<slug>/
- [x] S6 Build + visual QA (headless screenshots)
- [x] S7 Publish to gh-pages; verify live URL (live 2026-11-06)
- [x] S8 QR code + front-page screenshot → presentation/

## 9 · Build, preview, publish
- **Build:** `python course_site/build.py` (needs `pip install markdown pyyaml`) → `course_site/_site/`.
- **Preview:** `python -m http.server 8765 -d course_site/_site` → http://127.0.0.1:8765/
- **Publish:** `bash course_site/publish.sh` → force-pushes `_site/` to the `gh-pages` branch. Live URL: https://sakib1418.github.io/RL_course_design/
- **Edit a page:** change the markdown in `content/`; change week or session titles only in `specs/*.md`; rebuild; publish.
- **Headshot:** replace the `SF` monogram in `content/_partials/instructor.md` with `<img class="avatar" src="{{root}}assets/img/headshot.jpg" alt="Sakib Ferdous">` after adding the photo.
- **Presentation assets:** `presentation/qr_course_site.png|svg` (decodes to the live URL), `front_page_2880x1800.png` (slide image), `front_page_full.png`.
