x = 5

def change_x():
    global x
    x = 10  # Now we are changing global var x
    print("Inside of the function:", x)

change_x()
print("Outside:", x)  # 10 (Global var x changed)
