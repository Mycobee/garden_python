#this file is going to be ran every 15 seconds by the cron job.
#Its going to post the moisture readout on the pins and send them to the env_measurements endpoint.

import time
import requests

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Reading MCP3008 values')
moisture = mcp.read_adc(0) / float(10)
url = 'https://garden-pi-be.herokuapp.com/api/v1/gardens/1/env_measurements'
params_hash = {'soil_moisture': moisture, 'soil_temperature': 69.25}

r = requests.post(url, params=params_hash)
print(r.text)
