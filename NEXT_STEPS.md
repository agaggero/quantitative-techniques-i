# Next Steps — *Quantitative Techniques I* (TC1)

**Date:** 2026-05-19
**For:** Prof. Alessio Gaggero (also for future-you)
**Status:** v0.9 — manuscript-complete first port; all 7 chapters + 3 appendices in place; first clean render pending.

---

## 1. Where we are right now

| Stream | Count | Status |
|---|---|---|
| Chapters | 7 | ✅ ported from `Topic_N_Notes.tex` + `Topic_N_Lab.Rmd` + `Topic_N_Tutorial.Rmd` + `Topic_N_Exercises.tex` |
| Appendices | 3 | ✅ App.A (prereqs) authored; App.B (tables) authored from R chunks; App.C (formula sheet) ported from `Exam_Prep_Guide.Rmd` |
| Preface (`index.qmd`) | 1 | ✅ written |
| Configuration | — | ✅ `en/_quarto.yml`, `references.bib`, `.gitignore`, `landing-page.html` |
| Style guide | — | ✅ [`STYLE_GUIDE.md`](STYLE_GUIDE.md) — enforced conventions |
| First render | — | 🟡 pending (next step) |
| Visual editor pass | — | 🟡 pending (needs human eyes on rendered HTML) |

Total: ~270 KB of `.qmd` source across 11 chapter/appendix files, plus configuration. The originating LaTeX/Rmd source corpus stays at `../Lecture_Notes/`, `../Slides/`, and `../Practice/` as reference originals.

---

## 2. How to build the book

From `BOOK_PROJECT/en/`:

```powershell
& "C:\PROGRA~1\Quarto\bin\quarto.cmd" render --to html
```

Output → `en/_output/`. Open `en/_output/index.html` in a browser.

On macOS / Linux: `cd en && quarto render`.

---

## 3. Required R packages (one-time install)

```powershell
$rscript = "C:\Program Files\R\R-4.5.3\bin\Rscript.exe"
& $rscript -e "install.packages(c('knitr','rmarkdown','readxl','dplyr','ggplot2','learnr'), repos='https://cloud.r-project.org')"
```

No external data-package dependency. All examples use simulated data with `set.seed(2026)` or small files committed to the repo.

---

## 4. Remaining work to v1.0

In priority order:

1. **First clean render** (`quarto render --to html` from `en/`). Expected first-render bugs: missing citations resolving to `[?]` placeholders, R-chunk failures from typos, MathJax glitches in inline math, callout-rendering quirks. Time: ~30 min to fix what surfaces.

2. **Visual editor pass** — open the rendered HTML in a browser and read every chapter once. Look for:
   - Math-in-callout rendering glitches (style guide §7 says display math goes outside callouts; flag any that slipped through).
   - A/B/C/D MCQ option blocks that didn't get the bullet-list treatment.
   - Cross-references to other chapters that resolve to `[?]`.
   - Custom-macro residues (`\Var`, `\E`, `\Cov`).
   - Tables that overflow the page width (App.B has known risk).
   Time: ~1 hour.

3. **Notation harmonisation audit** — sweep `\mathbb{E}` vs `E[`, `\operatorname{Var}` vs `\mathrm{Var}`, `S^2` vs `\hat{\sigma}^2`, custom-macro residues. The 6-agent audit storm that closed Econometrics I in one afternoon is the model. Time: ~2-3 hours of agent-assisted work.

4. **PDF render** — `quarto render --to pdf`. PDF surfaces TikZ + pgfplots compatibility issues the HTML hides. Budget 2-3 iteration cycles. Time: ~2 hours.

5. **Instructor Edition PDF** — separate render that includes ★★ and ★★★ exercise solutions (which the chapter `.qmd` files deliberately omit). The mechanism is parallel to the `\ifshowsolutions` toggle in the original `Topic_N_Exercises.tex`. Time: ~1 day to set up properly with Quarto profiles.

6. **Publish** — `quarto publish gh-pages` or Quarto Pub. Time: ~30 min.

7. **Zenodo DOI deposit** — for citation in your CV and on the website. Time: ~1 hour.

---

## 5. Locked editorial decisions

See [../EDITORIAL_PLAN.md §4](../EDITORIAL_PLAN.md) for the full D1–D16 table. Highlights that constrain future work:

- **D1**: CC BY 4.0
- **D7**: English-only at v1.0 (Spanish deferred to v1.x; scaffolding kept flat, no empty `es/` directory)
- **D8**: No companion R package at v1.0 — data are inline
- **D9**: Excel workbooks stay as a companion (linked from each chapter), not woven into the rendered HTML
- **D10**: R-Studio `.R` scripts are archived in favour of the `Topic_N_Lab.Rmd` files (one source of truth per topic)
- **D14**: No custom LaTeX macros (`\Var`, `\Cov`, `\E` forbidden)
- **D15**: Separate Git repository from the Econometrics I book

---

## 6. If you're stuck

- **Render fails with "Module not found ... Files/Quarto/..."** → use the 8.3 short path `C:\PROGRA~1\Quarto\bin\quarto.cmd`.
- **R chunk fails** → confirm `R_LIBS_USER` and that the listed packages are installed.
- **`learnr` interactive tutorials in `Topic_N_Tutorial.Rmd` don't render as part of the book** → that's correct; the LearnR tutorials are intended to be deployed separately (e.g. to shinyapps.io) and linked from each chapter's Self-check section as an optional "try the interactive version" pointer.
- **The Excel workbooks at `../Practice/Excel/` don't appear in the rendered book** → also correct; per D9, they stay as a companion. Each chapter has a brief callout pointing students at the corresponding workbook.

---

## 7. Source map

Per-chapter source mapping:

| Chapter | Theory | Lab | Self-check | Exercises |
|---|---|---|---|---|
| 1 Univariate | `Lecture_Notes/Topic_1/Topic_1_Notes.tex` | `Topic_1_Lab.Rmd` | `Topic_1_Tutorial.Rmd` | `Practice/Exercises/Topic_1_Exercises.tex` |
| 2 Bivariate | `Topic_2_Notes.tex` | `Topic_2_Lab.Rmd` | `Topic_2_Tutorial.Rmd` | `Topic_2_Exercises.tex` |
| 3 Probability | `Topic_3_Notes.tex` | `Topic_3_Lab.Rmd` | `Topic_3_Tutorial.Rmd` | `Topic_3_Exercises.tex` |
| 4 Random Vars | `Topic_4_Notes.tex` | `Topic_4_Lab.Rmd` | `Topic_4_Tutorial.Rmd` | `Topic_4_Exercises.tex` |
| 5 Distributions | `Topic_5_Notes.tex` | `Topic_5_Lab.Rmd` | `Topic_5_Tutorial.Rmd` | `Topic_5_Exercises.tex` |
| 6 Index Numbers | `Topic_6_Notes.tex` | `Topic_6_Lab.Rmd` | `Topic_6_Tutorial.Rmd` | `Topic_6_Exercises.tex` |
| 7 Time Series | `Topic_7_Notes.tex` | `Topic_7_Lab.Rmd` | `Topic_7_Tutorial.Rmd` | `Topic_7_Exercises.tex` |
| App.A | (authored from scratch + Topic_3 set-theory) | — | — | — |
| App.B | (authored from scratch via R chunks) | — | — | — |
| App.C | (ported from) `Lecture_Notes/Exam_Prep_Guide.Rmd` | — | — | — |
