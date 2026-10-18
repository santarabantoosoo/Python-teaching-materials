import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "# Explorer task. Temperature\n\n"
        "Read the start:\n\n"
        "```python\n"
        "from weather import temperature\n"
        "print(\"Where do you live?\")\n"
        "location = input()\n"
        "temp = temperature(location)\n"
        "```\n\n"
        "The temperature comes from the internet. It is not always the same.\n\n"
        "### \U0001f527 Workaround: `weather` module not installed?\n"
        "Copy this at the **top of your file** to make it run locally:\n\n"
        "```python\n"
        "# --- MOCK weather module (paste at top) ---\n"
        "def temperature(location):\n"
        '    """Return a fake temperature for testing."""\n'
        "    location = location.lower()\n"
        "    if \"nuuk\" in location or \"greenland\" in location:\n"
        "        return -5.0\n"
        "    if \"cairo\" in location or \"egypt\" in location:\n"
        "        return 32.0\n"
        "    if \"london\" in location or \"uk\" in location:\n"
        "        return 12.0\n"
        "    if \"dubai\" in location or \"uae\" in location:\n"
        "        return 38.0\n"
        "    return 20.0  # default\n"
        "# -------------------------------------------\n"
        "```\n\n"
        "### Step 1\n"
        "Show a message for each temperature range.\n\n"
        "**Example:**\n"
        "| You type | Program shows |\n"
        "|---|---|\n"
        "| `Nuuk` | `Current temperature in Nuuk is -5.0` + `It's freezing cold` |\n\n"
        "**Type your program:**\n"
        "(Write it in your editor, including the mock at the top)\n\n"
        "**Run it. What did you see? Write here:**\n"
        "(Write output in your editor)\n\n"
        "### Checklist\n"
        "Test and tick:"
    )
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
    mo.md(
        "---\n"
        "**Good luck! \U0001f389**"
    )
    return


if __name__ == "__main__":
    app.run()