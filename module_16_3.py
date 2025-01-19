from fastapi import FastAPI, Path
from typing import Annotated

# Создаем объект FastAPI
app = FastAPI()

# Инициализируем словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# Создаем GET запрос по маршруту '/users'
@app.get("/users")
def get_users():
    return users

# Создаем POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(min_length=1, description="Enter username")],
    age: Annotated[int, Path(ge=1, description="Enter age")]
):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# Создаем PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[str, Path(description="Enter user ID")],
    username: Annotated[str, Path(min_length=1, description="Enter username")],
    age: Annotated[int, Path(ge=1, description="Enter age")]
):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return f"User {user_id} not found"

# Создаем DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[str, Path(description="Enter user ID")]
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found"