# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # ✅ load .env FIRST
# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# if not DATABASE_URL:
#     raise RuntimeError("DATABASE_URL is not set")

# engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base = declarative_base()
# import os
# from dotenv import load_dotenv
# import psycopg2

# load_dotenv()

# def get_conn():
#     return psycopg2.connect(
#         host=os.getenv("DATABASE_HOST"),
#         port=os.getenv("DATABASE_PORT"),
#         user=os.getenv("DATABASE_USER"),
#         password=os.getenv("DATABASE_PASSWORD"),
#         dbname=os.getenv("DATABASE_NAME")
#     )
    
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_conn():
    return psycopg2.connect(
        host=os.environ["DATABASE_HOST"],
        port=os.environ.get("DATABASE_PORT", 5432),
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        dbname=os.environ["DATABASE_NAME"],
        cursor_factory=RealDictCursor,
    )
