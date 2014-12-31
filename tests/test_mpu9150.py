import unittest

from mock import MagicMock, call

from mpu9150 import mpu9150
from i2c_interface import i2c_interface


class TestMPU9150(unittest.TestCase):
    def setUp(self):
        self.i2c = i2c_interface()
        self.imu = mpu9150(self.i2c)

    def testReadAccX(self):
        self.i2c.read_word = MagicMock(return_value=0x39bc)
        accX = self.imu.read_x_acc()
        expected = [call(mpu9150.ACCEL_XOUT_L)]
        self.assertEquals(self.i2c.read_word.call_args_list, expected)
        self.assertEquals(accX, 0x39bc)


if __name__ == "__main__":
    unittest.main(verbosity=5)
