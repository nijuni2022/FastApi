from main import collection , app
from pydantic import BaseModel
from copy import deepcopy
from typing import Optional



class User(BaseModel):
   
   nome: Optional[str]
   telefone: Optional[str]
   email: Optional[str]
   endereco: Optional[str]
   user_id : str

@app.post("/atualizar")
def update(user: User):
    
    user_dict = dict(user)
    
    found_user_old = collection.find_one({"user_id":user_dict.get("user_id"), "status":"ativo"}, {"_id":0})
    
    new_user = deepcopy(found_user_old)
    new_user.update({
        "nome": user_dict.get("nome"),
        "telefone": user_dict.get("telefone"),
        "email": user_dict.get("email"),
        "endereco": user_dict.get("endereco"),
        "user_id": user_dict.get("user_id")

    })
    collection.update_one(found_user_old, {"$set":new_user})
    return "registro atualizado", 200
