

# Third-party imports
from flask import Flask, jsonify, request
import pandas
import numpy
import joblib


# Load model
model = joblib.load('./model/PVFaultClassification_RandomForestModel')

app = Flask(__name__)


@app.route('/predict',methods=['POST'])
def predict():
    """
    Handle a request to the predict end-point.
    """

    request_body = request.get_json(silent=True)

    # convert input data into dataframe
    cols = numpy.array(request_body['data']['columns'])
    arr = numpy.array(request_body['data']['values'])

    # run prediction
    query_df = pandas.DataFrame(data=arr, columns=cols)
    predictions = model.predict(query_df)

    return jsonify({
        "status": {
            "code": 200,
            "status": "SUCCESS"
        },
        "result": str(predictions[0])
    })


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
