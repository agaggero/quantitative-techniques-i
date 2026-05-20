# TC1 Callout & MCQ Formatting Audit

**Audit date:** 2026-05-19  
**Files audited:** `BOOK_PROJECT/en/chapters/*.qmd`

---

## Summary

- **Files audited:** 10
- **Total MCQ blocks (callout-tip + collapse=true with options):** 56
- **MCQ blocks NOT in bullet-list format:** 0
- **Display-math-in-callout instances:** 26
- **Non-canonical callout types:** 0

### Open/Close count per file

| File | `:::{...}` openers | `:::` closers (bare) | Diff |
|---|---:|---:|---:|
| 01-univariate.qmd | 43 | 43 | +0 |
| 02-bivariate.qmd | 30 | 30 | +0 |
| 03-probability.qmd | 34 | 34 | +0 |
| 04-random-variables.qmd | 34 | 34 | +0 |
| 05-distributions.qmd | 23 | 23 | +0 |
| 06-index-numbers.qmd | 29 | 29 | +0 |
| 07-time-series.qmd | 23 | 23 | +0 |
| appendix-a-prerequisites.qmd | 3 | 3 | +0 |
| appendix-b-tables.qmd | 0 | 0 | +0 |
| appendix-c-formula-sheet.qmd | 15 | 15 | +0 |

(Note: openers include only `.callout-…` blocks. Closers count bare `:::` lines, which include closers for non-callout fenced divs too. A negative diff is normal if the file uses non-callout fenced divs.)

---

## 01-univariate.qmd

- Callout openers: 43
- Bare `:::` closers: 43

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 674: **OK (bullet list)**
- Line 687: **OK (bullet list)**
- Line 700: **OK (bullet list)**
- Line 713: **OK (bullet list)**
- Line 726: **OK (bullet list)**
- Line 739: **OK (bullet list)**
- Line 752: **OK (bullet list)**
- Line 765: **OK (bullet list)**
- Line 778: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

- Callout at line 166 (callout-note) → math at line 170
- Callout at line 166 (callout-note) → math at line 174
- Callout at line 202 (callout-note) → math at line 206
- Callout at line 202 (callout-note) → math at line 209
- Callout at line 216 (callout-note) → math at line 220
- Callout at line 240 (callout-note) → math at line 245
- Callout at line 285 (callout-note) → math at line 291
- Callout at line 311 (callout-note) → math at line 317
- Callout at line 311 (callout-note) → math at line 321
- Callout at line 371 (callout-note) → math at line 376
- Callout at line 409 (callout-note) → math at line 412
- Callout at line 421 (callout-note) → math at line 425
- Callout at line 437 (callout-note) → math at line 440
- Callout at line 477 (callout-note) → math at line 480 [inline-form $$...$$]

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 793 → solution at line 804: OK (`callout-tip collapse="true"`)
- Exercise at line 826 → solution at line 834: OK (`callout-tip collapse="true"`)
- Exercise at line 846 → solution at line 854: OK (`callout-tip collapse="true"`)

---

## 02-bivariate.qmd

- Callout openers: 30
- Bare `:::` closers: 30

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 650: **OK (bullet list)**
- Line 663: **OK (bullet list)**
- Line 676: **OK (bullet list)**
- Line 689: **OK (bullet list)**
- Line 702: **OK (bullet list)**
- Line 715: **OK (bullet list)**
- Line 728: **OK (bullet list)**
- Line 741: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

- Callout at line 111 (callout-note) → math at line 116
- Callout at line 143 (callout-note) → math at line 148
- Callout at line 203 (callout-note) → math at line 208
- Callout at line 232 (callout-note) → math at line 237
- Callout at line 337 (callout-note) → math at line 342
- Callout at line 337 (callout-note) → math at line 348
- Callout at line 401 (callout-note) → math at line 406

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 756 → solution at line 770: OK (`callout-tip collapse="true"`)
- Exercise at line 778 → solution at line 786: OK (`callout-tip collapse="true"`)

---

## 03-probability.qmd

- Callout openers: 34
- Bare `:::` closers: 34

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 602: **OK (bullet list)**
- Line 615: **OK (bullet list)**
- Line 628: **OK (bullet list)**
- Line 641: **OK (bullet list)**
- Line 654: **OK (bullet list)**
- Line 667: **OK (bullet list)**
- Line 680: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

