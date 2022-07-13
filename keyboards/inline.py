from aiogram import Bot, Dispatcher
from aiogram.types import \
    InlineKeyboardButton, InlineKeyboardMarkup

import config as cfg

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

hope = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Оценить", callback_data='Catalog'))

ho = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text="Скрудж", callback_data="а"),
    InlineKeyboardButton(text="Лолз", callback_data="б"),
    InlineKeyboardButton(text="BLB market", callback_data="в"),
    InlineKeyboardButton(text="ACC", callback_data="г"),
    InlineKeyboardButton(text="Авито/Юла", callback_data="д"),
    InlineKeyboardButton(text="Другое", callback_data="е"))

book = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text="Отлично", callback_data="ames"),
    InlineKeyboardButton(text="Хорошо", callback_data="ilms"),
    InlineKeyboardButton(text="Нормально", callback_data="TP"),
    InlineKeyboardButton(text="Плохо", callback_data="P"),
    InlineKeyboardButton(text="Ужасно", callback_data="UJ")
)

btnBitcoin = InlineKeyboardButton(text="Bitcoin", callback_data="cc_bitcoin")
btnEthereum = InlineKeyboardButton(text="Ethereum", callback_data="cc_ethereum")
btnLitecoin = InlineKeyboardButton(text="Liteecoin", callback_data="cc_litecoin")


crupto_list = InlineKeyboardMarkup(row_width=3)
crupto_list.insert(btnBitcoin)
crupto_list.insert(btnEthereum)
crupto_list.insert(btnLitecoin)
