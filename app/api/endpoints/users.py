from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User
from app.models.user import User as UserModel
from app.core.security import get_password_hash
from app.db.session import get_db


router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  """Create new user"""
  # Create a user instance
  existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
  if existing_user:
    raise HTTPException(
      status_code=400,
      detail="Email already registered"
    )
  # If email isn't used, create new user
  db_user = UserModel(
    email=user.email,
    full_name=user.full_name,
    hashed_password=get_password_hash(user.password),
    user_type=user.user_type
  )

  #Add to Database
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  
  return db_user
