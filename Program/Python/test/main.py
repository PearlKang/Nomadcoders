#2 Variables and Functions
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
# def tax_calc(money):
#     return money * 0.35
# def pay_tax(tax):
#     print("thank you for paying", tax)
# to_pay = tax_calc(150000000)
# pay_tax(to_pay)
# pay_tax(tax_calc(150000000))

#2.11 Reutrn Recap
# my_name = "ben"
# my_age = 35
# my_color_eyes = "brown"
# print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")
# def make_juice(fruit):
#     return f"{fruit}+🥤"
# def add_ice(juice):
#     return f"{juice}+🧊"
# def add_sugar(iced_juice):
#     return f"{iced_juice}+🍬"
# juice = make_juice("🍎")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)
# print(perfect_juice)

#3 Control Flow
#3.0 If
# if 10 > 5:
#     print("Corrent!")
# a = 10
# if a == 10:
#     print("True!")

#3.1 Else & Elif
# password_correct = True
# if password_correct:
#     print("Here is your money")
# else:
#     print("Wrong password")
# winner = 10
# if winner > 10:
#     print("Winner is greater than 10")
# elif winner < 10:
#     print("Winner is less than 10")
# else:
#     print("Winner is 10")

#3.2 Recap
# winner = 5
# if winner <= 10:
#     print("If")
# elif winner <= 25:
#     print("elif")
# elif winner == 0:
#     print("elif 2")
# elif winner == 50:
#     print("elif 3")
# else:
#     print("Else")

#3.3 And & Or
# age = int(input("How old are you? "))
# print("user answer is", age)
# print(type(age))
# if age < 18:
#     print("You can't drink.")
# elif age >= 18 and age <= 35:
#     print("You drink beer!")
# elif age == 60 or age == 70:
#     print("Birthday party!")
# else:
#     print("Go ahead!")

#3.4 Python Standard Library
# from random import randint
# user_choice = int(input("choose number: "))
# pc_choice = randint(1, 50)
# if user_choice == pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("Lower! Computer chose", pc_choice)
# elif user_choice < pc_choice:
#     print("Higher! Computer chose", pc_choice)

#3.5 While
# """
# from random import randint
# user_choice = int(input("choose number: "))
# pc_choice = randint(1, 50)
# if user_choice == pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("Lower! Computer chose", pc_choice)
# elif user_choice < pc_choice:
#     print("Higher! Computer chose", pc_choice)
# """
# # while True:
# #     print("Hi im Ture")
# distance = 0
# while distance < 20:
#     print("I'm running:", distance, "km")
#     distance = distance + 1

#3.6 Python Casino
# from random import randint
# print("Welcome to Python Casino")
# pc_choice = randint(1, 100)
# playing = True
# while playing:
#     user_choice = int(input("choose number (1-100): "))
#     if user_choice == pc_choice:
#         print("You won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

#3.7 Recap
"""
from random import randint
print("Welcome to Python Casino")
pc_choice = randint(1, 100)
playing = True
while playing:
    user_choice = int(input("choose number (1-100): "))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")
"""

#4 Data Structures
#4.0 Methods
# mon = "Mon"
# tue = "Tue"
# wed = "Wed"
# thu = "Thu"
# fri = "Fri"
# days_of_week = ["Mon", "Thu", "Wed", "Thur", "Fri"]
# name = "ben"
# print(name.upper())
# print(name.capitalize())
# print(name.startswith("b"))
# print(name.endswith("n"))
# print(name.replace("e", "😂"))

#4.1 Lists
# days_of_week = ["Mon", "Thu", "Wed", "Thur", "Fri"]
# sample = [1, 2, 3, True, False, "hi", "blar", [1, 2, 3, [False, True]]]]
# print(days_of_week.count("Wed"))
# print(days_of_week)
# days_of_week.append("Sat")
# days_of_week.append("Sun")
# print(days_of_week[3])
# print(days_of_week)
# days_of_week.reverse()
# print(days_of_week)
# days_of_week.remove("Fri")
# print(days_of_week)
# days_of_week.clear()
# print(days_of_week)

#4.2 Tuples
# days_list = ["Mon", "Thu", "Wed"]
# days_tuple = ("Mon", "Thu", "Wed")
# # days_list.~~~
# # days_tuple.count or .index # 변경x
# print(days_list[0], days_tuple[0])
# print(days_list[-1], days_tuple[-1])
# print(days_list[-3], days_tuple[-3])

