import random, requests, os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    # random
    feel = ['기쁨','슬픔','분노','증오','즐거움','공포','사랑','혐오','욕망']
    feeling = random.choice(feel)

    return render_template('pong.html', name_in_html=name, feeling_in_html=feeling)

@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()

    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    bonus = lotto['bnusNo']


    return render_template('lotto.html', w=winner, b=bonus, n=num)

@app.route('/write')
def write():

    return render_template('write.html')

@app.route('/send')
def send():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chatId = os.getenv('CHAT_ID')

    text = request.args['message']

    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={text}')
    return render_template('send.html')