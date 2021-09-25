from fastapi import FastAPI, HTTPException
from .crud import *
from http import HTTPStatus
from specification import User

app = FastAPI(title="Examples API")


@app.get("/")
async def root() -> dict:
    return {"status": HTTPStatus.OK}


@app.post("/user/create")
async def create_user(data: User) -> dict:
    data = data.dict()
    resource = create(data)
    return {"status": HTTPStatus.CREATED, "resource_id": resource}


@app.get("/user/read")
async def get_user(resource_id: str) -> dict:
    data = read(resource_id)
    return {"status": HTTPStatus.OK, "data": data}


@app.delete("/user/delete")
async def delete_user(resource_id: str) -> dict:
    delete(resource_id)
    return {"status": HTTPStatus.OK}

