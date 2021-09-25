import os
import json
import uuid

db_path = "./db/"


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def create(data: dict) -> uuid.UUID:
    resource_id = uuid.uuid4()
    file_name = db_path + str(resource_id) + ".json"
    with open(file_name, 'w') as fd:
        json.dump(data, fd)
    return resource_id


def read(resource_id: str) -> dict:
    file_name = db_path + resource_id + ".json"
    with open(file_name, 'r') as fd:
        data = json.load(fd)
        return data


def delete(resource_id: str):
    file_name = db_path + resource_id + ".json"
    os.remove(file_name)
