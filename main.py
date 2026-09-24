""" 
Pydantic models for the application.
And validation using Python type annotations.
"""

from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    username: str
    email: str
    age: int