from ucollections import namedtuple

ZERO_BOTTOM = 400
ZERO_TOP = 500
ESP_MAX_VALUE = 1024
BACKWARD_SPEED_K = 1

class Axis:
    action = 0
    speed = 0
    value = 0
# Axis = namedtuple('AxisRaw', ('action', 'speed'))
AxisRaw = namedtuple('AxisRaw', ('action', 'speed', 'value'))


class Control:
    ACTION_STOP = 0
    ACTION_BACKWARD = 1
    ACTION_FORWARD = 2
    ACTION_LEFT = 1
    ACTION_RIGHT = 2

    x_axis = AxisRaw(0, 0, 0)
    y_axis = AxisRaw(0, 0, 0)

    x_actions = ('stop', 'left', 'right')
    y_actions = ('stop', 'backward', 'forward')


    def read_raw(self, value_x, value_y):
        self.x_axis = self._decrypt_value(value_x)
        self.y_axis = self._decrypt_value(value_y)


    def _decrypt_value(self, value):
        if value < ZERO_BOTTOM:
            action = 1
            speed = ((ZERO_BOTTOM - value) / ZERO_BOTTOM) * ESP_MAX_VALUE
        elif value > ZERO_TOP:
            action = 2
            speed = ((value - ZERO_TOP) / (ESP_MAX_VALUE - ZERO_TOP)) * (ESP_MAX_VALUE)
        else:
            action = 0
            speed = 0

        return AxisRaw(action, int(speed), value)


    def y_to_string(self):
        return self._to_string(self.y_actions, self.y_axis)


    def x_to_string(self):
        return self._to_string(self.x_actions, self.x_axis)


    def _to_string(self, actions, axis):
        return actions[axis.action] + ' ' + str(axis.speed) + 'km/h (' + str(axis.value) + ')'


    def output(self):
        return ",".join([str(self.x_axis.action), str(self.x_axis.speed), str(self.y_axis.action), str(self.y_axis.speed)])
        # return ",".join([str(self.x_axis.action), str(self.x_axis.speed), str(self.y_axis.action), str(self.y_axis.speed]))


    def input(self, byte_str):
        self.x_axis.action, self.x_axis.speed, self.y_axis.action, self.y_axis.speed = str(byte_str).split(",")
