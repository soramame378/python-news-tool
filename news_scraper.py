import requests
from bs4 import BeautifulSoup

def get_news():

    url = "https://news.yahoo.co.jp/"

    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    titles = []

    for item in soup.select("a.sc-110wjhy-2"):
        titles.append(item.text)

    return titles[:5]