import werkzeug
from Tools.scripts.serve import app
from flask import Flask, render_template, request, jsonify
import requests
from markupsafe import escape

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    return render_template('form.html')


@app.route('/get/<id>', methods=['GET', 'POST'])
def index(id):
    if request.method == 'GET':
        # Get the data from the form
        data = request.form
        # Make the API request
        response = requests.get('https://jsonplaceholder.typicode.com/todos/%s' % escape(id))

    return str(response.json())


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


app.run()
