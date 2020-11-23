from flask import Flask, render_template, request, jsonify

from grandpy.bot.parser import Parser
from grandpy.bot.wiki_api import WikiAPI

app = Flask(__name__)

parser = Parser()
wiki = WikiAPI()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process():
	if request.method == 'POST':
		message = request.form['message']
		print('[VIEWS] user input : ' + message)
		parsed_message = parser.get_keywords(message)
		print('[VIEWS] parsed input : ' + str(parsed_message))
		reply = wiki.get_search_result(' '.join(parsed_message))
		print('[VIEWS] Title page : ' + wiki.page.title)
		coord = wiki.get_coordinates()
		print('[VIEWS] Coordinates : ' + str(coord))


	return jsonify(result=reply)


if __name__ == "__main__":
    app.run()