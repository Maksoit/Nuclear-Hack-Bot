from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import json
from core.keyboards.inline import get_inline_check, get_inline_start
from core.utils.dbconnect import Request
from core.utils.statesform import TextSteps


async def get_inline(message: Message, bot: Bot):
    await message.answer('Hello, its inline buttons', reply_markup=get_inline_keyboard())

async def get_start(message: Message, bot: Bot, state: FSMContext):
    # await request.create_feedback(message.from_user.id)

    # await message.answer(f'Сообщение #{counter}')
    # await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, а ты знал, что <b>Это send_message</b> ")
    await message.answer("Привет!\nЯ - бот для хакатона Nuclear Hack. \nЯ создан, чтобы помогать людям узнавать загруженность станций" \
                         "\nЧтобы ввести запрос в свободной форме отправь команду \"\\text\"" \
                         "\nЧтобы воспользоваться кнопками для выбора станции отправь команду \"\\buttons\" ", reply_markup=get_inline_start() )
    # await message.reply(f"Это message.reply")
    # await bot.send_message(message.from_user.id,
     #                      f"Твой id: {message.from_user.id}", reply_markup=get_reply_keyboard())

async def get_text(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(text = message.text)
    # Здесь типо парсинг и выделение станции из запроса, но пока просто текст
    await message.answer(f"Выбранная станция {message.text} - Верно?", reply_markup=get_inline_check())
    await state.set_state(TextSteps.IS_CORRECT)
    



