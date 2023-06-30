# s={
#     "roll.no" : 14,
#     "name" : "Rom",
#     "branch" : "CO"
# }
# print(s)

# s1={
#     "roll.no" : 14,
#     "roll.no" : "Rom",
#     "branch" : "CO"
# }
# print(s1)

# s2={
#     "roll.no" : "Rom",
#     "name" : "Rom",
#     "branch" : "CO"
# }
# print(s2)

# s4={
#     1:1.0,
#     1.0:01.1
# }
# print(s4)

# rollno=int(input("Enter your roll.no: ")) ; name=(input("Enter your name: "))
# s={
#     "roll.no" : rollno,
#     "name" : name,
#     "branch" : "CO"
# }
# print(s)

# print("this \
#       is \
#       co"
# )

# print("this \
# is \
# co"
# )

#accessing elements of dictionaries
# print(s["name"])
# print(s.values())
# print(s.keys())
# print(s.items())

# s={
#     "roll.no" : 14,
#     "name" : "Rom",
#     "branch" : "CO"
# }

# #displaying a dictionary
# for i in s:
#     print(i)

# for i in s.values():
#     print(i)

# for i in s.keys():
#     print(i,s[i])

# for i in s.items():
#     print(i)

# for i,j in s.items():
#     print(i,j)

# s5={
#     "roll.no" : 14,
#     "name" : ["Rom","Patel"],
#     "branch" : "CO"
# }
# print(s5)
# print(s["name"][0])

# #updating elements
# s["rollno"]=12
# print(s)

# d1={"key1":"val1" , "key2":"val2"}
# print(d1)
# s.update(d1)
# print(s)
# s.update({"rollno":10})
# print(s)

#adding elements
# s["roll"]=15
# print(s)

#deleting an element
# print(d1.pop("key1"))
# print(d1)

# print(d1.popitem())
# print(d1)

# d1.clear()
# print(d1)

# del d1["key1"]
# print(d1)

# sqr={}
# for i in range(6):
#     sqr[i]=i**2
# print(sqr)

# sqr={i:i**2 for i in range(6)}
# print(sqr)

# tbl={i:2*i for i in range(1,11)}
# print(tbl)

# num=int(input("Enter a number: "))
# table={i:num*i for i in range(1,11)}
# print(table)

# #user-defined functions
# def add(x,y):
#     return x+y
# print(add(4,3))
# print(add("Hell","o"))

# def add(x,y):
#     print (x+y)
# add(4,5)

# def add(x=9,y=5):
#     print (x+y)
# add(4,8)

# num=int(input("num1: "))
# num1=int(input("num2: "))
# add(num,num1)

# print("Multiplication")
# def mul(*y):
#     print(y)
#     print(y[0]*y[1]*y[2])
# mul(4,2,3)

# print("substraction")
# def sub(*y):
#     print(y)
#     print(y[0]-y[1])
# sub(3,9)

# def display(**y):
#     print(y["name"])
#     print(y["rollno"])
#     print(y["branch"])
#     print(y)
# display(name = "Rom", rollno=14, branch="CO")

# #lambda functions
# def sqr(num):
#     print(num**2)
# sqr(4)

# sqr=lambda x : x**2
# print(sqr(4))

# cube=lambda n : n**3
# print(cube(3))

# tbl={i:11*i for i in range(1,13)}
# print(tbl)

# num=int(input("Enter a number: "))
# r=int(input("Enter  range: "))
# table={i:num*i for i in range(1,r+1)}
# print(table)

#file handling
f=open("co_1.txt","+a")
f.write("This is co file\n")
f.writelines(["list1\n","list2"])
f.seek(0)
print("read")
print(f.read())

#src.txt to dest.txt copy
src=open("source.txt","+w")
src.write("This is source")
dst=open("destination.txt","+a")
dst.write("This is destination\n")
src.seek(0)
data=src.read()
dst.write(data)
dst.seek(0)
print("This is dest: ",dst.read())
