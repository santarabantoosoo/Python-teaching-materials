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


## questions for the app 

### math

1- 2×2=4
2- 4×5=20
3- 6×2=12
4- 2×8=16
5- 5×3=15
6- 6×1=6
7- 7×3=21
8- 4×7=42
9- 10×2=20
10- 6×4=24


### science

1- ماهي عاصمة إنجلترا (لندن)

2- أين يقع لسان المزمار (أعلى الجهاز التنفسي)

3- أين تقع قناة ستاكيوس (في الأذن)

4- كم يستغرق نمو الطماطم 
(6أشهر)