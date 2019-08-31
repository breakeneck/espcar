from ucollections import namedtuple

# Axis = namedtuple('AxisRaw', ('action', 'speed'))
# AxisRaw = namedtuple('AxisRaw', ('action', 'speed', 'value'))

TYPE_ABSCISSA = 0
TYPE_ORDINATE = 1


class Axis:
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

    def read(self, value):
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
        if self.type == TYPE_ABSCISSA:
            return ('stop', 'left', 'right')[self.action]
        else:
            return ('stop', 'backward', 'forward')[self.action]

    def __str__(self):
        return self.action_to_str() + ' ' + str(self.speed) + 'km/h'


class Control:
    ACTION_STOP = 0
    ACTION_BACKWARD = 1
    ACTION_FORWARD = 2
    ACTION_LEFT = 1
    ACTION_RIGHT = 2

    x = Axis(TYPE_ABSCISSA)
    y = Axis(TYPE_ORDINATE)

    def read(self, value_x, value_y):
        self.x.read(value_x)
        self.y.read(value_y)

    def output(self):
        return ",".join(
            [str(self.x.action), str(self.x.speed), str(self.y.action), str(self.y.speed)])

    def input(self, byte_str):
        self.x.action, self.x.speed, self.y.action, self.y.speed = str(byte_str).split(",")
