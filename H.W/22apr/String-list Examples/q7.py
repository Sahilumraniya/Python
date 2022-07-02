# 7. Ask 10 numbers from the user and store them in a list. Now, ask user to enter a number between 1 to 10. Delete the element present at that index number and print the list. Now aks user to enter the number that he/she wants to delete. Delete that number itself from the list and print the resultant list.

i=0
li=[]
while i<10:
    n=int(input("Enter Number : "))
    li.insert(i, n)
    i+=1
print(li)
n=int(input("Enter Index Which You Want : "))
li.pop(n)
print(li)
n=int(input("Enter Number Which You Want : "))
li.remove(n)
print(li)
