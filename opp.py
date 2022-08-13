class Employees:
    leves=8
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def displayDetails(self):
        print(f"--------------- Details of {self.name} ---------------")
        print("Age : ",self.age)
        print("Gender : ",self.gender)

class Manger(Employees):
    education="MBA"
    def __init__(self, name, age, gender,experience):
        super().__init__(name,age,gender)
        self.experience=experience

    def displayDetails(self):
        super().displayDetails()
        print("Education : ",self.education)
        print("Experience : ",self.experience)

    @classmethod
    def addEmployee(cls):
        print("Enter Following Details")
        name=input("Enter employee's name : ")
        age=int(input("Enter age : "))
        gender=input("Enter gender : ")
        experssion=int(input("Enter experssion : "))
        return cls(name,age,gender,experssion)
        

class SalesExecutive(Employees):
    target=1500000

    def __init__(self,name,age,gender,territory):
        super().__init__(name,age,gender)
        self.territory=territory
    
    def displayDetails(self):
        super().displayDetails()
        print("Target : ",self.target)
        print("Territory : ",self.territory)

    @classmethod
    def addEmployee(cls):
        print("Enter Following Details")
        name=input("Enter employee's name : ")
        age=int(input("Enter age : "))
        gender=input("Enter gender : ")
        territory=input("Enter territory : ")
        return cls(name,age,gender,territory)

emp_list=[]
e=Manger("Sahil",18,"male",2)
emp_list.append(e)
while True:
    print("----------------------------------")
    print("0 for exit")
    print("1 for Add employee")
    print("2 for Display employee's details")
    print("3 for Delect employee")
    print("----------------------------------")
    ch=int(input("Enetr your choice : "))
    if ch==0:
        break
    elif ch==1:
        print("M for add manger employee")
        print("SE for add SalesExecutive employee")
        emp=input("Enetr your choice : ").lower()
        type_lookup={"m":Manger.addEmployee,"se":SalesExecutive.addEmployee}
        # new_emp=type_lookup[emp]()
        # emp_list.append(new_emp)
        emp_list.append(type_lookup[emp]())
        print("Employee is success fully add")

    elif ch==2:
        sr=0
        print("Sr.no\tname")
        for employee in emp_list:
            print(f"{sr}\t{employee.name}")
            sr+=1
        sr_no=int(input("Enetr Sr.No : "))
        emp_list[sr_no].displayDetails()
    elif ch==3:
        sr=0
        print("Sr.no\tname")
        for employee in emp_list:
            print(f"{sr}\t{employee.name}")
            sr+=1
        sr_no=int(input("Enetr Sr.No : "))
        emp_list.pop(sr_no)
        
    else:
        print("You enter worng choice : ")