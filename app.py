from flask import Flask
from flask import Request
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def status() -> Request:
    """GET method for API status verification.

    Returns
    -------
    response : Request
        JSON message with API status.
    """
    
    message = {
        "status": 200,
        "message": [
            "This API is up and running!"
        ]
    }
    response = jsonify(message)
    response.status_code = 200

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
