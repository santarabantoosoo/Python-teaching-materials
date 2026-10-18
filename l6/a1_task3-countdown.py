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
        "## Task 3. Countdown\n\n"
        "### Step 1\n"
        "Change one line. Start from 10, not from 3.\n\n"
        "```python\n"
        "count = 10\n"
        "while count >= 1:\n"
        "    print(count)\n"
        "    count = count - 1\n"
        "```\n\n"
        "### Step 2\n"
        "Add one line at the end:\n\n"
        "```python\n"
        "print(\"Lift off!\")\n"
        "```\n\n"
        "It runs after the loop. Do not indent it.\n\n"
        "Type your countdown program:\n"
        "(Write in your editor)\n\n"
        "Run it. What did you see? Write here:\n"
        "(Write output in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_start10 = mo.ui.checkbox(label="Starts from 10 (`count = 10`)")
    chk_prints10to1 = mo.ui.checkbox(label="Prints 10 down to 1")
    chk_liftoff = mo.ui.checkbox(label="Shows `Lift off!` after loop (not indented)")
    chk_condition = mo.ui.checkbox(label="Correct condition: `while count >= 1:`")
    
    mo.vstack([chk_start10, chk_prints10to1, chk_liftoff, chk_condition], gap=4)
    return (chk_start10, chk_prints10to1, chk_liftoff, chk_condition)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()