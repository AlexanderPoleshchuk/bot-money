import telebot
from transfer import *


TOKEN = '1041180949:AAGytEak0z9ljL4yZQDehaIGijec1p0UFy0'
bot = telebot.TeleBot(TOKEN)


eur = ['eur', 'euro', 'евро', 'угко', 'угк']
usd = ['usd', '$', 'гыв', 'баксы', 'доллары','зеленые','баксов','долларов','ye','зеленых']
byn = ['byn', 'инт', 'белок', ',бел', 'рублей']
rub = ['rub', 'кги', 'россии','рублей']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!\nЯ конвертирую белорусские рубли в доллары США, евро, российские рубли '
                                      'и обратно по актуальному курсу НБРБ.\n\n— Белорусские рубли в другие валюты: '
                                      '100 '
                                      'BYN(byn)\n— Доллары США: 120 USD(usd)\n— Евро: 90 EUR(eur)\n— Российские '
                                      'рубли: 240 RUB(rub) ')


@bot.message_handler(content_types=['text'])
def send_text(message):
    MONEY = message.text.split(' ')[0]
    if len(message.text.split(' ')) == 2:
        if message.text.split(' ')[1].lower() in eur:
            bot.send_message(message.chat.id, f'{transfer_eur(MONEY)}')
        elif message.text.split(' ')[1].lower() in usd:
            bot.send_message(message.chat.id, f'{transfer_usd(MONEY)}')
        elif message.text.split(' ')[1].lower() in rub:
            bot.send_message(message.chat.id, f'{transfer_rub(MONEY)}')
        elif message.text.split(' ')[1].lower() in byn:
            bot.send_message(message.chat.id, f'{transfer_byn(MONEY)}')
        else:
            bot.send_message(message.chat.id, f'{show_course()}')
    else:
        bot.send_message(message.chat.id, f'{show_course()}')

bot.polling()
