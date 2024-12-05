# class Car:
#     category = "motor vehicle"
#     def display(self):
#         print("This is a car")

# new_car = Car()
# print(new_car.category)
# new_car.display()
# print(Car.category)

# ====================================================================

# class Car:
#     category = "motor vehicle"
#     def __init__(self, name):
#         self.name = name


# new_car=Car("Audi")
# print(new_car.name)

# ====================================================================

# class Car:
#     category = "motor vehicle"

#     def __init__(self, name):
#         self.name = name
    
#     def display(self):
#         print(self.name)

#     def update(self, add_name):
#         self.name = add_name
#         print(self.name)

# new_car = Car("Audi")
# new_car.display()
# new_car.update("BMW")

# =============================================================================================

# write a python program to define and use a class representing a bank account,
# 1).create a class name "BankAccount" with the following,
# 	1.and attribute 'account_holder' to store the name of account holder
# 	2.and attribute 'balance' to store the account balance initialize to 0 
# 2).add the following method to the class ,
# deposit(amount) :- add the given amount
# withdraw(amount) :- subtract given amount from the balance if sufficient func exists
# display_balance() :-print current balance

# 3). write a small script to demonstrate following create an object of the balance account class,
# 	perform a few deposit and withdrawal operations
# 	display balance after each operations

# class BankAccount:
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount", amount)

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Amount should be positive")
#         elif amount > self.balance:
#             print("Amount does not have a sufficient amount")
#         else:
#             self.balance -= amount

#     def display_balance(self):
#         print("Account holder", self.account_holder)
#         print("Current balance:", self.balance)

# new_account = BankAccount("Saman")
# new_account.deposit(10000)
# new_account.withdraw(5000)
# new_account.display_balance()

# =============================================================================================


