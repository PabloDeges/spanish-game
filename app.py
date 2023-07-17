from flask import Flask, url_for, render_template, request
import random

app = Flask(__name__)

current_vocab = None
result_message = None
score = 0;

###

spanish_words = [
    ('el', 'the'),
    ('ser', 'be'),
    ('y', 'and'),
    ('un', 'a'),
    ('en', 'in'),
    ('tener', 'have'),
    ('haber', 'have'),
    ('por', 'for'),
    ('con', 'with'),
    ('no', 'no'),
    ('poder', 'can'),
    ('decir', 'say'),
    ('dar', 'give'),
    ('ir', 'go'),
    ('saber', 'know'),
    ('ver', 'see'),
    ('querer', 'want'),
    ('llegar', 'arrive'),
    ('pasar', 'pass'),
    ('llamar', 'call'),
    ('pensar', 'think'),
    ('comer', 'eat'),
    ('sentir', 'feel'),
    ('vivir', 'live'),
    ('trabajar', 'work'),
    ('aprender', 'learn'),
    ('estudiar', 'study'),
    ('jugar', 'play'),
    ('amor', 'love'),
    ('casa', 'house'),
    ('amigo', 'friend'),
    ('vida', 'life'),
    ('familia', 'family'),
    ('tiempo', 'time'),
    ('mundo', 'world'),
    ('día', 'day'),
    ('noche', 'night'),
    ('hombre', 'man'),
    ('mujer', 'woman'),
    ('niño', 'child'),
    ('ciudad', 'city'),
    ('país', 'country'),
    ('trabajo', 'job'),
    ('escuela', 'school'),
    ('libro', 'book'),
    ('calle', 'street'),
    ('coche', 'car'),
    ('gato', 'cat'),
    ('perro', 'dog'),
    ('color', 'color'),
    ('sol', 'sun'),
    ('luna', 'moon'),
    ('agua', 'water'),
    ('fuego', 'fire'),
    ('aire', 'air'),
    ('planta', 'plant'),
    ('árbol', 'tree'),
    ('verde', 'green'),
    ('rojo', 'red'),
    ('azul', 'blue'),
    ('blanco', 'white'),
    ('negro', 'black'),
    ('grande', 'big'),
    ('pequeño', 'small'),
    ('nuevo', 'new'),
    ('viejo', 'old'),
    ('bueno', 'good'),
    ('malo', 'bad'),
    ('feliz', 'happy'),
    ('triste', 'sad'),
    ('difícil', 'difficult'),
    ('fácil', 'easy'),
    ('interesante', 'interesting'),
    ('abrir', 'open'),
    ('cerrar', 'close'),
    ('entrar', 'enter'),
    ('salir', 'exit'),
    ('comprar', 'buy'),
    ('vender', 'sell'),
    ('esperar', 'wait'),
    ('mirar', 'look'),
    ('escuchar', 'listen'),
    ('hablar', 'speak'),
    ('entender', 'understand'),
    ('escribir', 'write'),
    ('leer', 'read'),
    ('pintar', 'paint'),
    ('cantar', 'sing'),
    ('bailar', 'dance')
]

class Vocabulary:

    es = ""
    en = ""

    def __init__(self, spanish_word, english_translation):
        self.es = spanish_word
        self.en = english_translation

# create vocab objects and store them in word_list
word_list = []
for spanish_word, english_translation in spanish_words:
    vocabulary = Vocabulary(spanish_word, english_translation)
    word_list.append(vocabulary)

###

@app.route("/", methods=["GET", "POST"])
def play_game():
    global current_vocab, result_message, score

    if current_vocab is None:
        current_vocab = random.choice(word_list)
    

    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_translation = current_vocab.en

        if user_answer.strip().lower() == correct_translation.lower():
            result_message = '¡ muy bien ! (+5)'
            score += 5
        elif user_answer == "":
            pass
        else:
            result_message = 'Incorrect. The correct translation was : ' + " '" + correct_translation + "' " + "(-10)"
            if score - 10 > 0:
                score -= 10

        current_vocab = random.choice(word_list)

    return render_template('game.html', spanish_word=current_vocab.es, result_message=result_message, score=score)



if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)