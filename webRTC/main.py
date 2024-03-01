from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def baseRoute():
    return {"details" : "baseRoute"}

