import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8377951897:AAH_tR3T8-BXUQ3ii8kerkTCr3OU30zcXb4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет 🤍\n"
        "Это CoupleQuest — пространство для вас двоих.\n\n"
        "Скоро здесь появятся квесты и примирение 💞"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
