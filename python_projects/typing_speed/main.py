from datetime import datetime
import random

try:
    with open('data.txt', 'r') as file:
        data = file.read()
except Exception:
    print("Something went wrong!")



data_container =data.split('\n')
print(data_container[2])