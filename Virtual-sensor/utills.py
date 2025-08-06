# utils.py

import time
import random

def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def noisy(base, deviation):
    return round(random.gauss(base, deviation), 2)

def rand_range(low, high):
    return round(random.uniform(low, high), 2)
