import random

def read_sensor():
    temperature = round(random.uniform(20,35),2)
    humidity = round(random.uniform(40,80),2)

    return temperature, humidity