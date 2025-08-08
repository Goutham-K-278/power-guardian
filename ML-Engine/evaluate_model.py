import joblib
from sklearn.metrics import classification_report
from data_fetch import fetch_data
from preprocess import preprocess

def evaluate():
    df = fetch_data()
    X, y, mlb, scaler = preprocess(df)

    model = joblib.load("model.pkl")
    y_pred = model.predict(X)

    print(classification_report(y, y_pred, target_names=mlb.classes_))

if __name__ == "__main__":
    evaluate()
