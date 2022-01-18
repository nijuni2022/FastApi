from typing import Optional
from pydantic import BaseModel
import fastapi
import uuid
from main import collection , app



class User(BaseModel):
   
   nome: str
   telefone: str
   email: str
   endereco: str




@app.post("/cadastro")
def read_item(user: User):
   user_dict = dict(user)
   user_dict.update({"user_id": str(uuid.uuid4())})
   user_dict.update({"status": "ativo"})
   collection.insert_one(user_dict)
   return "usuario criado", 200



