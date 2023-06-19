# Phonedir = {}
# Phonedir[("Mohammed")] = 111111111111
# Phonedir[("Amal")] = 222222222222222

# name=input("Enter name: ")
# print (Phonedir[(name)])

Phonedir1 = {'name': 'Mohammed', 'phone': 1111111}
Phonedir2 = {'name': 'Amal', 'phone': 22222222}
Phonedir3 = {'name': 'Ahmed', 'phone': 3333333}

name=input("Enter name: ").lower()

if name == "mohammed":
    print(Phonedir1['phone'])

elif name=="amal":
    print(Phonedir2['phone'])

elif name=="ahmed":
    print(Phonedir3['phone'])

else:
    print("Sorry, the number is not found")