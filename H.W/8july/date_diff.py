"""
def date_diff(day1,mount1,day2,mounth2):
    day=0
    for i in range(mount1,mounth2):
        if i%2==0 and i!=8 and i!=2:
            for j in range(0,30):
                day+=1
        elif i==2:
            for j in range(0,28):
                day+=1
        else:
            for j in range(0,31):
                day+=1
    return (day-day1+day2)

day1=int(input("Enter Starting date : "))
mount1=int(input("Enter Starting mounth : "))
day2=int(input("Enter Ending date : "))
mount2=int(input("Enter Ending mounth : "))
print(date_diff(day1,mount1,day2,mount2))
"""
def date_diff(day1,mount1,year1,day2,mounth2,year2):
    day=0
    for i in range(mount1,mounth2):
        if i%2==0 and i!=8 and i!=2:
            for j in range(0,30):
                day+=1
        elif i==2:
            if leapyear(year1):
                for j in range(0,29):
                    day+=1
            else:
                for j in range(0,28):
                    day+=1
        else:
            for j in range(0,31):
                day+=1
    return (day-day1+day2)

def leapyear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 1
    else:
        return 0

def dateyear_diff(day1,mount1,year1,day2,mounth2,year2):
    day=0
    start=date_diff(day1,mount1,year1,31,12,year1)
    end=date_diff(1,1,year2,day2,mounth2,year2)
    for k in range(year1+1,year2):
        for i in range(1,13):
            if i%2==0 and i!=8 and i!=2:
                for j in range(0,30):
                    day+=1
            elif i==2:
                if leapyear(k):
                    for j in range(0,29):
                        day+=1
                else:
                    for j in range(0,28):
                        day+=1                    
            else:
                for j in range(0,31):
                    day+=1
            # mounth+=1
    if(year1==year2 ):
        if leapyear(year1):
            return day+start+end-366
        else:
            return day+start+end-365
    return day+start+end

print("Enter starting date(dd/mon/year) : ")
date1=int(input())
mount1=int(input())
year1=int(input())
print("Enter Ending date(dd/mon/year) : ")
date2=int(input())
mount2=int(input())
year2=int(input())

print(str(dateyear_diff(date1,mount1,year1,date2,mount2,year2))+" days")