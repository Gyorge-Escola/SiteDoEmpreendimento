from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# permite o JS acessar a API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois você pode restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def status():
    return {"message": "API funcionando"}

@app.post("/soma")
def soma(data: dict):
    return {"resultado": data["a"] + data["b"]}