# Phonedir = {}
# Phonedir[("Mohammed")] = 111111111111
# Phonedir[("Amal")] = 222222222222222

# name=input("Enter name: ")
# print (Phonedir[(name)])

Phonedir1 = {'name': 'Mohammed', 'phone': 1111111111}
Phonedir2 = {'name': 'Amal', 'phone': 2222222222}
Phonedir3 = {'name': 'Ahmed', 'phone': 3333333333}


while True:
    name_or_number=int(input("\npress (1) to search by name\n"+
                         "press (2) to search by number\n"+
                         "press (0) to Quit  \n"))

    if name_or_number==1:
        name=input("Enter name: ").lower()

        if name == "mohammed":
            print("The "+name+"'s Phone number is ",Phonedir1['phone'])

        elif name=="amal":
         print("The "+name+"'s Phone number is ",Phonedir2['phone'])

        elif name=="ahmed":
            print("The "+name+"'s Phone number is ",Phonedir3['phone'])

        else:
            print("Sorry, the number is not found")

    elif name_or_number==2:
    
         number=int(input("Enter the number: "))

         if len(str(number))!=10:
            print("This is invalid number")

         elif number == 1111111111:
             print("This phone number belong to ",Phonedir1['name'])

         elif number==2222222222:
            print("This phone number belong to ",Phonedir2['name'])

         elif number==3333333333:
            print("This phone number belong to ",Phonedir3['name'])

         else:
            print("Sorry, the number is not found")

    elif name_or_number==0:
        break