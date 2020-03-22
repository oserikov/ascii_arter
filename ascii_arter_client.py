import base64
import requests

imgname = "octocat.png"

# 127.0.0.1 is the address of your machine from inside the machine itself
# and 5000 is the default port for flask, flask is the thing that runs the ascii-art-drawing-server
endpoint_url = "http://127.0.0.1:5000/img2ascii"

with open(imgname, "rb") as img_f:
    # images are stored as binary smth on drive
    # lets convert this to string-like base64 byte-string (cause we know how to convert backwards)
    base64encoded_img = base64.b64encode(img_f.read())

# base64encoded_img is actually a byte-string, lets convert it to simple python string
base64encoded_img_string = base64encoded_img.decode("utf-8")

# we will send the json with textual representation of our image to the ascii-art-drawing server
# so we create a dict with our data cause dicts are sort of pythonic jsons
request_body = {"base64encoded_image": base64encoded_img_string}

# we will send a POST request to the server
# one could use GET but i prefer POST cause it allows to send the json(or some else data) along with the request
# while GET forces to pass all the data in the 'url', that's ugly
response = requests.post(endpoint_url, json=request_body)

# when http, status code received indicates whether everything went ok or you did smth wrong or the server is broken etc
# all the status codes starting with 2 are for "everything went ok"
# so if the code starts with 2 we know we just received a response with the ascii-art from server
if str(response.status_code).startswith('2'):
    ascii_image = response.json()["ascii_encoded_image"]
    print(ascii_image)
else:
    print("ERROR: something went wrong")
