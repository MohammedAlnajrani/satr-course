from datetime import date
import calendar
import datetime


theday=[]
namelist=[]
DOBlist=[]
i=0
cc=0
namecoun=0
sec_key_cc=1
while True:
    select=input("whice to continue? (y) (n): \n")
    
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
        

        personInfo={'names':name, 'dateOfBirt':calAge(DOB)}

        #personInfo [name] = calAge(DOB)

        theday.append(DOB.strftime("%A"))


        
        #first_key = list(personInfo)[0]
        first_val = list(personInfo.values())[0]

        #sec_key = list(personInfo)[1]
        sec_val = list(personInfo.values())[1]

        namelist.append(first_val)
        DOBlist.append(sec_val)
        
        

        print(personInfo)
        perdob=print(namelist[cc],"is",DOBlist[cc],"years old and she/he was born on",theday[cc])
        
        #for check
        # print(namelist)
        # print(DOBlist)
        


        cc=cc+1
        
       


    
        
        
        # personInfo={'names':name, 'dateOfBirt':calAge(DOB)}
        # #print("your age is:",calAge(DOB),"years")
        # print(personInfo['names'],"is",calAge(DOB),"years old and she/he was born on",DOB.strftime("%A"))
    elif select.lower()=="n":
        tempage=DOBlist[0]
        tempname=namelist[0]

        counter=0


        while  counter < cc:

            
            # first_key = list(personInfo)[counter]
            # first_val = list(personInfo.values())[counter]

            # sec_key = list(personInfo)[counter+1]
            # sec_val = list(personInfo.values())[counter+1]

        
            #print(first_val,"is",sec_val,"years old and she/he was born on",DOB.strftime("%A"))

            print(namelist[counter],"is",DOBlist[counter],"years old and she/he was born on",theday[counter],"\n")
            

            # We can use filter function 
            if DOBlist[counter] > tempage:
                tempage==DOBlist[counter]
                tempname=namelist[counter]

            counter=counter+1


            
            

            
        
        Elder = tempname

        print("The Elder one is :", Elder,"\n")   
        print("Total people is ", counter)

        break
    else:
        print("invalid input...type (y) to Continue OR (n) to Quit: \n")
    