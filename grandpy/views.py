import time

from flask import Flask, render_template, request, jsonify

from grandpy.bot.parser import Parser
from grandpy.bot.wiki_api import WikiAPI
from grandpy.bot.gmaps_api import GmapsAPI
from grandpy.bot.answers import get_answer


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


@app.route('/process', methods=['POST'])
def process():
    
    if request.method == 'POST':
        message = request.form['message']
        print("[VIEWS] message : " + message)
        parsed_message = ' '.join(parser.get_keywords(message))
        print("[VIEWS] parsed_message : " + parsed_message)
        wiki_result = wiki.get_search_result(parsed_message)
        gmaps_result = gmaps.get_coordinates(parsed_message)

        if wiki_result == 'error':
            first_message = get_answer('error')
            second_message = None
            coord = None
            url = None
            title = None
        else:
            coord = gmaps_result['coord']
            addr = gmaps_result['addr']
            first_message = get_answer('valid') + addr
            second_message = wiki_result['summary']
            url = wiki_result['url']
            title = wiki_result['title']
            print('[VIEWS] user input : ' + message)
            print('[VIEWS] parsed input : ' + parsed_message)
            print('[VIEWS] Wiki page : ' + url)
            print('[VIEWS] address : ' + addr)

    res = {
        "first_message": first_message,
        "second_message": second_message,
        "gmap_coord": coord,
        "url": url,
        "title": title
    }
    return jsonify(result=res)


if __name__ == "__main__":
    app.run()
