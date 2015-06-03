from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
#def translate():
	original_text = request.form['textbox']
	return render_template('results.html', text_to_translate=original_text)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))