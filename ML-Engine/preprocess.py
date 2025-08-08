import pandas as pd
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer

def preprocess(df):
    # Convert fault labels (comma-separated) to multi-label format
    df['faults'] = df['faults'].apply(lambda x: x.split(','))

    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(df['faults'])

    # Drop non-numeric columns except location (if needed)
    X = df.drop(['faults', 'location'], axis=1)

    # Scale numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, mlb, scaler