#4.3 Dicts
# player = {
#     'name': 'ben',
#     'age': 35,
#     "live": True,
#     'fav_food': ["🍕", "🍔"]
# }
# print(player)
# print(player.get('age'))
# print(player.get('fav_food'))
# print(player['fav_food'])
# print(player)
# player.pop('age')
# print(player)
# player['xp'] = 1500
# print(player)
# player['fav_food'].append("🍜")
# print(player)
# print(player.get('fav_food'))
# print(player['fav_food'])

#4.4 Recap
# print("ben".upper())
# print("ben".endswith("a"))
# numbers = [5, 3, 1, 5, 7, 3, "True", True, 12]
# print(numbers)
# numbers.append(["🍕", "🍔"])
# print(numbers[7])
# print(numbers[-1])
# print(numbers)
# numbers.clear()
# print(numbers)
# number = (1, 2, 3, 4, 5, True, "xxxxx")
# print(number.count)
# player = {
#     "name": "ben",
#     "age": 12,
#     "alive": True,
#     "fav_food": ("🍕", "🍔"),
#     "friend": {
#         "name": "lynn",
#         "fav_food": ["🍎"]
#     }
# }
# print(player)
# print(player["friend"]["fav_food"])
# player["fav_food"] = "🍎"
# print(player)
# player.pop("alive")
# print(player)
# player['friend']['fav_food'].append("🍌")
# print(player)

#4.5 For Loops
# websites = (
#     "google.com",
#     "airbnb.com",
#     "twitter.com",
#     "facebook.com",
#     "tiktok.com"
# )
# for webstie in websites:
#     print("webstie is equals to", webstie)

#4.6 URL Formatting
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com"
# )
# for website in websites:
#     # if website.startswith("https://"):
#     #     print("good to go")
#     # else:
#     #     print("we have to fix it")
#     # if not website.startswith("https://"): # == False
#     #     print("have to fix it")
#     if not website.startswith("https://"): # == False
#         website = f"https://{website}"
#     print(website)

#4.7 Requests
"""
# import requests
from requests import get
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)
for website in websites:
    # if website.startswith("https://"):
    #     print("good to go")
    # else:
    #     print("we have to fix it")
    # if not website.startswith("https://"): # == False
    #     print("have to fix it")
    if not website.startswith("https://"): # == False
        website = f"https://{website}"
    print(website)
"""

#4.8 Status Codes
"""
from requests import get
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)
results = {}
for website in websites:
    if not website.startswith("https://"): # == False
        website = f"https://{website}"
    response = get(website)
    # print(response)
    # print(response.status_code)
    if response.status_code == 200:
        # print(f"{website} is OK")
        results[website] = "OK"
    else:
        # print(f"{website} not OK")
        results[website] = "FAILED"
print(results)
"""

#4.9 Recap
"""
from requests import get
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    "https://httpstat.us/101",
    "https://httpstat.us/200",
    "https://httpstat.us/300",
    "https://httpstat.us/404",
    "https://httpstat.us/502",
)
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response_stat_code = get(website).status_code
    if response_stat_code >= 500:
        results[website] = f"{response_stat_code} status code is Server Error"
    elif response_stat_code >= 400:
        results[website] = f"{response_stat_code} status code is Client Error"
    elif response_stat_code >= 300:
        results[website] = f"{response_stat_code} status code is Redirection"
    elif response_stat_code >= 200:
        results[website] = f"{response_stat_code} status code is Successful"
    elif response_stat_code >= 100:
        results[website] = f"{response_stat_code} status code is Informational Response"
    else:
        results[website] = "FAILED"
print(results)
"""

#5 OOP
#5.0 Introduction
#5.1 Why We Need OOP
ben = {
    "name": "Ben",
    "XP": 1000,
    "team": "Team X",
}
def create_player_for_team(name, xp, team):
    return ""
def create_player(name, xp, team):
    return {
        "name": name,
        "XP": xp,
        "team": team,
    }
def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")
introduce_player(ben)
# introduce_player(1212)
ben2 = create_player("Ben2", 1500, "Team X")
ben3 = create_player("Ben3", 1500, "Team Blue")
teams = {
    "Team X": [ben2],
    "Team Blue": [ben3],
}
