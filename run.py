#!/usr/bin/env python3
"""
run.py - Behave wrapper with CLI flags for test execution

Usage:
    python run.py                    # Run all tests
    python run.py --tags @smoke     # Run tests with @smoke tag
    python run.py --name "Demo"   # Run scenarios matching name
    python run.py --headless true    # Run in headless mode (default)
    python run.py --headless false  # Run with visible browser
    python run.py -w 2             # Run with 2 parallel workers
    python run.py --slow-motion 1.5  # Run with 1.5s delay between steps
    python run.py --format pretty   # Output format (pretty, json, progress)
    python run.py --dry-run         # Show what would run without executing
"""

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Run behave tests with customizable options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "--tags", "-t", "--tag",
        help="Run scenarios with specific tags (e.g., @smoke, @regression)"
    )

    parser.add_argument(
        "--name", "-n",
        help="Run scenarios matching name (partial match)"
    )

    parser.add_argument(
        "--format", "-f",
        default="pretty",
        choices=["pretty", "json", "progress", "quiet"],
        help="Output format (default: pretty)"
    )

    parser.add_argument(
        "--headless",
        type=lambda x: x.lower() == "true",
        default=True,
        metavar="true|false",
        help="Run browser in headless mode (default: true)"
    )

    parser.add_argument(
        "--slow-motion",
        type=float,
        default=0,
        metavar="SECONDS",
        help="Add delay between step executions (e.g., 0.5, 1.0)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show scenarios that would run without executing"
    )

    parser.add_argument(
        "--stop",
        action="store_true",
        help="Stop on first failure"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
        "--wip",
        action="store_true",
        help="Run only @wip tagged scenarios (implies --stop)"
    )

    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=1,
        help="Number of parallel workers (default: 1)"
    )

    parser.add_argument(
        "behave_args",
        nargs=argparse.REMAINDER,
        help="Additional arguments passed directly to behave"
    )

    args = parser.parse_args()

    behave_cmd = ["behave"]

    if args.tags:
        behave_cmd.extend(["--tags", args.tags])

    if args.name:
        behave_cmd.extend(["--name", args.name])

    num_workers = args.workers

    if num_workers > 1:
        try:
            subprocess.run(["behavex", "--version"], capture_output=True, check=True)
            behave_cmd[0] = "behavex"
            behave_cmd.insert(1, f"--parallel-processes={num_workers}")
            print(f"Running with {num_workers} parallel workers (behavex)")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"behavex not found, running serial execution")
            num_workers = 1
            behave_cmd.extend([f"--format={args.format}"])
    else:
        behave_cmd.extend([f"--format={args.format}"])

    if num_workers == 1:
        behave_cmd.append("--show-source")

    if args.headless:
        os.environ["HEADLESS"] = "true"
    else:
        os.environ["HEADLESS"] = "false"

    if args.slow_motion > 0:
        os.environ["SLOW_MOTION"] = str(args.slow_motion)
        print(f"Running in slow motion: {args.slow_motion}s delay between steps")

    if args.dry_run:
        behave_cmd.append("--dry-run")

    if args.stop or args.wip:
        behave_cmd.append("--stop")

    if args.verbose:
        behave_cmd.append("--verbose")

    if args.wip:
        behave_cmd.extend(["--tags", "@wip"])

    behave_cmd.extend(args.behave_args)

    behave_cmd.append("features/")

    print(f"Running: {' '.join(behave_cmd)}")
    print("-" * 60)

    result = subprocess.run(behave_cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()