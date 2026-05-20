# TC1 Audit 01 — Notation consistency

**Date**: 2026-05-19
**Files audited**: 10 (7 chapters + 3 appendices)
**Auditor**: Claude (notation pass, read-only)

## Summary

- Total convention violations found: **0 substantive** (5 minor cosmetic items noted under "Soft observations")
- Most affected file(s): n/a — corpus is clean
- Severity: **GREEN — minor cosmetic only**

The just-ported TC1 textbook is **fully compliant** with the locked math-notation conventions in STYLE_GUIDE.md §4-§5. All forbidden patterns produced zero matches, and all required notational primitives are present and used consistently across the 10 files.

## Per-pattern findings

### Forbidden custom macros (`\Var`, `\Cov`, `\E`, `\Prob`, `\Mean`, `\Corr`)
- **Zero matches.** None of these macros appear in any chapter or appendix.

### `\mathrm{Var|Cov|Corr|E}` (should be `\operatorname{...}`)
- **Zero matches.** The use of `\mathrm{...}` in the corpus is only for **distribution-name labels** (e.g. `\mathrm{Poisson}(3)`, `\mathrm{Bernoulli}(p)`, `\mathrm{Geom}(p)`, `\mathrm{Hyp}(N,K,n)`, `\mathrm{NB}(r,p)`, `\mathrm{DU}(k)`) and for `\mathrm{SSR}` (the sum-of-squared-residuals label) in 02-bivariate.qmd lines 343, 346, 832. These are valid uses of `\mathrm` for non-Var/Cov labels and do **not** violate the rule.

### `\text{Var|Cov|Corr|E}`
- **Zero matches.** No drift.

### Plain `E[..]` or `E(..)` in math mode
- **Zero matches** in display/inline math. The only `E[X]` occurrences are inside R code chunks (`cat("E[X] =", EX, ...)`, plot legends, R variable names): all legitimate non-math contexts:
  - `03-probability.qmd:492` — `legend("topright", legend = c("Running average", "E[X] = 3.5"), ...)`
  - `04-random-variables.qmd:395, 396, 443` — `cat("E[X]  =", EX, ...)` in R chunks
  - `05-distributions.qmd:419` — `cat("E[X] =", mu_b, ...)`
  - `appendix-c-formula-sheet.qmd:288, 289` — `cat("E[X] =", EX, ...)`
- All math-mode expectations correctly use `\mathbb{E}[X]` (83 occurrences across 4 files).

### `\mathbb{P}(A)` or `\Pr(A)` (should be `P(A)`)
- **Zero matches.** Probability is uniformly `P(A)` (153 matches across 6 files), consistent with STYLE_GUIDE §4 line 81.

### `F(X)` or `f(X)` (capital arg with lowercase fn)
- **Zero matches.** All CDF/PDF arguments are lowercase where math notation is used: `F(x)`, `f(x)`, `F_X(x)`, `f_X(x)`. The capitalized "F(x)" in 04-random-variables.qmd:414, 430, 451 and appendix-c-formula-sheet.qmd:304 are R-plot axis labels, not math (legitimate).

### `s^2` for sample variance
- **Zero matches in math.** The only `s^2` matches are R-code variable names (`Sx2`, `k_vals^2`, `outcomes^2`), not math notation. Sample variance is uniformly `S^2` (17 math occurrences).

### `\widetilde{S}^2`
- **Zero matches.**

### `\hat{\sigma}^2` for sample variance
- **3 matches** — but all in legitimate **expository asides** explaining the divisor-n vs divisor-(n-1) convention:
  - `01-univariate.qmd:361` — inside a `callout-warning` titled "Common mistake: confusing $S^2$ with the divisor-$n-1$ estimator"
  - `appendix-a-prerequisites.qmd:167` — text explaining R's `var()` uses n-1
  - `appendix-c-formula-sheet.qmd:49` — "Confusing $S^2$ (divisor $n$) with $\hat{\sigma}^2$ (divisor $n-1$)"
- These are explicitly permitted by the audit brief ("it's fine to MENTION the n-1 convention in an aside"). The **canonical formula uses divisor n** everywhere (01-univariate.qmd:353, appendix-c-formula-sheet.qmd:49). No drift.

### `\binom{n}{k}` usage
- **Uniform.** 20+ uses across `03-probability.qmd`, `05-distributions.qmd`, `appendix-a-prerequisites.qmd`, `appendix-b-tables.qmd`, `appendix-c-formula-sheet.qmd`. All use the bracketed form `\binom{n}{k}`. No `{n \choose k}`, `C^n_k`, or unbraced `\binom n k` found.

### `\bar{x}` (sample mean)
- **58 matches** across 6 files. Uniform — no `\overline{x}` drift in mean-of-x position.
- `\overline{...}` appears 11 times but only for:
  - **Mean of a product** (e.g. `\overline{xy}`, `\overline{x^2}`, `\overline{y^2}`) in 02-bivariate.qmd and appendix-c-formula-sheet.qmd. This is correct multi-character overline notation (LaTeX `\bar{xy}` would render wrong; `\overline{xy}` is the right tool).
  - **Set complement** `\overline{A \cup B}` in 03-probability.qmd:96. Legitimate non-mean use.
