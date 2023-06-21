from datetime import date
import calendar
import datetime


theday=[]
i=0
class_list = dict() 
while True:
    select=input("whice to continue? (y) (n): ")
    
    if select.lower()=="y":
        i=i+1 
        name=input("Enter your name: ")
        print("Enter you DOB\n")
        yearDOB = int(input('year: '))
        monthDOB = int(input('month: '))
        dayDOB = int(input('day: '))
        DOB = date(yearDOB, monthDOB, dayDOB)

       
        def calAge(DOB):
            now = date.today()
            age = now.year - DOB.year - ((now.month, now.day) < (DOB.month, DOB.day))
            
 
            return age
        

        #temp = data.split(':') 
        #class_list[temp[0]] = temp[1] 
        personInfo={'names':name, 'dateOfBirt':calAge(DOB)}

        personInfo [name] = calAge(DOB)

        theday.append(DOB.strftime("%A"))
    

    
        
        
        # personInfo={'names':name, 'dateOfBirt':calAge(DOB)}
        # #print("your age is:",calAge(DOB),"years")
        # print(personInfo['names'],"is",calAge(DOB),"years old and she/he was born on",DOB.strftime("%A"))
    elif select.lower()=="n":
        print(i)
        
        counter=0
        if  i > counter:
            first_key = list(personInfo)[counter]
            first_val = list(personInfo.values())[counter]

            sec_key = list(personInfo)[counter+1]
            sec_val = list(personInfo.values())[counter+1]

        
            #print(first_val,"is",sec_val,"years old and she/he was born on",DOB.strftime("%A"))
            print(first_val,"is",sec_val,"years old and she/he was born on",theday[counter])
            print(counter)

            counter=counter+1
        break 
    else:
        print("invalid input...type (y) to Continue OR (n) to Quit: \n")
    