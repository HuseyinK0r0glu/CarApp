from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# to run it locally 
# DATABASE_URL = "postgresql://postgres:newpassword@localhost:5432/cardb"

# to run with docker we dont use localhost 
DATABASE_URL = "postgresql://postgres:newpassword@db:5432/cardb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        # Yield pauses a function's execution and returns a value temporarily
        yield db
    finally:
        db.close()
