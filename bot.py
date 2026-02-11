impoimport asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8377951897:AAH_tR3T8-BXUQ3ii8kerkTCr3OU30zcXb4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("💑 Создать пару"), KeyboardButton("🔑 Подключиться")],
            [KeyboardButton("💖 Квест на сегодня")],
            [KeyboardButton("🕊 Мы поссорились")]
        ],
        resize_keyboard=True
    )

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет 🤍\n"
        "Это CoupleQuest.\n\n"
        "Мы начнём с простого и будем двигаться шаг за шагом.",
        reply_markup=main_menu()
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer(
        f"Ты нажал(а): {message.text}\n\n"
        "Пока это заглушка — скоро тут появится логика 💫",
        reply_markup=main_menu()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
