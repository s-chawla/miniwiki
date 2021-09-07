import sqlalchemy.orm as orm
from fastapi.exceptions import HTTPException

from app import models, validation
from app.tasks import create_task, update_task
from app.schemas import country as country_schema


def get_contries(db: orm.Session):
    """
    This functions returns the list of countries
    """
    return db.query(models.Country).all()


def get_country_by_id(db: orm.Session, country_id: int):
    """
    This functions retuns the Country by id of the country
    Args-
        country_id:id of the country
    Returns-
        country Details
    """
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_countries_by_continentid(db: orm.Session, continent_id: int):
    """
    This functions retuns the list of Countries in a Continent
    Args-
        continent_id:id of the continent
    Returns-
        list of countries
    """
    return (
        db.query(models.Country)
        .filter(models.Country.continent_id == continent_id)
        .all()
    )


def get_country_by_name(db: orm.Session, country_name: str):
    """
    This functions retuns the Country by Name of the country
    Args-
        country_name:Name of the country
    Returns-
        country details
    """
    return db.query(models.Country).filter(models.Country.name == country_name).first()


def create_country(db: orm.Session, country: country_schema.CreateCountry):
    """
    This functions create a new country
    Args-
        country: country object
    Returns-
        country: newly created object
    """
    try:

        validation.validate.validate_country(db, country)
        create_task.delay(model_name=models.Country.__name__, data=country.dict())

    except Exception as e:

        raise HTTPException(status_code=400, detail=str(e))

    return country


def delete_country(db: orm.Session, country_id: int):
    """
    This functions deletes a County based on id
    """
    db.query(models.Country).filter(models.Country.id == country_id).delete()
    db.commit()


def update_country(db: orm.Session, country: country_schema.Country):
    """
    This functions updates the country based on the object passed
    """
    try:

        validation.validate.validate_country(db, country)
        update_task.delay(
            model_name=models.Country.__name__, id=country.id, data=country.dict()
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return country
