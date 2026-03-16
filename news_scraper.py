# HTTP通信を行うライブラリ
import requests

# HTML解析ライブラリ（スクレイピングで使用）
from bs4 import BeautifulSoup


# ニュース取得関数
def get_news():

    # 取得するニュースサイト
    url = "https://news.yahoo.co.jp/"

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