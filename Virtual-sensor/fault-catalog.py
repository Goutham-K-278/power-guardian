# fault_catalog.py

FAULT_TYPES = {
    "normal": "No fault detected",
    "voltage_drop": "Voltage dropped below threshold",
    "energy_theft": "Unexpected high current draw (possible theft)",
    "wire_cut": "Zero voltage and current (line disconnected)",
    "animal_fault": "Sudden high current due to line contact",
    "multi_fault": "Combination of multiple faults detected"
}
