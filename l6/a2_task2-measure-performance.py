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
        "## Task 2. Explorer task. Measure performance\n\n"
        "Add a counter: `correct`.\n"
        "Give it a start value.\n"
        "Add 1 each time the answer is right.\n\n"
        "At the end show:\n"
        "```python\n"
        "print(\"You answered\", correct, \"out of\", questions, \"correctly\")\n"
        "```\n\n"
        "Type your program with correct counter:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_correct_init = mo.ui.checkbox(label="Initializes `correct = 0` before loop")
    chk_correct_inc = mo.ui.checkbox(label="Increments `correct = correct + 1` when answer is right")
    chk_final = mo.ui.checkbox(label="Shows `You answered X out of Y correctly` at end")
    chk_uses_vars = mo.ui.checkbox(label="Uses `correct` and `questions` variables in final print")
    
    mo.vstack([chk_correct_init, chk_correct_inc, chk_final, chk_uses_vars], gap=4)
    return (chk_correct_init, chk_correct_inc, chk_final, chk_uses_vars)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()