from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# servir arquivos estáticos
app.mount("/front-end", StaticFiles(directory="front-end"), name="front-end")


# rota que o JS vai chamar
@app.get("/api/somar")
def somar(a: int, b: int):
    return {"resultado": a * b}

# abrir o site
@app.get("/")
def home():
    return FileResponse("front-end/index.html")