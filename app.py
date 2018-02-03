import pandas as pd
from flask import Flask,render_template

app = Flask(__name__)

black = ""
whites = []
sentence_make = True

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/on')
def generate_bc():
    _generate_blackcard()
    bc = get_bc()
    return render_template("home.html",blackcard2=bc)

def _generate_blackcard():
    if sentence_make:
        dfB = pd.read_excel('/home/OnlyAtN1ght/mysite/Black_Cards.xlsx', sheet_name='Sheet1')
        scardB = dfB.sample()
        black_card = scardB.iloc[0]['Content']
        set_black_card(black_card)
        global sentence_make
        sentence_make = False

def set_black_card(bc):
    global black
    black = bc

def get_bc():
    return black

@app.route("/card")
def see_black_card():
    bc = get_bc()
    return render_template("home.html",blackcard2=bc)

@app.route("/draw_white_card")
def draw_white_card():
    wc = generate_wc()
    return render_template("home.html",all_white_cards = wc,blackcard2=get_bc())

@app.route("/show_white_cards")
def show_white_cards():
    return render_template("home.html",blackcard2 = get_bc(),white_card_disp = get_wc())

def generate_wc():
    cardsW = []
    dfW = pd.read_excel('/home/OnlyAtN1ght/mysite/White Cards.xlsx', sheet_name='Sheet1')
    for i in range(0,10):
        scardW = dfW.sample(n=None, frac=None, replace=True, weights=None, random_state=None, axis=None)
        cardW = scardW.iloc[0]['Content']
        cardsW.append(cardW)
    return cardsW

def set_whites(wc):
    global whites
    whites = wc

def get_wc():
    if whites != []:
        return whites
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

@app.route("/choose_white_card/<string:card>")
def choose_white_card(card):
    global whites
    whites.append(card)
    return render_template("home.html",blackcard2 = get_bc(),white_card_disp = get_wc())

@app.route("/display_sentence")
def display_sentence():
    s = get_sentence()
    global sentence_make
    sentence_make = True
    return render_template("home.html",sentences = s)

def get_sentence():
    sentences = []
    for cardW in whites:
        if "___" in black:
            sentence = black.replace('___',cardW).replace('..','.').replace('.?','?').replace('!.','.').replace(". "," ")
        else:
            sentence = black + " "+ cardW
        sentences.append(sentence)
    return sentences

@app.route("/reset")
def reset():
    global sentence_make
    sentence_make = True
    global black
    black = ""
    global whites
    whites = []
    return render_template("home.html")