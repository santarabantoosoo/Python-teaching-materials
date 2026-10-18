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
    # Practise using selection

    ## Task 2. favourite number

    **Start from this code:**

    ```python
    favourite = 13
    print("My favourite number is", favourite)
    ```

    ### Step 1: Make it a guessing game (توَقّع)

    Ask: `Guess my favourite number:`

    If correct show: `Amazing, that's right!`

    If wrong show: `Sorry, it's not <guess>` + `My favourite number is 13`

    **Hint:**
    - New variable: `guess`
    - Convert input to integer: `guess = int(input())`
    - Use `==` to compare

    **Type this code:**

    ```python
    favourite = 13
    print("Guess my favourite number:")
    guess = int(input())
    if               :
        print("Amazing, that's right!")
    else:
        print("Sorry, it's not", guess)
        print("My favourite number is", favourite)
    ```

    ### Step 2
    At the very end, always show:
    ```python
    print("Nice playing with you")
    ```
    It shows every time. Not only inside `if`.

    ### Step 3: Checklist
    Test with 13 and with 7. Tick:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_correct = mo.ui.checkbox(label="Correct guess shows the correct message?")
    chk_wrong = mo.ui.checkbox(label="Wrong guess shows the wrong-guess message?")
    chk_reveal = mo.ui.checkbox(label="Favourite number shown only when guess is wrong?")
    chk_goodbye = mo.ui.checkbox(label="Goodbye message always shown?")
    
    mo.vstack([chk_correct, chk_wrong, chk_reveal, chk_goodbye], gap=4)
    return (chk_correct, chk_wrong, chk_reveal, chk_goodbye)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()