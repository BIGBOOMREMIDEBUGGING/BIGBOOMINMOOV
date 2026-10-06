import pyfirmata2
import time


board = pyfirmata2.Arduino('COM3')

horizontal = board.get_pin('d:11:s')

horizontal.write(0)
print("0")
time.sleep(2)
horizontal.write(90)
print("90")
time.sleep(2)

board.exit()