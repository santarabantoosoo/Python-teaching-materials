import marimo

__generated_with = "0.17.4"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.DataFrame({"name": ["Ada", "Grace", "Alan"], "score": [95, 88, 92]})
    df.head()
    return (df,)


if __name__ == "__main__":
    app.run()
