# Power Guardian 2.0 - ML Module
## Overview
This module trains and serves a multi-label machine learning model to detect
multiple power line faults in real-time.

## Features
- Predicts multiple faults at once
- Uses synthetic + real-world SCADA-like datasets
- Optimized for accuracy and low latency

## How to Use
1. Install dependencies:
   pip install -r requirements.txt
2. Train the model:
   python train.py
3. Predict from saved model:
   python predict.py

## Files
- `train.py` — Train the model
- `predict.py` — Load model.pkl and predict
- `model.pkl` — Saved trained model
- `requirements.txt` — Dependencies
- `README.md` — Documentation
