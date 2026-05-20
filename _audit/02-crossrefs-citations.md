# TC1 Audit 02 — Cross-references and Citations

**Audited**: 10 chapter files in `en/chapters/`, `en/index.qmd`, `references.bib`
**Date**: 2026-05-19
**Method**: single read pass, no files edited

---

## 1. Summary counts

| Item | Count |
|---|---|
| Internal cross-refs (markdown links to other .qmd or section anchors) | 14 |
| ...broken or wrong | **1** (one wrong section number — link text says "1.5.5" but target is "1.5.4") |
| `{#sec-...}` anchors defined | 25 (all unique book-wide) |
| `@authoryear` citation calls | 2 (both `@wooldridge2020`) |
| ...unresolved (key missing from `references.bib`) | **2** (both `@wooldridge2020`) |
| `\cite{...}` LaTeX macros | 0 |
| `@sec-...` Quarto cross-refs | 0 (book uses old-style `[Section X](path#sec-...)` instead) |
| `[@TODO]` / `[@?]` placeholders | 0 |
| HTML-comment `TODO` notes for editor | 4 |
| Markdown image references `![...](path)` | 0 (all figures are R-generated) |
| Hardcoded external URLs in chapters | 1 (`https://quarto.org` in `index.qmd`, line 43; build-tool reference, fine) |
| `references.bib` keys defined | 5 (`newbold2013`, `pena2002`, `walpole2017`, `wackerly2008`, `ine_ipc`) |
| ...actually cited in the text | 0 |

---

## 2. Internal cross-reference inventory

### Inter-chapter links (markdown `[Chapter N](0N-…)` etc.) — all targets exist

| Source file:line | Link text | Target | Status |
|---|---|---|---|
| 01-univariate.qmd:23 | "Chapter 2" | `02-bivariate.qmd` | OK |
| 01-univariate.qmd:23 | "Chapter 4" | `04-random-variables.qmd` | OK |
| 01-univariate.qmd:164 | "Appendix A" | `appendix-a-prerequisites.qmd` | OK |
| 02-bivariate.qmd:24 | "Section 2.7" | `02-bivariate.qmd#sec-rlab` | OK (target `{#sec-rlab}` at line 492) |
| 02-bivariate.qmd:28 | "Chapter 1" | `01-univariate.qmd` | OK |
| 02-bivariate.qmd:98 | "Chapter 1" | `01-univariate.qmd` | OK |
| 02-bivariate.qmd:194 | "Section 2.6" | `02-bivariate.qmd#sec-anscombe` | OK (target `{#sec-anscombe}` at line 302) |
| 02-bivariate.qmd:206 | "Chapter 1" | `01-univariate.qmd` | OK |
| 02-bivariate.qmd:314 | "Section 2.7" | `02-bivariate.qmd#sec-rlab` | OK |
| 02-bivariate.qmd:440 | "Section 2.9" | `02-bivariate.qmd#sec-causation` | OK (target at line 469) |
| 02-bivariate.qmd:494 | "Chapter 1" | `01-univariate.qmd` | OK |
| 02-bivariate.qmd:517 | "Chapter 1" | `01-univariate.qmd` | OK |
| 03-probability.qmd:186 | "Appendix A" | `appendix-a-prerequisites.qmd` | OK |
| 06-index-numbers.qmd:24 | "Chapter 7" | `07-time-series.qmd` | OK |
| 06-index-numbers.qmd:358 | "Chapter 7" | `07-time-series.qmd` | OK |
| 07-time-series.qmd:126 | "Chapter 2" | `02-bivariate.qmd` | OK |
| 07-time-series.qmd:262 | "Chapter 6" | `06-index-numbers.qmd` | OK |

### Intra-chapter anchor link — one mismatch

| Source file:line | Link text | Target | Status |
|---|---|---|---|
| 01-univariate.qmd:150 | "Section 1.5.5" | `#sec-boxplot` | **Misleading**: the box-plot section is numbered **1.5.4** in the file (line 399). The anchor jump will still work, but the human-readable label is off by one. |

### Section anchor labels — uniqueness check

All 25 `{#sec-...}` labels are unique across the 10 chapter/appendix files. No silent Quarto cross-ref collisions.

The book mixes two style conventions:
- Most prose links use **plain markdown**: `[Section 2.6](02-bivariate.qmd#sec-anscombe)`.
- No file uses the Quarto-native `@sec-anscombe` shorthand.

