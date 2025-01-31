from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import networkx as nx


app = FastAPI()

# Configuração de CORS para permitir conexões do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Criar um grafo simples
G = nx.Graph()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Adiciona o arquivo como um nó no grafo
    G.add_node(file.filename, content=open(file_path).read())

    return {"message": f"Ficheiro {file.filename} recebido e indexado!"}

@app.get("/graph/")
async def get_graph():
    """ Retorna os dados do grafo """
    nodes = [{"id": i, "label": n} for i, n in enumerate(G.nodes)]
    edges = [{"from": list(G.nodes).index(u), "to": list(G.nodes).index(v)} for u, v in G.edges]
    return {"nodes": nodes, "edges": edges}

@app.post("/pergunta/")
async def perguntar(pergunta: str = Form(...)):
    """ Simples busca no grafo """
    for node, data in G.nodes(data=True):
        if pergunta.lower() in data.get("content", "").lower():
            return {"resposta": f"A informação pode estar no documento: {node}"}
    return {"resposta": "Nenhuma informação relevante encontrada."}

@app.get("/")
async def root():
    return {"message": "API FastAPI rodando! Acesse /docs para ver a documentação."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
