# Hardware: Raspberry pi pico with pico display
#       433MHz RFM9x LORA => Pico
#                   VIN   => 3.3v (36)
#                   GND   => GND  (28)
#                   SCK   => GP26 (31)
#                   MISO  => GP28 (34)
#                   MOSI  => GP27 (32)
#                   CS    => GP22 (29)
#                   RST   => GP21 (27)
# Firmware: CircuitPython 8
# Tests: LoRa receive data
# Success: Listens for data received via LoRa radio and displays it on the console

import board
import busio
import adafruit_rfm9x
import time
import digitalio

spi_mosi = board.GP27
spi_clk = board.GP26
spi_miso = board.GP28
spi_lora = busio.SPI(spi_clk, MOSI=spi_mosi, MISO=spi_miso)
cs_lora = digitalio.DigitalInOut(board.GP22)
cs_lora.direction = digitalio.Direction.OUTPUT
cs_lora.value = False
reset_lora = digitalio.DigitalInOut(board.GP21)
rfm9x = adafruit_rfm9x.RFM9x(spi_lora, cs_lora, reset_lora, 433.0, baudrate=1000000)
print("Started")
while True:
    data = rfm9x.receive()
    
    if data:
        print(data)
    else:
        pass
        # print("Nothing received")
    time.sleep(.1)