This is internally consistent and renders fine in both HTML and PDF; the editor may want to standardise on `@sec-...` later (it would auto-generate the "Section 2.6" text and survive renumbering), but no current ref is broken because of it.

---

## 3. Citations

### Keys defined in `references.bib`

`newbold2013`, `pena2002`, `walpole2017`, `wackerly2008`, `ine_ipc` — five entries, well-formed BibTeX.

### Citation calls in chapters

Only **one** `@authoryear` key is invoked anywhere in the book, and it is **not** in `references.bib`:

| File:line | Citation call | In bib? |
|---|---|---|
| 02-bivariate.qmd:24 | `[@wooldridge2020]` | **NO** — undefined key. Quarto will emit `?` in HTML and a missing-citation warning in PDF. |
| 02-bivariate.qmd:490 | `[@wooldridge2020]` | **NO** — same undefined key. |

An HTML-comment self-note already flags this at 02-bivariate.qmd:868:

> `<!-- TODO(editor): citation [@wooldridge2020] is reused from the Econometrics I book; confirm or replace once references.bib for TC1 is finalised. -->`

The five defined keys (`newbold2013` etc.) are **never cited in the prose** of any chapter — they only appear in the Preface's prose acknowledgements as author names. The bibliography section of the rendered book will be empty unless those keys are cited (or unless `nocite` is added to the YAML to force-include them).

### `[@TODO]` and `[@?]` placeholders

None found anywhere.

---

## 4. Editor `TODO` notes (HTML comments) — informational, not breakage

| File:line | Note |
|---|---|
| 02-bivariate.qmd:866 | Topic 2 lecture notes also cover residual diagnostics and log-linearised models; intentionally trimmed. |
| 02-bivariate.qmd:868 | The `@wooldridge2020` citation needs confirmation/replacement. |
| 04-random-variables.qmd:362 | Markov's inequality omitted; decide whether to add. |
| 04-random-variables.qmd:691–694 | Bivariate joint-distribution material intentionally scoped out of Chapter 4. |

These are intentional editorial notes and will not break the render.

---

## 5. External URLs

Only one chapter-level external URL: `https://quarto.org` in `index.qmd:43` (the build instructions). Shape is fine, not fetched.

The `references.bib` entry `ine_ipc` contains `https://www.ine.es/` in `howpublished`; that is the right top-level domain for the Spanish Statistical Office and looks reasonable.

No URLs appear in Chapter 6 prose despite the heavy use of INE-style data; the source is referred to descriptively ("Spanish IPC, published monthly by the INE").

---

## 6. Image / figure paths

Searched all 10 `.qmd` files for `![...](...)` markdown image syntax: **zero matches**. Every figure in the book is generated by an executable R chunk (and shows up in `_files/` and `_freeze/` after render). No risk of stale/broken external image paths.

---

## 7. Worst offender

**`chapters/02-bivariate.qmd`** is the worst offender by a wide margin: it owns both copies of the only unresolved citation key (`@wooldridge2020`) and two of the four editor TODO comments. Everything else in the book passes cleanly.

---

## 8. Verdict

**Mostly clean — first render will succeed, but with two visible citation warnings and one off-by-one label.**

Minimum-diff fixes the editor should make before the next render (in priority order):

1. **Decide `@wooldridge2020`.** Either add a `@book{wooldridge2020, ...}` entry to `references.bib` (Wooldridge, *Introductory Econometrics*, Cengage, 6e is the obvious one), or rewrite the two prose mentions in 02-bivariate.qmd to drop the citation (e.g. "developed in later courses on econometrics."). Until one of these happens, the rendered HTML/PDF will show "?" markers next to those sentences.
2. **Fix the "Section 1.5.5"/"1.5.4" mismatch** in 01-univariate.qmd:150 — change the link text from `[Section 1.5.5]` to `[Section 1.5.4]` (the anchor `#sec-boxplot` already resolves correctly).
3. *(Cosmetic, not blocking)* Decide whether the five `references.bib` keys that are currently defined-but-uncited should be (a) `nocite`d in the YAML so they appear in the bibliography for completeness, or (b) cited inline somewhere (a `Further reading` paragraph in the Preface or per-chapter would be natural), or (c) deleted from the .bib until they are actually used.

None of these is a render-blocker — Quarto will produce a book either way — but addressing #1 and #2 takes about two minutes and removes the only user-visible defects.
