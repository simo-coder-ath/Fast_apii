from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str
    name: str = Field(min_length=1)
    author: str = Field(min_length=1)
    publisher: str = Field(min_length=1)