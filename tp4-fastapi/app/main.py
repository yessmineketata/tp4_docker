from typing import Union
from fastapi import FastAPI, HTTPException, Header

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/secure")
async def secure_endpoint(api_key: str = Header(...)):
    """
    Ici FastAPI acceptera api_key ou api-key automatiquement
    """
    if api_key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Welcome to the secure endpoint!"}
