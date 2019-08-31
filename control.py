from ucollections import namedtuple
# Axis = namedtuple('AxisRaw', ('action', 'speed'))
# AxisRaw = namedtuple('AxisRaw', ('action', 'speed', 'value'))


# ACTION_STOP = 0
# ACTION_BACKWARD = 1
# ACTION_FORWARD = 2
# ACTION_LEFT = 1
# ACTION_RIGHT = 2


from machine import Pin, ADC
import time


class Joy:
    adc_x = ...
    adc_y = ...
    sw = ...

    raw_x = ...
    raw_y = ...
    is_click = False

    def __init__(self, pin_x: int, pin_y: int, sw: int):
        self.adc_x = ADC(Pin(pin_x))
        self.adc_x.atten(ADC.ATTN_11DB)
        self.adc_x.width(ADC.WIDTH_10BIT)

        self.adc_y = ADC(Pin(pin_y))
        self.adc_y.atten(ADC.ATTN_11DB)
        self.adc_y.width(ADC.WIDTH_10BIT)

        self.sw = Pin(sw, Pin.IN, Pin.PULL_UP)

    def _read_click(self):
        first = self.sw.value()
        time.sleep(0.05)
        second = self.sw.value()

        if first and not second:
            print('button pressed')
            return True
        elif not first and second:
            print('Button released!')
            return False

        return False

    def read(self):
        self.raw_x = self.adc_x.read()
        self.raw_y = self.adc_y.read()
        self.is_click = self._read_click()


class Axis:
    TYPE_ABSCISSA = 0
    TYPE_ORDINATE = 1

    type = ...
    action = 0
    speed = 0
    value = 0

    ZERO_BOTTOM = 400
    ZERO_TOP = 500
    ESP_MAX_VALUE = 1024

    ACTION_NONE = 0
    ACTION_FIRST = 1
    ACTION_SECOND = 2

    def __init__(self, type):
        self.type = type

    def read_raw(self, value):
        if value < self.ZERO_BOTTOM:
            self.action = self.ACTION_FIRST
            self.speed = ((self.ZERO_BOTTOM - value) / self.ZERO_BOTTOM) * self.ESP_MAX_VALUE
        elif value > self.ZERO_TOP:
            self.action = self.ACTION_SECOND
            self.speed = ((value - self.ZERO_TOP) / (self.ESP_MAX_VALUE - self.ZERO_TOP)) * self.ESP_MAX_VALUE
        else:
            self.action = self.ACTION_NONE
            self.speed = 0

    def action_to_str(self):
        if self.type == self.TYPE_ABSCISSA:
            return ('stop', 'left', 'right')[self.action]
        else:
            return ('stop', 'backward', 'forward')[self.action]

    def __str__(self):
        return self.action_to_str() + ' ' + str(int(self.speed)) + 'km/h'


class Control:
    x = Axis(Axis.TYPE_ABSCISSA)
    y = Axis(Axis.TYPE_ORDINATE)
    is_click = False

    _joy = ...

    def setup_joy(self, pin_x, pin_y, pin_sw):
        self._joy = Joy(pin_x, pin_y, pin_sw)

    def read_joy(self):
        self._joy.read()

        self.x.read_raw(self._joy.raw_x)
        self.y.read_raw(self._joy.raw_y)
        self.is_click = self._joy.is_click

        time.sleep(0.1)

    def load(self, byte_str):
        self.x.action, self.x.speed, self.y.action, self.y.speed = str(byte_str).split(",")

    def __str__(self):
        return ",".join(
            [str(self.x.action), str(self.x.speed), str(self.y.action), str(self.y.speed)])
