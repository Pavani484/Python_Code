# from second import *
# m2(int(input("Enter a number: ")))
# a, b = map(int, input("Enter two numbers with space: ").split())
# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)
#............................
# num=int(input("Enter a number: "))
# prime(num)
#.....................
# n=int(input("Enter a number : "))
# li=[]
# for i in range(n):
#     a=int(input("Enter elements into list : "))
#     li.append(a)
# print(li)
# p=int(input("Enter a position to insert element : "))
# e=int(input("Enter an element : "))
# li.insert(p-1,e)
# print(li)
# e1=int(input("Enter an element : "))
# if e1 in li:
#     li.remove(e1)
#     print(li)
# else:
#     print("element is not found in list")
# p1=int(input("Enter a position to remove: "))
# if p1 > 0 and p1 <= len(li):
#     li.pop(p1)
# print(li)
# e2=int(input("Enter an element to print the position: "))
# if e2 in li:
#     print(li.index(e2))
# else:
#     print("element is not found in list")
#....................................
# t = ()
# l = list(t)
# for i in range(5):
#     num = int(input("Enter element: "))
#     l.append(num)
# t = tuple(l)
# print("Tuple after inserting elements:", t)
# delete_element = int(input("Enter element to delete: "))
#
# if delete_element in t:
#     l = list(t)
#     l.remove(delete_element)
#     t = tuple(l)
#     print("Tuple after deletion:", t)
# else:
#     print("Element not found in tuple")
# search_element = int(input("Enter element to find position: "))
#
# if search_element in t:
#     position = t.index(search_element)
#     print("Position of element is:", position)
# else:
#     print("Element not found in tuple")
# #.....................
# s = set()
# for i in range(5):
#     num = int(input("Enter element: "))
#     s.add(num)
# print("Set after inserting elements:", s)
# delete_element = int(input("Enter element to delete: "))
# if delete_element in s:
#     s.remove(delete_element)
#     print("Set after deletion:", s)
# else:
#     print("Element not found in set")
# search_element = int(input("Enter element to find position: "))
# if search_element in s:
#     print("Set does not support position/index because it is unordered.")
# else:
#     print("Element not found in set")
#     #.....................................
# d = {}
# name = input("Enter name: ")
# email = input("Enter email: ")
# mobile = input("Enter mobile: ")
# city = input("Enter city: ")
# pin = input("Enter pin: ")
# d["name"] = name
# d["email"] = email
# d["mobile"] = mobile
# d["city"] = city
# d["pin"] = pin
# print("\nDictionary after insertion:")
# print(d)
# print("\nAll key-value pairs:")
# for key, value in d.items():
#     print(key, ":", value)
# new_name = input("\nEnter new name to replace existing name: ")
# d["name"] = new_name
# print("Updated dictionary:", d)
# remove_key = input("\nEnter key to remove: ")
# if remove_key in d:
#     del d[remove_key]
#     print("Dictionary after removing key:", d)
# else:
#     print("Key not found")
# check_value = input("\nEnter value to check: ")
# if check_value in d.values():
#     print("Value exists in dictionary")
# else:
#     print("Value not found")
# state = input("\nEnter state: ")
# d["state"] = state
# print("Final dictionary:", d)
#..............................
# class A:
#     def __init__(self):
#         print("class a constructor")
# class B(A):
#     def __init__(self,x):
#         super().__init__()
#         print("class b constructor",x)
# class C(B):
#     def __init__(self):
#         super().__init__(10)
#         print("class c constructor")
# obj = C()
#.....................
# class A:
#     def function_one(self):
#         print("class a function one")
#     def function_two(self):
#         print("class a function two")
# class B(A):
#     def function_two(self):
#         super().function_two()
#         print("class b function two")
#     def function_three(self):
#         print("class b function three")
# one=B()
# one.function_one()
# one.function_two()
# one.function_three()
#...........................................
# def function(x,y,z):
#     print("x=",x)
#     print("y=",y)
#     print("z=",z)
# function(10,20,30)
#function(100,200)#error:number of arguments are not equal to no. of parameters
# function(y=10,x=10,z=30)
#function(10,20,y=30)#assigning multiple values to y
# function(10,z=20,y=30)
##positional aruguments is following keyword arguments
#positional aruguments  has high priority than keyword aruguments
#.............................
#default paramters first priority to the positional aruguments and then default parameters.
#............
#arbitory,in arbitory parameters the written data type is tuple.these are used when we don't know how many paramters we can pass.
# def function(*a):
#     for i in a:
#         print(i,end=" ")
#     print()
# function()
# function(1)
# function(1,2,3)
# function(1,"pavani","python",9.8,1000)
# ....................................
# def function(x,*y,z=100):
#     print(x)
#     print(y)
#     print(z)
# function(10,20,30,40,60)
# function(10,20,30,40)
# function(10,20,30,z=108)
# .........................
# def patient(name,blood_group,*diseases,email="name@gmail.com"):
#     print("Patient:", name)
#     print("Blood group:", blood_group)
#     print(diseases)
#     print(email)
# patient("abc","a+","fever","headache",email="abc@gmail.com")
#...................................
# def student(name,*email,**address):
#     print("Student", name)
#     print("Email", email)
#     print("Address", address)
# student(
#     "pavani","pavani@gmail.com","pav@gmail.com",no=123,street="kothuru"
# )
#.........................................
# f=open("exam.txt","w")
# f.write("hello Pavani! How are you?\n")
# f.close()
# f=open("exam.txt","a")
# f.write("let start working on python\n")
# f.close()
# f=open("exam.txt","r")
# print(f.read())
# l=f.readline()
# l=f.readlines()
# print(l)
# f.close()
# f=open("exam.txt","a")
# f.write("let start files in python")
# f.close()
# f=open("exam.txt","r")
# print(f.read())
#.............................
# import math,datetime
# li=list(map(int,input("enter enter to find lcm and gcd:").split()))
# g=math.gcd(li[0],li[1],li[2],li[3])
# l=math.lcm(li[0],li[1],li[2],li[3])
# print("lcm is:",l)
# print("gcd is:",g)
# print("current time is:",datetime.datetime.now())
#.....................
# import numpy as np
# arr= np.array(([1,2],[3,4]))
# arr2=np.array([[5,6],[7,8]])
# print("addition:",arr+arr2)
# print("multiplication:",arr*arr2)
# print("matrix multiplication:",np.matmul(arr,arr2))
# #............................................
# import pandas as pd
# data={
#     'roll number':[1,2,3],
#     'name':["Pavani","lalitha","ammu"],
#     'age':[20,23,21],
#     'city':["Banglore","guntur","madanapalli"],
#     'course':["python",'CA',"Java"]
# }
# df=pd.DataFrame(data)
# df.to_csv('data.csv',index=False)
# df.to_json('data.json',orient='records')
#...............................
# import pandas as pd
# data={
#     "name":["pavani","lalitha","saritha","ammu","radha"],
#     "department":["statistics","Accounts","mathematics","computers","commerce"],
#     "marks":[90,95,70,90,70]
# }
# d={
#     "name":["a","b","c","d"],
#     "dep":["s","a","m","c"]
# }
# df=pd.DataFrame(data)
# d=pd.DataFrame(d)
# d.to_json("data.json",orient="records")
# df.to_csv("data.csv",index=False)
# d=pd.read_csv("data.csv")
# print(d)
# df=pd.read_json("data.json")
# print(df)
#............
# def maximum(li):
#     m=float('-inf')
#     for i in li:
#         if i>m:
#             m=i
#     print("maximum value in list:", m)
# maximum([20,30,45,67,90])
#..............
# u=input("enter username:")
# p=input("enter password:")
# us="admin"
# pw="password123"
# if u==us and p==pw:
#     print("Login successful")
# else:
#     print("invalid credentials")
#.................
# n=list(map(int,input("enter elements into list with space:").split()))
# li=[]
# for i in n:
#     if i not in li:
#         li.append(i)
# print(li)
#.......................
# x=['hi','python','we','write','python','we','say','hi','python',"pavani"]
# dict={}
# for i in x:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)
# print(max(dict.values()))
#...........................
# x=[('a',10),('b',20),('c',30),('d',40)]
# for key,value in x:
#     print(value,end=" ")
# for i in x:
#     print(i[1],end=" ")
# .....................
# x=['a','b','c','d']
# y=[10,20,30,40]
# dict={}
# for i,j in zip(x,y):
#     dict[i]=j
# print(dict)
#...........................

