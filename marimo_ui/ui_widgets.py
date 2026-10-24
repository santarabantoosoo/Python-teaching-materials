# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas",
#     "altair",
#     "plotly",
#     "matplotlib",
#     "anywidget",
#     "traitlets",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Marimo UI Widgets Reference

    ## 1. Text & Code Inputs
    """)
    return


@app.cell
def _(mo):
    text_input = mo.ui.text(
        value="",
        placeholder="Type your name...",
        label="Text Input",
    )
    text_input
    return (text_input,)


@app.cell
def _(mo):
    text_area = mo.ui.text_area(
        value="",
        placeholder="Write a longer message here...",
        rows=4,
        label="Text Area",
    )
    text_area
    return (text_area,)


@app.cell
def _(mo):
    code_editor = mo.ui.code_editor(
        value='def greet(name):\n    return f"Hello, {name}!"',
        language="python",
        label="Code Editor",
    )
    code_editor
    return (code_editor,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2. Number & Slider Inputs
    """)
    return


@app.cell
def _(mo):
    number_input = mo.ui.number(
        start=0,
        stop=100,
        step=1,
        value=10,
        label="Number Input",
    )
    number_input
    return (number_input,)


@app.cell
def _(mo):
    slider = mo.ui.slider(
        start=0,
        stop=100,
        step=5,
        value=50,
        show_value=True,
        label="Slider",
    )
    slider
    return (slider,)


@app.cell
def _(mo):
    range_slider = mo.ui.range_slider(
        start=0,
        stop=100,
        step=5,
        value=[20, 80],
        show_value=True,
        label="Range Slider",
    )
    range_slider
    return (range_slider,)


@app.cell
def _(mo):
    matrix = mo.ui.matrix(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        min_value=-10,
        max_value=10,
        step=1,
        label="Matrix Input",
    )
    matrix
    return (matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. Boolean & Selection Inputs
    """)
    return


@app.cell
def _(mo):
    checkbox = mo.ui.checkbox(
        value=True,
        label="Checkbox",
    )
    checkbox
    return (checkbox,)


@app.cell
def _(mo):
    switch = mo.ui.switch(
        value=False,
        label="Switch",
    )
    switch
    return (switch,)


@app.cell
def _(mo):
    radio = mo.ui.radio(
        options=["Python", "JavaScript", "Rust"],
        value="Python",
        label="Radio Buttons",
    )
    radio
    return (radio,)


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(
        options=["Apple", "Banana", "Cherry", "Mango"],
        value="Apple",
        searchable=True,
        label="Dropdown",
    )
    dropdown
    return (dropdown,)


@app.cell
def _(mo):
    multiselect = mo.ui.multiselect(
        options=["Red", "Green", "Blue", "Yellow"],
        value=["Red", "Blue"],
        label="Multiselect",
    )
    multiselect
    return (multiselect,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. Buttons & Triggers
    """)
    return


@app.cell
def _(mo):
    button = mo.ui.button(
        value=0,
        on_click=lambda count: count + 1,
        kind="success",
        label="Click Me",
    )
    button
    return (button,)


@app.cell
def _(mo):
    run_button = mo.ui.run_button(
        kind="warn",
        label="Run Action",
    )
    run_button
    return (run_button,)


@app.cell
def _(mo):
    refresh = mo.ui.refresh(
        options=["1s", "5s", "10s", "30s"],
        label="Auto Refresh",
    )
    refresh
    return (refresh,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. Date & Time Inputs
    """)
    return


@app.cell
def _(mo):
    date_picker = mo.ui.date(
        value="2026-01-15",
        label="Date Picker",
    )
    date_picker
    return (date_picker,)


@app.cell
def _(mo):
    datetime_picker = mo.ui.datetime(
        value="2026-01-15T09:30",
        label="Datetime Picker",
    )
    datetime_picker
    return (datetime_picker,)


@app.cell
def _(mo):
    date_range_picker = mo.ui.date_range(
        value=("2026-01-01", "2026-01-31"),
        label="Date Range Picker",
    )
    date_range_picker
    return (date_range_picker,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 6. File & Media Inputs
    """)
    return


@app.cell
def _(mo):
    file_upload = mo.ui.file(
        filetypes=[".csv", ".txt", ".json"],
        multiple=False,
        kind="area",
        label="Upload a File",
    )
    file_upload
    return (file_upload,)


@app.cell
def _(mo):
    file_browser = mo.ui.file_browser(
        selection_mode="file",
        multiple=True,
        label="File Browser",
    )
    file_browser
    return (file_browser,)


