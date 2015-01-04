import sys
sys.path.append("../../Adafruit_Python_GPIO/Adafruit_GPIO")

import i2c_interface
import I2C

class Device(i2c_interface):

    def __init__(self):
        self.i2c = I2C.get_i2c_device(0x1f)

    def read_byte(self, address):
        return self.i2c.readU8(address)

    def read_word(self, address):
        return self.i2c.readU16(address)

    def write_byte(self, address, value):
        self.i2c.write8(address, value)

    def write_word(self, address, value):
        self.i2c.write16(address, value)