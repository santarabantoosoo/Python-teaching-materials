import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Times tables practice

    ## Task 3. Explorer task. Keep going + your limit

    ### Part A: keep asking until 3 correct
    Check `correct` in the `while` line.

    Example output:
    ```
    You answered 3 out of 5 correctly
    ```

    Type your while line for Part A:
    (Write in your editor)

    ### Part B: let the user choose the limit
    Before the game, ask for total questions.
    Or ask for total correct answers needed.

    Type your program for Part B:
    (Write in your editor)

    ### Checklist
    Test and tick:
    """)
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
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()