# x=['a','b','c','d']
# y=[10,20,30,40]
# li=[]
# for i,j in zip(x,y):
#     li.append((i,j))
# print(li)
#.................
# li=list(range(2,51,2))
# print(li)
# s=set(range(101,0,-2))
# print(s)
#................
# li=[1,3,10,2,5]
# print(li[1::2])
# li1=[]
# for i in range(1,len(li),2):
#     li1.append(li[i])
# print(li1)
# li2=[li[i] for i in range(1,len(li),2)]
# print(li2)
#....................
# li=[1,3,10,2,5]
# li1=[]
# for i in li:
#     li1.append(i**2)
# print(li1)
# li2=[i**2 for i in li]
# print(li2)
# li3=[]
# li4=[]
# for i in li:
#     if i%2!=0:
#         li3.append(i)
#     else:
#         li4.append(i)
# print(li3)
# print(li4)
#...................
# x=['a','b','c','d']
# y=[10,20,30,40]
# dict={}
# for i in range(len(x)):
#     dict[x[i]]= y[i]
# print(dict)
#or
# x=['a','b','c','d']
# y=[10,20,30,40]
# z={(x[i],y[i])for i in range(len(x))}
# print(z)
#..................
# num=int(input("Enter number of elements: "))
# li=[]
# for i in range(num):
#     n=int(input("enter numbers:"))
#     li.append(n)
# for i in range(len(li)-1,-1,-1):
#     print(li[i],end=" ")
# l=[ li[i] for i in range(len(li)-1,-1,-1)]
# print(l)
#................
# li=[1,2,3,4,5]
# l=[i**2 if i%2==0 else i**3 for i in li]
# print(l)
#....................
# n=int(input("Enter a number: "))
# li=[]
# l1=[]
# for i in range(n):
#     n1=int(input("Enter a number: "))
#     li.append(n1)
# for i in range(0,n,2):
#     l1.append(li[i])
# print(l1)
#........................
# n=6
# li=[]
# for i in range(n):
#     n1=int(input("Enter a number: "))
#     li.append(n1)
# print(li)
# s=0
# for i in range(n):
#     if li[i] % 2!= 0:
#         s+=li[i]
# print(s)
# #................
#lambda function
# ad=lambda num1,num2:  num1+num2
# print(ad(20,40))
#.........
# e = lambda num: "even" if num % 2 == 0 else "odd"
# print(e(20))
# #...................
# b=lambda num,num1: "greater" if num > num1 else "smaller"
# print(b(20,20))
#.........................
# li=[10,11,12,9,6,2]
# n=[i for i in li if i%2==0]
# print(n)
# #or
# y=list(filter(lambda num:num%2==0,li))
# print(y)
# y=list(filter(lambda x:print(x),range(1,10)))
# y=list(filter(lambda num:num<10,li))
# print(y)
#.....................
x=[10,11,12,9,6,2]
l=[i**2  for i in x]
print(l)
#or
a=[]
for i in x:
    a.append(i*i)
print(a)

