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
        "## Task 5. Explorer task. The element of time\n\n"
        "Add a one-second pause between numbers.\n\n"
        "First line:\n"
        "```python\n"
        "from time import sleep\n"
        "```\n\n"
        "Inside the loop:\n"
        "```python\n"
        "    sleep(1)\n"
        "```\n\n"
        "Type your program with sleep:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_import = mo.ui.checkbox(label="Imports sleep: `from time import sleep`")
    chk_inside = mo.ui.checkbox(label="Calls `sleep(1)` inside the loop")
    chk_indent = mo.ui.checkbox(label="`sleep(1)` is indented (inside while)")
    chk_pause = mo.ui.checkbox(label="Program pauses 1 second between numbers")
    
    mo.vstack([chk_import, chk_inside, chk_indent, chk_pause], gap=4)
    return (chk_import, chk_inside, chk_indent, chk_pause)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()