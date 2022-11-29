import telebot
import random
from telebot import types

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    talk_to_me = types.InlineKeyboardButton(text='Поговори со мной', callback_data='talk_to_me')
    send_me_cat = types.InlineKeyboardButton(text='Отправь мне кошечку', callback_data='send_me_cat')
    kb.add(talk_to_me, send_me_cat)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nМеня зовут HelpBot, я буду твоим '
                                      f'персональным '
                                      f'помощником.\nЧем могу '
                                      f'тебе '
                                      'помочь?', reply_markup=kb)


def talk_to_me(callback):
    kb = types.InlineKeyboardMarkup(row_width=2)
    well = types.InlineKeyboardButton(text='Хорошо', callback_data='well')
    bad = types.InlineKeyboardButton(text='Плохо', callback_data='bad')
    kb.add(well, bad)
    bot.send_message(callback.message.chat.id, 'Рад, что ты тут чтобы пообщаться!\nКак твои дела?', reply_markup=kb)

    @bot.callback_query_handler(func=lambda callback_howareyou: callback_howareyou.data == 'well' or callback_howareyou.data
                                                                == 'bad')
    def howareyou(callback_howareyou):
        if callback_howareyou.data == 'well':
            cat_photo = open(f'cat_photos/cat{random.randint(0, 4)}.jpg', 'rb')
            bot.send_photo(callback_howareyou.message.chat.id, cat_photo, 'Ну тогда держи кошечку')
        elif callback_howareyou.data == 'bad':
            cat_photo = open(f'cat_photos/cat{random.randint(0, 4)}.jpg', 'rb')
            bot.send_photo(callback_howareyou.message.chat.id, cat_photo, 'Ну тогда держи кошечку')


@bot.callback_query_handler(func=lambda callback: callback.data == 'talk_to_me' or callback.data == 'send_me_cat')
def functions(callback):
    if callback.data == 'talk_to_me':
        talk_to_me(callback)
    elif callback.data == 'send_me_cat':
        cat_photo = open(f'cat_photos/cat{random.randint(0,4)}.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, cat_photo, 'Ну тогда держи кошечку')


bot.polling()