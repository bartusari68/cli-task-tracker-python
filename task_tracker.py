#!/usr/bin/env python3
"""
CLI Task Tracker (Python)

A minimal, standard-library-only CLI skeleton.
Commands (WIP): add, list, done, delete
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="A simple CLI task tracker (WIP).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    # list
    subparsers.add_parser("list", help="List all tasks")

    # done
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    # WIP: command handling will be implemented step-by-step
    if args.command == "add":
        print("WIP: add command not implemented yet.")
        return 0

    if args.command == "list":
        print("WIP: list command not implemented yet.")
        return 0

    if args.command == "done":
        print("WIP: done command not implemented yet.")
        return 0

    if args.command == "delete":
        print("WIP: delete command not implemented yet.")
        return 0

    # Should never happen due to required=True
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
