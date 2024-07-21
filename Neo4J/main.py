from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Neo4jConnection

app = FastAPI()
neo4j_uri = "neo4j+s://0ad56b7d.databases.neo4j.io"
conn = Neo4jConnection(uri=neo4j_uri, user="neo4j", pwd="1f34hV2y1AH-LnAMYBayxEKC_od69V2ACsJfzepPrkk")


class Student(BaseModel):
    id: str
    name: str
    age: int
    grade: str


@app.post("/students/")
def api_create_student(student: Student):
    conn.create_student(student.dict())
    return {"message": "Student created successfully"}


@app.get("/students/")
def api_get_students():
    students = conn.get_students()
    return students


@app.get("/students/{student_id}")
def api_get_student(student_id: str):
    student = conn.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{student_id}")
def api_update_student(student_id: str, student: Student):
    conn.update_student(student_id, student.dict())
    return {"message": "Student updated successfully"}


@app.delete("/students/{student_id}")
def api_delete_student(student_id: str):
    conn.delete_student(student_id)
    return {"message": "Student deleted successfully"}
