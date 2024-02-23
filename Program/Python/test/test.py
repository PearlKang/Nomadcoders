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
"""
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
"""

#5.2 Classes
"""
class Puppy:
    # pass
    def __init__(self):
        # print(self)
        # print("Puppy is born!")
        self.name = "Ruffus"
        self.age = 0.1
        self.breed = "Beagle"
ruffus = Puppy()
bibi = Puppy()
print(ruffus.name, ruffus.age, ruffus.breed)
print(bibi.name, bibi.age, bibi.breed)
"""

#5.3 Methods
"""
class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def __str__(self):
        # return "Hello!"
        return f"{self.breed} puppy named {self.name}"
ruffus = Puppy(
    name="Ruffus",
    age=0.1,
    breed="Beagle",
)
bibi = Puppy(
    name="Bibi",
    age=0.3,
    breed="Dalmatian",
)
print(ruffus.name, ruffus.age, ruffus.breed)
print(bibi.name, bibi.age, bibi.breed)
print(ruffus, bibi)
"""

#5.4 Inheritance
"""
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
class GuardDog(Dog):
    # def __init__(self, name, breed):
    #     self.name = name
    #     self.breed = breed
    #     self.age = 5
    def rrrrr(self):
        print("stay away!")
class Puppy(Dog):
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed
    # def __str__(self):
    #     return f"{self.breed} puppy named {self.name}"
    def woof_woof(self):
        print("Woof Woof!")
    # def introduce(self):
    #     self.woof_woof()
    #     print(f"My name is {self.name} and I am a baby {self.breed}")
    #     self.woof_woof()
ruffus = Puppy(
    name="Ruffus",
    age=0.1,
    breed="Beagle",
)
bibi = Puppy(
    name="Bibi",
    age=0.3,
    breed="Dalmatian",
)
# ruffus.woof_woof()
# ruffus.introduce()
# bibi.introduce()
"""

#5.5 Inheritance part Two
"""
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def sleep(self):
        print("zzzzzzzzz.....")
class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggresive = True
    def rrrrr(self):
        print("stay away!")
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        self.spoiled = True
    def woof_woof(self):
        print("Woof Woof!")
ruffus = Puppy(
    name="Ruffus",
    breed="Beagle",
)
bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian",
)
ruffus.woof_woof()
ruffus.sleep()
bibi.rrrrr()
bibi.sleep()
"""

#5.6 Recap
"""
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def sleep(self):
        print("zzzzzzzzz.....")
class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggresive = True
    def rrrrr(self):
        print("stay away!")
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        self.spoiled = True
    def woof_woof(self):
        print("Woof Woof!")
ruffus = Puppy(
    name="Ruffus",
    breed="Beagle",
)
bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian",
)
"""

#5.7 Code Challenge
"""
class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")
ben1 = Player(
    name="ben1",
    team="Team X"
)
ben2 = Player(
    name="ben2",
    team="Team Blue"
)
ben1.introduce()
ben2.introduce()
"""
"""
class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    def show_players(self):
        for player in self.players:
            player.introduce()
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
    def show_total_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"{self.team_name} is {total_xp} Points.")
team_x = Team("Team X")
team_x.add_player("ben1")
team_blue = Team("Team Blue")
team_blue.add_player("ben1")
team_blue.add_player("ben2")
team_blue.show_players()
team_blue.show_total_xp()
team_blue.remove_player("ben2")
team_blue.show_players()
"""

#6 Job Scraper
#6.0 Introduction
#6.1 Disclaimer
#6.2 BeautifulSoup
"""
# from requests import get
import requests
from bs4 import BeautifulSoup
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("section", id="category-2", class_="jobs").find_all("li", )
print(jobs)
"""

#6.3 Jobs
"""
import requests
from bs4 import BeautifulSoup
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
# print(jobs)
for job in jobs:
    title = job.find("span", class_="title").text
    # _region = job.find("span", class_="region").text
    # print(title, "-------------", region)
    # companies = job.find_all("span", class_="company")
    # company, position, _ = job.find_all("span", class_="company")
    company, position, region = job.find_all("span", class_="company")
    company = company.text
    position = position.text
    region = region.text
    print(title, company, position, region, "---------\n")
"""

