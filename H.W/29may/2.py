# Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

s = set()
n = int(input("Enter number which you want to store in set : "))
for i in range(n):
    element = int(input(f"Enter {i} number in set : "))
    # if element == (item for item in s):
    for i in s:
        if element == i:
            print("This element present in set")
    # print("This is already")
    # else:
    s.add(element)
print(s)
print(type(s))
