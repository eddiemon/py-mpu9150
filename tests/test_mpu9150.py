import unittest

from mpu9150 import mpu9150
from i2c_interface import i2c_interface


class TestMPU9150(unittest.TestCase):

    class i2cMock(i2c_interface):
        '''Mock class for I2C interface. Creates a dictionary that represents
        memory which can be read and written from. All values in one "address"
        in the dictionary shall be 8 bits.'''
        memory = dict()

        def read_byte(self, addr):
            return self.memory.get(str(addr), 0)

        def read_word(self, addr):
            return self.read_byte(addr) + (self.read_byte(addr + 1) << 8)


        def write_byte(self, addr, value):
            self.memory[str(addr)] = value & 0xff

        def write_word(self, addr, value):
            self.memory[str(addr)] = value & 0xff
            self.memory[str(addr+1)] = (value >> 8) & 0xff

    def setUp(self):
        self.i2c = self.i2cMock()
        self.imu = mpu9150(self.i2c)

    def testReadAccXRaw(self):
        self.i2c.write_word(mpu9150.ACCEL_XOUT_L, 0x39bc)

        value = self.imu.read_x_acc_raw()
        self.assertEquals(value, 0x39bc)

    def testReadAccX(self):
        self.i2c.write_word(mpu9150.ACCEL_XOUT_L, 0xf830)

        value = self.imu.read_x_acc()
        self.assertEquals(value, -2000)

    def testReadAccYRaw(self):
        self.i2c.write_word(mpu9150.ACCEL_YOUT_L, 0x48e3)

        value = self.imu.read_y_acc_raw()
        self.assertEquals(value, 0x48e3)

    def testReadAccY(self):
        self.i2c.write_word(mpu9150.ACCEL_YOUT_L, 0xf830)

        value = self.imu.read_y_acc()
        self.assertEquals(value, -2000)

    def testReadAccZRaw(self):
        self.i2c.write_word(mpu9150.ACCEL_ZOUT_L, 0x5a3f)

        value = self.imu.read_z_acc_raw()
        self.assertEquals(value, 0x5a3f)

    def testReadAccZ(self):
        self.i2c.write_word(mpu9150.ACCEL_ZOUT_L, 0xf830)

        value = self.imu.read_z_acc()
        self.assertEquals(value, -2000)

    def testSetAccFullScaleRange(self):
        self.i2c.write_byte(mpu9150.ACCEL_CONFIG, 0xff)

        self.imu.set_acc_full_scale_range(mpu9150.AFS_SEL_4G)
        self.assertEquals(self.i2c.read_byte(mpu9150.ACCEL_CONFIG), 0xef)

    def testSetSampleRateDivider(self):
        self.imu.set_sample_rate_divider(0x3c)
        self.assertEqual(self.i2c.read_byte(mpu9150.SMPRT_DIV), 0x3c)



if __name__ == "__main__":
    unittest.main(verbosity=5)