#6.4 Recap
"""
import requests
from bs4 import BeautifulSoup
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
all_jobs = []
for job in jobs:
    title = job.find("span", class_="title").text
    company, position, region = job.find_all("span", class_="company")
    # url = job.find("a")["href"]
    # url = job.find("a")
    # if url:
    #     url = url["href"]
    url = job.find("div", class_="tooltip").next_sibling["href"]
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": f"https://weworkremotely.com/{url}"
    }
    all_jobs.append(job_data)
print(all_jobs)
"""

#6.5 Pagination
"""
import requests
from bs4 import BeautifulSoup
# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
all_jobs = []
def scrape_page(url):
    print(f"Scrapping {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com/{url}"
        }
        all_jobs.append(job_data)
def get_pages(url):
    # response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))
# print(buttons)
total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")
for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    # print("request page", x+1)
    # print(url)
    scrape_page(url)
print(len(all_jobs))
"""

#6.6 Code Challenge
"""
import requests
from bs4 import BeautifulSoup
keywords = [
    "flutter",
    "python",
    "golang"
]
# r = requests.get("https://remoteok.com/remote-flutter-jobs")
# print(r.status_code)
# print(r.content)
# inspect (refresh) > network pannel > first request(type document) > header > request header > User-Agent
r = requests.get(f"https://remoteok.com/remote-{keywords[2]}-jobs", headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
print(r.status_code)
print(r.content)
"""
"""
import requests
from bs4 import BeautifulSoup
keywords = [
    "flutter",
    "python",
    "golang"
]
all_jobs = []
def scrape_page(url):
    print(f"Scrapping {url}...")
    response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("td", class_="company")[1:]
    for job in jobs:
        title = job.find("h2", itemprop="title")
        name = job.find("h3", itemprop="name")
        # location, location_tooltip = job.find_all("div", class_="location")
        location = job.find("div", class_="location")
        salary = job.find("div", class_="location").next_sibling
        compny_url = job.find("a", itemprop="url")["href"]
        job_data = {
            "title": title.text,
            "name": name.text,
            "location": location.text,
            "salary": salary.text,
            "url": f"https://remoteok.com{compny_url}"
        }
        all_jobs.append(job_data)
for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    scrape_page(url)
print(all_jobs)
"""
"""
import requests
from bs4 import BeautifulSoup
# class Jobs:
#     def __init__(self, title, company, location, salary, url):
#         self.title = title
#         self.company = company
#         self.location = location
#         self.salary = salary
#         self.url = url
class JobScraper:
    def __init__(self, keywords):
        self.keywords = keywords
        self.all_lists = []
    def job_scraping(self, keyword):
        print(f"{keyword} Page Scrapping ...")
        response = requests.get(f"https://remoteok.com/remote-{keyword}-jobs", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        })
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("td", class_="company")[1:]
        for job in jobs:
            title = job.find("h2", itemprop="title")
            company = job.find("h3", itemprop="name")
            if len(job.find_all("div", class_="location")) >= 2:
                location, *others, salary = job.find_all("div", class_="location")
            else:
                location = job.find("div", class_="location")
            company_url = job.find("a", itemprop="url")["href"]
            job_data = {
                "title": title.text,
                "company": company.text,
                "location": location.text,
                "salary": salary.text,
                "url": f"https://remoteok.com{company_url}"
            }
            self.all_lists.append(job_data)
    def all_job_scraping(self):
        for keyword in self.keywords:
            self.job_scraping(keyword)
    def print_lists(self):
        print(self.all_lists)
keywords = ["flutter", "python", "golang"]
job_scraping = JobScraper(keywords)
job_scraping.all_job_scraping()
job_scraping.print_lists()
"""

#6.7 Dynamic Scraping
#6.8 Playwright
"""
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://google.com")

page.screenshot(path="screenshot.png")
"""

#6.9 Keyword Arguments
"""
# a, b > positional argument
# def plus(a, b):
#     return a + b

# plus(1, 2)

# keyword argument
def plus(a, b, c, d, e):
    return a + b

plus(1, 2, False, [1, 2], "hello")
plus(a=1, b=2, c=False, d=[1, 2], e="hello")
plus(e=1, c=2, b=False, d=[1, 2], a="hello")
# plus(e=1, c=2, b=False, d=[1, 2], "hello")
plus(1, c=2, b=False, d=[1, 2], a="hello")
"""

