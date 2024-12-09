from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os
import crud_functions

api = '7677773567:AAGXrlyrLZVkNjJ8V4vjQmnjwGHvbso8_hM'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Рассчитать'))
keyboard.add(KeyboardButton('Информация'))
keyboard.add(KeyboardButton('Купить'))

inline_keyboard = InlineKeyboardMarkup()
inline_keyboard.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
inline_keyboard.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))

buying_inline_keyboard = InlineKeyboardMarkup()
for i in range(1, 5):
    buying_inline_keyboard.add(InlineKeyboardButton(f'Product{i}', callback_data='product_buying'))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я помогу вам рассчитать норму калорий. Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    await message.reply("Этот бот помогает рассчитать норму калорий и покупать продукты.")

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.reply("Формула Миффлина-Сан Жеора:\nBMR = 10 * вес + 6.25 * рост - 5 * возраст + 5")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.reply("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories} ккал.", reply_markup=keyboard)
    await state.finish()

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = crud_functions.get_all_products()
    for product in products:
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        photo_path = f'product{product[0]}.jpeg'
        if os.path.exists(photo_path):
            await bot.send_photo(chat_id=message.chat.id, photo=open(photo_path, 'rb'))
        else:
            await message.answer(f"Изображение для {product[1]} не найдено.")
    await message.answer("Выберите продукт для покупки:", reply_markup=buying_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.reply("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_messages(message: types.Message):
    print('Введите команду /start чтобы начать общение')
    await message.answer('Введите команду /start чтобы начать общение')

if __name__ == '__main__':

    crud_functions.initiate_db()

    crud_functions.populate_products()

    executor.start_polling(dp, skip_updates=True)

    crud_functions.close_connection()