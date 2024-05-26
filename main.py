from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
async def hello():
    return {"name": "Sasha",
            "nameTwo": "Vova"}


logging.basicConfig(level="DEBUG")
