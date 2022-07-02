# 5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
"""
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
"""

maths=int(input("Input the marks obtained in Mathematics :"))
physics=int(input("Input the marks obtained in Physics :"))
chemistry=int(input("Input the marks obtained in Chemistry :"))
print("Total marks of Maths, Physics and Chemistry : ",maths+physics+chemistry)
print("Total marks of Maths, Physics : ",maths+physics)
if maths>=65 and physics>=55 and chemistry>=50 and (maths+physics+chemistry)>=190 and (maths+physics)>=140:
    print("The candidate is eligible.")
else:
    print("The candidate is not eligible.")