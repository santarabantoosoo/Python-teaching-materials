# concepts learned

name = input("whats ur name?")

answer= int(input("1+2="))
if answer==3: 
   print("right")
else: 
   print("wrong")


## Choosing UI elemets 

radio = mo.ui.radio(
    options=["Python", "Scratch", "R"],
    value="Python",
    label="Radio Buttons",
)
radio


button = mo.ui.button(
    kind="success",
    label="Submit answer",
)
button