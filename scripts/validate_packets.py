#!/usr/bin/env python3
"""Validate shot packet JSON files against shot_packet.schema.json.

Also lints prompt.full_text for pipeline IDs (K-SHOT-SCRIPT-001).

Usage:
  python3 scripts/validate_packets.py path/to/packet.json [more.json ...]
  python3 scripts/validate_packets.py path/to/dir   # recursive *.json

Exit 0 if all pass; 1 if any fail.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "02_Tools" / "schemas" / "shot_packet.schema.json"

ID_LINT = re.compile(r"[\[\]]|CHAR_|LOC_|WARD_|PROP_|VEH_|ANI_|LOOK_")

REQUIRED = [
    "shot_id",
    "mode",
    "duration_target",
    "aspect",
    "resolution",
    "prompt",
    "bible_pins",
    "status",
]


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def collect_files(args: list[str]) -> list[Path]:
    files: list[Path] = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.json")))
        elif p.is_file():
            files.append(p)
        else:
            print(f"MISS  {a}", file=sys.stderr)
    return files


def validate_one(path: Path, schema: dict) -> list[str]:
    errs: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"json: {e}"]

    if not isinstance(data, dict):
        return ["root must be object"]

    for k in REQUIRED:
        if k not in data:
            errs.append(f"missing required: {k}")

    mode_enum = schema.get("properties", {}).get("mode", {}).get("enum", [])
    if "mode" in data and mode_enum and data["mode"] not in mode_enum:
        errs.append(f"mode not in {mode_enum}: {data.get('mode')}")

    status_enum = schema.get("properties", {}).get("status", {}).get("enum", [])
    if "status" in data and status_enum and data["status"] not in status_enum:
        errs.append(f"status not in {status_enum}: {data.get('status')}")

    dur = data.get("duration_target")
    if isinstance(dur, int):
        if dur < 1 or dur > 15:
            errs.append(f"duration_target out of 1..15: {dur}")
        policy = data.get("duration_policy", "standard_8s_cap")
        if policy == "standard_8s_cap" and dur > 8:
            errs.append(f"duration_target {dur} exceeds standard_8s_cap")

    prompt = data.get("prompt")
    if not isinstance(prompt, dict):
        errs.append("prompt must be object")
    else:
        if "full_text" not in prompt or not str(prompt.get("full_text", "")).strip():
            errs.append("prompt.full_text required non-empty")
        else:
            ft = str(prompt["full_text"])
            if ID_LINT.search(ft):
                errs.append("prompt.full_text fails ID lint (brackets or TYPE_ tokens)")
            # optional field consistency
            if data.get("gen_prompt_lint") == "pass" and ID_LINT.search(ft):
                errs.append("gen_prompt_lint=pass but full_text has IDs")
            if data.get("gen_prompt_lint") == "fail":
                errs.append("gen_prompt_lint marked fail")

    pins = data.get("bible_pins")
    if isinstance(pins, dict) and "style" not in pins:
        errs.append("bible_pins.style required")

    return errs


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    schema = load_schema()
    files = collect_files(argv[1:])
    if not files:
        print("No JSON files found", file=sys.stderr)
        return 2
    failed = 0
    for f in files:
        errs = validate_one(f, schema)
        if errs:
            failed += 1
            print(f"FAIL  {f}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS  {f}")
    print(f"SUMMARY pass={len(files) - failed} fail={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
