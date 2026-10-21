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
    # People in space

    ## Worked example. Weather
    Read this program.

    ```python
    print("What's the weather like?")
    weather = input()
    print(advice)
    ```

    It gives clothing advice. Test it once for every branch.
    Use `if` / `elif` / `else`.

    ---

    ## Task 1. People in space

    Read the short program.

    ```python
    from space import people
    number = people()
    print(number, "people in space right now")
    ```

    The number comes from the internet. It is not always the same.

    ### 🔧 Workaround: `space` module not installed?
    Copy this at the **top of your file** to make it run locally:

    ```python
    # --- MOCK space module (paste at top) ---
    def people():
        "\""Return a fake number of people in space for testing."\""
        return 7  # Change this to test different scenarios
    # -------------------------------------------
    ```

    ### Step 1
    Ask the user to guess (توقع).
    Ask: `How many people do you think are in space right now?`
    Keep all 3 lines. Only add lines.

    **New variable:** `guess`.
    **Convert to integer:** `guess = int(input())`

    **Type the lines you added:**
    (Write them in your editor)

    ### Step 2
    Compare `number` with `guess`. Three branches:

    | Guess | Real | Output |
    |---|---|---|
    | 8 | 8 | `That's right!` + `8 people in space right now` |
    | 5 | 8 | `It's actually more than that` + `8 people in space right now` |
    | 9 | 8 | `It's actually fewer than that` + `8 people in space right now` |

    **Use:** `if` / `elif` / `else`. Use `==`, `<`, `>`.

    **Type your full program:**
    (Write it in your editor, including the mock at the top)

    **Red error (خطأ)? Fix it (صلّّحه).** Tick what you found:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_spelling = mo.ui.checkbox(label="Misspelt `if` or `else`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside the branch")
    chk_equal = mo.ui.checkbox(label="Used `=` instead of `==")
    chk_quotes = mo.ui.checkbox(label="Quote mistake (variable vs word like `\"snowy\"`)")
    
    mo.vstack([chk_spelling, chk_colon, chk_indent, chk_equal, chk_quotes], gap=4)
    return (chk_spelling, chk_colon, chk_indent, chk_equal, chk_quotes)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()