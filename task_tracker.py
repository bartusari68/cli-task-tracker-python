#!/usr/bin/env python3
"""
CLI Task Tracker (Python)

A clean, standard-library-only CLI task tracker.
Storage: local JSON file (tasks.json) placed next to this script.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).with_name("tasks.json")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def load_tasks() -> list[dict[str, Any]]:
    """
    Load tasks from tasks.json.
    If the file doesn't exist, return an empty list.
    If the file is corrupted, raise a ValueError with a clear message.
    """
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("tasks.json is not valid JSON. Fix or delete the file.") from exc

    if not isinstance(data, list):
        raise ValueError("tasks.json must contain a JSON array of tasks.")

    # Basic shape validation (lightweight)
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each task must be a JSON object.")
        if "id" not in item or "title" not in item or "done" not in item:
            raise ValueError("Each task must include: id, title, done.")

    return data


def save_tasks(tasks: list[dict[str, Any]]) -> None:
    DATA_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def next_id(tasks: list[dict[str, Any]]) -> int:
    if not tasks:
        return 1
    return max(int(t["id"]) for t in tasks) + 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="A simple CLI task tracker (JSON storage).",
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

    try:
        tasks = load_tasks()
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    # WIP: command handling will be implemented next
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

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
