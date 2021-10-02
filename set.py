# Set 

set1 = {"apple", "mango", "orange"}

#print(set1)


# it is not posible 
# print(set1[0])

for x in set1:
    print(x)


#del set1
print(set1)

#-----------------------------------------------

set2 ={"car", "bike", "bus"}

print(set2)

print(len(set2))

print("car" in set2)

#-----------------------------------------------

set3 = {"Football", "Cricket", "Badminton"}

set3.add("racing")
#print(set3)


set3.update(["Basketball" , "Golf"])
#print(set3)


set3.remove("Football")
#print(set3)

set3.discard("Basketball")
#print(set3)

#-----------------------------------------------

set1 = {"apple", "mango", "orange"}

set3 = {"Football", "Cricket", "Badminton"}

set4 =set1.union(set3)

#print(set4)

#-----------------------------------------------