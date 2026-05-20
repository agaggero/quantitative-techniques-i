# R Code-Style Consistency Audit — TC1 Textbook (English Edition)

**Date:** 2026-05-19
**Auditor:** automated review (single read pass)
**Files audited:** 10 `.qmd` files in `en/chapters/`
**Style reference:** `STYLE_GUIDE.md` §8

---

## Headline numbers

| Metric | Count |
|--------|------:|
| Total R chunks audited | **92** |
| Chunks with correct chapter-prefixed label | 92 |
| Chunks with no / generic / wrong-prefix label | **0** |
| `set.seed()` calls observed across the book | 8 |
| Seeds equal to the project-locked value `2026` | **6 of 8 (75%)** |
| Chapters using a non-2026 seed | 1 (Ch. 1, by design — see §2) |
| Non-standard library imports flagged | 0 (cosmetic note on `library(dplyr)`) |

**Per-chapter chunk inventory**

| File | Chunks | Prefix | All labelled? |
|------|------:|--------|:--:|
| `01-univariate.qmd`           | 10 | `ch01-` | yes |
| `02-bivariate.qmd`            | 13 | `ch02-` | yes |
| `03-probability.qmd`          | 11 | `ch03-` | yes |
| `04-random-variables.qmd`     |  8 | `ch04-` | yes |
| `05-distributions.qmd`        | 12 | `ch05-` | yes |
| `06-index-numbers.qmd`        | 10 | `ch06-` | yes |
| `07-time-series.qmd`          | 15 | `ch07-` | yes |
| `appendix-a-prerequisites.qmd` |  0 | n/a (none expected) | n/a |
| `appendix-b-tables.qmd`       |  5 | `appB-` | yes |
| `appendix-c-formula-sheet.qmd` |  8 | `appC-` | yes |

---

## 1. Chunk-label prefix discipline (§8.1)

**Verdict: clean.** Every R chunk in every chapter carries the expected
`ch0N-…` (chapters) or `appB-…` / `appC-…` (appendices) prefix. No
unlabelled chunks (`{r}`), no generic numeric labels (`{r chunk-1}`),
no cross-chapter prefix bleed (no `ch02-…` chunk inside Ch. 3, etc.).

Representative labels seen:

- Ch. 1: `ch01-setup`, `ch01-data`, `ch01-freq-table`, `ch01-central`,
  `ch01-outlier`, `ch01-dispersion`, `ch01-cv-compare`, `ch01-hist`,
  `ch01-skew-kurt`, `ch01-lorenz`.
- Ch. 4: `ch04-setup`, `ch04-discrete-pmf`, `ch04-discrete-mean-var`,
  `ch04-discrete-cdf`, `ch04-continuous-pdf`, `ch04-continuous-probs`,
  `ch04-continuous-cdf`, `ch04-chebyshev`.
- App. B: `appB-norm-table`, `appB-binom-table`,
  `appB-binom-table-large`, `appB-pois-table`, `appB-crit-table`.
- App. C: `appC-setup`, `appC-t1-exercise` … `appC-t7-exercise`.

No action required.

---

## 2. `set.seed()` discipline (§8.2)

The book-wide locked seed is **`set.seed(2026)`**. Inventory of every
`set.seed()` call observed:

| Chapter | Chunk | Seed | Notes |
|---------|-------|-----:|-------|
| Ch. 1 (univariate) | `ch01-data`       | **42** | *Deliberate deviation.* The prose in §1.8 explains: "The chapter-wide seed is `set.seed(2026)`, but to remain consistent with the LearnR tutorial that uses the same dataset we keep the lab seed at 42." Editor decision needed. |
| Ch. 1 (univariate) | `ch01-cv-compare` | **99** | Second deviation inside the same chapter. Not justified in surrounding prose. Likely an artefact of porting the original lab. |
| Ch. 2 (bivariate)            | `ch02-data`   | 2026 | matches lock |
| Ch. 3 (probability)          | `ch03-setup`  | 2026 | matches lock |
| Ch. 4 (random variables)     | `ch04-setup`  | 2026 | matches lock |
| Ch. 5 (distributions)        | `ch05-setup`  | 2026 | matches lock |
| Ch. 6 (index numbers)        | `ch06-setup`  | 2026 | matches lock |
| Ch. 7 (time series)          | `ch07-setup`  | 2026 | matches lock |
| App. C (formula sheet)       | `appC-setup`  | 2026 | matches lock |

App. A has no chunks; App. B uses no `set.seed()` (deterministic tables
from `pnorm`/`dbinom`/`dpois`/`qnorm`).

**Flag for editor**

- **`ch01-data` uses `set.seed(42)`** — explicitly justified in prose for
  cross-consistency with the LearnR tutorial. Decision: either (a)
  keep and accept the documented exception, or (b) switch to `2026`
  and re-render the LearnR tutorial with the same seed.
- **`ch01-cv-compare` uses `set.seed(99)`** — *no prose justification*.
  Looks like an oversight from the port. Editor should either switch
  to `set.seed(2026)` (recommended, makes the chapter internally
  consistent on a single non-default seed) or change it to match the
  `42` deviation already documented.

Six of the eight seeds (75%) are on `2026`; if the editor adopts the
recommended change for `ch01-cv-compare`, the rate becomes 7/8 = 87.5%
on `2026`, with a single intentional, documented exception in Ch. 1.

---

## 3. Library imports — first-chunk declarations (§8.3)

Permitted set per the style guide: `knitr`, `rmarkdown`, `readxl`,
`dplyr`, `ggplot2`, `learnr`.

