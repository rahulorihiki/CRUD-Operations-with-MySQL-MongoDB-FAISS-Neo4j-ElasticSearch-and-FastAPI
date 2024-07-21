from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import (
    create_connection,
    create_document,
    read_document,
    update_document,
    delete_document,
)

app = FastAPI()
es = create_connection()


class Document(BaseModel):
    id: str
    content: dict


@app.post("/documents/")
def api_create_document(doc: Document):
    create_document(es, "myindex", doc.id, doc.content)
    return {"message": "Document created successfully"}


@app.get("/documents/{doc_id}")
def api_read_document(doc_id: str):
    doc = read_document(es, "myindex", doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


@app.put("/documents/{doc_id}")
def api_update_document(doc_id: str, doc: Document):
    update_document(es, "myindex", doc_id, doc.content)
    return {"message": "Document updated successfully"}


@app.delete("/documents/{doc_id}")
def api_delete_document(doc_id: str):
    delete_document(es, "myindex", doc_id)
    return {"message": "Document deleted successfully"}
