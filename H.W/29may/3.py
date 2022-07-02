# Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

l1=[]
for i in range(10):
    num=int(input("Enetr number : "))
    l1.append(num)
l2=l1.copy()
l2.reverse()
print(l1)
print(l2)