# config.py

API_ENDPOINT = "http://localhost:5000/api/data"
SENSOR_ID = "vs-101"
SEND_INTERVAL = 2  # seconds

# Base values for normal operation
BASE_VOLTAGE = 230.0
BASE_CURRENT = 5.0

# Fault chances
PROBABILITIES = {
    "voltage_drop": 0.1,
    "energy_theft": 0.05,
    "wire_cut": 0.02,
    "animal_fault": 0.03,
    "multi_fault": 0.01
}