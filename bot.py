import telebot
import main
import config


bot = telebot.TeleBot(config.BOT_KEY)


# Пример обработки присланного текста
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
            "Привет, я могу прислать тебе google.com/doodles. Напиши /start")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    
    elif message.text == "/start":
        dict_doodles = main.get_new_doodles()
        for key, value in dict_doodles.items():
            #print(key, value)
            bot.send_photo(message.from_user.id, value, caption=key)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Ты прислала мне: "+message.text+"\n\nНапиши /help.")


bot.polling(none_stop=True, interval=0)