#6.10 Interactivity
"""
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/jobsfeed")

time.sleep(5)

# selector . class
page.click("button.Aside_searchButton__Xhqq3")

# page.locator("button.Aside_searchButton__Xhqq3").click()

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

# selector # id
page.click("a#search_tab_position")
""
time.sleep(5)

page.keyboard.down("End")

time.sleep(5)

page.keyboard.down("End")

time.sleep(5)

page.keyboard.down("End")

time.sleep(5)

page.keyboard.down("End")

time.sleep(5)
""

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

time.sleep(5)
# print(page.content())
content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
"""

#6.11 Collecting Jobs
"""
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# page.goto("https://www.wanted.co.kr/jobsfeed")

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))
"""

#6.12 Exporting To Excel
"""
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# page.goto("https://www.wanted.co.kr/jobsfeed")

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)

file = open("jobs.csv", "w")
writer = csv.writer(file)
# writer.writerow(["1","2","3","4"])
writer.writerow(
    [
        "Title",
        "Company",
        "Location",
        "Reward",
        "Link",
    ]
)
for job in jobs_db:
    writer.writerow(job.values())
"""

#6.13 Code Challenge
"""
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# page.goto("https://www.wanted.co.kr/jobsfeed")

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(
    [
        "Title",
        "Company",
        "Location",
        "Reward",
        "Link",
    ]
)
for job in jobs_db:
    writer.writerow(job.values())

file.close()
"""

#Code Challenge - class
"""
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class JobScraper():
    def __init__(self, keywords):
        self.keywords = keywords

    def get_content(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

        for x in range(5):
            time.sleep(2)
            page.keyboard.down("End")
        
        content = page.content()

        p.stop()

        return content

    def get_job_lists(self, content):
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        
        jobs_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            location = job.find("span", class_="JobCard_location__2EOr5").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text

            job = {
                "title": title,
                "company_name": company_name,
                "location": location,
                "reward": reward,
                "link": link,
            }

            jobs_db.append(job)

        return jobs_db

    def create_csv(self, keyword, jobs_db):
        if len(jobs_db) <= 0:
            return

        file = open(f"{keyword}_jobs.csv", mode="w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(jobs_db[0].keys())

        for job in jobs_db:
            writer.writerow(job.values())

        file.close()

    def job_scraper(self, keyword):
        content = self.get_content(keyword)
        jobs_db = self.get_job_lists(content)
        self.create_csv(keyword, jobs_db)

    def run_app(self):
        for keyword in self.keywords:
            self.job_scraper(keyword)

keywords = [
    "flutter",
    "nextjs",
    "kotlin",
    "python",
    "javascript",
]

job_scraper = JobScraper(keywords)
job_scraper.run_app()
"""

#7 [Bonus] Build a website with flask
#7.0 Introduction
#7.1 Hello Flask
"""
from flask import Flask

app = Flask("JobScrapper")

@app.route("/")
def home():
    return "hey there!!"

app.run("127.0.0.1", port=8080, debug=True)
"""

#7.2 Render Template
"""
#main.py
from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    # return "<h1>hey there!</h1><a href='/hello'>go to hello</a>"
    return render_template("home.html", name="ben")

@app.route("/hello")
def hello():
    return "hello you!"

app.run("127.0.0.1", port=8080, debug=True)
"""
"""
#home.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Job Scrapper</title>
  </head>
  <body>
    <h1>Hello to you! My name is {{name}}</h1>
  </body>
</html>
"""

#7.3 Form
"""
from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    # return "<h1>hey there!</h1><a href='/hello'>go to hello</a>"
    return render_template("home.html", name="ben")

@app.route("/search")
def hello():
    return render_template("search.html")

app.run("127.0.0.1", port=8080, debug=True)
"""
"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Job Scrapper</title>
  </head>
  <body>
    <h1>Job Scrapper</h1>
    <h4>What job do you want?</h4>
    <form action="/search">
      <input type="text" name="keyword" placeholder="Write keyword please" />
      <button>Search</button>
    </form>
  </body>
</html>
"""

#7.4 Recap
