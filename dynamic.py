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
s=input("enter a string:")
s1=""
for i in s:
    s1=i+s1
    print(s1)
#...............
s=input("enter a string :")
left=0
right=len(s)-1
palin=True
while left<right:
    if s[left]!=s[right]:
        palin=False
        break
    left+=1
    right-=1
if palin:
    print("palin")
else:
    print("not palin")
#......................
s=input("enter a string:")
s1={}
for i in s:
    if i in s1:
        s1[i]+=1
    else:
        s1[i]=1
print(s1)
#............
s=input("enter a number:").lower()
s1=""
for i in s:
    if i in "aeiou":
        s1+="*"
    else:
        s1+=i
print(s1)
# # ..................
s=input("enter a number:")
s1=s.split(" ")
l=""
for i in s1:
    if len(i)>len(l):
        l=i
print(l)
#............
s=input("enter a string:")
m=""
s1=set()
for i in s:
    if i not in s1:
        m+=i
        s1.add(i)
print(m)
#........................
s1=input("enter a string:")
s2=input("enter a string:")
if len(s1)!=len(s2):
    print("not")
else:
    fre={}
    for i in s1:
        fre[i]=fre.get(i,0)+1
    for i in s2:
        if i not in fre or fre[i]==0:
            print("not")
            break
        fre[i]-=1
    else:
        print("yes")
#................
