from tkinter import N
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, keyboard_button
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo, InlineInfo


# select_macbook = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text='Текст для инлайн кнопки!', callback_data='inline_callback_1')
#         ],
#     [
#         InlineKeyboardButton(text='Inline Button 2', callback_data='inline_callback_2')
#         ],
#     [
#         InlineKeyboardButton(text='Inline Button 3', callback_data='inline_callback_3')
#         ],
#         [
#         InlineKeyboardButton(text='Link', url="https://www.youtube.com/watch?v=XJCYxIbsXmk&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=6")
#     ],
#     [
#         InlineKeyboardButton(text='Profile', url ="tg://user?id=1081261451")
#     ]
#     ])


# def get_inline_keyboard():
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.button(text='Builder button 1', callback_data=MacInfo(call_type='inline', call_but='builder', num=1))
#     keyboard_builder.button(text='Builder button 2', callback_data=MacInfo(call_type='inline', call_but='builder', num=2))
#     keyboard_builder.button(text='Builder button 3', callback_data=MacInfo(call_type='inline', call_but='builder', num=3))
#     keyboard_builder.button(text='Link', url = "https://www.youtube.com/watch?v=XJCYxIbsXmk&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=6")
#     keyboard_builder.button(text='Link', url = "tg://user?id=1081261451")
    
#     keyboard_builder.adjust(3, 2)
#     return keyboard_builder.as_markup()

def get_inline_start():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Ввести запрос в свободной форме', callback_data=InlineInfo(type='loss', IsLocated=False, IsContact=False, animal='') )
    keyboard_builder.button(text='Воспользоваться кнопками для выбора станции', callback_data=InlineInfo(type='find', IsLocated=False, IsContact=False, animal=''))
    
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()

def get_inline_animal():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Кот', callback_data=InlineInfo(type='', IsLocated=False, IsContact=False, animal='cat'))
    keyboard_builder.button(text='Собака', callback_data=InlineInfo(type='', IsLocated=False, IsContact=False, animal='dog'))
    
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

def get_inline_geo_contact():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Отправить геолокацию', callback_data=InlineInfo(IsLocated=True, IsContact=False, type='', animal=''), request_location = True)
    keyboard_builder.button(text='Отправить свой контакт', callback_data=InlineInfo(IsLocated=False, IsContact=True, type='', animal=''), request_contact = True)
    
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()