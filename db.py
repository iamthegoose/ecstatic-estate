import redis
import json
from pydantic import BaseModel, ConfigDict
import psycopg2


psycopg2.connect()

class Response(BaseModel):
    world: str
    name: str


b = Response.model_validate(a)

print(b.world)
