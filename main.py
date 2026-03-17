# FastAPI本体をインポート
from fastapi import FastAPI, Query

# CORS設定のためのミドルウェア
from fastapi.middleware.cors import CORSMiddleware

# 作成したニュース取得関数を読み込む
from news_scraper import get_news


# FastAPIアプリケーションを作成
# FastAPIはAPIを作成するためのフレームワークで、簡単にAPIを構築できる
app = FastAPI()


# CORS設定
# （ブラウザからAPIを呼び出すために必要）
app.add_middleware(

    # CORSミドルウェア(別のURLからのアクセスを許可する仕組み)を追加
    CORSMiddleware,

    # APIアクセスを許可するドメイン　実際はワイルドカードではなく　allow_origins=["https://your-site.com"]
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


# /news にアクセスされたときの処理 受取り口
# categoryクエリパラメータを受け取る（例: /news?category=it）
# クエリパラメータはURLの?以降に付加される情報で、APIに追加の情報を渡すために使用される
# categoryのデフォルト値は"top"（トップニュース）で、指定がない場合はトップニュースを返す
# Queryはクエリパラメータを定義するための関数で、デフォルト値やバリデーションを設定できる
# 例: /news?category=it でITニュースを取得することができる
# URL = 処理の入口
# クエリパラメータ = URLの?以降の情報 (例: category=it)
@app.get("/news")
def news(category: str = Query("top")):

    try:

        # ニュース取得関数を実行
        news_data = get_news(category)

        # 成功レスポンスをJSON形式で返す
        # 成功レスポンスは、APIが正常に処理されたことを示すための情報で、通常はステータスコード200とともに返される
        # 例: {"status": "success", "data": [...] } のような形式で、ニュースデータを含むレスポンスを返すことができる
        #JSON形式は、データを構造化して表現するための共通フォーマットで、APIレスポンスでよく使用される
        # 例: {"status": "success", "data": [...] } のような形式で、ニュースデータを含むレスポンスを返すことができる
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