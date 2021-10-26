

# Third-party imports
from flask import Flask, jsonify, request
import pandas
import numpy

# Local imports
from model_api.model import ModelApi
from model_api import MODEL_DIR

# Load model
MODEL = ModelApi()
MODEL.load(MODEL_DIR)

app = Flask(__name__)


@app.route("/predict")
def predict():
    """
    Handle a request to the predict end-point.
    """

    req_body = request.get_json(silent=True)

    # convert input data into dataframe
    names = numpy.array(req_body['data']['names'])
    input_arr = numpy.array(req_body['data']['ndarray'])

    # run prediction
    query_df = pandas.DataFrame(data=input_arr, columns=names)
    predictions = MODEL.predict(query_df)
    p_packged = [[p] for p in predictions]

    return jsonify({
        "status": {
            "code": 200,
            "status": "SUCCESS"
        },
        "data": {
            "ndarray": p_packged
        }
    })


if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', port=8080, debug=False)
