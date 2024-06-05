apt update
apt upgrade
mkdir mybot
cd mybot
apt install openssl
openssl genrsa -out webhook_pkey.pem 2048
openssl req -new -x509 -days 365 -key webhook_pkey.pem -out webhook_cert.pem
apt install telnet
apt install net-tools
apt install python3
apt install python3-pip
python3 -m pip install cherrypy
pip install ndg-httpsclient
pip install pyopenssl
pip install pyasn1
pip install ndg-httpsclient
pip install pyasn1
pip install pyopenssl
python3 -m venv venv
chown ubuntu:ubuntu *
chmod 777 *
source venv/bin/activate
pip install pytelegrambotapi
deactivate


