"""
Model Class
"""
import os
import joblib


class ModelApi:
    """Model Api"""

    def __init__(self):
        """
        Constructor
        """
        self._model = None

    def predict(self, X):
        """
        Make predictions.
        :param X: A data frame.
        :return: A sequence of predictions with the same length as X.
        """
        return self._model.predict(X)

    def load(self, model_dir):
        """
        Load model weights from a local path.
        :param model_dir: A string representing a directory.
        """
        self._model = joblib.load(os.path.join(model_dir, 'PVFaultClassification_RandomForestModel'))
        return self
