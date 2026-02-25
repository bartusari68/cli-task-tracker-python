#!/usr/bin/env python3
"""
CLI Task Tracker (Python)

A clean, standard-library-only CLI task tracker.
Storage: local JSON file (tasks.json) placed next to this script.

Commands:
  add <title>         Add a new task
  list [--all]        List tasks (default: pending only)
  done <id>           Mark task as done
  delete <id>         Delete a task
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

VERSION = "1.0.0"
DATA_FILE = Path(__file__).with_name("tasks.json")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def load_tasks() -> list[dict[str, Any]]:
    """
    Load tasks from tasks.json.
    - If file doesn't exist: return empty list.
    - If corrupted: raise ValueError with a clear fix suggestion.
    """
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            "tasks.json is not valid JSON. Fix the file or delete it to reset."
        ) from exc

    if not isinstance(data, list):
        raise ValueError("tasks.json must contain a JSON array (list) of tasks.")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each task must be a JSON object.")
        if "id" not in item or "title" not in item or "done" not in item:
            raise ValueError("Each task must include: id, title, done.")

    return data


def save_tasks(tasks: list[dict[str, Any]]) -> None:
    DATA_FILE.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def next_id(tasks: list[dict[str, Any]]) -> int:
    if not tasks:
        return 1
    return max(int(t["id"]) for t in tasks) + 1


def find_task(tasks: list[dict[str, Any]], task_id: int) -> dict[str, Any] | None:
    for t in tasks:
        if int(t.get("id", -1)) == task_id:
            return t
    return None


def format_task(task: dict[str, Any]) -> str:
    done = bool(task.get("done"))
    status = "✅" if done else "⬜"
    task_id = task.get("id")
    title = task.get("title", "")
    return f"{status} [{task_id}] {title}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="A simple CLI task tracker (JSON storage).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--all",
        action="store_true",
        help="Show all tasks (including completed ones)",
    )

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    return parser


def cmd_add(tasks: list[dict[str, Any]], title: str) -> int:
    title = title.strip()
    if not title:
        print("Error: title cannot be empty.")
        return 1

    task = {
        "id": next_id(tasks),
        "title": title,
        "done": False,
        "created_at": now_iso(),
        "completed_at": None,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: [{task['id']}] {task['title']}")
    return 0


def cmd_list(tasks: list[dict[str, Any]], show_all: bool) -> int:
    if not tasks:
        print('No tasks yet. Add one with: python task_tracker.py add "Task title"')
        return 0

    visible = tasks if show_all else [t for t in tasks if not t.get("done")]
    if not visible:
        print("All tasks are completed 🎉 (use --all to view history)")
        return 0

    for t in visible:
        print(format_task(t))
    return 0


def cmd_done(tasks: list[dict[str, Any]], task_id: int) -> int:
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Error: task with id {task_id} not found.")
        return 1

    if task.get("done"):
        print(f"Already done: [{task_id}] {task.get('title')}")
        return 0

    task["done"] = True
    task["completed_at"] = now_iso()
    save_tasks(tasks)
    print(f"✅ Done: [{task_id}] {task.get('title')}")
    return 0


def cmd_delete(tasks: list[dict[str, Any]], task_id: int) -> int:
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Error: task with id {task_id} not found.")
        return 1

    tasks.remove(task)
    save_tasks(tasks)
    print(f"🗑️ Deleted: [{task_id}] {task.get('title')}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        tasks = load_tasks()
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    if args.command == "add":
        return cmd_add(tasks, args.title)

    if args.command == "list":
        return cmd_list(tasks, args.all)

    if args.command == "done":
        return cmd_done(tasks, args.id)

    if args.command == "delete":
        return cmd_delete(tasks, args.id)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
