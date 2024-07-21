
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faiss_crud import FAISSIndexManager
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index_manager = FAISSIndexManager('faiss_index.index')

class TextData(BaseModel):
    text: str

@app.post("/add/")
async def add_text(data: TextData):
    embedding = model.encode([data.text])
    index_manager.add_embeddings(embedding)
    return {"message": "Text added successfully."}

@app.get("/search/")
async def search_text(query: str, k: int = 5):
    embedding = model.encode([query])
    distances, indices = index_manager.search(embedding[0], k)
    return {"distances": distances.tolist(), "indices": indices.tolist()}

@app.post("/update/")
async def update_text(ids: list, new_texts: list):
    # Not implemented as FAISS does not support direct updates
    raise HTTPException(status_code=501, detail="Update not supported.")

@app.delete("/delete/")
async def delete_text(ids: list):
    # Not implemented as FAISS does not support direct deletion
    raise HTTPException(status_code=501, detail="Deletion not supported.")
