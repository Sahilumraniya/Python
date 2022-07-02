# 6. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order. Now print both the lists.

i=0
li=[]
while i<10:
    n=int(input("Enter Number : "))
    li.insert(i, n)
    i+=1
print(li)
print(li[::-1])