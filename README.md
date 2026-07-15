# CPCM Prep

Study materials for the NCMA **Certified Professional Contracts Manager** exam.

Live at: **contractmanagementncma.com**

Question bank current as of 2026-07-13 (399 questions); run the audit checklist before trusting counts in this file.

## Contents

| File | What it is |
|---|---|
| `index.html` | Interactive study hub — question bank, mock exam, deficiency log, CPE ledger. Open in a browser or serve as the site. |
| `audio-lessons.js` | Twelve spoken-narration lessons for the Audio Lessons tab (Web Speech API). |
| `study-guide.js` | The study guide rendered for the in-app **Study Guide** tab. Auto-generated from `STUDY-GUIDE.md` by `gen-guide.py` — re-run after editing the guide. |
| `STUDY-GUIDE.md` | The written curriculum. All CMBOK competencies, framework/foundations, protests and financing mechanics, plus the federal statutes cross-cut. |
| `CNAME` | GitHub Pages custom domain config — points the repo at `contractmanagementncma.com`. |

## Deploying to contractmanagementncma.com

The domain's future scope isn't decided yet — could stay just the study hub, could grow into a publishing site later (publishing articles on contract management counts toward CPE, which is directly relevant here). Deploying at the **root domain** now keeps both options open: expanding later just means adding paths, not restructuring.

**1. DNS — at your registrar, set:**

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

(GitHub Pages' four apex-domain IPs. If the registrar supports `ALIAS`/`ANAME` instead, that also works and is sometimes cleaner.)

**2. GitHub Pages — after `gh repo create --push`:**

```bash
gh api -X POST repos/:owner/cpcm-prep/pages -f source.branch=main -f source.path=/
```

Or via the web UI: repo → Settings → Pages → Source: `main` / root. The `CNAME` file already in this repo tells Pages the custom domain; GitHub will detect it automatically once DNS resolves.

**3. Verify** — `dig contractmanagementncma.com` should return the four IPs above once DNS propagates (can take a few hours).

## Using the hub

Open `index.html` in any browser. No build step, no dependencies. Progress saves via `localStorage` when run outside the Claude artifact runtime (i.e. once deployed here), so it persists across visits.

**Tabs:**
- **Status** — exam-readiness gate (three criteria, stricter than the 72.2% pass line), accuracy by competency, next recommended action, CPE runway, progress backup (export/import)
- **Drill** — 399 questions, filterable by domain
- **Mock Exam** — blueprint-weighted draws (20 up to full-length 180), real-exam pacing timer, scenario markers, per-question pacing report
- **Deficiency Log** — every question you've missed, held open until you get it right, with miss-reason tagging (knowledge / misread / second-guessed)
- **Study Guide** — the full written curriculum rendered in-app, with a jump-to-section table of contents and section filter
- **Audio Lessons** — twelve spoken lessons (~92 min) via the device's text-to-speech
- **CPE Ledger** — tracks progress toward the 120 hours required to apply
- **Exam Facts** — fees, thresholds, the official exam blueprint, sequence to certification

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

- [ ] Decide domain scope — study hub only, or expand into a CPE-eligible publishing site
- [ ] Itemize the 81 baseline CPE hours with documentation (NCMA audits a percentage of applications)
- [ ] CPE article pipeline — published writing on contract management earns CPE hours
- [ ] Periodic re-audit after each content merge (counts, answer-position balance, scenario share, guide/bank/audio sync)

## License

Private study material. Not for redistribution.
