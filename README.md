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

## 📦 Usage
```bash
python task_tracker.py add "Buy milk"
python task_tracker.py list
python task_tracker.py list --all
python task_tracker.py done 1
python task_tracker.py delete 1
