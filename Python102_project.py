from datetime import date,datetime


#/while True:
print("Enter you DOB\n")
yearDOB = int(input('year: '))
monthDOB = int(input('month: '))
dayDOB = int(input('day: '))

DOB = date(yearDOB, monthDOB, dayDOB)
# print(DOB)
# now= date.today()
# print(now)
# print

def calAge(DOB):
    now = date.today()
    age = now.year - DOB.year - ((now.month, now.day) < (DOB.month, DOB.day))
    #age = date.today - DOB.year
 
    return age

print("your age is:",calAge(DOB),"years")