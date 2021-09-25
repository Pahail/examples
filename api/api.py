from fastapi import FastAPI, HTTPException
from .crud import *
from http import HTTPStatus

app = FastAPI(title="Examples API")


@app.get("/")
async def root() -> dict:
    return {"status": HTTPStatus.OK}


@app.post("/create")
async def create_record(data: dict) -> dict:
    resource = create(data)
    return {"status": HTTPStatus.CREATED, "resource_id": resource}


@app.get("/read")
async def read_record(resource_id: str) -> dict:
    data = read(resource_id)
    return {"status": HTTPStatus.OK, "data": data}


@app.delete("/delete")
async def delete_record(resource_id: str) -> dict:
    delete(resource_id)
    return {"status": HTTPStatus.OK}

