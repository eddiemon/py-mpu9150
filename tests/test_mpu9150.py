import unittest

from mpu9150 import mpu9150
from i2c_interface import i2c_interface


class TestMPU9150(unittest.TestCase):
    def setUp(self):
        self.i2c = i2c_interface()
        self.imu = mpu9150(self.i2c)

    def testReadAccX(self):
        # Override read word functions in I2C I/F
        # with a little bit of logic
        def read_word(addr):
            return 0x39bc if addr == mpu9150.ACCEL_XOUT_L else 0

        self.i2c.read_word = read_word

        value = self.imu.read_x_acc()
        self.assertEquals(value, 0x39bc)

    def testReadAccY(self):
        # Override read word functions in I2C I/F
        # with a little bit of logic
        def read_word(addr):
            return 0x48e3 if addr == mpu9150.ACCEL_YOUT_L else 0

        self.i2c.read_word = read_word

        value = self.imu.read_y_acc()
        self.assertEquals(value, 0x48e3)

    def testReadAccZ(self):
        # Override read word functions in I2C I/F
        # with a little bit of logic
        def read_word(addr):
            return 0x5a3f if addr == mpu9150.ACCEL_ZOUT_L else 0

        self.i2c.read_word = read_word

        value = self.imu.read_z_acc()
        self.assertEquals(value, 0x5a3f)

    def testSetAccFullScaleRange(self):
        self.i2c.value = 0xff
        self.i2c.addr = 0x0000

        # Override read and write byte functions in I2C I/F
        # with a little bit of logic
        def write_byte(addr, value):
            self.i2c.addr = addr
            self.i2c.value = value

        self.i2c.write_byte = write_byte

        def read_byte(addr):
            if addr == mpu9150.ACCEL_CONFIG:
                return self.i2c.value
            else:
                return 0

        self.i2c.read_byte = read_byte

        self.imu.set_acc_full_scale_range(mpu9150.AFS_SEL_4G)
        self.assertEquals(self.i2c.addr, mpu9150.ACCEL_CONFIG)
        self.assertEquals(self.i2c.value, 0xef)


if __name__ == "__main__":
    unittest.main(verbosity=5)
