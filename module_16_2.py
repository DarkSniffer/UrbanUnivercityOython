from fastapi import FastAPI, Path
from typing import Annotated

# Создаем объект FastAPI
app = FastAPI()

# Прописываем маршрут к главной странице
@app.get("/")
async def read_mainpage():
    return {"message": "Главная страница"}

# Прописываем маршрут к странице администратора
@app.get("/user/admin")
async def read_adminpage():
    return {"message": "Вы вошли как администратор"}

# Прописываем маршрут к страницам пользователей с параметром в пути и валидацией
@app.get("/user/{user_id}")
async def read_user_id(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Прописываем маршрут к страницам пользователей с передачей данных в адресной строке и валидацией
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
