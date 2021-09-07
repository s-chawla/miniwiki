import sqlalchemy.orm as orm
from fastapi.exceptions import HTTPException

from app import models, validation
from app.schemas import city as city_schema

from app.tasks import create_task, update_task


def get_cities(db: orm.Session):
    """
    This functions returns the list of cities
    """
    return db.query(models.City).all()


def create_city(db: orm.Session, city: city_schema.CreateCity):
    """
    This functions create a new city
    Args-
        city: city object
    Returns-
        city: newly created object
    """
    try:
        db_city_model = models.City(
            name=city.name,
            population=city.population,
            area=city.area,
            country_id=city.country_id,
        )

        validation.validate.validate_city(db, city)
        create_task.delay(model_name=models.City.__name__, data=city.dict())

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return db_city_model


def get_city_by_id(db: orm.Session, city_id: int):
    """
    This functions retuns the city by id of the city
    Args-
        city_id : id of the city
    Returns-
        city Details
    """
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities_by_countryid(db: orm.Session, country_id: int):
    """
    This functions retuns the list of cities in a Country
    Args-
        country_id:id of the country
    Returns-
        list of cities
    """
    return db.query(models.City).filter(models.City.country_id == country_id).all()


def update_city(db: orm.Session, city: city_schema.postCity):
    """
    This Funciton updates the City based on the id passed with new values
    """

    try:
        db_city = city_schema.City(
            id=city.id,
            name=city.name,
            population=city.population,
            area=city.area,
            country_id=city.country_id,
        )
        validation.validate.validate_city(db, city)
        update_task.delay(
            model_name=models.City.__name__, id=city.id, data=db_city.dict()
        )

    except Exception as e:

        raise HTTPException(status_code=400, detail=str(e))

    return db_city


def delete_city(db: orm.Session, city_id: int):
    """
    This functions deletes a City based on id
    """
    db.query(models.City).filter(models.City.id == city_id).delete()
    db.commit()
