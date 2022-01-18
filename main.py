from fastapi import FastAPI

from pymongo import MongoClient
from fastapi.responses import JSONResponse

client = MongoClient("localhost", 27017)

db = client.get_database("crud")
collection = db.get_collection("agenda")

app = FastAPI()