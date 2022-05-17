from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Rota raiz
@app.get("/")
def root():
    return {"Primeiro" :"Exemplo"}

# Criando modelo de dados
class Usuario(BaseModel):
    id: int
    name: str
    mail: str
    phone: str

# Criando base de dados

bd = [ 
    Usuario(id=1, name="Leonardo", mail="example@mail.com", phone="98769878"),
    Usuario(id=2, name="Leandro", mail="example1@mail.com", phone="94435676")
]

# Rota GET ALL

@app.get("/usuarios")
def get_usuarios():
    return bd

# Rota GET USER ID
@app.get("/usuarios/{id_usuario}")
def get_usuario_by_id(id_usuario: int):
    for usuario in bd:
        if(usuario.id==id_usuario):
            return usuario

    return {"Status": 404, "Mensagem": "Usuario não encontrado"}


# Rota INSERT NEW USER
@app.post("/usuarios")
def post_usuario(usuario: Usuario):
    #criar regras de validação
    bd.append(usuario)
    return usuario
