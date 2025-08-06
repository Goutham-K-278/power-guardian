# sensor.py

import time
import requests
from config import API_ENDPOINT, SENSOR_ID, SEND_INTERVAL
from data_profile import generate_reading
from logger import get_logger

logger = get_logger()

def run():
    while True:
        data = generate_reading(SENSOR_ID)
        logger.info(f"Sending: {data}")

        try:
            response = requests.post(API_ENDPOINT, json=data)
            logger.info(f"Server response: {response.status_code}")
        except Exception as e:
            logger.error(f"Failed to send data: {e}")

        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    run()
