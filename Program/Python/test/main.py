#2.0 Hello world
# print("Hello world!")

#2.1 Variables
# a = 2
# b = 5
# c = a + b
# print(c)
# my_age = 88 #snake case, 보통 파이썬에서 자주 사용
# myAge = 88  #camel case, 보통 javascript에서 사용
# myage = 88
# 123my_age = 88
# my_age123 = 88
# */my_age = 88
# my age = 88

#2.2 Booleans and Strings
# my_name = "Ben"
# print(my_name)
# dead = False # True

#2.3 Recap
# my_name = "Ben"
# age = 12
# dead = False
# print("Hello my name is", my_name)
# print("and I'm", age, "years old")

#2.4 Functions
# print(True)
# print("hello")
# print(12)
# print(True, "hello", 12)
# def say_hello():
#     print("hello how r u?")
# say_hello()

#2.5 Indentation
# def say_hello():
#     print("hello how r u?")
# def say_bye():
#     print("bye bye")
# say_hello()

#2.6 Parameters
# def say_hello(user_name):
#     print("hello", user_name, "how are you?")
# say_hello("ben")
# say_hello("ben2")
# say_hello("ben3")

#2.7 Multiple Parameters
# def say_hello(user_name, user_age):
#     print("hello", user_name)
#     print("you are", user_age, "years old")
# say_hello("ben", 35)

#2.8 Recap
# def tax_calculator(money):   #salary, bank account, balance
#     print(money * 0.35)
# tax_calculator(1500000000000)
# tax_calculator(150)

#2.9 Default Parameters
# def say_hello(user_name="anonymous"):
#     print("hello", user_name)
# say_hello("Ben")
# say_hello()
# def plus(a=0, b=0):
#     print(a + b)
# def minus(a=0, b=0):
#     print(a - b)
# def multiply(a=0, b=0):
#     print(a * b)
# def divide(a=0, b=1):
#     print(a / b)
# def power_of(a=0, b=0):
#     print(a ** b)

#2.10 Return Values
# def tax_calc(money):
#     print(money * 0.35)
# def pay_tax(tax):
#     print("thank you for paying", tax)
def tax_calc(money):
    return money * 0.35
def pay_tax(tax):
    print("thank you for paying", tax)
to_pay = tax_calc(150000000)
pay_tax(to_pay)
pay_tax(tax_calc(150000000))

