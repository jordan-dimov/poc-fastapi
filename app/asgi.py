from fastapi import FastAPI

from mangum import Mangum

app = FastAPI()


@app.get("/")
def list_items():
    return {"Items": []}


@app.get("/item/{item_id}")
def get_item(item_id: int, msg: str = None):
    return {"item": {"id": item_id}, "msg": msg}


def handler(event, context):

    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)

    return response
