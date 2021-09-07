from typing import Optional

from pydantic import BaseModel

# from ..database import *


class CreateContinent(BaseModel):
    name: str
    population: int
    area: int


class Continent(CreateContinent):
    id: Optional[int]

    class Config:
        orm_mode = True
