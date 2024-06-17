apt update
apt upgrade
mkdir tgbot
cd tgbot
apt install openssl
apt install telnet
apt install net-tools
apt install python3
apt install python3-pip
python3 -m pip install cherrypy
apt install python3.12-venv
python3 -m venv venv
chown ubuntu:ubuntu *
chmod 777 *
source venv/bin/activate
pip install pytelegrambotapi
pip install ndg-httpsclient
pip install pyopenssl
pip install pyasn1
pip install ndg-httpsclient
pip install pyasn1
pip install pyopenssl
pip install telebot
deactivate







