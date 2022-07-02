# 4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.

x = int(input("X-coordinate : "))
y = int(input("Y-coordinate : "))
if x > 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the First quadrant.")
elif x < 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the Second quadrant.")
elif x < 0 and y < 0:
    print(f"The coordinate point ({x},{y}) lies in the Thrid quadrant.")
else:
    print(f"The coordinate point ({x},{y}) lies in the Fourth quadrant.")