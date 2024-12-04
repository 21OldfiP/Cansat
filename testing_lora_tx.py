# Hardware: Raspberry pi pico with pico display
#       433MHz RFM9x LORA => Pico
#                   VIN   => 3.3v (36)
#                   GND   => GND  (28)
#                   SCK   => GP18  (4)
#                   MISO  => GP0  (6)
#                   MOSI  => GP19  (5)
#                   CS    => GP1  (2)
#                   RST   => GP2  (1)
# Firmware: CircuitPython 8
# Tests: LoRa radio
# Success: LoRa sends X,Y A or B when you press corresponding button

import board
import busio
import adafruit_rfm9x
import time
import digitalio
import picoexplorer as display

cs_lora = digitalio.DigitalInOut(board.GP1)
cs_lora.direction = digitalio.Direction.OUTPUT
cs_lora.value = False
reset_lora = digitalio.DigitalInOut(board.GP2)
rfm9x = adafruit_rfm9x.RFM9x(display.spi, cs_lora, reset_lora, 433.0, baudrate=5000000)
rfm9x.tx_power = 23
print("Started")

while True:
    for b in display.buttons:
        if display.buttons[b].value == False:
            print("Button " + b + " pressed")
            rfm9x.send(b)
            
            
    time.sleep(1)