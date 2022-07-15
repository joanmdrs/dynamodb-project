from fastapi import FastAPI 
from models import UserModel
from serialize import UserOut, UserUpdate
app = FastAPI()


@app.get("/")
def index():
    instance =UserModel.scan()
    
    return list(instance)

@app.post("/")
def create(user:UserOut):
    user = user.dict()

    instance =UserModel()
    instance.email = user['email']
    instance.first_name = user['first_name']
    instance.last_name = user['last_name']
    instance.save()
    return

@app.delete("/{email}")
def deletar(email:str):
    #update_item('views', 1, action='add')
    instance = UserModel.get(email)
    instance.delete(UserModel.email==email)
    return

@app.put("/{email}")
def update(email:str, user:UserUpdate):
    user = user.dict()
    instance = UserModel.get(email)
    instance.update(actions=[
        UserModel.first_name.set(user['first_name']),
        UserModel.last_name.set(user['last_name'])
    ])
    
    return






