#File

#File write
f = open("sample.txt", "w")

# f = open("F:/codes to upload/sample.txt", "w")   --> Perticular location

f.write("Learn python")

f.close()


#------------------------------------------

#File read
f = open("sample.txt", "r")

read = f.read()
print(read)

f.close()