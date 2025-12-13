from pathlib import Path
from .scanner import ProjectInfo


def write_bootstrap(info: ProjectInfo, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    script = out / "bootstrap.sh"
    lines = ["#!/usr/bin/env bash", "set -euo pipefail", ""]
    if info.language == "python":
        lines += [
            "python -m venv .venv",
            "source .venv/bin/activate",
            "pip install -r requirements.txt",
        ]
    elif info.language == "node":
        lines += [
            "npm install",
        ]
    else:
        lines += [
            "# TODO: add setup steps for this project.",
        ]
    script.write_text("\n".join(lines), encoding="utf-8")


def write_onboarding(info: ProjectInfo, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    doc = out / "ONBOARDING.md"
    contents = [
        "# Onboarding Checklist",
        "",
        "- [ ] Clone the repo",
        "- [ ] Run `./bootstrap.sh`",
    ]
    if info.language == "python":
        contents.append("- [ ] Run `pytest`")
    elif info.language == "node":
        contents.append("- [ ] Run `npm test`")
    doc.write_text("\n".join(contents), encoding="utf-8")
