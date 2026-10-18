import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Explorer task. Temperature

    Read the start:

    ```python
    from weather import temperature
    print("Where do you live?")
    location = input()
    temp = temperature(location)
    ```

    The temperature comes from the internet. It is not always the same.

    ### Step 1
    Show a message for each temperature range.

    **Example:**
    | You type | Program shows |
    |---|---|
    | `Nuuk` | `Current temperature in Nuuk is -5.0` + `It's freezing cold` |

    **Type your program:**
    (Write it in your editor)

    **Run it. What did you see? Write here:**
    (Write output in your editor)

    ### Checklist
    Test and tick:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_cold = mo.ui.checkbox(label="Freezing cold message for negative temps?")
    chk_cool = mo.ui.checkbox(label="Cool message for 0-15?")
    chk_warm = mo.ui.checkbox(label="Warm message for 15-25?")
    chk_hot = mo.ui.checkbox(label="Hot message for 25+?")
    chk_print_temp = mo.ui.checkbox(label="Prints 'Current temperature in <location> is <temp>'?")
    chk_input = mo.ui.checkbox(label="Used input() for location?")
    chk_elif = mo.ui.checkbox(label="Used if / elif / else correctly?")
    
    mo.vstack([
        chk_cold, chk_cool, chk_warm, chk_hot,
        chk_print_temp, chk_input, chk_elif
    ], gap=4)
    return (chk_cold, chk_cool, chk_warm, chk_hot, chk_print_temp, chk_input, chk_elif)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()