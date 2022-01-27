# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    phone = request.args.get("phone", None)

    # For debugging
    print(f"got phone {phone}")

    response = {}

    # Check if user sent a name at all
    if not phone:
        response["ERROR"] = "no phone found, please send a phone."
    # Check if the user entered a number not a name

    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Your phone is {phone}"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('phone')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Phone is {phone}",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no phone found, please send a phone."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)