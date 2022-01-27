from io import BytesIO
from io import StringIO
from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
import barcode
from io import BytesIO

from flask import make_response, url_for, redirect
from flask import request, render_template, flash
import barcode
import qrcode


app = Flask(__name__)
CORS(app)

def gen_code39(content):
    fp = StringIO()
    makepng = barcode.writer.ImageWriter()
    barcode.generate("Code39", content, output=fp, writer=makepng)
    image = fp.getvalue()
    fp.close()
    return image


@app.route('/generate_qrcode/<uuid>', methods=['POST'])
def render_code39(uuid):
    response = make_response(gen_code39(uuid))
    response.headers["Content-type"] = "image/png"
    return response


app.run()
