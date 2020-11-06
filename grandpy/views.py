from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# @app.route('/process', methods=['GET'])
# def process():
#     text = request.form['txt']
#     print(text)
#     return text


if __name__ == "__main__":
    app.run()