# JU EE 3rd Year 1st Sem Question Bank — Progress & Handoff (`qbank_progress.md`)

## Local status on 27 November 2026

All six subjects are populated in the local 2022–2026 database. This pass added 16 source papers and 313 syllabus-mapped question entries.

| Added subject | Papers | Question entries |
|---|---:|---:|
| Electrical Machine III | 5 | 116 |
| Linear Control System | 5 | 98 |
| Power Electronics | 6 | 99 |

The rebuilt database has 33 paper entries, including the existing annotated PLM paper. The flat database contains 694 questions and 13 image references.

- The 2025 Linear Control System scan lacks printed pages 4–5. The hub includes the available pages and flags the gap.
- Power Electronics 2022 contains only Part II, and 2023 contains only Part I. The 2024 regular paper's Part I heading says 2023, while its reference and Part II say 2024. The hub records these differences.

The original handoff below is retained as history.

## Original handoff

**Repository:** `https://github.com/hunkycolony-003/ju-sem5-exampaper-hub` (branch `main`, latest pushed commit before this doc: `9f8ea5f`)  
**Local Repo Path:** `/Users/soumodeep/.gemini/antigravity/playground/white-prominence/ju-sem5-exampaper-hub`  
**Source PDFs Root:** `/Users/soumodeep/Resources/EE_3rd_Year_1st_Sem`  
**Pre-rendered PNG / Local OCR Cache:** `/Users/soumodeep/.gemini/antigravity/brain/1adc9881-597c-4fe9-b71d-a5afce869ed4/scratch/ocr_png/`  
**Compiled Local Vision OCR Binary (macOS):** `/Users/soumodeep/.gemini/antigravity/brain/1adc9881-597c-4fe9-b71d-a5afce869ed4/scratch/vision_ocr`

---

## 1. Current Completion Status

**Current DB Totals (`data/index.json`, `data/questions.json`, `data/images.json`):**
- **Subjects Populated:** `3 / 6` (`pspd`, `ispm`, `plm`)
- **Papers Indexed:** `17` (`2022–2026` only; pre-2022 papers intentionally excluded per user instruction)
- **Total Flat Questions (`data/questions.json`):** `381` (plus `14` annotated/solved questions in `data/paper_2023.json` preserved for PLM `2023 (Solved)`)
- **Total Question Images (`data/images.json`):** `5` raster PNG crops (`pspd`)

### Subject-by-Subject Status

| # | Subject ID | Subject Name & Paper Code | Status | Papers (`>= 2022`) | Qs | Images |
|---|---|---|---|---|---|---|
| 1 | `pspd` | Power System Planning & Design (`Ex/EE/PC/B/T/312`) | **DONE & PUSHED** (`38f380e`) | `2026` (30q, 2 imgs), `2025` (28q, 1 img), `2024` (28q, 1 img), `2024s` (23q, 0 imgs), `2023` (31q, 1 img) | 140 | 5 |
| 2 | `ispm` | Introduction to Statistical and Probabilistic Methods (`Ex/EE/PC/B/T/315`) | **DONE & PUSHED** (`9f8ea5f`) | `2026` (22q), `2025` (23q), `2024` (20q), `2024s` (22q), `2023` (26q), `2023s` (20q), `2022` (20q) + 9 Z-tables in `sharedNote` | 153 | 0 |
| 3 | `em3` | Electrical Machine - III (`Ex/EE/PC/B/T/311`) | **READY FOR OCR (PNG + Vision OCR DONE)** | Rendered & Vision-OCR'd at `scratch/ocr_png/em3/{2026,2025,2024,2024s,2023}/` (5 papers × 4 pages) | — | — |
| 4 | `lcs` | Linear Control System (`Ex/EE/PC/B/T/313`) | **PENDING** | See Section 2 for exact PDFs | — | — |
| 5 | `pe` | Power Electronics (`Ex/EE/PC/B/T/314`) | **PENDING** | See Section 2 for exact PDFs | — | — |
| 6 | `plm` | Prog. Logic & Microcontroller (`Ex/EE/PC/B/T/316`) | **DONE & PUSHED** (`57bd3c1`) | `2025` (27q), `2024` (23q), `2024s` (18q), `2023 (Solved)` (`paper_2023.json`, 14q), `2023` (20q) | 88 (+14 solved) | 0 |

---

## 2. Exact Source PDFs Remaining (Strictly `>= 2022`, Deduplicated by MD5)

### Subject 3: `em3` — `3. Electrical Machine - III` (**Next Up**)
All 5 unique `>= 2022` PDFs are **already rendered to 200 DPI PNGs and Vision-OCR'd**:
- `2026` (`sortKey: 2026.0`, `yearLabel: "2026"`, `Regular`): `2026 - Electrical Machines III.pdf` (`4` pages) → `scratch/ocr_png/em3/2026/{page-*.png,ocr.txt}`
- `2025` (`sortKey: 2025.0`, `yearLabel: "2025"`, `Regular`): `2025 - Electrical Machines - III.pdf` (`4` pages; `2025 - Electrical Machines III.pdf` has identical MD5 `8ec34861`) → `scratch/ocr_png/em3/2025/`
- `2024` (`sortKey: 2024.2`, `yearLabel: "2024"`, `Regular`): `2024 - Electrical Machines III.pdf` (`4` pages) → `scratch/ocr_png/em3/2024/`
- `2024s` (`sortKey: 2024.1`, `yearLabel: "2024 (S)"`, `Supplementary`): `2024 - Electrical Machines III S.pdf` (`4` pages) → `scratch/ocr_png/em3/2024s/`
- `2023` (`sortKey: 2023.0`, `yearLabel: "2023"`, `Regular`): `2023 - Electrical Machines III.pdf` (`4` pages) → `scratch/ocr_png/em3/2023/`

