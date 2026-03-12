import requests
from bs4 import BeautifulSoup
"""一時的な可視化のため、実際のスクレイピングコードをコメントアウトしています。
def get_news():

    url = "https://news.yahoo.co.jp/"

    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    titles = []

    for item in soup.select("a.sc-110wjhy-2"):
        titles.append(item.text)

    return titles[:5]
"""

"""テスト用のダミーデータを返す関数"""
def get_news():
    return [
        "テストニュース1",
        "テストニュース2",
        "テストニュース3"
    ]