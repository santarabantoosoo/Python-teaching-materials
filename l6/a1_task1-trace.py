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

    ## Worked example
    What will this program show?

    ```python
    count = 3
    print(count)
    count = count - 1
    print(count)
    ```

    Use a trace table. Track the line, the value, and the Output (الناتج).

    | line | count | output |
    |---|---|---|
    | 1 | 3 | |
    | 2 | | 3 |
    | 3 | 2 | |
    | 4 | | 2 |

    Answer: it shows 3 and 2.

    ---

    ## Task 1. Trace it

    Read the longer program.

    ```python
    count = 3
    print(count)
    count = count - 1
    print(count)
    count = count - 1
    print(count)
    count = count - 1
    ```

    First 4 rows are done. Complete the rest:

    | Line | count | output |
    |---|---|---|
    | 5: count = ? | | |
    | 6: output = ? | | |
    | 7: count = ? | | |

    What will the program show? Write here:
    (Write in your editor)

    ### Checklist
    Test and tick:
    """)
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
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()