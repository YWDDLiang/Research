#!/usr/bin/env python3
"""Validate the research knowledge-base indexes and paper reports."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PAPERS_JSON = ROOT / "crystal" / "bibliography" / "papers.json"
CRYSTAL_INDEX = ROOT / "crystal" / "README.md"

REQUIRED_FIELDS = {
    "slug", "title", "year", "venue", "group", "category", "role",
    "paper_url", "project_url", "report_path", "status", "summary",
    "problem", "task", "data", "mechanism", "evidence", "assumptions",
    "alternative", "baseline", "killer", "contribution", "transfer",
    "verdict", "use", "not_claim", "next_exp", "scores", "last_verified",
}

REQUIRED_REPORT_HEADINGS = [
    "## 1. Scientific problem",
    "## 2. Mathematical task",
    "## 3. Data-generating process",
    "## 4. Core mechanism",
    "## 5. Claim–evidence alignment",
    "## 6. Hidden assumptions",
    "## 7. Strongest alternative explanation",
    "## 8. Missing baseline",
    "## 9. Killer experiment",
    "## 10. Contribution type",
    "## 11. Transferable abstraction",
    "## 12. Final verdict",
]


def is_http_url(value: str) -> bool:
    return bool(re.match(r"^https?://", value))


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def main() -> int:
    errors: list[str] = []

    try:
        payload = load_json(PAPERS_JSON)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    papers = payload.get("papers")
    if not isinstance(papers, list):
        print("ERROR: papers.json must contain a list under 'papers'.")
        return 1

    if payload.get("count") != len(papers):
        errors.append(
            f"papers.json count={payload.get('count')} but contains {len(papers)} papers."
        )

    try:
        index_text = CRYSTAL_INDEX.read_text(encoding="utf-8")
    except FileNotFoundError:
        index_text = ""
        errors.append(f"Missing crystal index: {CRYSTAL_INDEX}")

    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()

    for i, paper in enumerate(papers, start=1):
        prefix = f"paper[{i}]"
        if not isinstance(paper, dict):
            errors.append(f"{prefix} is not an object.")
            continue

        missing = sorted(REQUIRED_FIELDS - set(paper))
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
            continue

        slug = str(paper["slug"])
        title = str(paper["title"])
        report_path = str(paper["report_path"])

        if not re.match(r"^[a-z0-9][a-z0-9-]*$", slug):
            errors.append(f"{slug}: invalid slug.")

        if slug in seen_slugs:
            errors.append(f"Duplicate slug: {slug}")
        seen_slugs.add(slug)

        normalized_title = re.sub(r"\s+", " ", title.strip().lower())
        if normalized_title in seen_titles:
            errors.append(f"Duplicate title: {title}")
        seen_titles.add(normalized_title)

        year = paper["year"]
        if not isinstance(year, int) or not (1900 <= year <= 2100):
            errors.append(f"{slug}: invalid year {year!r}")

        paper_url = str(paper["paper_url"])
        project_url = str(paper["project_url"])
        if not is_http_url(paper_url):
            errors.append(f"{slug}: paper_url must be http(s).")
        if project_url and not is_http_url(project_url):
            errors.append(f"{slug}: project_url must be empty or http(s).")

        scores = paper["scores"]
        if (
            not isinstance(scores, list)
            or len(scores) != 6
            or any(not isinstance(x, int) or not (0 <= x <= 2) for x in scores)
        ):
            errors.append(f"{slug}: scores must be six integers in [0, 2].")

        report = ROOT / report_path
        if not report.exists():
            errors.append(f"{slug}: missing report {report_path}")
            continue

        report_text = report.read_text(encoding="utf-8")
        if f'slug: "{slug}"' not in report_text:
            errors.append(f"{slug}: report front matter slug mismatch.")
        if f"# {title}" not in report_text:
            errors.append(f"{slug}: report title mismatch.")

        for heading in REQUIRED_REPORT_HEADINGS:
            if heading not in report_text:
                errors.append(f"{slug}: missing heading '{heading}'")

        relative_link = f"./papers/{slug}.md"
        if relative_link not in index_text:
            errors.append(f"{slug}: report is not linked from crystal/README.md")

        for field in [
            "summary", "problem", "task", "mechanism", "alternative",
            "baseline", "killer", "verdict",
        ]:
            value = str(paper[field]).strip()
            if len(value) < 20:
                errors.append(f"{slug}: field '{field}' is too short for an audit.")

    report_files = {
        path.stem for path in (ROOT / "crystal" / "papers").glob("*.md")
    }
    orphan_reports = sorted(report_files - seen_slugs)
    if orphan_reports:
        errors.append(f"Orphan paper reports: {', '.join(orphan_reports)}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "Validation passed: "
        f"{len(papers)} indexed papers, {len(report_files)} reports, "
        "all required audit sections and links present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
