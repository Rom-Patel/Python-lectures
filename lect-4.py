#tuples
t1=(5,6,7,8,9)
t2=([1,2,3,4],"hi")
t1=t1+t2
print(t1)
print(t1*4)

t1=(1,2,3)
t2=(4,5,6)
t1+=t2
#t1=t1+t2
print(t1)
print(t1*3)

t3="Rom"
print(t3)

t4=["Rom"]
print(t4)

t5=tuple("Rom")
print(t5)

#list
l=list("Rom")
print(l)

str="Rom Patel"
t=tuple(str)
print(t)

t=tuple(str.split())
print(t)

s="Rom Patel"
t=list(s.split())
print(t)

ch="|"
l=["rom","patel"]
print(ch.join(l))
print(ch)
print(l)

#sets
s=set()
s={1,2,3,4}
s={"Hello","World","Python",(1,2,3,4)}
print(s)
print(type(s))

# traversing a set
s={"Hello","World","Python",(1,2,3,4)}
for i in s:
    print(i)

s={"Hello","World","Python",(1,2,3,4)}
print("Hello" in s)
print ("word" in s)

# adding elemets
s={"Hello","World","Python",(1,2,3,4)}
s.add("Coder")
print(s)

# updating sets
s={"Hello","World","Python",(1,2,3,4)}
s.update({"React","Python"})
print(s)
s.update(["React","Python"])
s.update("Java")
print(s)

# deleting items in a set
s={"Hello","World","Python",(1,2,3,4)}
print(s.pop())
print(s)

s.remove("Python")
s.discard("Python")
print(s)

s.clear()
print(s)

del s
# print(s)

#methods or operations on set
s1={1,2,3,4}
s2={3,4,5,6}
print("Union: ",s1.union(s2))
print("Intersection: ",s1.intersection(s2))
print("Difference a-b: ",s1.difference(s2))
print("Difference b-a: ",s2.difference(s1))
print("Symmetric Difference a-b: ",s1.symmetric_difference(s2))
print("Symmetric Difference b-a: ",s2.symmetric_difference(s1))