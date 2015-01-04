class mpu9150:
    # Accelerometer addresses
    ACCEL_CONFIG = 0x1c
    ACCEL_XOUT_L = 0x3b
    ACCEL_YOUT_L = 0x3d
    ACCEL_ZOUT_L = 0x3f
    # Accelerometer values
    AFS_SEL_2G = 0x0
    AFS_SEL_4G = 0x1
    AFS_SEL_8G = 0x2
    AFS_SEL_16G = 0x3

    def __init__(self, i2c_bus):
        self.i2c = i2c_bus

    def read_x_acc(self):
        return self.i2c.read_word(self.ACCEL_XOUT_L)

    def read_y_acc(self):
        return self.i2c.read_word(self.ACCEL_YOUT_L)

    def read_z_acc(self):
        return self.i2c.read_word(self.ACCEL_ZOUT_L)

    def set_acc_full_scale_range(self, value):
        current_value = self.i2c.read_byte(self.ACCEL_CONFIG)
        new_value = current_value & 0xe7
        new_value |= value << 3
        self.i2c.write_byte(self.ACCEL_CONFIG, new_value)
