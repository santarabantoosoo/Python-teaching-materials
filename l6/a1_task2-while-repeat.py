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

    ## Task 2. Repeat with while

    Same actions again and again. Use `while` to repeat.

    ### Step 1
    Copy and paste this in your editor.

    ```python
    count = 3
    while              :
        print(count)
        count = count - 1
    ```

    ### Step 2
    Pick the right condition and add it to your code. Last value printed must be 1.

    - `while count > 1:`
    - `while count >= 1:`
    - `while count < 1:`
    - `while count == 1:`

    ### Checklist
    Red error (خطأ)? Fix it (صلّحه). Tick what you found:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    chk_spelling = mo.ui.checkbox(label="Misspelt `while`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside `while`")
    chk_condition = mo.ui.checkbox(label="Correct condition: `while count >= 1:`")

    mo.vstack([chk_spelling, chk_colon, chk_indent, chk_condition], gap=4)
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
