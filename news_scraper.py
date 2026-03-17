# HTTP通信を行うライブラリ
# requestsはWebサイトからデータを取得するためのライブラリ
import requests

# HTML解析ライブラリ（スクレイピングで使用）
# BeautifulSoupはHTMLを解析して、必要な情報を抽出するためのライブラリ
from bs4 import BeautifulSoup


def get_news(category="top"):

    # カテゴリURL
    urls = {

        "top": "https://news.yahoo.co.jp/",

        "it": "https://news.yahoo.co.jp/categories/it",

        "business": "https://news.yahoo.co.jp/categories/business",

        "world": "https://news.yahoo.co.jp/categories/world",

        "sports": "https://news.yahoo.co.jp/categories/sports"
    }

    # URL取得
    url = urls.get(category, urls["top"])

    # ブラウザアクセスを装うヘッダー
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # HTTPリクエスト送信
    res = requests.get(url, headers=headers)

    # HTML解析
    soup = BeautifulSoup(res.text, "html.parser")

    # ニュース保存リスト
    news_list = []

    # すべてのaタグ取得
    for item in soup.select("a"):

        # タイトル取得
        title = item.text.strip()

        # リンク取得
        link = item.get("href")

        # タイトルが長いものだけ採用
        if len(title) > 20 and link:

            # 辞書形式で保存
            news_list.append({
                "title": title,
                "link": link
            })

    # 最初の5件だけ返す
    return news_list[:5]