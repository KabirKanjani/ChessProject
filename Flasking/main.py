import os
from stockfish import Stockfish
import flask_cors
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = '/test_docs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
#
@app.route('/bestMove', methods=['POST'])
@cross_origin()

def checkMove():
    print("Hello")
    json = request.args
    data = json['fen']
    # print(data)
    stockfish = Stockfish(
        path="D:\Download\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
    stockfish.update_engine_parameters(
        {"Hash": 2048,
         "UCI_Chess960": "true"})  # Gets stockfish to use a 2GB hash table, and also to play Chess960.
    #
    stockfish.set_fen_position(data)
    #
    print(stockfish.get_best_move())
    return stockfish.get_top_moves(3)


# @app.route('/bestMove', methods=['POST'])
# @cross_origin()
# def getBestMove():
#     try:
#         print("Hello")
#         json = request.args
#         print(json)
#         return json
#         # data = request.json()["fen"]
#         # # print(data)
#         # stockfish = Stockfish(
#         #     path="D:\Download\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
#         # stockfish.update_engine_parameters(
#         #     {"Hash": 2048,
#         #      "UCI_Chess960": "true"})  # Gets stockfish to use a 2GB hash table, and also to play Chess960.
#         # #
#         # stockfish.set_fen_position(data)
#         # #
#         # print(stockfish.get_best_move())
#         # response = jsonify(message="Simple server is running")
#         # response.headers.add("Access-Control-Allow-Origin", "*")
#         # return stockfish.get_top_moves(3)
#     except Exception as e:
#         print(str(e))
#         return e
#

@app.route('/upload', methods=['POST'])
@cross_origin()
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER, 'test_docs')
    if not os.path.isdir(target):
        print(target)
        os.mkdir(target)
        print(1)
    logger.info("welcome to upload`")
    file = request.files['file']
    print(file)
    filename = secure_filename(file.filename)
    print(filename)
    destination = os.path.join(os.getcwd(), "test_docs", filename)
    print(destination)
    print(os.getcwd())

    try:
        file.save(destination)
        print("Yes")
    except:
        print("No")
    response = "Whatever you wish too return"
    print(response)
    return response


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
    flask_cors.CORS(app, expose_headers='Authorization')
