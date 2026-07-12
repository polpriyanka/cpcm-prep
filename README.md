# CPCM Prep

Study materials for the NCMA **Certified Professional Contracts Manager** exam.

## Contents

| File | What it is |
|---|---|
| `index.html` | Interactive study hub — question bank, deficiency log, CPE ledger. Open in a browser. |
| `STUDY-GUIDE.md` | The written curriculum. All 7 CMBOK competencies plus the federal statutes cross-cut. |

## Using the hub

Open `index.html` in any browser. No build step, no dependencies.

**Tabs:**
- **Status** — accuracy by competency, next recommended action, CPE runway
- **Drill** — 48 questions, filterable by domain
- **Deficiency Log** — every question you've missed, held open until you get it right
- **CPE Ledger** — tracks progress toward the 120 hours required to apply
- **Exam Facts** — fees, thresholds, sequence to certification

> **Note on persistence:** progress saving uses a storage API that only exists inside the Claude artifact runtime. Opened as a local file, the hub works fully but **does not save between sessions**. See *Roadmap* below.

## Study loop

1. Read a competency in `STUDY-GUIDE.md`
2. Drill that domain in the hub
3. Anything you miss lands in the Deficiency Log
4. Re-read only the sections you missed
5. Clear the log. Repeat.

The `⚠ Trap` markers in the study guide flag places where real-world experience actively misleads you on the exam. Those are the highest-value re-reads.

## Status

- **CPE:** 81 / 120 hours banked. 39 remaining before the application can be submitted.
- **Source of truth:** CMBOK 7th Edition. These materials are scaffolding, not a substitute.

## Roadmap

- [ ] Swap the artifact storage API for `localStorage` so progress persists when run locally
- [ ] Expand question bank past 48
- [ ] Deepen the *Pricing & Cost Analysis* material
- [ ] Add a timed mock-exam mode
- [ ] Itemize the 81 baseline CPE hours with documentation (NCMA audits a percentage of applications)

## License

Private study material. Not for redistribution.
