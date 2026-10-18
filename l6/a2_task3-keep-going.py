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
        "## Task 3. Explorer task. Keep going + your limit\n\n"
        "### Part A: keep asking until 3 correct\n"
        "Check `correct` in the `while` line.\n\n"
        "Example output:\n"
        "```\n"
        "You answered 3 out of 5 correctly\n"
        "```\n\n"
        "Type your while line for Part A:\n"
        "(Write in your editor)\n\n"
        "### Part B: let the user choose the limit\n"
        "Before the game, ask for total questions.\n"
        "Or ask for total correct answers needed.\n\n"
        "Type your program for Part B:\n"
        "(Write in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    chk_while_correct = mo.ui.checkbox(label="Part A: `while correct < 3:` (stops at 3 correct)")
    chk_part_a = mo.ui.checkbox(label="Part A: tracks total questions asked (`questions` counter)")
    chk_part_a_output = mo.ui.checkbox(label="Part A: shows `You answered 3 out of X correctly`")
    chk_part_b_ask = mo.ui.checkbox(label="Part B: asks user for limit before game (`input()`)")
    chk_part_b_limit = mo.ui.checkbox(label="Part B: uses user limit in while condition")
    
    mo.vstack([chk_while_correct, chk_part_a, chk_part_a_output, chk_part_b_ask, chk_part_b_limit], gap=4)
    return (chk_while_correct, chk_part_a, chk_part_a_output, chk_part_b_ask, chk_part_b_limit)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()