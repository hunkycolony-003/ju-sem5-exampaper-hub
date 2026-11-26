#!/usr/bin/env python3
"""Rebuild data/index.json, data/questions.json, and data/images.json inside ju-sem5-exampaper-hub."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

DATA_DIR = Path(__file__).resolve().parent
REPO_ROOT = DATA_DIR.parent
PAPERS_DIR = DATA_DIR / "papers"
INDEX_PATH = DATA_DIR / "index.json"
QUESTIONS_PATH = DATA_DIR / "questions.json"
IMAGES_PATH = DATA_DIR / "images.json"
SOLVED_2023_PATH = DATA_DIR / "paper_2023.json"
MIN_YEAR = 2022

SUBJECT_CATALOG = [
    {
        "order": 1,
        "id": "pspd",
        "codePrefix": "Ex/EE/PC/B/T/312",
        "name": "Power System Planning & Design",
        "paperTitle": "POWER SYSTEM PLANNING & DESIGN",
    },
    {
        "order": 2,
        "id": "ispm",
        "codePrefix": "Ex/EE/PC/B/T/315",
        "name": "Introduction to Statistical and Probabilistic Methods",
        "paperTitle": "INTRODUCTION TO STATISTICAL AND PROBABILISTIC METHODS",
    },
    {
        "order": 3,
        "id": "em3",
        "codePrefix": "Ex/EE/PC/B/T/311",
        "name": "Electrical Machine - III",
        "paperTitle": "ELECTRICAL MACHINE - III",
    },
    {
        "order": 4,
        "id": "lcs",
        "codePrefix": "Ex/EE/PC/B/T/313",
        "name": "Linear Control System",
        "paperTitle": "LINEAR CONTROL SYSTEM",
    },
    {
        "order": 5,
        "id": "pe",
        "codePrefix": "Ex/EE/PC/B/T/314",
        "name": "Power Electronics",
        "paperTitle": "POWER ELECTRONICS",
    },
    {
        "order": 6,
        "id": "plm",
        "codePrefix": "Ex/EE/PC/B/T/316",
        "name": "Prog. Logic & Microcontroller",
        "paperTitle": "PROGRAMMABLE LOGIC & MICROCONTROLLER",
    },
]


def slug_qnum(qnum: str, fallback_idx: int) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "", str(qnum or "")).lower()
    return cleaned or f"q{fallback_idx:02d}"


def get_image_dims(src: str):
    if not src or src.startswith("data:") or Image is None:
        return None, None
    img_path = REPO_ROOT / src
    if not img_path.is_file():
        return None, None
    try:
        with Image.open(img_path) as im:
            return im.width, im.height
    except Exception:
        return None, None


def rebuild() -> None:
    subjects_out = []
    flat_questions = []
    flat_images = []

    for subj in SUBJECT_CATALOG:
        sid = subj["id"]
        subj_dir = PAPERS_DIR / sid
        papers_meta = []

        if subj_dir.is_dir():
            loaded_papers = []
            for pfile in sorted(subj_dir.glob("*.json")):
                paper = json.loads(pfile.read_text(encoding="utf-8"))
                if int(paper.get("year") or 0) < MIN_YEAR:
                    continue
                paper["subjectId"] = sid
                rel_path = f"data/papers/{sid}/{pfile.name}"

                q_count = 0
                has_diagram = bool(paper.get("hasDiagram"))
                has_solutions = False
                used_ids = set()

                for p_idx, part in enumerate(paper.get("parts") or [], start=1):
                    part_label = part.get("partLabel") or f"PART {p_idx}"
                    ref_code = part.get("refCode") or f"{subj['codePrefix']}/{int(paper.get('year') or 0)}"
                    current_group = None

                    for row in part.get("rows") or []:
                        if not isinstance(row, dict):
                            continue
                        kind = row.get("kind")
                        if kind == "group":
                            current_group = row.get("label") or None
                        elif kind == "question":
                            q_count += 1
                            has_solutions = has_solutions or bool(row.get("solution") or row.get("solutionLatex"))
                            base_qid = f"{paper['id']}-p{p_idx}-{slug_qnum(row.get('qNum'), q_count)}"
                            qid = base_qid
                            suffix = 2
                            while qid in used_ids:
                                qid = f"{base_qid}-{suffix}"
                                suffix += 1
                            used_ids.add(qid)
                            row["questionId"] = qid
                            if "images" not in row or row["images"] is None:
                                row["images"] = []

                            imgs = row.get("images") or []
                            if row.get("diagramSvg") or imgs:
                                has_diagram = True

                            for img_idx, img_entry in enumerate(imgs, start=1):
                                if isinstance(img_entry, str):
                                    src = img_entry
                                    caption = row.get("diagramCaption") or ""
                                    alt = caption or f"{subj['name']} {paper.get('yearLabel')} Q{row.get('qNum')}"
                                    img_id = f"{qid}-img{img_idx}"
                                    norm_entry = {"imageId": img_id, "src": src, "alt": alt, "caption": caption}
                                    imgs[img_idx - 1] = norm_entry
                                else:
                                    src = img_entry.get("src") or ""
                                    caption = img_entry.get("caption") or ""
                                    alt = img_entry.get("alt") or caption or f"{subj['name']} {paper.get('yearLabel')} Q{row.get('qNum')}"
                                    img_id = img_entry.get("imageId") or f"{qid}-img{img_idx}"
                                    img_entry["imageId"] = img_id
                                    img_entry.setdefault("alt", alt)

                                w, h = get_image_dims(src)
                                flat_images.append({
                                    "imageId": img_id,
                                    "kind": "raster",
                                    "questionId": qid,
                                    "subjectId": sid,
                                    "subjectName": subj["name"],
                                    "subjectCode": subj["codePrefix"],
                                    "paperId": paper["id"],
                                    "year": paper.get("year"),
                                    "yearLabel": paper.get("yearLabel") or str(paper.get("year") or ""),
                                    "part": part_label,
                                    "qNum": row.get("qNum"),
                                    "topic": row.get("topic"),
                                    "src": src,
                                    "alt": alt,
                                    "caption": caption or None,
                                    "width": w,
                                    "height": h,
                                })

                            if row.get("diagramSvg"):
                                flat_images.append({
                                    "imageId": f"{qid}-svg1",
                                    "kind": "svg",
                                    "questionId": qid,
                                    "subjectId": sid,
                                    "subjectName": subj["name"],
                                    "subjectCode": subj["codePrefix"],
                                    "paperId": paper["id"],
                                    "year": paper.get("year"),
                                    "yearLabel": paper.get("yearLabel") or str(paper.get("year") or ""),
                                    "part": part_label,
                                    "qNum": row.get("qNum"),
                                    "topic": row.get("topic"),
                                    "src": None,
                                    "alt": row.get("diagramCaption") or f"Q{row.get('qNum')} Diagram",
                                    "caption": row.get("diagramCaption"),
                                    "svg": row.get("diagramSvg"),
                                })

                            flat_questions.append({
                                "questionId": qid,
                                "subjectId": sid,
                                "subjectName": subj["name"],
                                "subjectCode": subj["codePrefix"],
                                "paperId": paper["id"],
                                "year": paper.get("year"),
                                "yearLabel": paper.get("yearLabel") or str(paper.get("year") or ""),
                                "examType": paper.get("examType") or "Regular",
                                "part": part_label,
                                "partIndex": p_idx,
                                "refCode": ref_code,
                                "groupLabel": current_group,
                                "qNum": row.get("qNum"),
                                "marks": row.get("marks"),
                                "co": row.get("co"),
                                "topic": row.get("topic"),
                                "textLatex": row.get("textLatex") or "",
                                "images": imgs,
                                "diagramSvg": row.get("diagramSvg"),
                                "diagramCaption": row.get("diagramCaption"),
                                "sourcePdf": paper.get("sourcePdf"),
                            })

                paper["hasDiagram"] = has_diagram
                pfile.write_text(json.dumps(paper, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

                loaded_papers.append((
                    -(float(paper.get("sortKey") if paper.get("sortKey") is not None else (paper.get("year") or 0))),
                    -(float(paper.get("year") or 0)),
                    str(paper.get("id") or ""),
                    {
                        "id": paper["id"],
                        "year": paper.get("year"),
                        "sortKey": paper.get("sortKey"),
                        "yearLabel": paper.get("yearLabel") or str(paper.get("year") or ""),
                        "examType": paper.get("examType") or "Regular",
                        "sourcePdf": paper.get("sourcePdf"),
                        "hasDiagram": has_diagram,
                        "hasSolutions": has_solutions,
                        "partCount": len(paper.get("parts") or []),
                        "questionCount": q_count,
                        "path": rel_path,
                    },
                ))

            # Preserve the repo's original annotated 2023 paper entry for PLM
            if sid == "plm" and SOLVED_2023_PATH.is_file():
                solved = json.loads(SOLVED_2023_PATH.read_text(encoding="utf-8"))
                solved_q_count = sum(len(pt.get("questions") or []) for pt in solved.get("parts") or [])
                loaded_papers.append((
                    -2023.1,
                    -2023.1,
                    "plm-2023-solved",
                    {
                        "id": "plm-2023-solved",
                        "year": 2023,
                        "sortKey": 2023.1,
                        "yearLabel": "2023 (Solved)",
                        "examType": "Annotated",
                        "sourcePdf": "2023 Examination Archive",
                        "hasDiagram": False,
                        "hasSolutions": True,
                        "partCount": len(solved.get("parts") or []),
                        "questionCount": solved_q_count,
                        "path": "data/paper_2023.json",
                    },
                ))

            loaded_papers.sort(key=lambda item: (item[0], item[1], item[2]))
            papers_meta = [item[3] for item in loaded_papers]

        subj_entry = dict(subj)
        subj_entry["papers"] = papers_meta
        subjects_out.append(subj_entry)

    now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")

    index_payload = {
        "schemaVersion": "1.0",
        "university": "Jadavpur University",
        "program": "B.E. Electrical Engineering · 3rd Year 1st Semester",
        "assetsDir": "data/assets",
        "updatedAt": now_iso,
        "subjects": subjects_out,
    }
    INDEX_PATH.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    questions_payload = {
        "schemaVersion": "1.0",
        "updatedAt": now_iso,
        "totalQuestions": len(flat_questions),
        "questions": flat_questions,
    }
    QUESTIONS_PATH.write_text(json.dumps(questions_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    images_payload = {
        "schemaVersion": "1.0",
        "updatedAt": now_iso,
        "totalImages": len(flat_images),
        "images": flat_images,
    }
    IMAGES_PATH.write_text(json.dumps(images_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        f"Rebuilt repo data/: {sum(len(s['papers']) for s in subjects_out)} papers, "
        f"{len(flat_questions)} questions, {len(flat_images)} images"
    )


if __name__ == "__main__":
    rebuild()
