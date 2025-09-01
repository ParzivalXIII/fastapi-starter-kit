# Main API entry point

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import get_db, init_db
from redis_cache import get_cache, set_cache

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database on startup
    print("Initializing database...")
    init_db()
    print("Database initialized successfully!")
    yield
    # Cleanup on shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.post("/user/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    cache_key = f"user:{db_user.id}"
    set_cache(cache_key, schemas.UserSchema.model_validate(db_user).model_dump())
    return db_user

@app.get("/user/{user_id}", response_model=schemas.UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    cache_key = f"user:{user_id}"
    cached_user = get_cache(cache_key)
    if cached_user:
        return cached_user
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    set_cache(cache_key, schemas.UserSchema.model_validate(user).model_dump())
    return user



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


