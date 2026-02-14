import time
import requests
import random

API_URL = "http://127.0.0.1:8000/api/state/1/"

while True:
    state = random.choice(["empty", "occupied"])

    print("Setting state:", state)

    requests.put(API_URL, data={"name": state})

    time.sleep(5)
