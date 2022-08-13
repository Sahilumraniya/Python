# 8. Make a Python program to day letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

s = input("Enter String : ")
d={}
for a in s:
    d.setdefault(a,s.day(a))
print(d)