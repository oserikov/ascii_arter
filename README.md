Simple http api example for passing images over POST requests

Consists of 
1. flask-*server* drawing an ascii-art given the image
2. *client* reading an image from the local filesystem and receiving an ascii representation of the image from the server

Depends on `flask` and `Pillow` packages

---

The server (at my machine) is started with `export FLASK_APP=ascii_arter_server.py && python3 -m flask run`
```bash
oleg@LAPTOP:/mnt/c/Users/oleg/ascii_arter$ export FLASK_APP=ascii_arter_server.py && python3 -m flask run
 * Serving Flask app "ascii_arter_server.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The client (at my machine) is executed with `oleg@LAPTOP:/mnt/c/Users/oleg/ascii_arter$ python3 ascii_arter_client.py`

---

An img2ascii algorithm is taken from this amazing repo [github.com/RameshAditya/asciify](https://github.com/RameshAditya/asciify)

An SO thread ([link](https://stackoverflow.com/questions/394882/how-do-ascii-art-image-conversion-algorithms-work)) with some thoughts on how does img2ascii conversion work