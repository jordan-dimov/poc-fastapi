from typing import Optional

from fastapi import FastAPI, HTTPException

from starlette.requests import Request

from mangum import Mangum

from app.model import ItemBackend

app = FastAPI(
    title="Proof of concept for a FastAPI lambda using Serverless and Mangum",
    description="This is just a small feasability POC",
    version="0.0.1a",
    openapi_prefix="/dev",
)

item_store = ItemBackend()


@app.get("/")
def list_items():
    items = item_store.list_items()
    return {"Items": items}


@app.get("/item/{item_id}")
def get_item(request: Request, item_id: int, msg: Optional[str] = None):
    event = request["aws.event"]
    try:
        item = item_store.get_item(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item_id": item_id, "item": item, "msg": msg, "event": event}


def handler(event, context):

    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)

    return response
