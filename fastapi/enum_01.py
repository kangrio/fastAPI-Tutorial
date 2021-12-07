from fastapi import FastAPI
from enum import Enum, IntEnum

class Users(IntEnum, Enum):
    mrchoke = 1
    taz = 2
    tony = 3
    soe = 4
    anwa = 5
    perm = 6
    ta = 7
    pin = 8

app = FastAPI()

@app.get("/users/{info}")
async def get_username(info: Users):
    return {"id": info.value, "username": info.name }