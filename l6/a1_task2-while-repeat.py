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
        "# Count\n\n"
        "## Task 2. Repeat with while\n\n"
        "Same actions again and again. Use `while` to repeat.\n\n"
        "### Step 1\n"
        "Type this start. It will not run yet.\n\n"
        "```python\n"
        "count = 3\n"
        "while              :\n"
        "    print(count)\n"
        "    count = count - 1\n"
        "```\n\n"
        "### Step 2\n"
        "Pick the condition. Last value printed must be 1.\n\n"
        "- `while count > 1:`\n"
        "- `while count >= 1:`\n"
        "- `while count < 1:`\n"
        "- `while count == 1:`\n\n"
        "Why did you pick it? Write here:\n"
        "(Write in your editor)\n\n"
        "### Step 3\n"
        "Type your full while program:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Red error (خطأ)? Fix it (صلّحه). Tick what you found:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_spelling = mo.ui.checkbox(label="Misspelt `while`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside `while`")
    chk_condition = mo.ui.checkbox(label="Correct condition: `while count >= 1:`")
    
    mo.vstack([chk_spelling, chk_colon, chk_indent, chk_condition], gap=4)
    return (chk_spelling, chk_colon, chk_indent, chk_condition)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()