# concepts learned

name = input("whats ur name?")

answer= int(input("1+2="))
if answer==3: 
   print("right")
else: 
   print("wrong")


## Choosing UI elemets 

button = mo.ui.button(
    kind="success",
    label="submit answer",
)
button


radio = mo.ui.radio(
    options=["Python", "JavaScript", "Rust"],
    value="Python",
    label="Radio Buttons",
)
radio


datetime_picker = mo.ui.datetime(
    value="2026-01-15T09:30",
    label="Datetime Picker",
)
datetime_picker


slider = mo.ui.slider(
    start=0,
    stop=100,
    step=5,
    value=50,
    show_value=True,
    label="Slider",
)
slider
