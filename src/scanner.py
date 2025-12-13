import os
from dataclasses import dataclass


@dataclass
class ProjectInfo:
    language: str | None = None
    dependencies_file: str | None = None


def scan_project(path: str) -> ProjectInfo:
    files = set(os.listdir(path))
    if "requirements.txt" in files:
        return ProjectInfo(language="python", dependencies_file="requirements.txt")
    if "package.json" in files:
        return ProjectInfo(language="node", dependencies_file="package.json")
    return ProjectInfo()
