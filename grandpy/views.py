from flask import Flask, render_template, request, jsonify

from grandpy.bot.parser import Parser
from grandpy.bot.wiki_api import WikiAPI
from grandpy.bot.gmaps_api import GmapsAPI

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

parser = Parser()
wiki = WikiAPI()
gmaps = GmapsAPI(app.config['GMAPS_APP_ID'])


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
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
        print(gmaps.get_informations(' '.join(parsed_message)))

    return jsonify(result=reply)


if __name__ == "__main__":
    app.run()
