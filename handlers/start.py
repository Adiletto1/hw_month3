from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О манге',
                                           callback_data='about_us'),
                types.InlineKeyboardButton(text='Об авторе',
                                           callback_data='об авторе')
            ],
            [
                types.InlineKeyboardButton(text='О боях',
                                           callback_data='о боях')
            ]
        ]
    )
    await message.answer(text='Привет', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer(
        'История начинается c собрания богов, на котором решается судьба человечества: жизнь или смерть. Согласившись с никчёмностью рода людского, боги выбирают второе... Но одна валькирия выдвигает предложение: позволить богам и людям сразиться в битве, которая станет последним лучом надежды для человечества. 13 богов сразятся против 13 людских чемпионов в битвах один на один, чтобы решить, будет ли человечество жить или сгинет в могуществе божественной силы.')


@start_router.callback_query(F.data == 'об авторе')
async def avtor(callb: types.CallbackQuery):
    await callb.message.answer('Имя автора: Shinya Umemura')


@start_router.callback_query(F.data == 'о боях')
async def fight_list(call: types.CallbackQuery):
    sb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Первый бой'),
                types.KeyboardButton(text='Второй бой')
            ],
            [
                types.KeyboardButton(text='Третий бой'),
                types.KeyboardButton(text='Четвёртый бой')
            ]
        ], resize_keyboard=True

    )
    await call.message.answer('Выберите бой:', reply_markup=sb)


@start_router.message(F.text == 'Первый бой')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    await message.answer('Рёфу Хойсен против Тора\nВремя боя:16 мин, 28сек\nРешающий удар: Гейррёд Молота Тора\nПобедитель: Тор')


@start_router.message(F.text == 'Второй бой')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    await message.answer('Зевс против Адама\nВремя боя:7мин, 13сек\nРешающий удар: Прямой удар\nПобедитель: Зевс')


@start_router.message(F.text == 'Третий бой')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    await message.answer('Посейдон против Сасаки Коджиро\nВремя боя:13мин, 7сек\nРешающий удар: Комбо ласточки и тигра тысячи мечей\nПобедитель: Сасаки Коджиро')


@start_router.message(F.text == 'Четвёртый бой')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    await message.answer('Геракл против Джека-Потрошителя\nВремя боя:26мин, 18сек\nРешающий удар: "Dear god" ("Боже милостливый")\nПобедитель: Джек-Потрошитель')





