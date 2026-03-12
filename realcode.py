#1.	Write a program to store n product prices in a list and find the maximum price
# n=int(input("enter a number of product prices:"))
# l1=[]
# for i in range(n):
#     l=int(input("enter a product price:"))
#     l1.append(l)
# print(max(l1))
# #(or)
# n=int(input("enter a number of product prices:"))
# l1=[]
# let_max=float('-inf')
# for i in range(n):
#     l=int(input("enter a product price:"))
#     l1.append(l)
#     if l1[i]>let_max:
#         let_max=l1[i]
# print(let_max)
#........................
#How do you remove duplicate elements from a list without using set()
# li=[9,4,5,6,6]
# l=[]
# for i in li:
#     if i not in l:
#         l.append(i)
# print(l)
#(or)
# li = [9,4,5,6,6]
# unique = []
# seen = {}
# for num in li:
#     if num not in seen:
#         unique.append(num)
#         seen[num] = True
#         print(seen)
# print(unique)
# ..................................
#Write a program to count how many even and odd numbers are present in a list
# li=[3,4,5,6,7,8,65,34,23,-45]
# e=0
# o=0
# for i in li:
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print("even numbers count is",e)
# print("odd numbers count is",o)
#...........................
#4.	How do you reverse a list without using reverse()?
# li=[4,5,6,7,8,9]
# l=len(li)
# r=[]
# for i in range(l-1,-1,-1):
#     r.append(li[i])
# print(r)
#(or)
# li=[4,5,6,7,8,9]
# r=li[::-1]
# print(r)
#....................
#Write a program to search an element in a list and display its position
# li=[4,5,3,6,7,8,9]
# s=int(input("enter the element you want to search:"))
# if s in li:
#     p=li.index(s)
#     print(s,"found in position",p)
# else:
#     print("element not found")
#..........................
#6.	How can you merge two lists and sort the result
# l1=[1,3,5,7,8,4]
# l2=[2,4,9,6,10]
# l1.extend(l2)
# l1.sort()
# print(l1)
#(or)
# l1=[1,3,5,7,8,4]
# l2=[2,4,9,6,10]
# m=sorted(l1+l2)
# print(m)
#(or)
#if elements are already sorted
# l1=[1,3,5,7,8,4]
# l2=[2,4,9,6,10]
# i=j=0
# m=[]
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         m.append(l1[i])
#         i+=1
#     else:
#         m.append(l2[j])
#         j+=1
# m.extend(l1[i:])
# m.extend(l2[j:])
# print(m)
#....................
#7.	Write a program to remove all negative numbers from a list.
# l=[-1,2,6,4,5,8,34,-56,74]
# for i in l:
#     if i<0:
#         l.remove(i)
# print(l)
# ....................
#8.	How do you find the second largest element in a list?
# li=[1,34,56,32,67]
# l=len(li)
# firstm=float('-inf')
# secondm=float('inf')
# for i in range(l):
#     if li[i]>firstm:
#         secondm = firstm
#         firstm=li[i]
#     elif li[i]>secondm and li[i]!=firstm:
#         secondm=li[i]
# print(secondm)
#....................
#9.	Write a program to rotate a list to the right by 1 position.
# li=[4,5,7,8,2]
# last=li[-1]
# for i in range(len(li)-1,0,-1):
#     li[i]=li[i-1]
# li[0]=last
# print(li)
#(or)
# def rotate_right(li, k):
#     n = len(li)
#     k = k % n
#     for _ in range(k):
#         last = li[-1]
#         for i in range(n-1, 0, -1):
#             li[i] = li[i-1]
#         li[0] = last
#     return li
# li = [1, 2, 3, 4, 5]
# print(rotate_right(li, 2))
#......................................
#10.How do you count occurrences of each element in a list?
# li=[2,3,6,5,4,3,2,2,2,3]
# dict={}
# for i in li:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
#...............................................
#Write a program to find the maximum and minimum element in a tuple.
# t=(3,4,57,8,9,6)
# mx=max(t)
# mi=min(t)
# print(mx,mi)
# #(or)
# t=(4,5,3,2,7,8,5,67,89)
# mx=float('-inf')
# mi=float('inf')
# for i in t:
#     if i>mx:
#         mx=i
#     elif i<mi:
#         mi=i
# print(mx,mi)
#...................................
# How do you convert a tuple into a list and modify it?
# t=(4,45,6,7,8,9)
# li=list(t)
# print(li)
# li.append(10)
# print(li)
#......................