| Chapter | First-chunk `library()` calls | Status |
|---------|-------------------------------|--------|
| Ch. 1 | none (Base R only; declared in a comment) | ok |
| Ch. 2 | `library(dplyr)` | ok (within allowed set) |
| Ch. 3 | none (Base R only) | ok |
| Ch. 4 | none (Base R only; declared in a comment) | ok |
| Ch. 5 | none (Base R only) | ok |
| Ch. 6 | none (Base R only; declared in a comment) | ok |
| Ch. 7 | none (Base R only) | ok |
| App. B | none — uses `knitr::kable()` via fully-qualified call | ok |
| App. C | none — uses `knitr::opts_chunk$set(…)` and `knitr::kable()` | ok |

Other namespace-qualified calls used through the book (no `library()`
required, all in the allowed core): `knitr::kable()`, `knitr::opts_chunk$set()`,
`stats::filter()` (Ch. 7).

**Note for editor (cosmetic, not a fix)**

- Ch. 2 actually *imports* `dplyr` (the only non-Base-R import in the
  whole book) but the subsequent code uses only Base R (`data.frame`,
  `mean`, `sum`, `lm`, `cor`, `cov`, `plot`, `abline`, `anscombe`).
  No `%>%` pipes, no `mutate`/`select`/`filter` calls. The
  `library(dplyr)` line is harmless but **unused** and could be
  dropped to keep Ch. 2 Base-R like the other chapters. Up to the
  editor.

**No flagged forbidden imports** (no `data.table`, no bulk
`library(tidyverse)`, no `kableExtra`, no `forecast`, no `tseries`,
no `ineq`, etc.). The book is genuinely Base-R + `knitr` only, which
is a healthy state for a teaching textbook.

---

## 4. Inline code style — backticks around R functions (§8.4)

Spot-checks across every chapter show consistent use of backticks in
prose when referring to R functions or arguments. Representative
examples:

- Ch. 1: "R's `var()` and `sd()` divide by $n-1$."
- Ch. 2: "We can also reproduce the calculations in R with `cov()`,
  `cor()`, `lm()`, and `summary()`."
- Ch. 5: "verify them in R using `dbinom`, `pbinom`, `dpois`, `ppois`,
  `dhyper`, `phyper`, `dgeom`, `pgeom`."
- Ch. 7: "We use `stats::filter()` …"
- App. A glossary table is entirely back-ticked function names.

Minor inconsistency in Ch. 5 (LO list at the top): function names are
shown *without* parentheses (`dbinom`, not `dbinom()`). Most of the
book uses the parenthesised form. **Cosmetic only — flag for editor
to harmonise** if a single convention is desired.

---

## 5. `echo: false` and `message: false` patterns (§8.5)

- **App. B (static reference tables):** **all 5 chunks** carry
  `#| echo: false` *and* `#| message: false`. Correct — only the
  rendered tables should be visible, not the `pnorm`/`dbinom`/`dpois`
  call sites. No action required.
- **App. C setup chunk (`appC-setup`):** uses `#| include: false`,
  plus a global `knitr::opts_chunk$set(echo = TRUE, warning = FALSE,
  message = FALSE, …)`. Sensible: hides the setup itself and silences
  warnings/messages for the exam-solution chunks. The collapsed
  callout-tip blocks around each `appC-tN-exercise` are intended to
  *show* the code (the chunks have `echo = TRUE`), which is the right
  pedagogical choice.
- **Chapters 1–7 setup chunks:** all use `#| message: false` and
  `#| warning: false`. `echo` is left at the default (`true`) so
  learners see the code — correct convention for the R Labs.
- **No App. B chunk is missing `echo: false`.** Verdict: clean.

---

## 6. Comments inside R chunks (§8.6)

Comments inside chunks are uniformly **brief, in English, and explain
*why* rather than *what***. No paragraphs of Spanish text found
anywhere. No transliterated LaTeX prose. Representative examples that
match the desired style:

- Ch. 1 `ch01-central`: `# Returns the most frequent value (the first one, in case of ties).`
- Ch. 1 `ch01-lorenz`:  `# Gini via the trapezoidal rule.`
- Ch. 2 `ch02-cov-cor-manual`: `# By hand using the divisor n (chapter convention)`
- Ch. 4 `ch04-chebyshev`: `# Discrete product-launch variable: use Chebyshev to bound P(|X - mu| < k*sigma)`
- Ch. 5 `ch05-binom-basics`: `# Point probabilities P(X = 0), P(X = 1), P(X = 2)`
- Ch. 5 `ch05-hyper-lottery`: `# Loteria 6/49: 6 winning numbers among 49; you pick 6` *(Spanish proper noun, not Spanish prose — fine)*
- Ch. 6 `ch06-linking`: `# Old series, base 2015 = 100, 2015–2019`
- Ch. 7 `ch07-create-data`: `# repeats each year`

No egregious cases to flag.

---

## Overall verdict

> **Cosmetic only.** The R code style is in very good shape and the
> book can render today without any style-related fix. Two seed
> deviations in Ch. 1 are the only items that need an explicit
> editorial decision; both are concentrated in a single chapter and
> neither blocks the render.

### Editor to-do checklist (in priority order)

1. **(Decision)** Ch. 1 — choose what to do with the two non-2026
   seeds:
   - `ch01-data` uses `set.seed(42)` — documented in prose. Keep, or
     migrate to 2026 and update the LearnR tutorial in parallel.
   - `ch01-cv-compare` uses `set.seed(99)` — **not documented**.
     Strongly suggest changing to `set.seed(2026)` to make the chapter
     internally consistent on one (intentional) deviation rather than
     two.
2. **(Cosmetic)** Ch. 2 — consider dropping the unused
   `library(dplyr)` from `ch02-setup`; the chapter is pure Base R.
3. **(Cosmetic)** Harmonise the LO-list convention for function names
   in prose (`dbinom` vs `dbinom()` in Ch. 5).

Nothing else flagged.
