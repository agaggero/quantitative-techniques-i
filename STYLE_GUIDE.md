# Style Guide — *Quantitative Techniques I* (TC1)

**Version:** 1.0
**Date:** 2026-05-19
**Purpose:** Every chapter / appendix `.qmd` in this book must follow this guide.
Reference implementation for comparison: `../../ECONOMETRIA I/ENGLISH/BOOK_PROJECT/en/chapters/01-initial-concepts.qmd` through `08-autocorrelation.qmd` (same Quarto book pattern; TC1 is monolingual English).

---

## 1. File location and naming

- All chapter files live in `BOOK_PROJECT/en/chapters/`
- Naming: `0N-<slug>.qmd` where slug is short kebab-case
  - `01-univariate.qmd`, `02-bivariate.qmd`, `03-probability.qmd`, `04-random-variables.qmd`, `05-distributions.qmd`, `06-index-numbers.qmd`, `07-time-series.qmd`
- Appendices: `appendix-a-prerequisites.qmd`, `appendix-b-tables.qmd`, `appendix-c-formula-sheet.qmd`

## 2. Frontmatter and status line

```markdown
---
title: "Univariate Descriptive Statistics"
---

> *Status: ported 2026-05-19. Reviewed by editor: pending.*

```

No subtitle, no author, no date in chapter frontmatter — those live in `_quarto.yml`.

## 3. Six-section chapter template (mandatory order)

Every chapter has these six top-level sections, exactly in this order:

```markdown
## Learning outcomes {.unnumbered}

By the end of this chapter the reader should be able to:

- (5-8 bullet points; one verb each: *describe, compute, interpret, distinguish*…)

## Motivating empirical question {.unnumbered}

> *One italicised sentence stating a real-world question the chapter equips students to answer.*

Then 1-2 paragraphs of context that point to the running example used in the chapter.

## N.1 Introduction

Theory body begins here. Number sections N.1, N.2, N.3 … where N is the chapter number.

## N.X R Lab — (descriptive title)

R code chunks with worked example on the chapter's running dataset.

## Self-check {.unnumbered}

5–8 multiple-choice questions in collapse callouts (see §6).

## Exercises {.unnumbered}

5–8 starred exercises (★ easy, ★★ medium, ★★★ analytical/proof). Solutions for ★ inline; ★★/★★★ in Instructor Edition (separate file, not in this chapter).
```

The headings `Learning outcomes`, `Motivating empirical question`, `Self-check`, and `Exercises` all use `{.unnumbered}` so they don't enter the numbered TOC.

## 4. Math notation conventions (D13 — LOCKED)

| Quantity | Notation |
|---|---|
| Sample mean | `\bar{x}` |
| Population mean | `\mu` |
| Sample variance (divisor $n$, **Spanish business-stats convention**) | `S^2 = \frac{1}{n}\sum (x_i - \bar{x})^2` |
| Sample standard deviation | `S` |
| Population variance | `\sigma^2` |
| Population standard deviation | `\sigma` |
| Expectation | `\mathbb{E}[X]` (NEVER plain `E[X]`) |
| Variance operator | `\operatorname{Var}(X)` (NEVER `\mathrm{Var}`, NEVER custom `\Var` macro) |
| Covariance | `\operatorname{Cov}(X, Y)` |
| Correlation | `\operatorname{Corr}(X, Y)` or `\rho_{XY}` |
| Estimators | `\hat{\theta}`, `\hat{\mu}`, `\hat{\sigma}^2` |
| Probability | `P(A)` or `\mathbb{P}(A)` — pick `P(A)` (simpler, consistent with the lecture notes) |
| PMF / PDF | `f(x)` or `f_X(x)`; `p(x)` for discrete PMF acceptable in Topic 5 |
| CDF | `F(x)` or `F_X(x)` |
| Binomial coefficient | `\binom{n}{k}` |
| Factorial | `n!` |

## 5. LaTeX macros — FORBIDDEN

Do **not** define or use any of:
- `\Var`, `\Cov`, `\E`, `\Prob`, `\Mean` (custom shorthand macros)
- `\v` followed immediately by `\varepsilon` on same line (parses as undefined `\varepsilon` macro then `\varepsilon`)

These caused real bugs in the sibling Econometrics I project. Use literal `\operatorname{Var}` etc. throughout.

## 6. Callouts

Quarto Pandoc-style fenced div callouts. Three types in active use:

### `callout-note` — definitions, examples, important asides

```markdown
::: {.callout-note}
## Definition: arithmetic mean

The arithmetic mean of a sample $\{x_1, \ldots, x_n\}$ is

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i.
$$
:::
```

### `callout-warning` — common mistakes / pitfalls

```markdown
::: {.callout-warning}
## Common mistake: confusing $S^2$ with $\hat{\sigma}^2$

This book uses divisor $n$ (the maximum-likelihood / Spanish business-stats convention). Many English textbooks use divisor $n-1$ and write $\hat{\sigma}^2$. Both are valid; they differ by a factor of $n/(n-1)$, which is negligible for $n \geq 30$.
:::
```

### `callout-tip` with `collapse="true"` — self-check MCQs

```markdown
::: {.callout-tip collapse="true"}
## Q1. Heading is the question label only

A short stem text in plain prose, ending in a colon:

- A. First option.
- B. Second option.
- C. Third option.
- D. Fourth option.

**Answer: B.** One- or two-sentence explanation of why B is right and the others wrong.
:::
```

