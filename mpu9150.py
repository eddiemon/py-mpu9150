class mpu9150:
    ACCEL_XOUT_L = 0x3b

    def __init__(self, i2c_bus):
        self.i2c = i2c_bus

    def read_x_acc(self):
        return self.i2c.read_word(self.ACCEL_XOUT_L)
