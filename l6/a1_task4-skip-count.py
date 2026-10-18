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
        "## Task 4. Skip counting upwards\n\n"
        "Start from 1.\n"
        "Skip count in 3s: 1, 4, 7, 10, 13, 16, 19.\n"
        "Stop after 19.\n\n"
        "### Rule\n"
        "Change 3 lines:\n"
        "1. Where counting starts.\n"
        "2. How `count` changes each time.\n"
        "3. The `while` condition.\n\n"
        "If it never stops, press Stop or Ctrl+C.\n\n"
        "Type your skip-counting program:\n"
        "(Write in your editor)\n\n"
        "Run it. What did you see? Write here:\n"
        "(Write output in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_start1 = mo.ui.checkbox(label="Starts from 1 (`count = 1`)")
    chk_step3 = mo.ui.checkbox(label="Increments by 3 (`count = count + 3`)")
    chk_condition = mo.ui.checkbox(label="Correct condition: `while count <= 19:`")
    chk_prints = mo.ui.checkbox(label="Prints: 1, 4, 7, 10, 13, 16, 19")
    chk_stop = mo.ui.checkbox(label="Stops after 19 (no infinite loop)")
    
    mo.vstack([chk_start1, chk_step3, chk_condition, chk_prints, chk_stop], gap=4)
    return (chk_start1, chk_step3, chk_condition, chk_prints, chk_stop)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()