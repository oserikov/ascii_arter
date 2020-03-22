# TO RUN THIS API:
# (1) set FLASK_APP environment variable to the name of this file
# (2) execute: python -m flask run
# e.g. in console: FLASK_APP=this_file_name.py python -m flask run
# see http://flask.pocoo.org/docs/1.0/cli/#application-discovery 
# for more info on FLASK_APP variable
import base64
from io import BytesIO

from flask import Flask, Response, request, json

# install Pillow package to make PIL work
from PIL import Image

import asciify

app = Flask(__name__)

ENDPOINT_PATH = "/img2ascii"


@app.route(ENDPOINT_PATH, methods=['POST'])
def hello_username_json():
    body = request.get_json()

    base64encoded_image = body["base64encoded_image"]
    image_decoded = base64.b64decode(base64encoded_image)

    image_obj = Image.open(BytesIO(image_decoded))  # https://stackoverflow.com/questions/26070547

    ascii_encoded_image = asciify.do(image_obj)

    print(ascii_encoded_image)

    response_dict = {
        "ascii_encoded_image": ascii_encoded_image
    }
    response_json = json.dumps(response_dict)
    content_type = "application/json; charset=utf-8"

    response = Response(response=response_json, content_type=content_type, status=200)
    return response
