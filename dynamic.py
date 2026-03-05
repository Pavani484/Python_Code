n=int(input("enter a number"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(fact)
#................
n=int(input("enter a number:"))
n1=int(input("enter a number:"))
for i in range(n,n1+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)
#.....................
n=int(input("enter a number:"))
n1=0
n2=1
for i in range(1,n+1):
    print(n1,end=" ")
    t=n1+n2
    n1=n2
    n2=t
#........................

a=int(input("enter a number:"))
b=int(input("enter a number:"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#...............
