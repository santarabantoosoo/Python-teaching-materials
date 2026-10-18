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

    ## Task 1. Trip critic

    **Goal:** Ask for the favourite trip. React to one special trip. Otherwise show a generic comment.

    ### Examples

    | Program asks | You type | Program shows |
    |---|---|---|
    | `Best trip ever?` | `The castle` | `The castle is not too bad` |
    | `Best trip ever?` | `Aqua park` | `Aqua park is my favourite too!` |

    ### Steps to complete:

    **Step 1:** Write code that asks `Best trip ever?` and stores the answer in a variable called `trip`

    **Step 2:** Write an `if` statement that checks if `trip` equals `"Aqua park"` (use `==`)

    **Step 3:** Inside the `if`, print: `trip + " is my favourite too!"`

    **Step 4:** Add an `else` that prints: `trip + " is not too bad"`

    **Step 5:** Run it. Test twice:
    - Once with `The castle`
    - Once with `Aqua park`

    **Red error (خطأ)? Fix it (صلّحه).** Tick what you found:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_spelling = mo.ui.checkbox(label="Misspelt `if` or `else`")
    chk_colon = mo.ui.checkbox(label="Forgot the colon `:` after `if` or `else`")
    chk_indent = mo.ui.checkbox(label="Forgot to indent inside `if` / `else`")
    chk_indent_wrong = mo.ui.checkbox(label="Indented `if` or `else` by mistake")
    chk_equal = mo.ui.checkbox(label="Used `=` instead of `==")
    chk_quotes_var = mo.ui.checkbox(label="Used quotes around a variable name")
    chk_quotes_str = mo.ui.checkbox(label="Forgot quotes around a word like `\"BFG\"`")
    
    # vstack MUST be the last expression to display
    mo.vstack([
        chk_spelling, chk_colon, chk_indent, chk_indent_wrong,
        chk_equal, chk_quotes_var, chk_quotes_str
    ], gap=4)
    return (chk_spelling, chk_colon, chk_indent, chk_indent_wrong, chk_equal, chk_quotes_var, chk_quotes_str)


@app.cell
def _(mo):
    # Code editor - skeleton for students to fill in (VISIBLE)
    code_editor = mo.ui.code_editor(
        value='# Step 1: Ask for the trip\n# print("Best trip ever?")\n# trip = input()\n\n# Step 2: Check if trip is "Aqua park"\n# if trip == "Aqua park":\n\n# Step 3: Print special message\n#     print(trip + " is my favourite too!")\n\n# Step 4: Else print generic message\n# else:\n#     print(trip + " is not too bad")',
        label="Write your code here (uncomment and complete each step)",
        language="python",
    )
    code_editor
    return (code_editor,)


@app.cell(hide_code=True)
def _(mo):
    # Run button - must be last expression to display
    run_button = mo.ui.run_button(label="▶ Run code")
    run_button
    return (run_button,)


@app.cell(hide_code=True)
def _(run_button, code_editor, mo):
    # Execute the student's code when button is clicked
    if run_button.value:
        mo.output.append(mo.md("### Output"))
        try:
            namespace = {}
            exec(code_editor.value, namespace)
        except Exception as e:
            mo.output.append(mo.md(f"**Error:** `{type(e).__name__}: {e}`"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ### ✅ Solution (click to reveal)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Collapsible solution - accordion must be last expression
    solution = mo.ui.accordion(
        {
            "Show solution": mo.md("""
    ```python
    print("Best trip ever?")
    trip = input()
    if trip == "Aqua park":
        print(trip + " is my favourite too!")
    else:
        print(trip + " is not too bad")
    ```
    """)
        }
    )
    solution
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