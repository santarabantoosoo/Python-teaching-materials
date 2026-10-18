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
        "## Worked example\n"
        "What will this program show?\n\n"
        "```python\n"
        "count = 3\n"
        "print(count)\n"
        "count = count - 1\n"
        "print(count)\n"
        "```\n\n"
        "Use a trace table. Track the line, the value, and the Output (الناتج).\n\n"
        "| line | count | output |\n"
        "|---|---|---|\n"
        "| 1 | 3 | |\n"
        "| 2 | | 3 |\n"
        "| 3 | 2 | |\n"
        "| 4 | | 2 |\n\n"
        "Answer: it shows 3 and 2.\n\n"
        "---\n\n"
        "## Task 1. Trace it\n\n"
        "Read the longer program.\n\n"
        "```python\n"
        "count = 3\n"
        "print(count)\n"
        "count = count - 1\n"
        "print(count)\n"
        "count = count - 1\n"
        "print(count)\n"
        "count = count - 1\n"
        "```\n\n"
        "First 4 rows are done. Complete the rest:\n\n"
        "| Line | count | output |\n"
        "|---|---|---|\n"
        "| 5: count = ? | | |\n"
        "| 6: output = ? | | |\n"
        "| 7: count = ? | | |\n\n"
        "What will the program show? Write here:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_trace5 = mo.ui.checkbox(label="Line 5: count = 0")
    chk_trace6 = mo.ui.checkbox(label="Line 6: output = 0")
    chk_trace7 = mo.ui.checkbox(label="Line 7: count = -1")
    chk_output = mo.ui.checkbox(label="Program shows: 3, 2, 1, 0")
    
    mo.vstack([chk_trace5, chk_trace6, chk_trace7, chk_output], gap=4)
    return (chk_trace5, chk_trace6, chk_trace7, chk_output)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()