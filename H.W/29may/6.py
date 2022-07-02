# Sort the above dictionary by the names of students.

data = {}

for i in range(10):
    key = input("Enter studant name : ")
    value = int(input("Enter marks : "))
    data.setdefault(key, value)
print(dict(sorted(data.items())))
