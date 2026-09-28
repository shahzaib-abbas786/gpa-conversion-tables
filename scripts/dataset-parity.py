#!/usr/bin/env python3
"""Dataset parity: JSON and CSV must carry the same rules, in the same order,
with matching shared values, and zero empty/null cells (a null reverse_formula
is valid only when a reverse_note explains the non-invertibility)."""
import csv, json, sys

d = json.load(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "..", "gpa-conversion-tables.json")))
rows = list(csv.DictReader(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "..", "gpa-conversion-tables.csv"))))
errors = []

jids = [c["id"] for c in d["conversions"]]
cids = [r["id"] for r in rows]
if jids != cids:
    errors.append(f"ID order mismatch: JSON {jids} vs CSV {cids}")

def wordcount(s): return len(s.split())

for c, r in zip(d["conversions"], rows):
    rid = c["id"]
    # shared scalar values
    for k in ("institution", "scale", "formula", "notes"):
        if (c.get(k) or "") != (r.get(k) or ""):
            errors.append(f"{rid}: {k} mismatch JSON={c.get(k)!r} CSV={r.get(k)!r}")
    if (c.get("source_page") or "") != (r.get("source_page") or ""):
        errors.append(f"{rid}: source_page mismatch")
    if (c.get("reverse_note") or "") != (r.get("reverse_note") or ""):
        errors.append(f"{rid}: reverse_note mismatch")
    jrf = c.get("reverse_formula")
    crf = r.get("reverse_formula")
    if jrf is None and crf != "NOT-INVERTIBLE":
        errors.append(f"{rid}: JSON reverse_formula null must mirror as NOT-INVERTIBLE in CSV")
    if jrf is not None and jrf != crf:
        errors.append(f"{rid}: reverse_formula mismatch {jrf!r} vs {crf!r}")
    # worked example
    ex = c.get("example", {})
    ei = ex.get("cgpa", ex.get("grade", ex.get("input_score", "")))
    eo = ex.get("percentage", ex.get("german_grade", ""))
    if str(ei) != r["example_input"] or str(eo) != r["example_output"]:
        errors.append(f"{rid}: example mismatch JSON=({ei},{eo}) CSV=({r['example_input']},{r['example_output']})")

# zero empty/null cells
for c in d["conversions"]:
    for k in ("id","institution","scale","formula","notes","source_page","reverse_formula"):
        v = c.get(k)
        if v is None or (isinstance(v, str) and not v.strip()):
            if k == "reverse_formula" and c.get("reverse_note"):
                continue  # documented non-invertible
            errors.append(f"{c['id']}: empty/null JSON field {k}")
    if not c.get("example"):
        errors.append(f"{c['id']}: missing example")
for r in rows:
    for k, v in r.items():
        if not (v or "").strip():
            # structural exemption: reverse_note exists only where the rule is
            # NOT invertible (mirrors the JSON, where reverse_note is absent)
            if k == "reverse_note" and r.get("reverse_formula") != "NOT-INVERTIBLE":
                continue
            errors.append(f"{r['id']}: empty CSV cell {k}")

# FAQ-style sanity: notes within 12 words for the 12 filled-this-session cells
LONG = {"vtu", "sppu"}  # pre-existing longer notes kept verbatim
for c in d["conversions"]:
    if c["id"] not in LONG and wordcount(c["notes"]) > 12:
        errors.append(f"{c['id']}: notes exceed 12 words ({wordcount(c['notes'])})")

if errors:
    print("PARITY: FAIL")
    for e in errors: print(" -", e)
    sys.exit(1)
print(f"PARITY: PASS — {len(jids)} rules, identical ID order, all shared values match, 0 empty cells (JSON+CSV)")
