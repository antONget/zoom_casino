from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import CommandStart


from config_data.config import Config, load_config

import logging

router = Router()
config: Config = load_config()


@router.message()
async def process_start_command(message: Message) -> None:
    """
    Запуск бота - нажата кнопка "Начать" или введена команда "/start"
    :param message:
    :return:
    """
    logging.info(f"process_start_command {message}")
    url = 'https://zref.io/112887'
    ikb_donate = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[[InlineKeyboardButton(
                                          text='Играть 💰',
                                          web_app=WebAppInfo(url=url))]])
    await message.answer_photo(photo='AgACAgIAAxkBAANoZsIZB_dM3ydZvP9QfloSmVEu56MAAoPeMRswGxBKPGO-fHV3P3EBAAMCAAN5AAM1BA',
                               caption='🎰 Лучшая игровая платформа в Telegram\n'
                                       '⏰ Моментальные выводы на карту и крипту\n'
                                       '🎁 Жирные бонусы для всех',
                               reply_markup=ikb_donate)
