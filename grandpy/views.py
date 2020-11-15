from flask import Flask, render_template, request, jsonify

from grandpy.bot.parser import Parser

app = Flask(__name__)

parser = Parser()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process():

	if request.method == 'POST':
		message = request.form['message']
		print(message)
		parsed_message = parser.get_keywords(message)
		print(parsed_message)
		reply = "Salut mon grand. Alors comme ça tu dis : " + ' '.join(parsed_message)

	return jsonify(result=reply)
	

if __name__ == "__main__":
    app.run()