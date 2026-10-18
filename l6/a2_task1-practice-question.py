import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "# Times tables practice\n\n"
        "## Worked example. Countdown\n"
        "```python\n"
        "count = 10\n"
        "while count >= 1:\n"
        "    print(count)\n"
        "    count = count - 1\n"
        "print(\"Lift off\")\n"
        "```\n\n"
        "`count` starts at 10. Goes down by 1 each time. Loop continues while `count` is at least 1.\n\n"
        "## Worked example. Ten sixes\n"
        "```python\n"
        "from random import randint\n"
        "rolls = 0\n"
        "sixes = 0\n"
        "while sixes < 10:\n"
        "    dice = randint(1,6)\n"
        "    print(dice)\n"
        "    if dice == 6:\n"
        "        sixes = sixes + 1\n"
        "    rolls = rolls + 1\n"
        "print(\"Ten sixes in\", rolls, \"dice rolls\")\n"
        "```\n\n"
        "Two counters: `rolls` and `sixes`.\n\n"
        "---\n\n"
        "## Task 1. A practice question\n\n"
        "### Step 1\n"
        "Put lines 2 to 11 inside a loop:\n"
        "```python\n"
        "while True:\n"
        "```\n"
        "`True` means repeat forever. Indent all lines inside.\n\n"
        "Type your while True program (first lines):\n"
        "(Write in your editor)\n\n"
        "### Step 2\n"
        "Run it. It never stops. Press Stop or Ctrl+C to end it.\n\n"
        "What did you see? Write here:\n"
        "(Write output in your editor)\n\n"
        "### Step 3\n"
        "Add a counter: `questions`. Give it a start value. Add 1 each time. Show it inside the loop:\n"
        "```python\n"
        "    print(\"Question\", questions)\n"
        "```\n\n"
        "Type the two lines you added for questions:\n"
        "(Write in your editor)\n\n"
        "### Step 4\n"
        "Ask exactly 3 questions. Change `True` to a check on `questions`. Continue only if 3 or fewer asked.\n\n"
        "Type your final while line + full program:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Red error (خطأ)? Fix it (صلّحه). Tick what you found:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_while_true = mo.ui.checkbox(label="Uses `while True:` to repeat forever")
    chk_indent = mo.ui.checkbox(label="All lines indented inside while")
    chk_counter = mo.ui.checkbox(label="Adds `questions` counter with start value + increment")
    chk_print_q = mo.ui.checkbox(label="Shows `print(\"Question\", questions)` inside loop")
    chk_limit3 = mo.ui.checkbox(label="Changes condition to `while questions <= 3:` (or `< 4`)")
    chk_spelling = mo.ui.checkbox(label="Misspelt `while` or `True`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    
    mo.vstack([chk_while_true, chk_indent, chk_counter, chk_print_q, chk_limit3, chk_spelling, chk_colon], gap=4)
    return (chk_while_true, chk_indent, chk_counter, chk_print_q, chk_limit3, chk_spelling, chk_colon)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()