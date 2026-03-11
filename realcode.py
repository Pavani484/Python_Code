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










