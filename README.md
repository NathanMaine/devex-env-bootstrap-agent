# DevEx Environment Bootstrapping Agent

Setting up a new work computer for a programmer usually takes days of installing messy software.
This AI acts like a wizard that installs everything automatically in minutes,
so the new hire can start working on day one.

## What This Is

A CLI that:

- Scans a project folder for language/dependency hints.
- Generates:
  - `bootstrap.sh` -- a generic setup script.
  - `ONBOARDING.md` -- a simple checklist.

## IP-Safety Boundaries

- No internal company scripts or secrets.
- Only uses generic commands (for example, `python -m venv`, `npm install`).
- Suitable for open-source use.

## Files

- `src/main.py` -- CLI entry.
- `src/scanner.py` -- detect basic stack.
- `src/generator.py` -- write files.

## Example

```bash
python src/main.py --project-path demo_project --output-dir out
```
