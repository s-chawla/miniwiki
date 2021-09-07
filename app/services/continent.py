import sqlalchemy.orm as orm

import app.models as models

from app.tasks import create_task, update_task
from app.schemas import continent as continent_schema


def get_continents(db: orm.Session):
    """
    This functions returns the list of continents
    """
    return db.query(models.Continent).all()


def get_continent_by_name(db: orm.Session, continent_name: str):
    """
    This functions retuns the Continent by Name of the continent
    Args-
        Continent_name:Name of the Continent
    Returns-
        Continent Details
    """
    return (
        db.query(models.Continent)
        .filter(models.Continent.name == continent_name)
        .first()
    )


def create_continent(db: orm.Session, continent: continent_schema.Continent):
    """
    This functions create a new continent
    Args-
        continent: continent object
    Returns-
        continent: newly created object
    """
    create_task.delay(model_name=models.Continent.__name__, data=continent.dict())
    return continent


def get_continent_by_id(db: orm.Session, continent_id: int):
    """
    This functions retuns the Continent by id of the continent
    Args-
        Continent_id:id of the Continent
    Returns-
        Continent Details
    """
    return (
        db.query(models.Continent).filter(models.Continent.id == continent_id).first()
    )


def update_continent(db: orm.Session, continent: continent_schema.Continent):
    """
    This functions updates the continent based on the object passed
    """

    update_task.delay(
        model_name=models.Continent.__name__, id=continent.id, data=continent.dict()
    )

    return continent


def delete_continent(db: orm.Session, continent_id: int):
    """
    This functions deletes a Continent based on id
    """
    db.query(models.Continent).filter(models.Continent.id == continent_id).delete()
    db.commit()
