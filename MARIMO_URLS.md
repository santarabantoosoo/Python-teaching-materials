# Marimo Notebook URLs for Python Teaching Materials

## Task 1: Trip Critic
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task1-trip-critic.py
```

## Task 2: Favourite Number
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task2-favourite-number.py
```

## Task 3: Eligible to Vote
**Raw URL:**
```
https://raw.githubusercontent.com/santarabantoosoo/Python-teaching-materials/main/task3-eligible-vote.py
```

---

## How to use

### Option 2: Paste in marimo.new
1. Go to https://marimo.new
2. Click "Load from URL" 
3. Paste the **Raw URL** above

### Option 3: Run locally
```bash
uv run marimo run task1-trip-critic.py
uv run marimo run task2-favourite-number.py
uv run marimo run task3-eligible-vote.py
```

### Option 4: Edit locally
```bash
uv run marimo edit task1-trip-critic.py
```

---

## Notebook Structure (all three)

Each notebook uses **Template B (static)**:
- `hide_code=True` on all cells
- Code skeleton in **markdown code block** at Step 1 **only if the original HTML has one** (Task 1 & 2 have snippets; Task 3 does not)
- Interactive checkboxes for error reflection
- No run button, no code editor, no solution accordion
- Designed for "copy to your editor, run locally" workflow