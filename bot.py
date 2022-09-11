from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import config
import telebot

from hh_parsing import parse_data
from handle_data import handel_vacancies

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def strat_bot(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = KeyboardButton("Проверить")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Бот готов к поиску вакансий', reply_markup=markup)


@bot.message_handler(regexp='Проверить')
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)
    for text in data[:5]:
        bot.send_message(message.chat.id, text)


@bot.message_handler()
def another_answer(message):
    bot.send_message(message.chat.id, 'Не понимаю.. Нажмите кнопку Проверить!')


if __name__ == '__main__':
     bot.infinity_polling()