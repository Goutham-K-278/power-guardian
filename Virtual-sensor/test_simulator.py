# test_simulation.py

from data_profile import generate_reading
from config import SENSOR_ID

for _ in range(10):
    print(generate_reading(SENSOR_ID))
