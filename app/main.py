from typing import List
import uvicorn
import fastapi
from fastapi import FastAPI
import sqlalchemy.orm as orm

from app.schemas import (
    continent as continent_schema,
    city as city_schema,
    country as country_schema,
)
from app.services import (
    continent as continent_service,
    city as city_service,
    country as country_service,
)
import app.database as database


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
def read_root():
    return {"status": "running"}


@app.get("/continents", response_model=List[continent_schema.Continent])
def get_continents(db: orm.Session = fastapi.Depends(database.get_db)):
    """
    Get the list of continents
    """

    return continent_service.get_continents(db=db)


@app.post("/add_continent", response_model=continent_schema.Continent)
def add_continent(
    continent: continent_schema.CreateContinent,
    db: orm.Session = fastapi.Depends(database.get_db),
):
    """
    Create a new continent
    """

    return continent_service.create_continent(db=db, continent=continent)


@app.get("/continent/{continent_id}", response_model=continent_schema.Continent)
def get_continent(
    continent_id: int, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    Returns continent from the continent_id
    """
    return continent_service.get_continent_by_id(continent_id=continent_id, db=db)


@app.put("/continent", response_model=continent_schema.Continent)
def update_continent(
    continent: continent_schema.Continent,
    db: orm.Session = fastapi.Depends(database.get_db),
):
    """
    Update the continent data for passed id
    """
    return continent_service.update_continent(continent=continent, db=db)


@app.delete("/continent/{continent_id}")
def delete_continent(
    continent_id: int, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    Deletes the continent for the passed id
    """
    continent_service.delete_continent(db, continent_id=continent_id)
    return {"message": f"successfully deleted post with id: {continent_id}"}


@app.post("/add_country", response_model=country_schema.Country)
def add_country(
    country: country_schema.CreateCountry,
    db: orm.Session = fastapi.Depends(database.get_db),
):
    """
    Create a country
    """

    return country_service.create_country(db=db, country=country)


@app.get("/countries", response_model=List[country_schema.Country])
def get_countries(db: orm.Session = fastapi.Depends(database.get_db)):
    """
    List of countries
    """
    return country_service.get_contries(db=db)


@app.get("/countries/{continent_id}", response_model=List[country_schema.Country])
def get_countries(
    continent_id: int, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    List of countries on one continent
    """
    return country_service.get_countries_by_continentid(
        db=db, continent_id=continent_id
    )


@app.get("/country/{country_id}", response_model=country_schema.Country)
def get_country(country_id: int, db: orm.Session = fastapi.Depends(database.get_db)):
    """
    Continent from the passed continent_id
    """
    return country_service.get_country_by_id(country_id=country_id, db=db)


@app.delete("/country/{country_id}")
def delete_country(country_id: int, db: orm.Session = fastapi.Depends(database.get_db)):
    """
    This api deletes the country whoese id is passed
    """
    country_service.delete_country(db, country_id=country_id)
    return {"message": f"successfully deleted country with id: {country_id}"}


@app.put("/country", response_model=country_schema.Country)
def update_country(
    country: country_schema.Country, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    Update the country data for passed id
    """
    return country_service.update_country(country=country, db=db)


@app.post("/add_city", response_model=city_schema.City)
def add_city(
    city: city_schema.CreateCity, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    Create a city
    """

    return city_service.create_city(db=db, city=city)


@app.get("/cites", response_model=List[city_schema.City])
def get_cities(db: orm.Session = fastapi.Depends(database.get_db)):
    """
    List of cities
    """
    return city_service.get_cities(db=db)


@app.get("/cites/{country_id}", response_model=List[city_schema.City])
def get_cities(country_id: int, db: orm.Session = fastapi.Depends(database.get_db)):
    """
    List of cities in a country
    """
    return city_service.get_cities_by_countryid(db=db, country_id=country_id)


@app.get("/city/{city_id}", response_model=city_schema.City)
def get_continents(city_id: int, db: orm.Session = fastapi.Depends(database.get_db)):
    """
    City from the passed city_id
    """
    return city_service.get_city_by_id(city_id=city_id, db=db)


@app.delete("/city/{city_id}")
def delete_city(city_id: int, db: orm.Session = fastapi.Depends(database.get_db)):
    """
    Deletes the city of passed id
    """
    city_service.delete_city(db, city_id=city_id)
    return {"message": f"successfully deleted city with id: {city_id}"}


@app.put("/city", response_model=city_schema.City)
def update_city(
    city: city_schema.postCity, db: orm.Session = fastapi.Depends(database.get_db)
):
    """
    Updates the city data for passed id
    """
    return city_service.update_city(city=city, db=db)
