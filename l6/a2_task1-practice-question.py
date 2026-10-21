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

    ## Worked example. Countdown
    ```python
    count = 10
    while count >= 1:
        print(count)
        count = count - 1
    print("Lift off")
    ```

    `count` starts at 10. Goes down by 1 each time. Loop continues while `count` is at least 1.

    ## Worked example. Ten sixes
    ```python
    from random import randint
    rolls = 0
    sixes = 0
    while sixes < 10:
        dice = randint(1,6)
        print(dice)
        if dice == 6:
            sixes = sixes + 1
        rolls = rolls + 1
    print("Ten sixes in", rolls, "dice rolls")
    ```

    Two counters: `rolls` and `sixes`.

    ---

    ## Task 1. A practice question

    ### Step 1
    Put lines 2 to 11 inside a loop:
    ```python
    while True:
    ```
    `True` means repeat forever. Indent all lines inside.

    Type your while True program (first lines):
    (Write in your editor)

    ### Step 2
    Run it. It never stops. Press Stop or Ctrl+C to end it.

    What did you see? Write here:
    (Write output in your editor)

    ### Step 3
    Add a counter: `questions`. Give it a start value. Add 1 each time. Show it inside the loop:
    ```python
        print("Question", questions)
    ```

    Type the two lines you added for questions:
    (Write in your editor)

    ### Step 4
    Ask exactly 3 questions. Change `True` to a check on `questions`. Continue only if 3 or fewer asked.

    Type your final while line + full program:
    (Write in your editor)

    ### Checklist
    Red error (خطأ)? Fix it (صلّحه). Tick what you found:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    chk_while_true = mo.ui.checkbox(label="Uses `while True:` to repeat forever")
    chk_indent = mo.ui.checkbox(label="All lines indented inside while")
    chk_counter = mo.ui.checkbox(label="Adds `questions` counter with start value + increment")
    chk_print_q = mo.ui.checkbox(label="Shows `print(\"Question\", questions)` inside loop")
    chk_limit3 = mo.ui.checkbox(label="Changes condition to `while questions <= 3:` (or `< 4`)")
    chk_spelling = mo.ui.checkbox(label="Misspelt `while` or `True`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:`")
    
    mo.vstack([chk_while_true, chk_indent, chk_counter, chk_print_q, chk_limit3, chk_spelling, chk_colon], gap=4)
    return (chk_while_true, chk_indent, chk_counter, chk_print_q, chk_limit3, chk_spelling, chk_colon)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()