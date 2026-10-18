# Marimo Notebook URLs for Python Teaching Materials

## L4 - Selection Basics

### Task 1: Trip Critic
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task1-trip-critic.py
```

### Task 2: Favourite Number
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task2-favourite-number.py
```

### Task 3: Eligible to Vote
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task3-eligible-vote.py
```

---

## L5 - People in Space & Temperature (A2 Worksheet)

### Task 1: People in space
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/l5/task1-people-in-space.py
```

### Task 2: Temperature
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/l5/task2-temperature.py
```

---

## How to use

### Option 2: Paste in marimo.new
1. Go to https://marimo.new
2. Click "Load from URL" 
3. Paste the **Raw URL** above

### Option 3: Run locally
```bash
# L4
uv run marimo run task1-trip-critic.py
uv run marimo run task2-favourite-number.py
uv run marimo run task3-eligible-vote.py

# L5
uv run marimo run l5/task1-people-in-space.py
uv run marimo run l5/task2-temperature.py
```

---

## Notebook Structure

All notebooks use **Template B (static)**:
- `hide_code=True` on all cells
- Code skeleton in **markdown code block** at Step 1 **only if the original HTML has one** (L4 Task 1 & 2 have snippets; L4 Task 3 does not; L5 Task 1 & 2 have snippets)
- Interactive checkboxes for error reflection
- No run button, no code editor, no solution accordion
- Designed for "copy to your editor, run locally" workflow

---

## Folder Structure in Repo

```
Python-teaching-materials/
├── task1-trip-critic.py              # L4 Task 1
├── task2-favourite-number.py         # L4 Task 2
├── task3-eligible-vote.py            # L4 Task 3
├── l5/
│   ├── task1-people-in-space.py      # L5 Task 1
│   └── task2-temperature.py          # L5 Task 2
└── MARIMO_URLS.md
```