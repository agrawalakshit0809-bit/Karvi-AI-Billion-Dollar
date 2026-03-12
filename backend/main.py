from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Karvi AI Online", "message": "Billion Dollar Journey Starts Now"}
