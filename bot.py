#!venv/bin/python
import config
import telebot
import cherrypy
import time
import eventlet
import requests
import logging
from time import sleep
import telebot


 # Каждый раз получаем по 10 последних записей со стены
URL_VK = f'https://api.vk.com/method/wall.get?domain=team&count=10&filter=owner&access_token={config.vk_access_token}&v=5.131'
FILENAME_VK = 'last_known_id.txt'
BASE_POST_URL = 'https://vk.com/team?w=wall-22822305_'

BOT_TOKEN = config.token
CHANNEL_NAME = '@myTestChannelForMyChatBot'

bot = telebot.TeleBot(BOT_TOKEN)

SINGLE_RUN=''

def get_data():
    timeout = eventlet.Timeout(10)
    try:
        feed = requests.get(URL_VK)
        return feed.json()
    except eventlet.timeout.Timeout:
        logging.warning('Got Timeout while retrieving VK JSON data. Cancelling...')
        return None
    finally:
        timeout.cancel()


def send_new_posts(items, last_id):
    for item in items:
        if item['id'] <= last_id:
            break
        link = '{!s}{!s}'.format(BASE_POST_URL, item['id'])
        bot.send_message(CHANNEL_NAME, link)
        # Спим секунду, чтобы избежать разного рода ошибок и ограничений (на всякий случай!)
        time.sleep(1)
    return


def check_new_posts_vk():
    # Пишем текущее время начала
    logging.info('[VK] Started scanning for new posts')
    with open(FILENAME_VK, 'rt') as file:
        last_id = int(file.read())
        if last_id is None:
            logging.error('Could not read from storage. Skipped iteration.')
            return
        logging.info('Last ID (VK) = {!s}'.format(last_id))
    try:
        feed = get_data()
        # Если ранее случился таймаут, пропускаем итерацию. Если всё нормально - парсим посты.
        if feed is not None:
            print(type(feed))
            entries = feed['response']['items'][1:]
            print(type(feed))
            print(type(entries))
            try:
                # Если пост был закреплен, пропускаем его
                tmp = entries[0]['is_pinned']
                # И запускаем отправку сообщений
                send_new_posts(entries[1:], last_id)
            except KeyError:
                send_new_posts(entries, last_id)
            # Записываем новый last_id в файл.
            with open(FILENAME_VK, 'wt') as file:
                try:
                    tmp = entries[0]['is_pinned']
                    # Если первый пост - закрепленный, то сохраняем ID второго
                    file.write(str(entries[1]['id']))
                    logging.info('New last_id (VK) is {!s}'.format((entries[1]['id'])))
                except KeyError:
                    file.write(str(entries[0]['id']))
                    logging.info('New last_id (VK) is {!s}'.format((entries[0]['id'])))
    except Exception as ex:
        logging.error('Exception of type {!s} in check_new_post(): {!s}'.format(type(ex).__name__, str(ex)))
        pass
    logging.info('[VK] Finished scanning')
    return





if __name__ == '__main__':
    # Избавляемся от спама в логах от библиотеки requests
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    # Настраиваем наш логгер
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.INFO,
                        filename='bot_log.log', datefmt='%d.%m.%Y %H:%M:%S')
    if not SINGLE_RUN:
        while True:
            check_new_posts_vk()
            # Пауза в 4 минуты перед повторной проверкой
            logging.info('[App] Script went to sleep.')
            time.sleep(60 * 1)
    else:
        check_new_posts_vk()
    logging.info('[App] Script exited.\n')
###########################################################################
# Хэндлер на все текстовые сообщения
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)

###########################################################################

# class WebhookServer(object):
#     @cherrypy.expose
#     def index(self):
#         if 'content-length' in cherrypy.request.headers and \
#                         'content-type' in cherrypy.request.headers and \
#                         cherrypy.request.headers['content-type'] == 'application/json':
#             length = int(cherrypy.request.headers['content-length'])
#             json_string = cherrypy.request.body.read(length).decode("utf-8")
#             update = telebot.types.Update.de_json(json_string)
#             # Эта функция обеспечивает проверку входящего сообщения
#             bot.process_new_updates([update])
#             return ''
#         else:
#             raise cherrypy.HTTPError(403)
#
# # Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
# bot.remove_webhook()
#
# # Ставим заново вебхук
# bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
#                 certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
#
# # Указываем настройки сервера CherryPy
# cherrypy.config.update({
#     'server.socket_host': config.WEBHOOK_LISTEN,
#     'server.socket_port': config.WEBHOOK_PORT,
#     'server.ssl_module': 'builtin',
#     'server.ssl_certificate': config.WEBHOOK_SSL_CERT,
#     'server.ssl_private_key': config.WEBHOOK_SSL_PRIV
# })
#
#  # Собственно, запуск!
# cherrypy.quickstart(WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})
#
# #Теперь запустим бесконечный цикл получения новых записей со стороны Telegram:
if __name__ == '__main__':
     bot.infinity_polling()