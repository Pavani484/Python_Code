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