#Write a program to count the number of times an element occurs in a tuple
# t=(2,4,5,6,3,2,6,5,5)
# dict={}
# for i in t:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
#.......................
# How do you unpack values from a tuple into variables?
# t=(4,5,6,3)
# a=t[0]
# b=t[1]
# c=t[2]
# d=t[3]
#.........................
#6.	Write a program to check whether an element exists in a tuple
# t=(3,4,5,6,99)
# s=int(input("enter an element to search:"))
# if s in t:
#     print(s,"is exists")
# else:
#     print(s,"is not exists")
#......................
#Write a program to reverse a tuple
# t=(3,4,5,6,8,7)
# l=len(t)
# print(l)
# for i in range(l-1,-1,-1):
#     print(t[i])
#...................................
#How do you concatenate two tuples.
# t1=(3,4,5,6,7)
# t2=(2,8,9,10)
# print(t1+t2)
#......................................
#1.	Write a program to remove duplicate values from a list using a set.
# li=[3,4,5,6,7,3,3,4]
# l=list(set(li))
# print(l)
#....................
#2.	How do you find common elements between two sets?
# s1={34,56,78,45}
# s2={56,34,67,89.68}
# for i in s1:
#     if i in s2:
#         print(i)
#(or)
# s1={34,56,78,45}
# s2={56,34,67,89.68}
# print(s1.intersection(s2))
# print(s1 & s2)
#.............................................
# n=int(input("enter total purchase amount:"))
# if n<1000:
#     print("no discount")
#     print("Total Payable amount:",n)
# elif n>1000 or n<5000:
#     d1=n*(10/100)
#     p1=n-d1
#     print("Total Payable amount:",p1)
# else:
#     d2 = n*(20/100)
#     p2 = n-d2
#     print("Total Payable amount:",p2)
#.............
# n=int(input("enter number of Subjects:"))
# s1=[]
# fail_count=0
# for i in range(n):
#     n1=int(input("enter number of marks in each subject:"))
#     s1.append(n1)
# T=0
# for i in s1:
#     if i>40:
#         print("pass")
#     else:
#         print("fail")
#         fail_count+=1
#     T+=i
# print("Total marks:",T)
# p=(T/(n*100))*100
# print("percentage:",p)
# if fail_count > 0:
#     print("Overall Result: FAIL")
# else:
#     print("Overall Result: PASS")
# if p<40:
#     print("D Grade")
# elif p>=40 and p<50:
#     print("C Grade")
# elif p>=50 and p<60:
#     print("B Grade")
# elif p>=60  and p<70:
#     print("A Grade")
# else:
#     print("Distinction")
# ...................
# n=int(input("enter a number:"))
# if n<0:
#     print("palindrome check is not valid for negative numbers")
# else:
#     s=0
#     t=n
#     r=0
#     d=len(str(n))
#     while t>0:
#         t1=t%10
#         r=r*10+t1
#         s=s+t1
#         t=t//10
#     print("number of digits:",d)
#     print("sum of digits:",s)
#     if r==n:
#         print("the number is palindrome")
#     else:
#         print("the number is not palindrome")
# .....................
# n=int(input("enter number of digits:"))
# l=[]
# for i in range(n):
#     l.append(int(input("enter elements:")))
# first=float('-inf')
# second=float('-inf')
# for i in range(len(l)):
#     if l[i]>first:
#         second=first
#         first=l[i]
#     elif l[i]>second and l[i]!=first:
#         second=l[i]
# print("second largest element:",second)
# s=0
# avg=0
# for i in l:
#     s=s+i
# le=len(l)
# avg=s/le
# print("average of elements:",avg)
# all_greater = True
# for i in l:
#     if i <= avg:
#         all_greater = False
#         break
#
# if all_greater:
#     print("All elements are greater than average")
# else:
#     print("All elements are NOT greater than average")
# li=[]
# for i in l:
#     if i not in li:
#         li.append(i)
# print("unique elements list:",li)
# .................

# s=input("enter a sentence:").lower()
# w=len(s.split())
# v=c=0
# print("number of words:",w)
# for i in s:
#     if i in "aeiou":
#         v+=1
#     elif i not in "aeiou" and i!=" ":
#         c+=1
# print("number of vowels:",v)
# print("number of consonants:",c)
# dict={}
# for i in s:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# m=max(dict.values())
# print("frequently occuring characters:",m)
# r=""
# s1=s.split()
# for i in range(len(s1)-1,-1,-1):
#     r+=s1[i]
# print(r)
#............................
# l1 = list(map(int, input("Enter roll numbers in event 1: ").split()))
# l2 = list(map(int, input("Enter roll numbers in event 2: ").split()))
# common = []
# only_one = []
#
# for i in l1:
#     if i in l2 and i not in common:
#         common.append(i)
#     elif i not in l2:
#         only_one.append(i)
#
# for i in l2:
#     if i not in l1:
#         only_one.append(i)
#
# print("Students common in both:", common)
# print("Students present in only one group:", only_one)
# total_unique = set(l1) | set(l2)
# print("Total unique participants:", len(total_unique))
# print("Unique participants list:", total_unique)
#............