### Subject 4: `lcs` — `4. Linear Control System`
Folder: `/Users/soumodeep/Resources/EE_3rd_Year_1st_Sem/4. Linear Control System`
- `2026`: `2026 - Linear Control System.pdf`
- `2025`: `2025 - Linear Control System.pdf`
- `2024`: `2024 - Linear Control System.pdf`
- `2024s`: `2024 - Linear Control System S.pdf`
- `2023`: `2023 - Linear Control System.pdf`
*(Note: skip study guides/compendiums/combined PDFs.)*

### Subject 5: `pe` — `5. Power Electronics`
Folder: `/Users/soumodeep/Resources/EE_3rd_Year_1st_Sem/5. Power Electronics`
- `2026`: `2026 - Power Electronics.pdf`
- `2025`: `2025 - Power Electronics.pdf`
- `2024`: `2024 - Power Electronics.pdf`
- `2024s`: `2024 - Power Electronics S.pdf`
- `2023`: `2023 - Power Electronics.pdf`
- `2022`: `2022 - Power Electronics.pdf`
*(Verify cover year & refCode of `2022`..`2026` during Vision OCR step.)*

---

## 3. Mandatory Execution Workflow (Follow Strictly to Save Quota & Avoid Safety Filters)

1. **One Subject at a Time, Queued Sequential Hydrogen Workers (`gemini-4-hydrogen-high`):**
   - Do **NOT** spawn workers for multiple subjects or all papers in parallel (conserves AI quota).
   - Use `/swarm` with **only `model: "gemini-4-hydrogen-high"`**.
   - Split a subject into at most 1 active queued worker at a time (e.g. `em3-ocr` for 3–5 papers, or Batch 1 + Batch 2 sequentially, killing the finished worker before spawning the next, then `em3-auditor`).

2. **Local Prep First (0 AI Quota + Avoids Copyright Recitation Filter):**
   - Render each PDF to 200 DPI PNGs (`pdftoppm -png -r 200`) and run the compiled macOS Apple Vision OCR binary:
     `/Users/soumodeep/.gemini/antigravity/brain/1adc9881-597c-4fe9-b71d-a5afce869ed4/scratch/vision_ocr <page-*.png> > ocr.txt`
   - Inside worker prompts, instruct workers to **build each JSON via a Python script reading/cleaning `<key>/ocr.txt`** alongside visual `read_file` verification of `page-*.png` (never echo large verbatim textbook wordings straight in a single LLM tool payload, which can trigger Gemini's recitation filter).

3. **JSON & Image Cropping Rules:**
   - **Reference Schema:** `data/papers/pspd/2026.json`
   - Output papers to: `data/papers/<subjectId>/<key>.json`
   - Crop **ONLY printed diagrams/schematics/plots/circuits** (ignore student handwriting, circled question numbers, margin notes, or scratches!) using Python PIL from 200 DPI `page-*.png` into:
     `data/assets/<subjectId>/<subjectId>-<key>/fig_<slug>.png`
   - Inspect every cropped PNG via `read_file` to verify no labels are cut off.
   - Reference cropped images in each question row:
     ```json
     "images": [
       {
         "src": "data/assets/<subjectId>/<subjectId>-<key>/fig_<slug>.png",
         "caption": "Fig. 1: ..."
       }
     ]
     ```
   - **Keep tables cleanly as HTML `<table>`** inside `textLatex` (or `sharedNote` for paper-wide reference tables).
   - **Prevent horizontal KaTeX overflow:** Do NOT wrap long comma-separated numeric datasets inside a single inline `$...$` span (`$340, 356, ...$`); keep long datasets as normal text numbers (`340, 356, ...`) so they line-wrap cleanly inside `.question-row`. Wrap mathematical variables/expressions individually (`$\mu = 350$`, etc.) and keep `$` delimiters balanced.

4. **Rebuild All Databases + Verify + Push:**
   After auditing each subject:
   ```bash
   python3 /Users/soumodeep/.gemini/antigravity/playground/white-prominence/ju-sem5-exampaper-hub/data/rebuild_db.py
   ```
   This atomically regenerates:
   - `data/index.json` (master manifest, enforces `MIN_YEAR = 2022`)
   - `data/questions.json` (flat array of all questions with deterministic `questionId`s)
   - `data/images.json` (flat database of all question images with `imageId`, `questionId`, `src`, `caption`, pixel `width`/`height`)
   
   Then run a quick HTTP server (`python3 -m http.server`) and verify the new subject in browser (`0` console errors, `0` `.katex-error`, `scrollWidth <= innerWidth`, cropped images visible on sheet & inside 80vw drawer), then commit and push `main` before moving to the next subject.

---

## 4. UI Design Rules Already Implemented (Do Not Regress)
- `index.html` preserves the 3-stage navigation:
  1. **Home (`#/`)**: 6 stacked subject cards with fan-out hover animation, clean `JU EE Question Paper Vault [2022–2026]` header + subject filter.
  2. **Subject Paper Grid (`#/<subjectId>`)**: Descending paper cards with **Header + Year Only** cover design (no miniature question tables inside card thumbnails).
  3. **Exam Paper Sheet & Drawer (`#/<subjectId>/<paperId>`)**: Authentic `.printed-paper-sheet`, Jadavpur University watermark, 3-state Confidence Tracker (`Mastered | Review | Unsolved` saved in `localStorage`), live Part Choice counters, Year pills, responsive header/toolbar with no horizontal clipping, `80vw` slide-over drawer (`#drawer-panel`), `Copy JSON` / `Copy LaTeX`, image/SVG rendering, and `Ask DeepSeek AI` tab.
