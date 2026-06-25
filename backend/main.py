from fastapi import FastAPI

from .Controllers.ActivityTrackerController import router as activity_router

app = FastAPI()

app.include_router(activity_router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}