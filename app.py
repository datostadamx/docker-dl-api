import numpy as np
from flask import Flask
from flask import Request
from flask import jsonify
from sigmoid import sigmoid_neuron


app = Flask(__name__)
ns = sigmoid_neuron(2, 'algo.txt')


@app.route('/', methods=['GET'])
def status():
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

@app.route('/predict/<int:a>/<int:b>')
def predict(a, b):
    
    i = np.array([a, b])
    p = ns.predict(i)
    
    message = {
        "status": 200,
        "message": [
            {
                "input": [a, b],
                "prediction": float(p)
            }
        ]
    }
    
    response = jsonify(message)
    response.status_code = 200
    
    return response
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
