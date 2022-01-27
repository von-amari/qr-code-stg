# app.py
from flask import Flask, request, send_file
import qrcode
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/generage_qrcode', methods=['POST'])
def generate_qrcode():
    # Retrieve the name from url parameter
    buffer = BytesIO()
    data = request.form.get('data')

    img = qrcode.make(data)
    img.save(buffer)
    buffer.seek(0)
    response = send_file(buffer, mimetype='image/png')
    return response


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()