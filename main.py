#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Code shamelessly taken from the pimoroni repository, thank you Sandy Macdonald:
https://github.com/pimoroni/bmp280-python/blob/master/examples/temperature-and-pressure.py
"""
import time
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""temperature-and-pressure.py - Displays the temperature and pressure.
Press Ctrl+C to exit!
""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    print('{:05.2f}*C {:05.2f}hPa'.format(temperature, pressure))
    time.sleep(1)
    
