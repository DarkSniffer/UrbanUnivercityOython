from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start (message):
    print('Привет, я бот, помогающий твоему здоровью!')
    await message.answer('Привет, рад видеть Тебя в этом Боте! Я призван помочь Твоему здоровью!')

@dp.message_handler()
async def all_message (message):
    print('Введите команду /start чтобы начать общение')
    # await message.answer(message.text)
    await message.answer('Введите команду /start чтобы начать общение')
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
