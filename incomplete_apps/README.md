# Incomplete apps

Gradio mini-apps used in class, each one missing exactly one idea so the
lesson can fill it in.

## `app.py` — AI Challenge Mini (if/else, no loop)

Same single Science question as `ai_challenge_no_if_app`, but now the
**Check** button is wired to an `if/else` decision:

- `if picked is None` → ask the student to pick a choice, game keeps running.
- `if picked.startswith(CORRECT_LETTER)` → "Correct!", else → "Not quite."
- After that one decision the radio and the button are disabled.

**Missing on purpose:** there is no `while` loop, so the game stops after a
single question. Adding the loop is the next exercise.

Run locally:

```bash
pip install -r requirements.txt
python app.py
```

Note: `import spaces` is the ZeroGPU hosting adapter used on Hugging Face
Spaces; it only exists inside a Space container.
