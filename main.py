import time
from sensor import read_sensor

print("Smart Environmental Monitor")
print("--------------------------")

while True:
    temp, hum = read_sensor()

    print("Temperature:", temp, "°C")
    print("Humidity:", hum, "%")
    print("--------------------------")

    time.sleep(2)