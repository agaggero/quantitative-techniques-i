"""Audit TC1 chapter .qmd files for callout block formatting issues."""
import re
from pathlib import Path

CHAPTERS_DIR = Path(r"G:\My Drive\UGR\GRADO\Asignaturas\TC1\BOOK_PROJECT\en\chapters")
files = sorted(CHAPTERS_DIR.glob("*.qmd"))

# Canonical callout types
CANONICAL_TYPES = {"callout-note", "callout-warning", "callout-tip"}

# Regex patterns
RE_CALLOUT_OPEN = re.compile(r'^:::\s*\{\.(callout-[a-z-]+)(.*)\}\s*$')
RE_FENCE_CLOSE = re.compile(r'^:::\s*$')
RE_FENCE_OPEN_ANY = re.compile(r'^:::\s*\{')  # any opener with attributes
RE_FENCE_NO_ATTRS = re.compile(r'^:::\s*$')

# MCQ option detection: lines starting with "- A.", "- B.", "- C.", "- D."
RE_OPT_A = re.compile(r'^-\s+A\.\s')
RE_OPT_B = re.compile(r'^-\s+B\.\s')
RE_OPT_C = re.compile(r'^-\s+C\.\s')
RE_OPT_D = re.compile(r'^-\s+D\.\s')

# Plain (non-bullet) option detection
RE_PLAIN_A = re.compile(r'^A\.\s')
RE_PLAIN_B = re.compile(r'^B\.\s')
RE_PLAIN_C = re.compile(r'^C\.\s')
RE_PLAIN_D = re.compile(r'^D\.\s')

# Display math: $$ on its own line
RE_DISPLAY_MATH_OPEN = re.compile(r'^\$\$\s*$')
RE_DISPLAY_MATH_INLINE = re.compile(r'\$\$.+\$\$')  # both delimiters on same line

# Exercise star detection
RE_EXERCISE_STAR1 = re.compile(r'^###\s+Exercise.*?(?<!★)★(?!★)')  # single star (not ★★ or ★★★)


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    return lines


