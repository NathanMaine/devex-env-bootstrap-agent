import argparse
from .scanner import scan_project
from .generator import write_bootstrap, write_onboarding


def main():
    parser = argparse.ArgumentParser(description="DevEx Env Bootstrap Agent")
    parser.add_argument("--project-path", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    info = scan_project(args.project_path)
    write_bootstrap(info, args.output_dir)
    write_onboarding(info, args.output_dir)
    print(f"Wrote bootstrap.sh and ONBOARDING.md to {args.output_dir}")


if __name__ == "__main__":
    main()
