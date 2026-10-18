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

    ## Explorer task. Eligible to vote

    Ask for the age. Say if the user can vote.

    **Rule:** 18 or over can vote.

    ### Examples

    | Program asks | You type | Program shows |
    |---|---|---|
    | `How old are you?` | `21` | `You are eligible to vote` |
    | `How old are you?` | `14` | `You are not eligible to vote` `4 more years to go` |

    ### Step 1: Write your program

    Run it. Test twice: with `21` and with `14`.

    ### Checklist
    Test and tick:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Interactive checklist for common errors
    chk_eligible = mo.ui.checkbox(label="Age 21 shows 'eligible to vote'?")
    chk_not_eligible = mo.ui.checkbox(label="Age 14 shows 'not eligible to vote'?")
    chk_years = mo.ui.checkbox(label="Shows correct years to go (e.g., 4 for age 14)?")
    chk_indent = mo.ui.checkbox(label="Lines inside if/else are indented?")
    chk_colon = mo.ui.checkbox(label="Colon : after if and else?")
    chk_equal = mo.ui.checkbox(label="Used >= or > correctly?")
    chk_input = mo.ui.checkbox(label="Used int(input()) for age?")
    
    mo.vstack([
        chk_eligible, chk_not_eligible, chk_years,
        chk_indent, chk_colon, chk_equal, chk_input
    ], gap=4)
    return (chk_eligible, chk_not_eligible, chk_years, chk_indent, chk_colon, chk_equal, chk_input)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Good luck! 🎉**
    """)
    return


if __name__ == "__main__":
    app.run()