from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import CommandStart


from config_data.config import Config, load_config

import logging

router = Router()
config: Config = load_config()


@router.message(CommandStart)
async def process_start_command(message: Message) -> None:
    """
    Запуск бота - нажата кнопка "Начать" или введена команда "/start"
    :param message:
    :return:
    """
    logging.info(f"process_start_command {message.chat.id}")
    video_id = 'BAACAgIAAxkBAAMEZsHDhms8en9MPKng-gjXL2G2VoMAAi5TAAIwGwhKE-DOmZ5VVnI1BA'
    url = 'https://zref.io/112887'
    ikb_donate = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[[InlineKeyboardButton(
                                          text='Играть 💰',
                                          web_app=WebAppInfo(url=url))]])

    await message.answer_video(video=video_id,
                               caption='🎰 Лучшая игровая платформа в Telegram\n'
                                       '⏰ Моментальные выводы на карту и крипту\n'
                                       '🎁 Жирные бонусы для всех',
                               reply_markup=ikb_donate)