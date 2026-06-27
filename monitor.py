import time
import random
from datetime import datetime

PRODUCTS = [
    {"id": "P101", "name": "Wireless Headphones", "base_price": 5000},
    {"id": "P102", "name": "Mechanical Keyboard", "base_price": 3500},
    {"id": "P103", "name": "Gaming Mouse", "base_price": 2200}
]

def fetch_simulated_price(base_price):
    if random.random() < 0.05:
        raise ConnectionError("Timeout: Failed to reach e-commerce server.")
    variation = random.randint(-300, 300)
    return max(100, base_price + variation)

def run_price_monitor():
    print("Initializing Web Price Monitor and System Logger...")
    with open("tracking_logs.txt", "w") as log_file:
        for _ in range(500):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            product = random.choice(PRODUCTS)
            try:
                current_price = fetch_simulated_price(product["base_price"])
                log_entry = f"{timestamp} [INFO] Product:{product['id']} Name:{product['name']} Price:{current_price} INR\n"
                log_file.write(log_entry)
            except ConnectionError as e:
                log_entry = f"{timestamp} [ERROR] Product:{product['id']} Status: FETCH_FAILED Reason:{str(e)}\n"
                log_file.write(log_entry)
    print("Logs compiled successfully! 'tracking_logs.txt' created with 500 entries.")

if __name__ == "__main__":
    run_price_monitor()