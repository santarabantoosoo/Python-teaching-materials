import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Envelop with money. Let's start.
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    osama = 100
    mousa = 100
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  Ask baraa for money
    """)
    return


@app.cell
def _():
    baraa = int(input("how much money?"))
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Compare the values
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check the type
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Other possibilities
    """)
    return


@app.cell
def _(mo):
    mo.image("l4/operators.png")  # run marimo from the repo root so this path resolves
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Using if - who has more money?
    """)
    return


app._unparsable_cell(
    r"""
    if : 
    print("baraa has more money")
    """,
    name="_"
)


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