**Critical**: the four options A/B/C/D are a **bullet list** (each line prefixed with `- `). Without the bullets, Markdown collapses them into one paragraph that renders inline. This was a real bug in Econometrics I — don't repeat it.

## 7. Math equations and callouts — CRITICAL

**Display math equations (`$$ … $$`) MUST appear OUTSIDE callout boxes** when feasible. Inline math (`$x$`) inside callouts is fine. Display math inside `::: {.callout-…} … :::` blocks sometimes renders poorly in HTML; the Econometrics I project hit this repeatedly.

If a definition needs a display equation, structure as:

```markdown
::: {.callout-note}
## Definition: arithmetic mean
:::

The arithmetic mean of a sample $\{x_1, \ldots, x_n\}$ is

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i.
$$

(The mean is the most common summary of central tendency.)
```

OR put the equation inside but only when it's a one-line inline-equivalent and you have confirmed it renders cleanly. When in doubt, put it outside.

## 8. R chunks

- Use chunk labels prefixed `ch0N-…`: e.g. `{r ch01-setup}`, `{r ch01-hist-wage}`, `{r ch01-summary-table}`. The prefix prevents label collisions across chapters.
- Setup chunk at the top of the R Lab section:

```r
#| message: false
#| warning: false
library(readxl)
library(dplyr)
# any chapter-specific libraries
```

- Prefer base R + `dplyr` for tabular ops. Use `ggplot2` only if a base graphic would be uglier (most univariate/bivariate work is fine in base).
- Datasets: simulate inline with `set.seed(2026)` (consistent seed across the whole book), or read from a local file in `data/` if needed.
- Comments: in English, brief, focused on the *why* not the *what*.

## 9. Exercises section

5–8 exercises, each with a star rating:

```markdown
### Exercise 1.1 ★ — Compute basic statistics

Given the sample $\{2, 4, 4, 5, 6, 7, 9\}$:

(a) Compute $\bar{x}$ and $S$.
(b) Identify the median.
(c) Sketch the box-plot.

::: {.callout-tip collapse="true"}
## Solution

(a) $\bar{x} = 5.29$, $S \approx 2.0$.
(b) Median $= 5$.
(c) Box from $Q_1 = 4$ to $Q_3 = 7$, median line at 5.
:::

### Exercise 1.2 ★★ — Effect of an outlier

(Problem text…)

### Exercise 1.3 ★★★ — Prove an algebraic identity

(Problem text…)
```

Solutions for ★ exercises go in collapse callouts inline (above pattern).
Solutions for ★★ and ★★★ exercises **do NOT appear in the chapter file** — they go to a separate Instructor Edition (out of scope for this porting pass; just write the problem statement, no solution).

## 10. Cross-references

- Internal section refs: `[Section 2.3](02-bivariate.qmd#sec-correlation)` after adding `{#sec-correlation}` to the heading.
- Appendix refs: `[Appendix A](appendix-a-prerequisites.qmd)`.
- Topic-to-Lecture-Notes mapping is in `SOURCES_MAP.md` (out of scope for porters; written by the editor).

## 11. Citations

- Use BibTeX keys in `references.bib` at the project root.
- Citation syntax: `[@newbold2013]` for in-text; `\cite{newbold2013}` works too.
- Suggested core entries for the v1 bibliography:
  - `@newbold2013` Newbold, Carlson, Thorne — *Statistics for Business and Economics* (the closest English anchor)
  - `@pena2002` Daniel Peña — *Análisis de datos multivariantes* (Spanish reference some students will own)
  - The full list is the editor's responsibility — porter agents can leave citations as `[@TODO]` if uncertain.

## 12. What this book deliberately does NOT do

- **No inferential statistics**: no hypothesis tests, no CIs, no $p$-values, no sampling distribution discussion. TC1 is descriptive + probabilistic only. Inferential content belongs in TC2 / Econometrics I.
- **No bilingual content**: this is the EN-only edition. The `es/` directory is a future hook (D7).
- **No companion R package**: data are simulated inline with `set.seed(2026)`. No `tc1ugr` package at v1.0 (D8).

## 13. Source files per topic (for porter agents)

For Topic N (= Chapter N), the canonical sources are:

| Source | Path | Use as |
|---|---|---|
| Lecture notes | `Lecture_Notes/Topic_N/Topic_N_Notes.tex` | Theory spine. Primary source. |
| Slides | `Slides/Topic_N/Topic_N.tex` | Cross-check: any definitions in slides not in notes? Worth a 1-paragraph mention. |
| R Lab | `Lecture_Notes/Topic_N/Topic_N_Lab.Rmd` | Body of the N.X R Lab section. |
| LearnR tutorial | `Lecture_Notes/Topic_N/Topic_N_Tutorial.Rmd` | Source for MCQs → Self-check section. |
| Exercises | `Practice/Exercises/Topic_N_Exercises.tex` | Source for the Exercises section. |
| Exam Prep Guide | `Lecture_Notes/Exam_Prep_Guide.Rmd` (Topic N section) | Formula table inspiration; goes mainly into Appendix C. |

(All paths relative to `TC1/`.)

---

End of style guide.
