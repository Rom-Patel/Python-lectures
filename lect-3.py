#program for greater than 10 
a = 10
if a>0:
    print("Greater than 0")
elif a==0:
    print("Is zero")
else:
    print("Less than 0")

print("program for even/odd")
i = int(input("Enter a number:"))
if i%2==0:
    print(i,"is Even")

else:
    print(i,"is Odd")

print("comparison of 2 user defined number:")
a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
if a>b:
    print(a,"is greater than",b)
elif b>a:
    print(b,"is greater than",a)
else:
    print(a,"is equal to",b)

print("Checking +ve,-ve or zero:")
a=int(input("Enter num 1: "))
if a>=0:
    if a==0:
        print("Zero")
    else:
        print(a,"is a positive number")
else:
    print(a,"is a negative number")

#for loop
for i in 0,1,2,3:
    print(i)

for i in range(1,9,3):#Here,1 is starting; 9 is end; 3 is step or increment,it can be decremented by -ve number
    print(i)

for i in range(10,1,-2):#decrement br 2 from 10 to 2
    print(i)

#while loop
i=1
while i<=10:
    print(i)
    i+=1

i=True
while i==True:
    print(i)
    n=int(input("Enter 1 if you want to continue:"))
    if n==1:
        i=True
    else:
        i=False

for i in range(1,11):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

i=1
while i<=10:
    if i%2==0:
        print(i,"is even")
        i+=1
    else:
        print(i,"is odd")
        i+=1

#type casting
a="a"
ascii=ord(a)
print(ascii)
print(chr(ascii))

a=1
a=1.0
a="str"
print(a)

a=1
print(a)
a=1.0
print(a)
a="str"
print(a)

a=1
print(a)
print(type(float(a)))
print(float(a))
print(type(str(a)))
print(str(a))

a="string"
for i in a:
    if i=="i":
        break
    else:
        print(i)

a="string"
for i in a:
    if i=="i":
        continue
    else:
        print(i)

for i in 0,1,2,3:
    print(i)

#for with else loop
a="string"
for i in a:
    if i=="i":
        pass
    else:
        print(i)
else:
    print("This has pass")

a="string"
for i in a:
    if i=="i":
        break
    else:
        print(i)
else:
    print("This has break")

a="string"
for i in a:
    if i=="i":
        continue
    else:
        print(i)
else:
    print("This has continue")

#while with else loop
i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1
else:
    print("This has break")

