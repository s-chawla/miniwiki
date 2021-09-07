from typing import Optional
from app.database import *
from pydantic import BaseModel


class BaseCity(BaseModel):
    name: str
    population: int
    area: int


class CreateCity(BaseCity):
    country_id: int


class City(BaseCity):
    id: Optional[int]

    class Config:
        orm_mode = True


class postCity(CreateCity, City):
    pass

    class Config:
        orm_mode = True
