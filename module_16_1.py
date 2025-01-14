from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
# Создаем объект API
app = FastAPI()

# Прописываем маршрут к главной странице
@app.get("/")
async def read_mainpage():
    return PlainTextResponse('"Главная страница"')

# Прописываем маршрут к странице администратора
@app.get("/user/admin")
async def read_adminpage():
    return PlainTextResponse('"Вы вошли как администратор"')

# Прописываем маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
async def read_user_info(username: str, age: str):
    return PlainTextResponse(f'\"Информация о пользователе. Имя: \'{username}\', Возраст: {age}\"')

# Прописываем маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def read_user_id(user_id: str):
    return PlainTextResponse(f'\"Вы вошли как пользователь № {user_id}\"')
