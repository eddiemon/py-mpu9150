import unittest

from mock import MagicMock

from mpu9150 import mpu9150
from i2c_interface import i2c_interface


class TestMPU9150(unittest.TestCase):
    def setUp(self):
        self.i2c = i2c_interface()
        self.imu = mpu9150(self.i2c)

    def testReadAccX(self):
        self.i2c.read_word = MagicMock(return_value=0x39bc)
        value = self.imu.read_x_acc()
        self.assertEquals(value, 0x39bc)

    def testReadAccY(self):
        self.i2c.read_word = MagicMock(return_value=0x48e3)
        value = self.imu.read_y_acc()
        self.assertEquals(value, 0x48e3)

    def testReadAccZ(self):
        self.i2c.read_word = MagicMock(return_value=0x5a3f)
        value = self.imu.read_z_acc()
        self.assertEquals(value, 0x5a3f)


if __name__ == "__main__":
    unittest.main(verbosity=5)
