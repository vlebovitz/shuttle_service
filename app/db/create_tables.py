from app.db.session import engine
from app.db.base import Base

def create_tables() -> None:
  Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
  create_tables()
  print("Tables created successfully")