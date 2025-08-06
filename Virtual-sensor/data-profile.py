# data-profile.py

import random
from config import BASE_VOLTAGE, BASE_CURRENT, PROBABILITIES
from utils import noisy, rand_range
from fault_catalog import FAULT_TYPES

def generate_fault():
    roll = random.random()
    faults = []

    for fault, chance in PROBABILITIES.items():
        if roll < chance:
            faults.append(fault)

    return faults if faults else ["normal"]

def generate_reading(sensor_id):
    faults = generate_fault()
    voltage = noisy(BASE_VOLTAGE, 2)
    current = noisy(BASE_CURRENT, 0.5)

    if "voltage_drop" in faults:
        voltage = rand_range(160, 200)
    if "energy_theft" in faults:
        current = rand_range(10, 15)
    if "wire_cut" in faults:
        voltage = 0
        current = 0
    if "animal_fault" in faults:
        current = rand_range(20, 30)
    if "multi_fault" in faults:
        voltage = rand_range(160, 200)
        current = rand_range(10, 15)

    power = round(voltage * current, 2)

    return {
        "sensor_id": sensor_id,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "voltage": voltage,
        "current": current,
        "power": power,
        "labels": faults,
        "description": [FAULT_TYPES[f] for f in faults]
    }
