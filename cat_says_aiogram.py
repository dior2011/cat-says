import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram import types
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ContentType, File, Message
from aiogram.types import FSInputFile
from cat_says import cat_say

TOKEN = "6796185877:AAE7DFikiOA-RW2YvKTnExVHuYqcMVPEAwc"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(text="Assalomu alaykum! Tekst yozing va bu bot uni huddi mushuk gapirgandek qilib!")

@dp.message(F.text)
async def rasm_yuborish(message: Message):
    cat_say(message.text)
    file = FSInputFile(f"cat_is_says_{message.text}.jpg")
    await message.answer_photo(photo=file)



    
    
async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

