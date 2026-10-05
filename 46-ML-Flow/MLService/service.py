import numpy as np
import bentoml

# Load the trained Iris model
iris_clf = bentoml.sklearn.get("iris_clf:latest")


@bentoml.service
class IrisClassifier:

    @bentoml.api
    def classify(self, input_series: np.ndarray) -> np.ndarray:
        model = iris_clf.load_model()

        result = model.predict(input_series)

        return result


# BentoML service
svc = IrisClassifier
