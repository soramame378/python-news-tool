from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
def get_news():
    return {"message": "news"}