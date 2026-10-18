import marimo

__generated_with = "0.17.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Practise using selection

    ## Task 1. Trip critic

    **Goal:** Ask for the favourite trip. React to one special trip. Otherwise show a generic comment.

    ### Examples

    | Program asks | You type | Program shows |
    |---|---|---|
    | `Best trip ever?` | `The castle` | `The castle is not too bad` |
    | `Best trip ever?` | `Aqua park` | `Aqua park is my favourite too!` |

    ### Step 1: Type this code

    ```python
    print("Best trip ever?")
    trip = input()
    if               :
        print(trip, "is not too bad")
    else:
        print(trip, "is my favourite too!")
    ```

    ### Step 2: Complete line 3 using `==` to check equality

    ### Step 3: Indent the lines that belong inside `if` / `else`

    ### Step 4: Run it. Test twice.
    - Once with `The castle`
    - Once with `Aqua park`

    **Red error (خطأ)? Fix it (صلّحه).** Tick what you found:
    """)
    return


@app.cell
def _(mo):
    # Interactive checklist for common errors - using individual checkboxes
    chk_spelling = mo.ui.checkbox(label="Misspelt `if` or `else`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:` after `if` or `else`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside `if` / `else`")
    chk_indent_wrong = mo.ui.checkbox(label="Indented `if` or `else` by mistake")
    chk_equal = mo.ui.checkbox(label="Used `=` instead of `==`")
    chk_quotes_var = mo.ui.checkbox(label="Used quotes around a variable name")
    chk_quotes_str = mo.ui.checkbox(label="Forgot quotes around a word like `\"BFG\"`")
    
    mo.vstack([
        chk_spelling, chk_colon, chk_indent, chk_indent_wrong,
        chk_equal, chk_quotes_var, chk_quotes_str
    ], gap=4)
    return (chk_spelling, chk_colon, chk_indent, chk_indent_wrong, chk_equal, chk_quotes_var, chk_quotes_str)


@app.cell
def _(mo):
    # Code editor for the student to write their solution
    code_editor = mo.ui.text_area(
        value='print("Best trip ever?")\ntrip = input()\nif trip == "Aqua park":\n    print(trip, "is my favourite too!")\nelse:\n    print(trip, "is not too bad")',
        label="Your solution (edit and click Run)",
        rows=12,
        code=True,
    )
    code_editor
    return (code_editor,)


@app.cell
def _(mo):
    # Run button
    run_button = mo.ui.run_button(label="▶ Run code")
    run_button
    return (run_button,)


@app.cell
def _(run_button, code_editor, mo):
    # Execute the student's code when button is clicked
    if run_button.value:
        mo.output.append(mo.md("### Output"))
        try:
            # Create a namespace for execution
            namespace = {}
            exec(code_editor.value, namespace)
        except Exception as e:
            mo.output.append(mo.md(f"**Error:** `{type(e).__name__}: {e}`"))
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()