class mpu9150:
    ACCEL_XOUT_L = 0x3b
    ACCEL_YOUT_L = 0x3d
    ACCEL_ZOUT_L = 0x3f

    def __init__(self, i2c_bus):
        self.i2c = i2c_bus

    def read_x_acc(self):
        return self.i2c.read_word(self.ACCEL_XOUT_L)

    def read_y_acc(self):
        return self.i2c.read_word(self.ACCEL_YOUT_L)

    def read_z_acc(self):
        return self.i2c.read_word(self.ACCEL_ZOUT_L)
