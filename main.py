
import telebot
import random
from telebot import types
from datetime import datetime
from collections import deque
# 1 variant
TPRP = {1111, 1000, 1456, 1123}
PL = {2222, 2000, 2789, 2876, 2543}
KL = {3000, 3231, 3431, 3938, 3876, 3730, 3333, 3366, 3390}
COO = {4444, 4243, 4455, 4000, 4999}  # 20%
OVB = {5555, 5000, 5111}  # 20%
RZ = {6666, 6000}
VL = {7777, 7000}
PS = {8888, 8000}
# 2 variant
proizv = {3000, 3231, 3431, 3938, 3876, 3730, 3333, 3366, 3390}  # 90%
komers = {4444, 4243, 4455, 4000, 4999}  # 20%

otrabotka = {}

bot = telebot.TeleBot("API")

wait = deque()


@bot.message_handler(commands=['start', 'help'])
def perviy(message):
    keyboard_perviy = types.ReplyKeyboardMarkup(resize_keyboard=None)

    key_1_0 = types.KeyboardButton('ПОСАДА')
    key_1_1 = types.KeyboardButton('РОБОТА')
    key_1_2 = types.KeyboardButton('АУДИТ')
    key_1_3 = types.KeyboardButton('ЕКЗАМЕН')
    key_1_4 = types.KeyboardButton('S O S')
    key_1_5 = types.KeyboardButton('ІНСТРУКЦІЯ')

    keyboard_perviy.add(key_1_1, key_1_2, key_1_3,)
    keyboard_perviy.add(key_1_0, key_1_5, key_1_4)


    bot.send_message(message.chat.id, 'Оберіть категорію', reply_markup=keyboard_perviy)


@bot.message_handler(content_types=['text'])
def vtoroy(message):
    #добавление в файл вводимого текста
    # txt = message.text
    # patch = '/Users/aleksandr/PycharmProjects/Project6/audit.txt'
    # v = open(patch, 'w')
    # v.write(txt)
    # v.close()
    # print(txt)
    # bot.send_message(message.chat.id, 'Введіть номер авто який перевіряєте')
    # конец добавление в файл вводимого текста


    if message.text == "АУДИТ":
        keyboard_vtoroy = types.ReplyKeyboardMarkup(resize_keyboard=None)

        key_2_0 = types.KeyboardButton('ПОВІЛЬНІ - 90%')
        key_2_1 = types.KeyboardButton('ШВИДКІ - 20%')

        keyboard_vtoroy.add(key_2_0)
        keyboard_vtoroy.add(key_2_1)

        bot.send_message(message.chat.id, 'кого хочеш перевірити?', reply_markup=keyboard_vtoroy)

    elif message.text == "ПОВІЛЬНІ - 90%":
        keyboard_vt = types.ReplyKeyboardRemove(True)
        # bot.send_message(message.chat.id, 'Введіть табельний номер Керівника робіт', reply_markup=keyboard_vt)
        bot.send_message(message.chat.id, "--".join(map(str, proizv)))
        bot.send_message(message.chat.id, 'Введіть номер авто який перевіряєте')

    elif message.text == "ШВИДКІ - 20%":
        keyboard_vt = types.ReplyKeyboardRemove(True)
        # bot.send_message(message.chat.id, 'Введіть табельний номер Керівника робіт', reply_markup=keyboard_vt)
        bot.send_message(message.chat.id, "--".join(map(str, komers)))
        bot.send_message(message.chat.id, 'Введіть номер авто який перевіряєте')



        # bot.send_message(message.chat.id, "--".join(map(str, proizv)))
        # goblin.discard(1243)
        # goblin.add(6666)
        # bot.send_message(message.chat.id, goblin)





bot.polling()



t(mydb)