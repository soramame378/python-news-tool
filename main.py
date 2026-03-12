from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_scraper import get_news

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def news():
    return get_news()