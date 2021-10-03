#Lambda function

def square(x):
    return x * x

print(square(4))    


#--------------------------------------
#we can simplify the above example using Lambda function

l = lambda x : x * x
print(l(4))

#---------------------------------------
#filter function

list1= [1,2,3,4,5,6]

def even(x):
    if x%2 ==0 :
        return x

f = filter(even, list1)

print(list(f))

#-----------------------------------------

#filter function with Lambda

list2 = [1,2,3,4,5,6,7,8]

f = filter(lambda x: x%2 ==0 ,list2)

#f = filter(lambda x: x%2 ==1 ,list2)

print(list(f))

#------------------------------------------