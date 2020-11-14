from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process():
	if request.method == 'POST':
	    message = request.form['message']
	    print(message)
	    reply = "Salut mon grand. Alors comme ça tu dis : " + message
	    return jsonify(result=reply)


if __name__ == "__main__":
    app.run()