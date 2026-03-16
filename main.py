# FastAPI本体をインポート
from fastapi import FastAPI, Query

# CORS設定のためのミドルウェア
from fastapi.middleware.cors import CORSMiddleware

# 作成したニュース取得関数を読み込む
from news_scraper import get_news


# FastAPIアプリケーションを作成
app = FastAPI()


# CORS設定
# （ブラウザからAPIを呼び出すために必要）
app.add_middleware(

    # CORSミドルウェアを追加
    CORSMiddleware,

    # APIアクセスを許可するドメイン
    allow_origins=[
        "*"
    ],

    # Cookieなど認証情報の送信を許可
    allow_credentials=True,

    # すべてのHTTPメソッドを許可
    allow_methods=["*"],

    # すべてのHTTPヘッダーを許可
    allow_headers=["*"],
)


# /news にアクセスされたときの処理
@app.get("/news")
def news(category: str = Query("top")):

    try:

        # ニュース取得関数を実行
        news_data = get_news(category)

        # 成功レスポンスをJSON形式で返す
        return {
            "status": "success",
            "data": news_data
        }

    # 例外（エラー）が発生した場合
    except Exception as e:

        # エラー内容を返す
        return {
            "status": "error",
            "message": str(e)
        }