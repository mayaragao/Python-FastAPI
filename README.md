# Python Fast API 

Repositório destinado ao desenvolvimento de rotas basicas em Python utilizando FastAPI. 

**Documentação**: https://fastapi.tiangolo.com

<a href="https://fastapi.tiangolo.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="FastAPI" height="35" width="40"/> </a>

##
### Instalação

Rode os comandos a seguir para instalar as dependencias do programa em um ambiente virtual na pasta do projeto.

```
pip3 install virtualenv
python -m venv venv
.\venv\Scripts\activate.bat
.\venv\Scripts\python -m pip install --upgrade pip
pip3 install -r requirements.txt
```

Após a instalação das dependencias necessárias, para iniciar o projeto, é necessário rodar o seguinte comando:

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


##
### Acesso a API
Acesse no seu navegador: http://localhost:8000/docs
