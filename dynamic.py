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

