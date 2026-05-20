# TC1 Book — Spelling, Typos, Translation-Residue Audit

**Scope.** All `en/chapters/*.qmd` (10 files, ~6,389 lines) plus `en/index.qmd` (59 lines). Single read-pass; **no files modified.**

**Method.** Targeted ripgrep passes for common English misspellings, British/American spelling variants, Spanish residues, stale TODO/placeholder markers, empty math blocks, doubled words, and heading-case consistency. The `_output/`, `_freeze/`, `.quarto/`, and `_quarto.yml` directories were ignored — they are build artefacts, not source.

---

## 1. English typos

**Result: 0 hits.**

Searched the canonical misspelling shortlist plus a wider net:

`recieve, seperate, occured, accomodate, untill, existance, definately, independant, wich, teh, adn, wether, achive, adress, begining, beleive, calender, comming, enviroment, goverment, happend, liason, maintainance, neccessary, noticable, occassion, priviledge, recomend, refered, relevent, sucess, tommorow, truely, writting`

Also checked: doubled words (`the the`, `to to`, …), missing-apostrophe contractions (`wont`, `cant`, `dont`, `isnt`, …), and `less/fewer + countable noun` style slips. **All clean.**

> **Top 3 worst typos:** *none found.* The prose is unusually clean.

---

## 2. British vs American spelling

**Verdict: British is dominant and consistent.**

### British forms present (56 hits across 9 files)
`analyse / analysed / analysing, behaviour, centre / centred, colour, organise / organising, organisation, recognise, modelling / modelled, summarise / summarising, finalise / finalised, idealisation, generalise / generalised, specialise, categorise, standardise, summarised, …`

Per-file British-form counts:

| File | hits |
|---|---:|
| `07-time-series.qmd` | 13 |
| `01-univariate.qmd` | 11 |
| `02-bivariate.qmd` | 8 |
| `04-random-variables.qmd` | 7 |
| `03-probability.qmd` | 6 |
| `05-distributions.qmd` | 5 |
| `06-index-numbers.qmd` | 4 |
| `appendix-a-prerequisites.qmd` | 1 |
| `appendix-c-formula-sheet.qmd` | 1 |

### American forms present

- `practice` (multiple) — **not a spelling error**: in British English `practice` is the noun (`in practice`), `practise` is the verb. All TC1 occurrences are the noun. **Keep as-is.**
- `license` — single hit in `index.qmd:37,39` ("CC BY 4.0 license"). In British English the noun is normally `licence`, the verb `license`. Here it is part of the proper name *"CC BY 4.0 license"* (Creative Commons themselves render it as `license`), so it is acceptable as a proper name. Minor drift only.
- `program` — not found as American spelling; not flagged.

