import telebot
import os
from telebot import types
from telebot.apihelper import close, stop_poll

bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник по фильтрации и организации информации", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔧 Информация о функциях бота')
        btn2 = types.KeyboardButton('❓ Кем создан бот?')
        btn3 = types.KeyboardButton('📄 Сократить информацию')
        btn4 = types.KeyboardButton('🔬 Сайты для проверки информации')
        btn5 = types.KeyboardButton('🔄 Перезагрузить бота')
        btn6 = types.KeyboardButton('🚫 Выключить бота')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '👀 Что тебя интересует?', reply_markup=markup)

    elif message.text == '🔧 Информация о функциях бота':
        bot.send_message(message.from_user.id,'Данный бот способен дать  ссылки на сайты проверки информации 🔬 \n А также дать ссылку на сайт сокращающий текстовую информацию 📄 ', parse_mode='Markdown')

    elif message.text == '❓ Кем создан бот?':
        bot.send_message(message.from_user.id, 'Данный чат-бот создан студентом группы Б9123-09.03.04, Дмитриенко Макаром Сергеевичем', parse_mode='Markdown')

    elif message.text == '📄 Сократить информацию':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сайт', url='https://robotext.io/reduction')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Данный сайт способен сократить любую текстовую информацию:", reply_markup=markup)

    elif message.text == '🔬 Сайты для проверки информации':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Проверить мировую статистику', url='https://world-statistics.org/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌍 Сайт для проверки мировой статистики:", reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton(text='Проверить медицинские данные', url='https://minzdrav.gov.ru/documents')
        markup.add(btn2)
        bot.send_message(message.from_user.id, "💊 Сайт для проверки медицинских данных", reply_markup=markup)

    elif message.text == '🔄 Перезагрузить бота':
        bot.send_message(message.from_user.id, "🔄 Нажмите для перезагрузки бота: /start", parse_mode='Markdown')

    elif message.text == '🚫 Выключить бота':
        bot.send_message(message.from_user.id, '😥 Прощай',parse_mode='Markdown')
        bot.polling(none_stop=False, interval=0)

bot.polling(none_stop=False, interval=0)
