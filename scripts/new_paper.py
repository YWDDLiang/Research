#!/usr/bin/env python3
"""Create a new paper-audit skeleton.

This intentionally does not mutate papers.json or crystal/README.md. Complete
the audit first, then add the entry to the main index.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "crystal" / "papers"


def valid_slug(value: str) -> str:
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", value):
        raise argparse.ArgumentTypeError(
            "slug must contain lowercase letters, numbers, and hyphens only"
        )
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, type=valid_slug)
    parser.add_argument("--title", required=True)
    parser.add_argument("--year", required=True, type=int)
    parser.add_argument("--venue", required=True)
    parser.add_argument("--paper-url", required=True)
    parser.add_argument("--project-url", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not re.match(r"^https?://", args.paper_url):
        print("ERROR: --paper-url must be an http(s) URL.", file=sys.stderr)
        return 2
    if args.project_url and not re.match(r"^https?://", args.project_url):
        print(
            "ERROR: --project-url must be empty or an http(s) URL.",
            file=sys.stderr,
        )
        return 2

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"{args.slug}.md"
    if path.exists():
        print(f"ERROR: {path} already exists.", file=sys.stderr)
        return 2

    today = dt.date.today().isoformat()
    title_yaml = args.title.replace('"', r'\"')
    venue_yaml = args.venue.replace('"', r'\"')
    template = f"""---
title: "{title_yaml}"
slug: "{args.slug}"
year: {args.year}
venue: "{venue_yaml}"
category: "TODO"
audit_role: "TODO"
paper_url: "{args.paper_url}"
project_url: "{args.project_url}"
last_verified: "{today}"
---

# {args.title}

> [返回晶体论文索引](../README.md) · 当前状态：**待完成审计，不得加入主索引**

## 0. 三十秒结论

**论文做了什么：** TODO

**去故事化判断：** TODO

**对当前研究最直接的用途：** TODO

## 1. Scientific problem

TODO

## 2. Mathematical task

TODO

## 3. Data-generating process

TODO

## 4. Core mechanism

TODO

## 5. Claim–evidence alignment

| Claim | Evidence | Alternative explanation | Allowed conclusion |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

## 6. Hidden assumptions

- TODO

## 7. Strongest alternative explanation

TODO

## 8. Missing baseline

TODO

## 9. Killer experiment

TODO

## 10. Contribution type

\\[
\\Delta=(\\Delta P,\\Delta I,\\Delta O,\\Delta C,\\Delta E,\\Delta K)
\\]

TODO

## 11. Transferable abstraction

TODO

## 12. Final verdict

TODO

## Reproduction / update log

- **{today}**：创建待审计骨架。
"""
    path.write_text(template, encoding="utf-8")
    print(f"Created {path.relative_to(ROOT)}")
    print(
        "Next: complete all sections, add metadata to papers.json and the "
        "index, then run validate_repo.py."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
