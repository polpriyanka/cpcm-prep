# CPCM Prep

Study materials for the NCMA **Certified Professional Contracts Manager** exam.

Live at: **contractmanagementncma.com** (once DNS + Pages are wired up — see below)

## Contents

| File | What it is |
|---|---|
| `index.html` | Interactive study hub — question bank, deficiency log, CPE ledger. Open in a browser or serve as the site. |
| `STUDY-GUIDE.md` | The written curriculum. All 7 CMBOK competencies plus the federal statutes cross-cut. |
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
- **Status** — accuracy by competency, next recommended action, CPE runway
- **Drill** — 48 questions, filterable by domain
- **Deficiency Log** — every question you've missed, held open until you get it right
- **CPE Ledger** — tracks progress toward the 120 hours required to apply
- **Exam Facts** — fees, thresholds, sequence to certification

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
- [ ] Expand question bank past 48
- [ ] Deepen the *Pricing & Cost Analysis* material
- [ ] Add a timed mock-exam mode
- [ ] Itemize the 81 baseline CPE hours with documentation (NCMA audits a percentage of applications)

## License

Private study material. Not for redistribution.
