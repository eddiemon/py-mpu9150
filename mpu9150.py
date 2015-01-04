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

    SMPRT_DIV = 0x25

    def __init__(self, i2c_bus):
        self.i2c = i2c_bus

    @staticmethod
    def twos_comp(val, bits):
        """compute the 2's compliment of int value val"""
        if( (val&(1<<(bits-1))) != 0 ):
            val = val - (1<<bits)
        return val

    def read_x_acc_raw(self):
        return self.i2c.read_word(self.ACCEL_XOUT_L)

    def read_x_acc(self):
        raw_value = self.read_x_acc_raw()
        return mpu9150.twos_comp(raw_value, 16)

    def read_y_acc_raw(self):
        return self.i2c.read_word(self.ACCEL_YOUT_L)

    def read_y_acc(self):
        raw_value = self.read_y_acc_raw()
        return mpu9150.twos_comp(raw_value, 16)

    def read_z_acc_raw(self):
        return self.i2c.read_word(self.ACCEL_ZOUT_L)

    def read_z_acc(self):
        raw_value = self.read_z_acc_raw()
        return mpu9150.twos_comp(raw_value, 16)

    def set_acc_full_scale_range(self, value):
        current_value = self.i2c.read_byte(self.ACCEL_CONFIG)
        new_value = current_value & 0xe7
        new_value |= value << 3
        self.i2c.write_byte(self.ACCEL_CONFIG, new_value)

    def set_sample_rate_divider(self, value):
        self.i2c.write_byte(self.SMPRT_DIV, value)
