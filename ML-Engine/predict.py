import joblib
import numpy as np

model = joblib.load("model.pkl")
mlb = joblib.load("label_binarizer.pkl")
scaler = joblib.load("scaler.pkl")

def predict_fault(data):
    data_scaled = scaler.transform([data])
    prediction = model.predict(data_scaled)
    faults = mlb.inverse_transform(prediction)
    return faults

if __name__ == "__main__":
    test_data = [230, 5, 50]  # voltage, current, frequency
    print(predict_fault(test_data))