@app.cell
def _(mo):
    microphone = mo.ui.microphone(
        label="Record Audio",
    )
    microphone
    return (microphone,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 7. Tables & DataFrames
    """)
    return


@app.cell
def _(mo):
    table = mo.ui.table(
        data=[
            {"student": "Alice", "score": 95, "passed": True},
            {"student": "Bob", "score": 82, "passed": True},
            {"student": "Charlie", "score": 68, "passed": False},
        ],
        selection="multi",
        label="Interactive Table",
    )
    table
    return (table,)


@app.cell
def _(mo):
    data_editor = mo.ui.data_editor(
        data=[
            {"item": "Notebook", "price": 4.5, "qty": 2},
            {"item": "Pencil", "price": 1.0, "qty": 5},
        ],
        label="Editable Data Table",
    )
    data_editor
    return (data_editor,)


@app.cell
def _(mo):
    import pandas as pd

    sample_df = pd.DataFrame(
        {
            "city": ["Cairo", "London", "Tokyo", "Paris"],
            "temp_c": [28, 16, 22, 19],
            "humidity": [40, 75, 65, 70],
        }
    )
    dataframe_widget = mo.ui.dataframe(sample_df)
    dataframe_widget
    return dataframe_widget, pd, sample_df


@app.cell
def _(mo, sample_df):
    data_explorer = mo.ui.data_explorer(sample_df)
    data_explorer
    return (data_explorer,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 8. Interactive Charts
    """)
    return


@app.cell
def _(mo, sample_df):
    import altair as alt

    altair_chart = mo.ui.altair_chart(
        alt.Chart(sample_df)
        .mark_bar()
        .encode(x="city", y="temp_c", color="city")
    )
    altair_chart
    return alt, altair_chart


@app.cell
def _(mo, sample_df):
    import plotly.express as px

    plotly_chart = mo.ui.plotly(
        px.scatter(
            sample_df,
            x="temp_c",
            y="humidity",
            text="city",
            title="Temperature vs Humidity",
        )
    )
    plotly_chart
    return plotly_chart, px


@app.cell
def _(mo):
    import matplotlib.pyplot as plt

    fig_mpl, ax_mpl = plt.subplots(figsize=(5, 3))
    ax_mpl.plot([1, 2, 3, 4], [10, 20, 15, 30], marker="o")
    ax_mpl.set_title("Interactive Matplotlib Plot")
    matplotlib_chart = mo.ui.matplotlib(ax_mpl)
    matplotlib_chart
    return ax_mpl, fig_mpl, matplotlib_chart, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 9. Containers, Forms & Composite Widgets
    """)
    return


@app.cell
def _(mo):
    tabs = mo.ui.tabs(
        {
            "Tab 1": mo.md("Content inside **Tab 1**"),
            "Tab 2": mo.ui.slider(0, 10, value=5, label="Slider inside Tab 2"),
        }
    )
    tabs
    return (tabs,)


@app.cell
def _(mo):
    array_widget = mo.ui.array(
        [
            mo.ui.text(placeholder="Item 1"),
            mo.ui.text(placeholder="Item 2"),
            mo.ui.slider(1, 10, value=5),
        ],
        label="Array of Widgets",
    )
    array_widget
    return (array_widget,)


@app.cell
def _(mo):
    dictionary_widget = mo.ui.dictionary(
        {
            "name": mo.ui.text(placeholder="Student name"),
            "age": mo.ui.number(start=5, stop=18, value=12),
            "active": mo.ui.checkbox(value=True),
        },
        label="Dictionary of Widgets",
    )
    dictionary_widget
    return (dictionary_widget,)


@app.cell
def _(mo):
    batch_widget = mo.md(
        """
        **Student Profile**
        - Name: {name}
        - Favorite Subject: {subject}
        """
    ).batch(
        name=mo.ui.text(placeholder="Enter name"),
        subject=mo.ui.dropdown(["Math", "Science", "Coding"], value="Coding"),
    )
    batch_widget
    return (batch_widget,)


@app.cell
def _(mo):
    form_widget = (
        mo.md(
            """
            **Submit Feedback**
            - Rating: {rating}
            - Comment: {comment}
            """
        )
        .batch(
            rating=mo.ui.slider(1, 5, value=5, show_value=True),
            comment=mo.ui.text(placeholder="Your thoughts..."),
        )
        .form(submit_button_label="Submit Form")
    )
    form_widget
    return (form_widget,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 10. Chat & Custom AnyWidget
    """)
    return


@app.cell
def _(mo):
    chat_widget = mo.ui.chat(
        lambda messages, config: f"Echo: {messages[-1].content}",
        prompts=["Hello!", "What can you do?"],
    )
    chat_widget
    return (chat_widget,)


@app.cell
def _(mo):
    import anywidget
    import traitlets

    class CounterAnyWidget(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const btn = document.createElement("button");
          btn.style.padding = "6px 12px";
          btn.textContent = "Custom Counter: " + model.get("count");
          btn.onclick = () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
          };
          model.on("change:count", () => {
            btn.textContent = "Custom Counter: " + model.get("count");
          });
          el.appendChild(btn);
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    custom_anywidget = mo.ui.anywidget(CounterAnyWidget())
    custom_anywidget
    return CounterAnyWidget, anywidget, custom_anywidget, traitlets


if __name__ == "__main__":
    app.run()
