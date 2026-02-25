# ✅ CLI Task Tracker (Python)

A clean, beginner-friendly **command-line task tracker** built with **Python**.  
Focused on **discipline**, **readable code**, and a **realistic mini-project workflow**.

---

## ✨ Goals
- Keep commits clean and meaningful (`feat:`, `docs:`, `fix:`)
- Build with a simple, maintainable structure
- Use **Python standard library only** (no external dependencies)

---

## ✅ Features
- ➕ Add tasks
- 📋 List tasks (optionally include completed)
- ✅ Mark tasks as done
- 🗑️ Delete tasks
- 💾 Persistent storage via local `tasks.json`

---

## 🧰 Tech Stack
- **Python 3**
- Standard library: `argparse`, `json`, `pathlib`, `datetime`

---

## 📦 Usage + 🖥️ Example Output
```console
$ python task_tracker.py add "Buy milk"
✅ Added: [1] Buy milk

$ python task_tracker.py list
⬜ [1] Buy milk

$ python task_tracker.py done 1
✅ Done: [1] Buy milk

$ python task_tracker.py list
All tasks are completed 🎉 (use --all to view history)

$ python task_tracker.py list --all
✅ [1] Buy milk

$ python task_tracker.py delete 1
🗑️ Deleted: [1] Buy milk
