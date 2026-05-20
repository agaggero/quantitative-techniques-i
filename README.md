# Quantitative Techniques I — Descriptive Statistics, Probability, and Index Numbers

Open monolingual-English undergraduate textbook for **Técnicas Cuantitativas I** at the University of Granada. Built with [Quarto](https://quarto.org).

## Status

🟢 **v1.0 — published 2026-05-20.** Live at [https://agaggero.github.io/quantitative-techniques-i/](https://agaggero.github.io/quantitative-techniques-i/). Source: [agaggero/quantitative-techniques-i](https://github.com/agaggero/quantitative-techniques-i). All 7 chapters + 3 appendices ported from the original LaTeX lecture notes, Beamer slide decks, R Labs, LearnR interactive tutorials, and exercise sets into a single Quarto book. Locked editorial conventions (`\mathbb{E}`, `\operatorname{Var}`, `S^2` with divisor $n$, no custom macros) applied consistently per [`STYLE_GUIDE.md`](STYLE_GUIDE.md).

## Build

```bash
cd en && quarto render
```

Output lands in `en/_output/`. On Windows, invoke Quarto via the 8.3 short path to avoid the Deno-launcher bug with spaces in `C:\Program Files\`:

```powershell
cd en
& "C:\PROGRA~1\Quarto\bin\quarto.cmd" render --to html
```

## Layout

```
BOOK_PROJECT/
├── en/                            independent EN Quarto project
│   ├── _quarto.yml
│   ├── index.qmd                  preface
│   ├── chapters/
│   │   ├── 01-univariate.qmd
│   │   ├── 02-bivariate.qmd
│   │   ├── 03-probability.qmd
│   │   ├── 04-random-variables.qmd
│   │   ├── 05-distributions.qmd
│   │   ├── 06-index-numbers.qmd
│   │   ├── 07-time-series.qmd
│   │   ├── appendix-a-prerequisites.qmd
│   │   ├── appendix-b-tables.qmd
│   │   └── appendix-c-formula-sheet.qmd
│   └── _output/                   rendered HTML (gitignored)
├── references.bib                 shared bibliography (BibTeX)
├── STYLE_GUIDE.md                 enforced editorial conventions
├── EDITORIAL_PLAN.md              (in ../) — full planning doc
└── landing-page.html              single-language landing
```

## Locked editorial decisions

The full decision log (D1–D16) is in [../EDITORIAL_PLAN.md §4](../EDITORIAL_PLAN.md). Key choices:

| | |
|---|---|
| License | CC BY 4.0 |
| Anchor text | None — TC1 is self-contained; optional Newbold/Carlson/Thorne crosswalk later |
| Languages | English only at v1.0 (Spanish edition deferred to v1.x) |
| Math conventions | `\bar{x}`, `\mu`, `S^2` (divisor $n$, Spanish business-stats), `\sigma^2`, `\mathbb{E}`, `\operatorname{Var}`, `\operatorname{Cov}` |
| Custom macros | Forbidden (`\Var`, `\Cov`, `\E` — use literal `\operatorname{...}` and `\mathbb{E}`) |
| Companion R package | Not at v1.0 — data simulated inline with `set.seed(2026)` |

## Sources

The canonical TC1 source materials live one level up at `../`. Each chapter draws from:

- `Lecture_Notes/Topic_N/Topic_N_Notes.tex` (theory spine)
- `Lecture_Notes/Topic_N/Topic_N_Lab.Rmd` (R Lab content)
- `Lecture_Notes/Topic_N/Topic_N_Tutorial.Rmd` (LearnR MCQs → Self-check)
- `Practice/Exercises/Topic_N_Exercises.tex` (exercises)
- `Slides/Topic_N/Topic_N.tex` (cross-check)

Editing the `.qmd` files in this `BOOK_PROJECT/en/chapters/` is the book's source of truth going forward; the original `.tex` and `.Rmd` files are reference originals.

## Contributing

This is the working repository for the TC1 textbook draft. Future contributions should follow [`STYLE_GUIDE.md`](STYLE_GUIDE.md) and obey the conventions locked in the editorial plan.
