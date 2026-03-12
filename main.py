# main.py 修正版
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from news_scraper import get_news
import os

app = FastAPI()

# CORS設定：どこからでもアクセス可能
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルートアクセスで index.html を返す
@app.get("/")
def home():
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))

# /news にアクセスしたらニュースデータを返す
@app.get("/news")
def news():
    return get_news()