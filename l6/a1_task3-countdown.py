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
    # Count

    ## Task 3. Countdown

    ### Step 1
    Change one line. Start from 10, not from 3.

    ```python
    count = 10
    while count >= 1:
        print(count)
        count = count - 1
    ```

    ### Step 2
    Add one line at the end:

    ```python
    print("Lift off!")
    ```

    It runs after the loop. Do not indent it.

    ### Checklist
    Test and tick:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    chk_start10 = mo.ui.checkbox(label="Starts from 10 (`count = 10`)")
    chk_prints10to1 = mo.ui.checkbox(label="Prints 10 down to 1")
    chk_liftoff = mo.ui.checkbox(label="Shows `Lift off!` after loop (not indented)")
    chk_condition = mo.ui.checkbox(label="Correct condition: `while count >= 1:`")

    mo.vstack([chk_start10, chk_prints10to1, chk_liftoff, chk_condition], gap=4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()
