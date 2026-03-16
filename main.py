# main.py 修正版

# FastAPI本体
from fastapi import FastAPI

# CORS設定（別ドメインからのアクセスを許可するため）
from fastapi.middleware.cors import CORSMiddleware

# HTMLファイルを返すための機能
from fastapi.responses import FileResponse

# ニュース取得関数を読み込む
from news_scraper import get_news

# ファイルパス操作用ライブラリ
import os


# FastAPIアプリ作成
app = FastAPI()


# -----------------------------
# CORS設定
# -----------------------------
# JavaScriptからAPIアクセスするために必要
# * = どこからでもアクセス可能
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 許可するURL
    allow_methods=["*"],   # 許可するHTTPメソッド
    allow_headers=["*"],   # 許可するヘッダ
)


# -----------------------------
# ルートアクセス
# -----------------------------
# http://127.0.0.1:8000 にアクセスしたとき
@app.get("/")

def home():

    # index.html をブラウザに返す
    return FileResponse(
        os.path.join(
            os.path.dirname(__file__),  # このファイルの場所
            "index.html"                # index.html
        )
    )


# -----------------------------
# ニュース取得API
# -----------------------------
# http://127.0.0.1:8000/news
@app.get("/news")

def news():

    # news_scraper.py の get_news() を実行
    # ニュースタイトルのリストを返す
    return get_news()