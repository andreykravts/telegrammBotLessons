#!venv/bin/python
import config
import telebot

#link to token in config file
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)


#Теперь запустим бесконечный цикл получения новых записей со стороны Telegram:
if __name__ == '__main__':
     bot.infinity_polling()