None.

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 695 → solution at line 705: OK (`callout-tip collapse="true"`)
- Exercise at line 715 → solution at line 723: OK (`callout-tip collapse="true"`)

---

## 04-random-variables.qmd

- Callout openers: 34
- Bare `:::` closers: 34

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 475: **OK (bullet list)**
- Line 488: **OK (bullet list)**
- Line 501: **OK (bullet list)**
- Line 514: **OK (bullet list)**
- Line 527: **OK (bullet list)**
- Line 540: **OK (bullet list)**
- Line 553: **OK (bullet list)**
- Line 566: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

None.

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 581 → solution at line 593: OK (`callout-tip collapse="true"`)
- Exercise at line 603 → solution at line 611: OK (`callout-tip collapse="true"`)

---

## 05-distributions.qmd

- Callout openers: 23
- Bare `:::` closers: 23

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 542: **OK (bullet list)**
- Line 555: **OK (bullet list)**
- Line 568: **OK (bullet list)**
- Line 581: **OK (bullet list)**
- Line 594: **OK (bullet list)**
- Line 607: **OK (bullet list)**
- Line 620: **OK (bullet list)**
- Line 633: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

None.

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 648 → solution at line 656: OK (`callout-tip collapse="true"`)
- Exercise at line 666 → solution at line 675: OK (`callout-tip collapse="true"`)
- Exercise at line 687 → solution at line 696: OK (`callout-tip collapse="true"`)

---

## 06-index-numbers.qmd

- Callout openers: 29
- Bare `:::` closers: 29

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 518: **OK (bullet list)**
- Line 531: **OK (bullet list)**
- Line 544: **OK (bullet list)**
- Line 557: **OK (bullet list)**
- Line 570: **OK (bullet list)**
- Line 583: **OK (bullet list)**
- Line 596: **OK (bullet list)**
- Line 609: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

- Callout at line 143 (callout-note) → math at line 147
- Callout at line 256 (callout-note) → math at line 261
- Callout at line 312 (callout-note) → math at line 317

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 624 → solution at line 632: OK (`callout-tip collapse="true"`)
- Exercise at line 640 → solution at line 648: OK (`callout-tip collapse="true"`)
- Exercise at line 656 → solution at line 664: OK (`callout-tip collapse="true"`)

---

## 07-time-series.qmd

- Callout openers: 23
- Bare `:::` closers: 23

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

- Line 456: **OK (bullet list)**
- Line 469: **OK (bullet list)**
- Line 482: **OK (bullet list)**
- Line 495: **OK (bullet list)**
- Line 508: **OK (bullet list)**
- Line 521: **OK (bullet list)**
- Line 534: **OK (bullet list)**
- Line 547: **OK (bullet list)**

### Display math (`$$...$$`) inside callouts

- Callout at line 610 (callout-tip) → math at line 617

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

- Exercise at line 562 → solution at line 570: OK (`callout-tip collapse="true"`)
- Exercise at line 582 → solution at line 589: OK (`callout-tip collapse="true"`)
- Exercise at line 597 → solution at line 610: OK (`callout-tip collapse="true"`)

---

## appendix-a-prerequisites.qmd

- Callout openers: 3
- Bare `:::` closers: 3

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

None.

### Display math (`$$...$$`) inside callouts

- Callout at line 158 (callout-warning) → math at line 163

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

No ★ (single-star) exercises detected.

---

## appendix-b-tables.qmd

- Callout openers: 0
- Bare `:::` closers: 0

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

None.

### Display math (`$$...$$`) inside callouts

None.

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

No ★ (single-star) exercises detected.

---

## appendix-c-formula-sheet.qmd

- Callout openers: 15
- Bare `:::` closers: 15

### MCQ blocks (`.callout-tip collapse="true"` with A/B/C/D)

None.

### Display math (`$$...$$`) inside callouts

None.

### Non-canonical callout types

None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.

### ★ exercise solutions

No ★ (single-star) exercises detected.

---

## Verdict

**COSMETIC.** No MCQ bullet bug. Some display-math-in-callout instances exist (style-guide §7 prefers them outside); these may render fine but are worth a manual look.