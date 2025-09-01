# Schema Definitions

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # "orm_mode=True" is deprecated