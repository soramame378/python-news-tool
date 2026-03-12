import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a")

for t in titles[:10]:
    print(t.text)