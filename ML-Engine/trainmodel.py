import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from data_fetch import fetch_data
from preprocess import preprocess

def train():
    df = fetch_data()
    X, y, mlb, scaler = preprocess(df)

    model = OneVsRestClassifier(RandomForestClassifier(n_estimators=200))
    model.fit(X, y)

    # Save model, label binarizer, and scaler
    joblib.dump(model, "model.pkl")
    joblib.dump(mlb, "label_binarizer.pkl")
    joblib.dump(scaler, "scaler.pkl")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train()
