# Sort the dictionary in ex-5 by the marks.

data = {}

for i in range(2):
    key = input("Enter studant name : ")
    value = int(input("Enter marks : "))
    data.setdefault(key, value)
# num = sorted(data.values())
# for n in num:
#     data.fromkeys(n)
# print(data)
