from io import BytesIO
from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    buffer = BytesIO()
    data = request.form.get('data')

    img = qrcode.make(data)
    img.save(buffer)
    buffer.seek(0)

    response = send_file(buffer, mimetype = 'image/png')
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')
    return img

if __name__ == '__main__':
    app.run()

