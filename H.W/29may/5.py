# Ask user to give name and marks of 10 different students. Store them in dictionary.

data={}

for i in range(10):
    key=input("Enter studant name : ")
    value=int(input("Enter marks : "))
    data.setdefault(key,value)
print(data)