from typing import Optional
from pydantic import BaseModel

from app.database import *


class BaseCountry(BaseModel):
    name: str
    population: int
    area: int
    no_national_park: int
    no_hospitals: int


class CreateCountry(BaseCountry):
    continent_id: Optional[int]


class Country(CreateCountry):
    id: Optional[int]
    # continent_id = int

    class Config:
        orm_mode = True