### Drift
No genuine drift. Aside from the one `license` (likely intentional, matches CC's own naming), the British set is universal. **Recommendation: leave as-is; British is the established convention.**

---

## 3. Spanish residues

**Result: only legitimate, italicised foreign-language proper nouns.** No prose-level Spanish leakage.

Hits and adjudication:

| File:line | Hit | Status |
|---|---|---|
| `index.qmd:7` | *Técnicas Cuantitativas I* | OK — italicised course name |
| `index.qmd:59` | *Análisis de datos multivariantes* (Daniel Peña) | OK — italicised book title |
| `01-univariate.qmd:948` | Málaga | OK — Spanish city name |
| `06-index-numbers.qmd:22, 24` | *Salario Mínimo Interprofesional*, *Índice de Precios al Consumo* | OK — italicised Spanish institutional names, immediately explained in English ("the Spanish CPI", "Spanish IPC") |
| `07-time-series.qmd:21` | Málaga | OK — proper noun |
| `07-time-series.qmd:163` | *Índices de Variación Estacional* | OK — italicised source for the IVE acronym, immediately translated |
| `05-distributions.qmd:470` | `# Loteria 6/49: …` (R code comment) | Minor — Spanish-style spelling without tilde (should be `Lotería` if kept, or "Lottery"). Cosmetic; inside an R comment. |

Searched for the danger list:
`solo, dado que, Heterocedasticidad, RLM, MCO, ELIO, apariencia, Salario, Educación, también, asimismo, así que, Sea X, Si X, En este caso, Por tanto, Supongamos, Consideremos, por lo tanto, sin embargo, además, pues, entonces, donde, cuando, esto es` — **none found in English prose.**

The Econometrics-I Spanish acronyms (`RLM`, `MCO`, `ELIO`, `Heterocedasticidad`) — **none present**, confirming clean separation between TC1 and the Econometrics I project.

The `\varepsilon` vs `\epsilon` check: only **one** file (`appendix-c-formula-sheet.qmd`) contains either, and it uses only one variant — no inconsistency to flag.

---

## 4. Stale TODO / FIXME / placeholders

**4 TODO comments — all editorial, intentional, addressed to "editor".**

| File:line | Comment |
|---|---|
| `02-bivariate.qmd:866` | `<!-- TODO(editor): Topic 2 lecture notes also cover … residual diagnostics … nonlinear models linearised by logs … consider whether to surface them in an appendix … -->` |
| `02-bivariate.qmd:868` | `<!-- TODO(editor): citation [@wooldridge2020] is reused from the Econometrics I book; confirm or replace once references.bib for TC1 is finalised. -->` |
| `04-random-variables.qmd:362` | `<!-- TODO: Markov's inequality is not stated in the Topic 4 lecture notes (only Chebyshev). If the editor wants it included … -->` |
| `04-random-variables.qmd:693` | Prose bullet ending "… TODO for editor." (visible to readers, not an HTML comment) |

**Recommendation:** the first three are HTML comments — invisible in the rendered book — and can stay until decisions are made. The fourth (`04-random-variables.qmd:693`) is a **plain-text bullet visible to readers** that says "TODO for editor"; this leaks the authoring process and should be rewritten before publication.

No `FIXME`, no `XXX`, no `???`, no `[insert …]`, no `<placeholder>`.

### Empty math blocks
**None.** The multiline regex flagged six `$$ \n \n $$` patterns but inspection of each (01:206–212, 01:949–954, 02:288–290, 02:383–385, 04:258–260, 07:254–256) shows **two separate populated math blocks** with a blank line between them. Stylistically intentional.

---

## 5. Capitalisation of distribution names

**Pattern is consistent within `05-distributions.qmd`:**

- **Capitalised** (proper-noun style): `Bernoulli`, `Poisson`, `Hypergeometric` (in headings such as `## 5.4 The Hypergeometric distribution`).
- **Lowercase** (common-noun style): `binomial`, `geometric`, `negative binomial`, `normal`, `discrete uniform` when used as ordinary adjectives ("the binomial PMF", "the geometric distribution", "a normal distribution").

This matches conventional statistical usage (eponymous names — Bernoulli, Poisson, Gauss-derived → capital; descriptive names — binomial, geometric → lowercase) and is internally consistent. No mixing within the same role.

`Theorem / Definition / Example` in callout headings: all Title-case, **112 occurrences, 0 lowercase**. Consistent.

---

## 6. Heading case

Chapter `##` headings and callout `##` headings both follow **sentence case for prose headings** (e.g., "Motivating empirical question", "When does the binomial apply?") and **Title-case nouns for callout types** (Definition, Example, Theorem, Common mistake). One outlier: `05-distributions.qmd:93` `## Three Bernoulli scenarios` — this *is* sentence case (Bernoulli is a proper noun). Not a flag.

No inconsistency detected.

---

## 7. Verdict

**Cosmetic, not blocking.**

The TC1 English source is in excellent shape for publication on the spelling/translation axis:
- 0 English typos in the canonical list (plus the broader net we ran).
- British spelling is universally adopted; the single `license` in `index.qmd` is the CC name and acceptable.
- No Spanish leakage in prose. Italicised Spanish proper nouns (Málaga, IPC, SMI, IVE source) are intentional pedagogical anchors and well-handled.
- 4 TODO comments, of which 3 are invisible HTML comments and 1 (`04-random-variables.qmd:693`) is reader-visible and worth a 30-second prose tidy.
- No empty math blocks, no doubled words, no contraction errors.
- Distribution-name capitalisation and callout-type capitalisation are both internally consistent.

**Two genuine, low-effort fixes worth making before v1.0:**
1. `04-random-variables.qmd:693` — rewrite the public-facing "TODO for editor" sentence into neutral closing prose (or move to a comment).
2. `05-distributions.qmd:470` — R-code comment "`# Loteria 6/49`" → spell as English "`# Lottery 6/49`" or restore the accent "`# Lotería 6/49`".

Everything else can ship.
