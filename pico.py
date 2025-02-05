import board
import busio
import adafruit_bmp280
import adafruit_ahtx0
import time


i2c = busio.I2C(board.GP1, board.GP0)

sensor = adafruit_ahtx0.AHTx0(i2c)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1036.5



while (True):
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)   


#while True:
print("\nTemperature: %0.1f C" % sensor.temperature)
print("Humidity: %0.1f %%" % sensor.relative_humidity)
#time.sleep(2)
