from aiogram import Bot, types, Dispatcher
from keyboards import inline
import config as cfg
from parser import pars
from aiogram.types import CallbackQuery
from aiogram.types import \
    InlineKeyboardMarkup

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    await message.answer("🖐")
    await message.answer("Привет, {}!".format(message.from_user.first_name))
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=inline.ho,
        text="🌀 Откуда вы к нам?")


@dp.message_handler(commands='payment')
async def payment(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text="Оплатить", url="qiwi.com/n/DEVELOPERTG")
    markup.add(button)
    await bot.send_message(message.chat.id, text="Перейти к оплате:", reply_markup=markup)


@dp.message_handler(commands='course')
async def course(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['💵 USD', '💶 EUR']
    keyboard.add(*buttons)
    await message.answer("Что вас интересует?", reply_markup=keyboard)


@dp.message_handler(commands=['menu'])
async def menu_message(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📢 Почему мы?", "⚙ Помощь", "❇ Заказать бота", "❌ Ничего не делать"]
    keyboard.add(*buttons)
    await message.answer("Выберите,что вас интересует:", reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    if message.text == '/help':
        await bot.send_message(message.from_user.id,
                               '📲 Если появились какие то проблемы обратитесь к нашему '
                               'администратору:\nhttps://t.me/voplopoll')

    elif message.text == '/zakaz':
        await bot.send_message(message.from_user.id,
                               '📌 Опишите как вы видите своего бота, какие функции вам '
                               'нужны, и все о вашем боте, все максимально подробно.\n\n\nПосле того,как все '
                               'напишите жмите на меня:\n/next')

    elif message.text == '📢 Почему мы?':
        await bot.send_message(message.from_user.id, '📈 Разработка ботов Telegram любой сложности\n\n— Адекватные,'
                                                     'договорные цены, которые начинаются от 10$\n— Короткие сроки '
                                                     'сдачи работы\n— Боты разной сложности и функций \n—Отвечаю '
                                                     '24/7\n\n\n✅Спокойной реагируем на неопределенность клиентов,'
                                                     'обсудим,как удобнее воплотить желаемое!')
    elif message.text == '❇ Заказать бота':
        await bot.send_message(message.from_user.id,
                               '📌 Опишите как вы видите своего бота, какие функции вам '
                               'нужны, и все о вашем боте, все максимально подробно.\n\n\nПосле того,как все '
                               'напишите жмите на меня:\n/next')

    elif message.text == '⚙ Помощь':
        await bot.send_message(message.from_user.id,
                               '📲 Если появились какие то проблемы обратитесь к нашему '
                               'администратору:\nhttps://t.me/voplopoll')
    elif message.text == '/next':
        await bot.send_message(message.from_user.id, '💰 Укажите ваш примерный или точный бюджет на '
                                                     'разработку.\n\n\nПосле того,как все напишите жмите на '
                                                     'меня:\n/again_next')
    elif message.text == '/again_next':
        await bot.send_message(message.from_user.id, '⏳ И наконец,укажите желаемый срок выполнения '
                                                     'работы.\n\n\nПосле того,как все '
                                                     'напишите жмите на меня:\n/end')
    elif message.text == '/end':
        await bot.send_message(message.from_user.id, '✅ Поздравляем,ваша заявка на заказ успешно '
                                                     'отправлена.\nСкоро с вами свяжутся наши '
                                                     'разработчики.\n\n\nЕсли вас интересует что то еще откройте '
                                                     'меню или введите "/" в строке сообщений', reply_markup=inline.hope)
    elif message.text == '💵 USD':
        await bot.send_message(message.from_user.id, f'💵 Курс доллара: {pars.dollar()} рублей')
    elif message.text == '💶 EUR':
        await bot.send_message(message.from_user.id, f'💶 Курс евро: {pars.euro()} рублей')
    elif message.text == '/binance':
        await bot.send_message(message.from_user.id, '@cryptocurrency_telegrambot')
    elif message.text == '❌ Ничего не делать':
        await bot.send_message(message.from_user.id, 'Хорошо')



@dp.callback_query_handler(text='а')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           'Гости из Скруджа:\n\n✅Добро пожаловать, {}!\n\nНажми,чтобы открыть меню:\n/menu\n\nНажми,'
                           'чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.callback_query_handler(text='б')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           'Гости из LolzTeam:\n\n✅Добро пожаловать, {}!\n\nНажми,чтобы открыть '
                           'меню:\n/menu\n\nНажми,чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.callback_query_handler(text='в')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           'Гости из BLB market:\n\n✅Добро пожаловать, {}!\n\nНажми,чтобы открыть '
                           'меню:\n/menu\n\nНажми,чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.callback_query_handler(text='г')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           'Гости из ACC:\n\n✅Добро пожаловать, {}!\n\nНажми,чтобы открыть меню:\n/menu\n\nНажми,'
                           'чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.callback_query_handler(text='д')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           'Гости из Авито/Юла:\n\n✅Добро пожаловать, {}!\n\nНажми,чтобы открыть '
                           'меню:\n/menu\n\nНажми,чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.callback_query_handler(text='е')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')
    await bot.send_message(query.from_user.id,
                           '✅Добро пожаловать, {}!\n\nНажми,чтобы открыть меню:\n/menu\n\nНажми,чтобы сразу перейти к '
                           'заказу:\n/zakaz'.format(
                               query.from_user.first_name))


@dp.message_handler(commands='end')
async def command_end(message: types.Message):
    types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    await message.answer('✅ Поздравляем,ваша заявка на заказ успешно отправлена.\nСкоро с вами свяжутся наши '
                         'разработчики.\n\n\nЕсли вас интересует что то еще откройте меню или введите "/" в строке '
                         'сообщений.', reply_markup=inline.hope)
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=inline.hope,
        text='📊 Оцените пожалуйста работу бота,нам очень важно ваше мнение:')


@dp.callback_query_handler(text="Catalog")
async def Catalog_callback(query: CallbackQuery):
    await query.message.edit_text('📊 Оцените пожалуйста работу бота,нам очень важно ваше мнение:',
                                  reply_markup=inline.book)


@dp.callback_query_handler(text="ames")
async def Games_callback(query: CallbackQuery):
    await query.message.edit_text('🥳 Благодарим за отзыв нам очень приятно.')


@dp.callback_query_handler(text="ilms")
async def Films_callback(query: CallbackQuery):
    await query.message.edit_text('🎉 Благодарим за отзыв,будем стараться подтягивать все на отлично')


@dp.callback_query_handler(text="TP")
async def TP_callback(query: CallbackQuery):
    await query.message.edit_text('😬 Благодарим за отзыв,будем стараться подтягивать все на отлично')


@dp.callback_query_handler(text="P")
async def P_callback(query: CallbackQuery):
    await query.message.edit_text('😔 Благодарим за отзыв,будем стараться подтягивать все на отлично')


@dp.callback_query_handler(text="UJ")
async def UJ_callback(query: CallbackQuery):
    await query.message.edit_text('😖 Благодарим за отзыв,будем стараться подтягивать все на отлично')


@dp.message_handler(commands='payment')
async def payment(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text="Оплатить", url="qiwi.com/n/DEVELOPERTG")
    markup.add(button)
    await bot.send_message(message.chat.id, text="Перейти к оплате:", reply_markup=markup)

