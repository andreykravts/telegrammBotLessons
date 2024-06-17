pip freeze > /home/ubuntu/tgbot/requirements.txt

python3 -m venv /home/ubuntu/tgbot/venv
source /home/ubuntu/tgbot/venv/bin/activate
pip install -r /home/ubuntu/tgbot/requirements.txt
