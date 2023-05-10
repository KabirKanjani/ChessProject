import cv2

import webbrowser
import time
import numpy as np
import os
# import chessvision
import cv2
import fitz
from stockfish import Stockfish
import flask_cors
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import requests
from pdf2image import convert_from_path

valid_board = 0
count_fen = 0
list_fen = []
check = False
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = '/test_docs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/GetFen', methods=['POST'])
@cross_origin()
def GetFen():
    if request.get_json():
        list_fen.append(f"{request.get_json()['fen']} w - - 0 1")
        print(request.get_json()['fen'])
        if request.get_json()['fen'] == 'Fin':
            global check
            check = True

    return "Thank you"


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    email = request.get_json()['Email']
    password = request.get_json()['Password']
    if email==password:
        return {"auth":True}
    else:
        return {"auth":False}


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
    if stockfish.get_best_move() == 'None':
        return {"Move": "Game Over"}
    return stockfish.get_top_moves(3)


def checkIfFinish():
    print("Hello Check", check)
    while (True):
        if check == True:
            logger.info("Done")
            return jsonify(list_fen)
        print(check)


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
    global check
    check = False
    global valid_board
    valid_board = 50
    target = os.path.join(UPLOAD_FOLDER, 'test_docs')
    if not os.path.isdir(target):
        print(target)
        os.mkdir(target)
        print(1)
    logger.info("welcome to upload`")
    file = request.files['file']
    headers = request.headers
    bearer = headers.get('Authorization')  # Bearer YourTokenHere
    # token = bearer.split()[1]  # YourTokenHere
    start_num = int(bearer)
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
    convert_pdf_to_image(destination, start_num)
    print("Chess")
    url = 'http://localhost/files/git/tensorflowjs/ChessboardFenTensorflowJs-master/?pageno=50'
    browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser)
    print("KAB")
    webbrowser.open(url)
    return checkIfFinish()


def convert_pdf_to_image(path, start_num):
    print("-------------Converting PDF to Image-------------------")
    last_page = int(start_num) + 20
    pages = convert_from_path(path, first_page=start_num, last_page=last_page)
    count = start_num
    for page in pages:
        page.save(f'Tactics_0{count}.png', 'PNG')
        count += 1

    for i in range(start_num, start_num + 20):
        convert_image_to_chessboards(f'Tactics_0{i}.png')


def convert_image_to_chessboards(filename):
    # Load the image
    print("-------------Converting Image to Chessboards-------------------")
    img = cv2.imread(filename)

    # Color-segmentation to get binary mask
    lwr = np.array([0, 0, 143])
    upr = np.array([179, 61, 252])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    msk = cv2.inRange(hsv, lwr, upr)

    # Extract chess-board
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 30))
    dlt = cv2.dilate(msk, krn, iterations=5)
    res = 255 - cv2.bitwise_and(dlt, msk)

    # Displaying chess-board features
    res = np.uint8(res)
    ret, corners = cv2.findChessboardCorners(res, (7, 7),
                                             flags=cv2.CALIB_CB_ADAPTIVE_THRESH +
                                                   cv2.CALIB_CB_FAST_CHECK +
                                                   cv2.CALIB_CB_NORMALIZE_IMAGE)

    if ret:
        print(type(corners))
        s1 = (corners[48][0][0] - corners[0][0][0]) / 5
        s2 = (corners[48][0][1] - corners[0][0][1]) / 5
        corners[0][0][0] = corners[0][0][0] - s1
        corners[0][0][1] = corners[0][0][1] - s2
        corners[48][0][0] = corners[48][0][0] + s1
        corners[48][0][1] = corners[48][0][1] + s2
        co = np.array([corners[0][0], corners[48][0]])
        # fnl = cv2.drawChessboardCorners(img, (7,7), co, ret)
        # cv2.imshow("fnl", img)
        print(corners[0][0][0], corners[48][0][0])

        cropped_image = img[int(corners[0][0][1]):int(corners[48][0][1]),
                        int(corners[0][0][0]):int(corners[48][0][0])]

        # Save the cropped image to a file
        global valid_board
        cv2.imwrite(f"Chessboards\cropped_image_0{valid_board}.png", cropped_image)
        SaveImageToServer(f"cropped_image_0{valid_board}.png", f"./Chessboards/cropped_image_0{valid_board}.png")
        valid_board = valid_board + 1
    else:
        print("No Checkerboard Found")


def SaveImageToServer(filename, filepath):
    print("-------------Saving Image to Servers-------------------")
    url = "http://localhost/files/git/tensorflowjs/ChessboardFenTensorflowJs-master/saveFile.php"

    payload = {}
    files = [
        ('image', (filename, open(filepath, 'rb'), 'image/png'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
    flask_cors.CORS(app, expose_headers='Authorization')
