from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callbackdata import InlineInfo
from aiogram.fsm.context import FSMContext
from core.utils.statesform import TextSteps

# async def select_macbook(call: CallbackQuery, bot: Bot):
#     call_type, call_but, num = call.data.split('_')
#     answer = f'{call.message.from_user.first_name}, ты выбрал {call_type} и {call_but} и {num}'
    
#     await call.message.answer(answer)
#     await call.answer()

# async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
#     call_type, call_but, num = callback_data.call_type, callback_data.call_but, callback_data.num
#     answer = f'{call.message.from_user.first_name}, ты выбрал {call_type} и {call_but} и {num}'
    
#     await call.message.answer(answer)
#     await call.answer()
    
async def select_text(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer("Введи свой запрос в свободной текстовой форме:")
    await state.set_state(TextSteps.GET_TEXT)
    await call.answer()
    
async def select_buttons(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer("Введи свой запрос в свободной текстовой форме:")
    await state.set_state(TextSteps.GET_TEXT)
    await call.answer()
    
    
