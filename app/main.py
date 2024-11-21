from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import auth, users 

app = FastAPI(title="Shuttle Service API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Include the auth router
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router,prefix="/users", tags=["users"])

@app.get("/")
async def root():
  return {"message" : "Welcome to the Shuttle Service API"}

@app.get("/health")
async def health_check():
  return {"status" : "healthy"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)