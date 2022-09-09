import config
import telebot

from hh_parsing import parse_data
from handle_data import handel_vacancies

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['check'])
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)
    for text in data[:5]:
        bot.send_message(message.chat.id, text)


if __name__ == '__main__':
     bot.infinity_polling()