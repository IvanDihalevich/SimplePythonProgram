# def item_printer(hello_world: any):
#         if type(hello_world) is int:
#             print(hello_world)
#         else:
#             for hello_world1 in hello_world:
#                 item_printer(hello_world1)
#
#
# input_data = [1, 2, 5, [2, 5], 1, [1, 4], [2, [3, 7]]]
#
# for item in input_data:
#     item_printer(item)


# def sum_and_count_lowercase_plus_uppercase(list1):
#     sum_of_values, count_lower, count_upper = 0, 0, 0
#
#     for item in list1:
#         if type(item) is int or type(item) is float:
#             sum_of_values += item
#
#         elif type(item) is str:
#             if item.islower():
#                 count_lower += 1
#             else:
#                 count_upper += 1
#
#         else:
#             sum_of_values1, count_lower1, count_upper1 = sum_and_count_lowercase_plus_uppercase(item)
#             sum_of_values += sum_of_values1
#             count_lower += count_lower1
#             count_upper += count_upper1
#
#     return sum_of_values, count_lower, count_upper
#
#
# input_list = [2, 0.3, 'a', 'G', 'b', ['d', 2, 'G'], (1, 2, 'a')]
#
# print(sum_and_count_lowercase_plus_uppercase(input_list))


# class CashMachine:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def get_balance(self):
#         return self.balance
#
#     def add_cash(self, value):
#         self.balance += value
#
#
# cash_machine_main = CashMachine(1111)
#
# print(cash_machine_main.get_balance())
#
# cash_machine_main.add_cash(500)
#
#
# def get_cash(cash_machine: CashMachine):
#     return cash_machine.get_balance()
#
#
# print(get_cash(cash_machine_main))


# class BookShop:
#     def __init__(self, number_of_books, cash, price):
#         self.number_of_books = number_of_books
#         self.cash = cash
#         self.price = price
#
#     def sell_book(self, number_of_books):
#         self.cash += number_of_books * self.price
#         self.number_of_books -= number_of_books
#
#     def add_book(self, number_of_books):
#         self.cash -= number_of_books * (self.price * 0.95)
#         self.number_of_books += number_of_books
#
#     def __str__(self):
#         return f"Books: {self.number_of_books} | Cash: {self.cash} | Price: {self.price}"
#
#
# book_shop_main = BookShop(5, 400, 30)
#
# print(book_shop_main)
#
# book_shop_main.add_book(13)
#
# print(book_shop_main)
#
# book_shop_main.sell_book(7)
#
# print(book_shop_main)


# class Student:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = f"{first_name}{last_name}@oa.edu.ua"
#
#     def __str__(self):
#         return f"First name: {self.first_name} | Last name: {self.last_name} | Age: {self.age} | Email: {self.email}"
#
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# input_data = [
#     ("Full", "name1"),
#     ("Full", "name2"),
#     ("Full", "name3"),
#     ("Full", "name4"),
#     ("Full", "name5"),
#     ("Full", "name6"),
#     ("Full", "name7")
# ]
#
#
# def create_student(raw_student):
#     return Student(raw_student[0], raw_student[1], 0)
#
#
# result = list(map(create_student, input_data))
#
# print(result[1])
#
# result = list(map(lambda raw_student: Student(raw_student[0], raw_student[1], 0), input_data))
#
# print(result[5])
# ___________________________________________________________________________ #



