# HTTP通信を行うためのライブラリ
import requests

# HTMLを解析するためのライブラリ（スクレイピングでよく使う）
from bs4 import BeautifulSoup


# ニュースを取得する関数
def get_news():

    # 取得するニュースサイトのURL
    url = "https://news.yahoo.co.jp/"

    # HTTPヘッダー
    # 一部のサイトは「ブラウザからのアクセス」でないとブロックするため
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # 指定URLにHTTPリクエストを送信
    # res にレスポンス（HTMLデータなど）が入る
    res = requests.get(url, headers=headers)

    # HTMLを解析するためBeautifulSoupに渡す
    # res.text → 取得したHTML文字列
    # html.parser → Python標準のHTML解析エンジン
    soup = BeautifulSoup(res.text, "html.parser")

    # ニュースタイトルを入れるリスト
    titles = []

    # HTML内のすべてのaタグ（リンク）を取得
    # soup.select()はCSSセレクタでHTML要素を取得できる
    for item in soup.select("a"):

        # aタグのテキスト部分（リンクタイトル）を取得
        # strip()は前後の空白や改行を削除する
        title = item.text.strip()

        # タイトルが短すぎるものは除外
        # （メニューなどの不要なリンクが含まれるため）
        if len(title) > 20:

            # ニュースタイトルリストに追加
            titles.append(title)

    # 最初の5件だけ返す
    return titles[:5]