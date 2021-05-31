from flask import Flask, jsonify, request, abort
import time

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/name', methods=['POST'])
def save_name():
    if request.method == 'POST':
        post_data = request.json
        app.logger.info(request.json)
        if post_data is not None:
            name = post_data['name']
            return jsonify(f'Successfully stored: {name}')
    abort(400)


@app.route('/message/<name>', methods=['GET'])
def message(name):

    # infinite loop intentional purpose
    index = 0
    while name == 'infinite':
        time.sleep(1)
        index += 1
        app.logger.info(f'I am sleeping {index} seconds')

    return jsonify(message=f"What's up {name}?")
