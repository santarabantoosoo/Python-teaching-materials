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

    ## Task 2. Explorer task. Measure performance

    Add a counter: `correct`.
    Give it a start value.
    Add 1 each time the answer is right.

    At the end show:
    ```python
    print("You answered", correct, "out of", questions, "correctly")
    ```

    Type your program with correct counter:
    (Write in your editor)

    ### Checklist
    Test and tick:
    """)
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
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()