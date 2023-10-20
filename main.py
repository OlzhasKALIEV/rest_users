import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import SessionLocal
from models_users.basemodels import Users, UserUpdate
from models_users.models import User

load_dotenv()

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/create/")
# POST: http://0.0.0.0:8000/api/create/ json = {"name": "Dmitriy","surname": "Ushakov","patronymic": "Vasilevich"}
def create_user_endpoint(user: Users):
    api_agify_url = os.getenv("API_AGIFY_URL")
    api_genderize_url = os.getenv("API_GENDERIZE_URL")
    api_nationalize_url = os.getenv("API_NATIONALIZE_URL")

    url_age = f"{api_agify_url}?name={user.name}"
    url_gender = f"{api_genderize_url}/?name={user.name}"
    url_nationality = f"{api_nationalize_url}/?name={user.name}"

    response_age = requests.get(url_age)
    response_gender = requests.get(url_gender)
    response_nationality = requests.get(url_nationality)

    data_age = response_age.json()
    data_gender = response_gender.json()
    data_nationality = response_nationality.json()

    user_data = User(
        name=user.name,
        surname=user.surname,
        patronymic=user.patronymic,
        age=data_age["age"],
        gender=data_gender["gender"],
        nationality=data_nationality["country"][0]['country_id']
    )

    db = SessionLocal()
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return {"message": "User created successfully"}


@app.get("/api/users")
# GET: http://0.0.0.0:8000/api/users?id=1
def get_users_id(id: int, db: Session = Depends(get_db)):
    users_id = db.query(User).filter_by(id=id).first()
    if users_id is None:
        raise HTTPException(status_code=404, detail="There is no user with this id")
    return users_id


@app.delete("/api/users")
# DELETE: http://0.0.0.0:8000/api/users?id=1
def delete_users_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="There is no user with this id")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


@app.put("/api/users")
# PUT: http://0.0.0.0:8000/api/users?id=2
# json = {
#     "name": "Новое имя пользователя",
#     "surname": "Новая фамилия пользователя",
#     "patronymic": "Новое отчество пользователя",
#     "age": 25,
#     "gender": "Мужской",
#     "nationality": "RU"
# }
def update_users_id(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="There is no user with this id")
    for field, value in user_update.dict().items():
        setattr(user, field, value)
    db.commit()
    return {"message": "User updated successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
