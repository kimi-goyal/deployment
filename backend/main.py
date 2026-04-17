# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from database import get_conn


# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # later restrict
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def root():
#     return {"status": "Backend running"}

# @app.get("/items")
# def read_items():
#     conn = get_conn()
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM items")
#     items = cur.fetchall()

#     cur.close()
#     conn.close()

#     return [{"id": item[0], "name": item[1]} for item in items]

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_conn
from db_init import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()   # ✅ auto initialize DB on deploy

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.get("/items")
def read_items():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM items")
    items = cur.fetchall()

    cur.close()
    conn.close()

    return [{"id": item[0], "name": item[1]} for item in items]