from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from app.config import settings

#Password hashing setup

pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
  """
    Verify a plain password against a hashed password
  """
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
  """
  Hash a password
  """
  return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
  """
  Create JMT access token
  """

  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  
  to_encode.update({"exp" : expire})
  encoded_jwt = jwt.encode(
    to_encode,
    settings.SECRET_KEY,
    algorithm=settings.ALGORITHM
  )
  return encoded_jwt


