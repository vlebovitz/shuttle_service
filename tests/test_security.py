from app.core.security import get_password_hash, verify_password

def test_password_hashing():
  # create test password
  original_password = "password123"

  #hash the password
  hashed_password = get_password_hash(original_password)

  print(f"Original Passowrd: {original_password}")
  print(f"Hashed Password: {hashed_password}")


  #verify the hashing works
  assert verify_password(original_password, hashed_password)

  wrong_password = "wrongpassword123"
  assert not verify_password(wrong_password, hashed_password)
  


