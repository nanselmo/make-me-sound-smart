from flask import Flask
from flask import render_template
from flask import request
from translate import translate
import os

app = Flask(__name__)


@app.route('/')
def show_index():
    #return "Hello"
    return render_template('index.html', submitted = False)


@app.route('/', methods=['POST'])
def display_translation():
    original_text = request.form['text_to_translate']
    new_text = translate(original_text)
    return render_template('index.html', submitted = True, translated_text = new_text)
    
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)