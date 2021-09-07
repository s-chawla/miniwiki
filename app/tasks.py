from app.schemas import continent
from worker import app
from app.database import SessionLocal
from app.models import City, Continent, Country

models_dict = {
    "City": City,
    "Country": Country,
    "Continent": Continent,
}

db = SessionLocal()


@app.task(name="create_task")
def create_task(model_name: str, data: dict):
    db_obj = models_dict[model_name](**data)
    db.add(db_obj)
    try:
        db.commit()
        db.refresh(db_obj)
    except:
        db.rollback()
    finally:
        db.close()
    return True


@app.task(name="update_task")
def update_task(model_name: str, id: int, data: dict):
    print("in update task", id, data)
    db_obj = db.query(models_dict[model_name]).get(id)
    for field, data in data.items():
        setattr(db_obj, field, data)
    db.add(db_obj)
    try:
        db.commit()
        db.refresh(db_obj)
    except:
        db.rollback()
    finally:
        db.close()
    return True


@app.task(name="delete_task")
def delete_task(model_name: str, id: int):
    db_obj = db.query(models_dict[model_name]).get(id)
    db.delete(db_obj)
    db.commit()
    return True
