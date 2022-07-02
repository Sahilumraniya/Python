"""9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]"""

d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
output = []

values = list(d.values())
print(values[1])
for index in range(len(values[1])):
    data = {}
    for key in d:
        data[key] = d[key][index]
    output.append(data)

print(output)
