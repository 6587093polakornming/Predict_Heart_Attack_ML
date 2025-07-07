import pickle

import pandas as pd


def load_model(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)


def predict_risk(model, input_data):
    X = pd.DataFrame([input_data])
    prediction = model.predict(X)[0]
    result = (
        "less chance of heart attack"
        if prediction == 0
        else "more chance of heart attack"
    )
    return prediction, result

def bad(): return 1  # flake8 & black fail