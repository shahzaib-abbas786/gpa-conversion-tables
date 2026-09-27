# gpa-conversion-tables

Official CGPA/GPA → percentage conversion formulas for CBSE, VTU, SPPU, Anna University, GTU, KTU, MAKAUT, Mumbai University, AKTU, Delhi University, JNTUH, HEC Pakistan and the German modified Bavarian formula — in one machine-readable dataset.

## How to read this

Each row is one published conversion rule. `formula` takes a **CGPA on the stated scale** and returns a **percentage** (the German row returns a German grade 1.0–5.0, where 1.0 is best and 4.0 is a pass). Every rule carries a worked example and a `source_page` link to the page that documents and calculates it. Universities change schemes between batches — treat this table as a reference, and your university's exam cell as the authority for official paperwork.

## Conversion rules

| Institution | Scale | Formula | Example (input → output) |
|---|---|---|---|
| CBSE (India, class X/XII) | 10-pt CGPA | % = CGPA × 9.5 | 8.0 → 76.0% |
| VTU (CBCS 2021–22 onwards) | 10-pt CGPA | % = (CGPA − 0.75) × 10 | 8.0 → 72.5% |
| VTU (older schemes) | 10-pt CGPA | % = CGPA × 10 | 8.0 → 80.0% |
| SPPU (Pune University, Circular No. 322/2020) | 10-pt CGPA | % = (CGPA − 0.75) × 10 | 8.0 → 72.5% |
| Anna University | 10-pt CGPA | % = CGPA × 10 − 7.5 | 8.0 → 72.5% |
| GTU (Gujarat Technological University) | 10-pt CGPA | % = (CGPA − 0.5) × 10 | 8.0 → 75.0% |
| KTU (Kerala Technological University) | 10-pt CGPA | % = (CGPA − 0.5) × 10 | 8.0 → 75.0% |
| MAKAUT | 10-pt CGPA | % = (CGPA − 0.5) × 10 | 8.0 → 75.0% |
| Mumbai University | 10-pt CGPA | % = CGPA × 7.1 + 11 | 8.0 → 67.8% |
| AKTU | 10-pt CGPA | % = (CGPA − 0.75) × 10 | 8.0 → 72.5% |
| Delhi University (CBCS) | 10-pt CGPA | % = CGPA × 9.5 | 8.0 → 76.0% |
| JNTU Hyderabad (R18+) | 10-pt CGPA | % = (CGPA − 0.5) × 10 | 8.0 → 75.0% |
| HEC Pakistan | 4.0 CGPA | % = (CGPA ÷ 4) × 100 | 3.2 → 80.0% |
| Germany / EU (Bologna) — ECTS bands | ECTS letter | A → 93%, B → 83%, C → 73%, D → 63%, E → 55%, F → 30% | B → 83% |
| Germany (modified Bavarian)† | any score | grade = 1 + 3 × (Nmax − Nd) ÷ (Nmax − Nmin) | 86/100, pass 50 → 1.84 |

†The modified-Bavarian row is a general German convention (Uni-Assist), not documented on a dedicated StudentKit page — every other row links to the page that calculates it.

The modified-Bavarian row: `Nd` is the score to convert, `Nmax` the best achievable score and `Nmin` the minimum passing score of the source system (e.g. 100 and 50 for percentages). 1.0 is the best German grade; 4.0 is a pass.

## Files

- `gpa-conversion-tables.json` — machine-readable (15 rules, worked examples, source links)
- `gpa-conversion-tables.csv` — the same data, spreadsheet-friendly

## Calculators

Every rule above runs live, free and without an account at:

- StudentKit: https://www.studentkit.tech/
- CGPA → Percentage calculator (all university formulas side by side): https://www.studentkit.tech/tools/cgpa-to-percentage-calculator

## Tags

`gpa` · `cgpa` · `education` · `conversion` · `dataset`

## Licence

MIT — use it, fork it, cite it.
