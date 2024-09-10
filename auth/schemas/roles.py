from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class Role(BaseModel):
    id: str
    name: str = Field(...)