- Conclusion: `\overline` is used exactly where it should be; no `\overline{x}` (single-letter) drift.

### `\operatorname{Var/Cov/Corr}` (positive check)
- **58 matches** across `02-bivariate.qmd`, `04-random-variables.qmd`, `05-distributions.qmd`, `appendix-c-formula-sheet.qmd`. The operator names are uniformly typeset with `\operatorname{...}`. No `\mathrm` or `\text` alternatives detected.

## Soft observations (non-violations, flagged for editor review)

1. **Capital `\bar{X}` / `\bar{Y}` (4 occurrences)** — STYLE_GUIDE §4 specifies `\bar{x}` (lowercase) for the sample mean. The following lines use the capital form:
   - `01-univariate.qmd:757-759` — three MCQ options for linear-transformation of a sample, e.g. "$\bar{Y} = a + b\bar{X}$ and $S_Y = |b|\,S_X$". Context is clear (transformation of variable X to Y) and capital is arguably more readable for a *transformed-variable* statement, but it's inconsistent with the canonical lowercase convention used everywhere else in the same chapter (32 `\bar{x}` instances). **Optional rename to lowercase.**
   - `07-time-series.qmd:131` — OLS-trend intercept formula `a = \bar{Y} - b\,\bar{t}`. Here `Y` is a time series capital letter throughout the chapter (uppercase `Y_t` is standard for time-series notation), so the capital `\bar{Y}` is arguably the *correct* match for that chapter's local convention. **No change recommended.**

2. **Distribution-name `\mathrm{Poisson}(...)` etc.** — Style guide doesn't explicitly cover this, but `\mathrm{Poisson}` is the universal Anglo convention; `\operatorname{Poisson}` would be equally valid. Current usage is consistent within and across chapters. **No change needed.**

3. **`\operatorname{SD}` (1 occurrence)** — `04-random-variables.qmd:278` uses `\operatorname{SD}(a + bX) = |b|\,\sigma`. The style guide doesn't lock SD notation; `\operatorname{SD}` is consistent with the `\operatorname{Var}` pattern used elsewhere in the same chapter. **No change needed.**

4. **`\operatorname{avg}` (2 occurrences)** — `appendix-c-formula-sheet.qmd:466`. Used for the seasonal-index averaging operator. Style guide silent; usage is internally consistent. **No change needed.**

5. **Lowercase `\text{IVE}` (~15 occurrences in 07-time-series.qmd and appendix-c)** — Spanish acronym for "Índice de Variación Estacional". The book is otherwise English-only; consider either (a) renaming the macro to `\text{SI}` (seasonal index) for English-edition consistency, or (b) keeping the Spanish acronym as a course-tradition artefact and adding a footnote on first use. This is an editorial/translation decision, not a notation-rule violation.

## Per-file violation table

| File | Hard violations | Soft observations |
|---|---|---|
| `01-univariate.qmd` | 0 | 1 (capital `\bar{X}/\bar{Y}` in MCQ lines 757-759) |
| `02-bivariate.qmd` | 0 | 0 |
| `03-probability.qmd` | 0 | 0 |
| `04-random-variables.qmd` | 0 | 0 |
| `05-distributions.qmd` | 0 | 0 |
| `06-index-numbers.qmd` | 0 | 0 |
| `07-time-series.qmd` | 0 | 1 (IVE acronym — translation question, not notation) |
| `appendix-a-prerequisites.qmd` | 0 | 0 |
| `appendix-b-tables.qmd` | 0 | 0 |
| `appendix-c-formula-sheet.qmd` | 0 | 1 (IVE acronym) |
| **Total** | **0** | **3** |

## Recommended fixes (ordered by impact)

None of the soft observations block v1.0 shipping. In descending order of cosmetic value:

1. **Optional**: rename `\bar{X}`, `\bar{Y}` to `\bar{x}`, `\bar{y}` in `01-univariate.qmd:757-759` for full lowercase consistency. Specific edits:
   - Line 757: `$\bar{Y} = a + b\bar{X}$ and $S_Y = |b|\, S_X$` → `$\bar{y} = a + b\bar{x}$ and $S_Y = |b|\, S_X$` (or keep S_Y/S_X capital as the *standard-deviation labels* differ from the *means*).
   - Lines 758, 759: same lowercase substitution.

2. **Editorial decision needed**: decide whether `\text{IVE}` (Spanish acronym) stays or becomes `\text{SI}` for the English edition. If keeping, add a one-time footnote on first use (07-time-series.qmd around line 167) clarifying the acronym.

3. **No-op**: the 3 `\hat{\sigma}^2` mentions are explicitly permitted and correctly placed in pedagogical asides; do not touch.

## Verdict

**The book can ship as-is for math-notation purposes.** The notation pass is clean. The three soft observations are cosmetic / editorial preferences, not violations. The corpus exhibits unusually disciplined notation hygiene for a freshly ported textbook — no `\Var`, no `\E`, no `\mathbb{P}`, no `s^2`, no `F(X)`, no `\widetilde{S}^2`, no plain `E[X]` in math mode, no `\binom n k` (unbraced), no `\mathrm{Var}` drift, no `\Pr`.

**Severity: GREEN.** No blocker. Proceed to next audit pass (likely cross-references, R-chunk labels, or callout-rendering checks).
