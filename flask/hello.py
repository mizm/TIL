from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/python")
def python():
    return 'funny'

@app.route("/dictionary/<string:word>")
def dictionary(word):
    my_dict = {'apple' : '사과'}
    if my_dict.get(word) :
        return f'{word}은(는) {my_dict[word]}!'
    else :
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다'