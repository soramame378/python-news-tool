# HTTP通信を行うライブラリ（Webページを取得するため）
import requests

# HTML解析ライブラリ（スクレイピング）
from bs4 import BeautifulSoup


# ニュース取得関数
def get_news():

    # ニュース取得元のURL
    url = "https://news.yahoo.co.jp/"

    # URLにアクセスしてHTMLを取得
    # resにはレスポンス（ページ情報）が入る
    res = requests.get(url)

    # HTMLを解析する準備
    # res.text = HTMLの中身
    # html.parser = Python標準のHTML解析エンジン
    soup = BeautifulSoup(res.text, "html.parser")

    # ニュースタイトルを保存するリスト
    titles = []

    # CSSセレクタでニュースタイトル部分を取得
    # a.sc-110wjhy-2 に該当するHTML要素を全部取得
    for item in soup.select("a.sc-110wjhy-2"):

        # 要素のテキスト（ニュースタイトル）を取得してリストに追加
        titles.append(item.text)

    # 最初の5件だけ返す
    return titles[:5]
