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



# def generate_qrcode():
#     buffer = BytesIO()
#     data = request.form.get('data')

#     img = qrcode.make(data)
#     img.save(buffer)
#     buffer.seek(0)

#     response = send_file(buffer, mimetype = 'image/png')
#     qr = qrcode.QRCode(
#         version=1,
#         box_size=10,
#         border=5)
#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image(fill='black', back_color='white')
#     img.save('qrcode001.png')
#     return img


app.run()

