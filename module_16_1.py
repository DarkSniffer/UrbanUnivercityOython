from fastapi import FastAPI

# Создаем объект API
app = FastAPI()

# Прописываем маршрут к главной странице
@app.get("/")
async def read_mainpage()-> dict:
    return {"message": "Главная страница"}

# Прописываем маршрут к странице администратора
@app.get("/user/admin")
async def read_adminpage()-> dict:
    return {"message": "Вы вошли как администратор"}

# Прописываем маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
async def read_user_info(username: str, age: int)-> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# Прописываем маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def read_user_id(user_id: int)-> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}