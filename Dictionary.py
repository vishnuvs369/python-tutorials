#DICTIONARY
# Word = Meaning (Dictionary)
# Key = Value

dict1 = {
    "name" : "vishnu",
    "age" : 24,
    "place" : "Vadakara"

}

#print(dict1)

#print(len(dict1))

for x in dict1 :
    print(x)

#---------------------------------------------

dict2 = {
    "Brand" : "apple",
    "price" : 100000,
    "Expiry" : "2022"

}

a = dict2["Brand"]

a = dict2.get("price")


#a = dict2.clear()

print(a)

print(dict2)