from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.security import verify_password, create_access_token
from app.db.session import get_db
from app.schemas.token import Token
from app.config import settings
from app.models.user import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/login", response_model=Token)
async def login_for_access_token(
  form_data: OAuth2PasswordRequestForm = Depends(),
  db: Session = Depends(get_db)
):
  """
  Get access token for future authenticated requests
  """
  # Add the user authentication logic here in the next step
  # 1. Get the user by email
  user = db.query(User).filter(User.email == form_data.username).first()
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect email",
      headers={"WWW-Authenticate": "Bearer"},
    )
  # 2. Verify password
  if not verify_password(form_data.password, user.hashed_password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect password",
      headers={"WWW-Authenticate": "Bearer"},
    )
  
  # 3. Create Access Token
  access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
    data={"sub" : user.email}, # "sub" is a JWT standard claim
    expires_delta=access_token_expires
  )

  #Return the token
  return {
    "access_token": access_token,
    "token_type": "bearer"
  }
  
  




