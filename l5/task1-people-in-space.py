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
        "# People in space\n\n"
        "## Worked example. Weather\n"
        "Read this program.\n\n"
        "```python\n"
        "print(\"What's the weather like?\")\n"
        "weather = input()\n"
        "print(advice)\n"
        "```\n\n"
        "It gives clothing advice. Test it once for every branch.\n"
        "Use `if` / `elif` / `else`.\n\n"
        "---\n\n"
        "## Task 1. People in space\n\n"
        "Read the short program.\n\n"
        "```python\n"
        "from space import people\n"
        "number = people()\n"
        "print(number, \"people in space right now\")\n"
        "```\n\n"
        "The number comes from the internet. It is not always the same.\n\n"
        "### \U0001f527 Workaround: `space` module not installed?\n"
        "Copy this at the **top of your file** to make it run locally:\n\n"
        "```python\n"
        "# --- MOCK space module (paste at top) ---\n"
        "def people():\n"
        '    """Return a fake number of people in space for testing."""\n'
        "    return 7  # Change this to test different scenarios\n"
        "# -------------------------------------------\n"
        "```\n\n"
        "### Step 1\n"
        "Ask the user to guess (\u062a\u0648\u0642\u0639).\n"
        "Ask: `How many people do you think are in space right now?`\n"
        "Keep all 3 lines. Only add lines.\n\n"
        "**New variable:** `guess`.\n"
        "**Convert to integer:** `guess = int(input())`\n\n"
        "**Type the lines you added:**\n"
        "(Write them in your editor)\n\n"
        "### Step 2\n"
        "Compare `number` with `guess`. Three branches:\n\n"
        "| Guess | Real | Output |\n"
        "|---|---|---|\n"
        "| 8 | 8 | `That's right!` + `8 people in space right now` |\n"
        "| 5 | 8 | `It's actually more than that` + `8 people in space right now` |\n"
        "| 9 | 8 | `It's actually fewer than that` + `8 people in space right now` |\n\n"
        "**Use:** `if` / `elif` / `else`. Use `==`, `<`, `>`.\n\n"
        "**Type your full program:**\n"
        "(Write it in your editor, including the mock at the top)\n\n"
        "**Red error (\u062e\u0637\u0623)? Fix it (\u0635\u0644\u0651\u0651\u062d\u0647).** Tick what you found:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_spelling = mo.ui.checkbox(label="Misspelt `if` or `else`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside the branch")
    chk_equal = mo.ui.checkbox(label="Used `=` instead of `==")
    chk_quotes = mo.ui.checkbox(label="Quote mistake (variable vs word like `\"snowy\"`)")
    
    mo.vstack([chk_spelling, chk_colon, chk_indent, chk_equal, chk_quotes], gap=4)
    return (chk_spelling, chk_colon, chk_indent, chk_equal, chk_quotes)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()