def audit_file(path: Path):
    lines = parse_file(path)
    n = len(lines)
    results = {
        "path": path.name,
        "mcq_blocks": [],          # list of dicts with line, ok, reason
        "math_in_callouts": [],    # list of (line, callout_type)
        "noncanonical_types": [],  # list of (line, type)
        "open_count": 0,
        "close_count": 0,
        "star_solutions": [],      # list of (exercise_line, solution_line, in_collapse_bool, reason)
    }

    # Walk through and identify callout blocks using a stack
    stack = []  # stack of (line_idx, type, attrs, start_line_idx)
    callout_blocks = []  # list of dicts: {start, end, type, attrs, content_lines}

    for i, line in enumerate(lines):
        m_open = RE_CALLOUT_OPEN.match(line)
        m_close = RE_FENCE_CLOSE.match(line)
        m_any_open = RE_FENCE_OPEN_ANY.match(line)

        if m_open:
            ctype = m_open.group(1)
            attrs = m_open.group(2)
            stack.append({"line": i, "type": ctype, "attrs": attrs.strip()})
            results["open_count"] += 1
            if ctype not in CANONICAL_TYPES:
                results["noncanonical_types"].append((i+1, ctype))
        elif m_any_open:
            # generic fenced div opener (not a callout) — push to stack as non-callout
            stack.append({"line": i, "type": None, "attrs": None})
        elif m_close:
            results["close_count"] += 1
            if stack:
                block = stack.pop()
                if block["type"] is not None:
                    callout_blocks.append({
                        "start": block["line"],
                        "end": i,
                        "type": block["type"],
                        "attrs": block["attrs"],
                        "content_lines": lines[block["line"]+1 : i],
                    })

    # MCQ analysis: callout-tip with collapse="true"
    for block in callout_blocks:
        if block["type"] != "callout-tip":
            continue
        if 'collapse="true"' not in block["attrs"]:
            continue
        # This is a self-check MCQ candidate (or could be a solution callout)
        # Check whether it contains MCQ options (A., B., C., D.)
        content = block["content_lines"]
        has_a_bullet = any(RE_OPT_A.match(l) for l in content)
        has_b_bullet = any(RE_OPT_B.match(l) for l in content)
        has_c_bullet = any(RE_OPT_C.match(l) for l in content)
        has_d_bullet = any(RE_OPT_D.match(l) for l in content)

        has_a_plain = any(RE_PLAIN_A.match(l) for l in content)
        has_b_plain = any(RE_PLAIN_B.match(l) for l in content)
        has_c_plain = any(RE_PLAIN_C.match(l) for l in content)
        has_d_plain = any(RE_PLAIN_D.match(l) for l in content)

        has_options_bullet = has_a_bullet and has_b_bullet and has_c_bullet and has_d_bullet
        has_options_plain = has_a_plain and has_b_plain and has_c_plain and has_d_plain

        is_mcq = has_options_bullet or has_options_plain

        if is_mcq:
            ok = has_options_bullet and not (has_a_plain and not has_a_bullet)
            results["mcq_blocks"].append({
                "start_line": block["start"] + 1,
                "ok": has_options_bullet,
                "has_plain_only": has_options_plain and not has_options_bullet,
                "missing": [
                    name for name, present in [("A", has_a_bullet), ("B", has_b_bullet),
                                                 ("C", has_c_bullet), ("D", has_d_bullet)]
                    if not present
                ],
            })

    # Display math inside callouts
    for block in callout_blocks:
        content = block["content_lines"]
        start_offset = block["start"] + 1
        in_math = False
        for j, l in enumerate(content):
            if RE_DISPLAY_MATH_OPEN.match(l):
                if not in_math:
                    results["math_in_callouts"].append({
                        "callout_line": block["start"] + 1,
                        "math_line": start_offset + j + 1,
                        "callout_type": block["type"],
                    })
                    in_math = True
                else:
                    in_math = False
            elif RE_DISPLAY_MATH_INLINE.search(l):
                results["math_in_callouts"].append({
                    "callout_line": block["start"] + 1,
                    "math_line": start_offset + j + 1,
                    "callout_type": block["type"],
                    "note": "inline-form $$...$$",
                })

    # ★ exercise solutions
    # Find each "### Exercise N.N ★ — ..." (single star) heading and check if
    # the next callout block in this file (before next exercise heading) is a
    # collapse=true callout.
    exercise_indices = []  # list of (line_idx, heading)
    for i, line in enumerate(lines):
        m = re.match(r'^###\s+Exercise\s+\d+\.\d+\s+(★+)', line)
        if m:
            exercise_indices.append((i, m.group(1)))

    # For each star-1 exercise, find the next callout in its range
    for idx, (line_i, stars) in enumerate(exercise_indices):
        end_i = exercise_indices[idx+1][0] if idx+1 < len(exercise_indices) else len(lines)
        if stars != "★":
            continue  # only star-1 expected to have inline solution
        # Find a callout that opens between line_i and end_i
        found_solution = False
        for b in callout_blocks:
            if line_i < b["start"] < end_i:
                # check if it's titled "Solution" or similar
                # First content line might have heading "## Solution"
                content_lower = "\n".join(b["content_lines"][:5]).lower()
                if "solution" in content_lower:
                    found_solution = True
                    is_tip_collapse = (b["type"] == "callout-tip" and
                                         'collapse="true"' in b["attrs"])
                    results["star_solutions"].append({
                        "exercise_line": line_i + 1,
                        "solution_line": b["start"] + 1,
                        "callout_type": b["type"],
                        "is_collapse": is_tip_collapse,
                        "attrs": b["attrs"],
                    })
                    break
        if not found_solution:
            results["star_solutions"].append({
                "exercise_line": line_i + 1,
                "solution_line": None,
                "callout_type": None,
                "is_collapse": False,
                "attrs": None,
                "note": "no solution callout found",
            })

    return results


# Run for each file
all_results = [audit_file(f) for f in files]

# Generate report
out = []
out.append("# TC1 Callout & MCQ Formatting Audit\n")
out.append("**Audit date:** 2026-05-19  ")
out.append("**Files audited:** `BOOK_PROJECT/en/chapters/*.qmd`\n")
out.append("---\n")

# Summary table
total_mcq = sum(len(r["mcq_blocks"]) for r in all_results)
total_mcq_bad = sum(sum(1 for m in r["mcq_blocks"] if not m["ok"]) for r in all_results)
total_math_in_callout = sum(len(r["math_in_callouts"]) for r in all_results)
total_noncanonical = sum(len(r["noncanonical_types"]) for r in all_results)

