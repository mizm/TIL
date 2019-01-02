import requests
import os

token = os.getenv('TELEGRAM_BOT_TOKEN')
chatId = os.getenv('CHAT_ID')

text = '반갑습니다'

requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={text}')