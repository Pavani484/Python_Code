# import first
# def m2(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
#...................
# def add(a,b):
#     print(f"addition of {a} and {b} is : {a+b}")
# def sub(a,b):
#     print(f"subtraction of {a} and {b} is : {a-b}")
# def mul(a,b):
#     print(f"multiplication of {a} and {b} is : {a*b}")
# def div(a,b):
#     print(f"division of {a} and {b} is : {a/b}")
#..........................
# def prime(num):
#     for i in range(2,num):
#         if num % i==0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
#.....................
# import sqlite3
# conn = sqlite3.connect("school.db")
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# age INTEGER,
# grade TEXT
# )
# """)
# cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (1, "Alice", 14, "A"))
# cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (2, "Bob", 15, "B"))
# cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (3, "Charlie", 14, "A"))
# cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (4, "pavani", 16, "A"))
# conn.commit()
# cursor.execute("SELECT * FROM students")
# print("Initial Records:")
# for row in cursor.fetchall():
#     print(row)
# cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("B", "Bob"))
# cursor.execute("DELETE FROM students WHERE id = ?", (3,))
# conn.commit()





