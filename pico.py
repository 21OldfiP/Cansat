import board
import busio

i2c = busio.I2C(board.GP1, board.GP0)
while not i2c.try_lock():
    pass 
print(i2c.scan())