out.append("## Summary\n")
out.append(f"- **Files audited:** {len(files)}")
out.append(f"- **Total MCQ blocks (callout-tip + collapse=true with options):** {total_mcq}")
out.append(f"- **MCQ blocks NOT in bullet-list format:** {total_mcq_bad}")
out.append(f"- **Display-math-in-callout instances:** {total_math_in_callout}")
out.append(f"- **Non-canonical callout types:** {total_noncanonical}")
out.append("")

# Unclosed callouts table
out.append("### Open/Close count per file\n")
out.append("| File | `:::{...}` openers | `:::` closers (bare) | Diff |")
out.append("|---|---:|---:|---:|")
for r in all_results:
    diff = r["open_count"] - r["close_count"]
    out.append(f"| {r['path']} | {r['open_count']} | {r['close_count']} | {diff:+d} |")
out.append("")
out.append("(Note: openers include only `.callout-…` blocks. Closers count bare `:::` lines, which include closers for non-callout fenced divs too. A negative diff is normal if the file uses non-callout fenced divs.)\n")
out.append("---\n")

# Per-file details
for r in all_results:
    out.append(f"## {r['path']}\n")
    out.append(f"- Callout openers: {r['open_count']}")
    out.append(f"- Bare `:::` closers: {r['close_count']}")
    out.append("")

    # MCQ
    out.append("### MCQ blocks (`.callout-tip collapse=\"true\"` with A/B/C/D)\n")
    if not r["mcq_blocks"]:
        out.append("None.")
    else:
        for m in r["mcq_blocks"]:
            status = "OK (bullet list)" if m["ok"] else "FAIL (plain lines, no bullets)"
            out.append(f"- Line {m['start_line']}: **{status}**" +
                       (f" — missing bullets: {m['missing']}" if m["missing"] else ""))
    out.append("")

    # Math in callout
    out.append("### Display math (`$$...$$`) inside callouts\n")
    if not r["math_in_callouts"]:
        out.append("None.")
    else:
        for m in r["math_in_callouts"]:
            note = m.get("note", "")
            out.append(f"- Callout at line {m['callout_line']} ({m['callout_type']}) → math at line {m['math_line']}" +
                       (f" [{note}]" if note else ""))
    out.append("")

    # Non-canonical types
    out.append("### Non-canonical callout types\n")
    if not r["noncanonical_types"]:
        out.append("None — all callouts are `callout-note`, `callout-warning`, or `callout-tip`.")
    else:
        for line, t in r["noncanonical_types"]:
            out.append(f"- Line {line}: `{t}`")
    out.append("")

    # Star solutions
    out.append("### ★ exercise solutions\n")
    if not r["star_solutions"]:
        out.append("No ★ (single-star) exercises detected.")
    else:
        for s in r["star_solutions"]:
            if s.get("note"):
                out.append(f"- Exercise at line {s['exercise_line']}: **{s['note']}**")
            elif not s["is_collapse"]:
                out.append(f"- Exercise at line {s['exercise_line']} → solution at line {s['solution_line']}: **FAIL** — type `{s['callout_type']}`, attrs `{s['attrs']}` (not `collapse=\"true\"`)")
            else:
                out.append(f"- Exercise at line {s['exercise_line']} → solution at line {s['solution_line']}: OK (`callout-tip collapse=\"true\"`)")
    out.append("")
    out.append("---\n")

# Final verdict
out.append("## Verdict\n")
if total_mcq_bad == 0 and total_math_in_callout == 0:
    out.append("**CLEAN.** No MCQ formatting bugs detected; no display math inside callouts.")
elif total_mcq_bad == 0:
    out.append("**COSMETIC.** No MCQ bullet bug. Some display-math-in-callout instances exist (style-guide §7 prefers them outside); these may render fine but are worth a manual look.")
else:
    out.append(f"**BLOCKING.** {total_mcq_bad} MCQ block(s) have options as plain lines, which Markdown will collapse into one paragraph. Fix before publishing.")

# Write
report_path = Path(r"G:\My Drive\UGR\GRADO\Asignaturas\TC1\BOOK_PROJECT\_audit\03-callouts-mcq.md")
report_path.write_text("\n".join(out), encoding="utf-8")
print(f"Wrote: {report_path}")
print(f"MCQ blocks total: {total_mcq}; bad: {total_mcq_bad}")
print(f"Math in callouts: {total_math_in_callout}")
print(f"Non-canonical types: {total_noncanonical}")
for r in all_results:
    diff = r["open_count"] - r["close_count"]
    print(f"  {r['path']}: open={r['open_count']} close={r['close_count']} diff={diff:+d}")
