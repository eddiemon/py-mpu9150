from mpu9150 import mpu9150
import unittest
from smbus import SMBus
from mock import Mock, patch, create_autospec

class TestMPU9150(unittest.TestCase):

    def setUp(self):
        self.smbus = create_autospec(SMBus)
        patch.dict('sys.modules', {'smbus': self.smbus})
        self.imu = mpu9150()


#    def testCanInstantiate(self):
#        imu = mpu9150
#        self.assertTrue(True)

    def testReadAccX(self):
        accX = self.imu.readAccX()
        self.assertEquals(accX == 0x40)
        


if __name__ == "__main__":
    unittest.main(verbosity=5)
