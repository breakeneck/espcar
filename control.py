from ucollections import namedtuple

ZERO_BOTTOM = 400
ZERO_TOP = 500
ESP_MAX_VALUE = 1024
BACKWARD_SPEED_K = 1

Axis = namedtuple('Axis', ('action', 'speed', 'value'))


class Control:
    ACTION_STOP = 0
    ACTION_BACKWARD = 1
    ACTION_FORWARD = 2
    ACTION_LEFT = 1
    ACTION_RIGHT = 2

    x_axis = Axis(0, 0, 0)
    y_axis = Axis(0, 0, 0)

    x_actions = ('stop', 'left', 'right')
    y_actions = ('stop', 'backward', 'forward')


    def decrypt(self, value_x, value_y):
        self.x_axis = self.decrypt_value(value_x)
        self.y_axis = self.decrypt_value(value_y)


    def decrypt_value(self, value):
        if value < ZERO_BOTTOM:
            action = 1
            speed = ((ZERO_BOTTOM - value) / ZERO_BOTTOM) * ESP_MAX_VALUE
        elif value > ZERO_TOP:
            action = 2
            speed = ((value - ZERO_TOP) / (ESP_MAX_VALUE - ZERO_TOP)) * (ESP_MAX_VALUE)
        else:
            action = 0
            speed = 0

        return Axis(action, int(speed), value)


    def y_to_string(self):
        return self.to_string(self.y_actions, self.y_axis)


    def x_to_string(self):
        return self.to_string(self.x_actions, self.x_axis)


    def to_string(self, actions, axis):
        return actions[axis.action] + ' ' + str(axis.speed) + 'km/h (' + str(axis.value) + ')'
