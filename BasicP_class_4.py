# def pnt_hello(year):
#     print("Hello Stater Pack #", year)
#     print("Hello Stater Pack #", year)
#     print("Hello Stater Pack #", year)
#     print("Hello Stater Pack #", year)

# pnt_hello("asd")
# pnt_hello(31)
# pnt_hello(True)
# pnt_hello(False)
# pnt_hello(3.14)

# def my_sum(num1, num2):
#     return num1 + num2

# sum_riw_vava = my_sum(14, 47)
# print(sum_riw_vava)

# def hungry(has_rice, has_spoon):
#     if has_rice == True and has_spoon:
#         return "You can eat rice"
#     else:
#         return "You don't eat rice"

# print(hungry(True, False))

# def calculator(num1, num2, cmd):
#     print("Calculator: ",num1, cmd, num2)
#     if cmd == "sum":
#         return num1 + num2
#     elif cmd == "minus":
#         return num1 - num2
    
# print(calculator(15, 5, "sum"))

# def pnt_n_time(time):
#     for t in range(1, time +1):
#         print(t, "Hello")

# pnt_n_time(4)

# box = ["pen", 30, True, "ruler"]
# print(box[0])
# print(box[1])
# print(box[3])
# box[0] = "book"
# print(box[0])
# print(box)

# box.append("pen")
# print(".append", box)

# box.pop(2)
# print(".pop", box)

# box = ["pen", 30, True, "ruler"]

# print("--------------------------------------")
# for i in box:
#     print(i, "Starter Pack")

# box_fruit = ["durian", "banana", "apple", "mango", "orange"]


# for f in box_fruit:
#     if f == "apple":
#         print("apple aroi")
#     else:
#         print("Not found")

# for i in range(6):
#     if box_fruit[i] == "apple":
#         print("apple aroi")
#     else:
#         print("Not found")

# box_fruit = ["durian", "banana", "apple", "mango", "orange"]

# def findfruit(name_fruit):
#     for f in box_fruit:
#         if f == "orange":
#             print("orange aroi")
#         elif f != "orange":
#             print("Not found")

# print(findfruit("orange"))

# students = [{"name": "Tanet Kejkornkaew", "age": 18, "ID": 68130500030},
#             {"name": "P'Jia", "age": 19, "ID": 67130500099}]
# for student in students:
#     if student ["age"]>= 18:
#         print("Pass")
#     else:
#         print("Not pass")

students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
            {"name": "satit", "age": 17, "ID": 6713050047}]
for student in students:
    if student ["age"]>= 18:
        print(student["name"], "Pass")
    else:
        print(student["name"], "Not pass")