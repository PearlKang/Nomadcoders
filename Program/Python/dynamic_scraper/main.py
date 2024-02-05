from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://google.com")
# page.goto("https://www.wanted.co.kr/search?query=python&tab=position")

page.screenshot(path="screenshot.png")


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