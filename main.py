import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
print(TOKEN)

dp = Dispatcher()

message_text = ("👋 Здравствуй! \n\n"

                "📆 С 12 июля по 4 августа 2024 года мы проводим конкурс. Победители получат возможность тестового "
                "проживания в нашем доме на территории выставки Open Village24.\n\n"

                "🏡 Для участия в конкурсе достаточно подписаться на официальный telegram-канал компании. Результаты "
                "будут опубликованы здесь.\n\n"

                "🌞 Прочувствуй загородную жизнь с DRHouse ")


def menu_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура главного меню"""
    rows = [
        [InlineKeyboardButton(text='Перейти в канал', url='https://t.me/drhousecosystem')],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(message_text, reply_markup=menu_keyboard())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
