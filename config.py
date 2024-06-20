# guide on
# https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token
token = '7112067289:AAEzbln8X3a9_fTUX-rM457kw_ksYCdSRzo'
WEBHOOK_HOST = 'ec2-184-72-163-59.compute-1.amazonaws.com'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = 'ec2-184-72-163-59.compute-1.amazonaws.com'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = '/home/ubuntu/tgbot/webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = '/home/ubuntu/tgbot/webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (token)
vk_access_token="vk1.a.hLQj3SlAyy5HReWm-TBmcYmr4m0iQNDuhxWDZ-it2gw5e9zVCyYe7bpE5I02y5nYzo36nGx8MNTH8fwukgaIIFALt6QOQb51ybqFRsnED7e0_rKwAQa2C66zUJT1UG6MpQGfJYOIBRZlWClIrS7T4LJNGYIO4tjo2M2yVp0mCu_vKhNlteOtR5Im25619LVgpWX_T6ANvgRhofDp_I-rzg"