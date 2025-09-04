# 🧩 15 Puzzle Game (PySide6)

A classic **15 Puzzle (Sliding Puzzle)** game built with Python and PySide6 (Qt for Python).

---

##  Overview

This is a graphical implementation of the 15 Puzzle game, where you slide tiles on a 4×4 grid to arrange them in order from **1 to 15**, leaving the empty space in the bottom-right corner.

---

## 📌 Features

* 4×4 sliding puzzle with random initial state
* Detects valid moves (swap with the empty tile)
* Win detection with a congratulatory pop-up 🎉
* Stylish GUI built with **Qt Designer** (`.ui` file)

---

## 🛠️ Requirements

* Python **3.8+**
* **PySide6**

Install dependencies:

```bash
pip install PySide6
```

---

## 📦 Installation

```bash
# Clone or download the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# (Optional) Create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> If no `requirements.txt` exists, simply run: `pip install PySide6`

---

## ▶️ Run

Make sure `ui_mainwindow.py` (generated from `mainwindow.ui`) is in the same folder. Then run:

```bash
python main.py
```

---

## 🎮 Controls / Gameplay

* Click on a tile next to the empty space to slide it.
* Continue sliding until all numbers are arranged in order:

```
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 []
```

* When you win, a **Congratulations** pop-up will appear.

---

## 🧰 Project Structure

```
<repo-name>/
├── main.py              # Main game logic
├── ui_mainwindow.py     # Auto-generated from mainwindow.ui
├── mainwindow.ui        # Qt Designer file
├── requirements.txt
└── README.md
```

---
