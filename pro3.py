from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql

app = FastAPI()

class Student(BaseModel):
    cname: str
    address: str

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="data_science",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/")
def home():
    return {"message": "FastAPI + MySQL Student Table"}

@app.get("/student")
def get_all_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    conn.close()
    return data

@app.get("/student/{cid}")
def get_student_by_id(cid: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE cid = %s", (cid,))
    data = cur.fetchone()
    conn.close()

    if not data:
        raise HTTPException(status_code=404, detail="Student not found")

    return data

@app.post("/student")
def add_student(student: Student):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO student (cname, address) VALUES (%s, %s)",
        (student.cname, student.address)
    )
    conn.commit()
    conn.close()
    return {"message": "Student added successfully"}

@app.put("/student/{cid}")
def update_student(cid: int, student: Student):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE student SET cname=%s, address=%s WHERE cid=%s",
        (student.cname, student.address, cid)
    )
    conn.commit()
    conn.close()
    return {"message": "Student updated successfully"}

@app.delete("/student/{cid}")
def delete_student(cid: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE cid=%s", (cid,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}
