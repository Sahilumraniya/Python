# 3. Write a Python program to find the largest of three numbers. 

print("Test Data (Enter Three Number): ")
n1=int(input())
n2=int(input())
n3=int(input())
print("1st Number :",n1)
print("2nd Number :",n2)
print("3rd Number :",n3)
if n1>n2:
    if n2>n3:
        print(f"{n1} is the largest number.")
    else: print(f"{n3} is the largest number.")
else:
    if n2>n3:
        print(f"{n2} is the largest number.")
    else: print(f"{n3} is the largest number.")
    