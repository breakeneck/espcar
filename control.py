FORWARD_MAX = 700
BACKWARD_MIN = 900
ESP_MAX_VALUE = 1024
BACKWARD_SPEED_K = 1


class Control:
    ACTION_STOP = 0
    ACTION_FORWARD = 1
    ACTION_BACKWARD = 2
    ACTION_LEFT = 3
    ACTION_RIGHT = 4
    
    action = 0
    speed = 0
    value_y = ...
    value_x = ...
    actionsList = ['stop', 'forward', 'backward', 'left', 'right']

    def read_action(self, value_y):
        self.value_y = value_y

        if self.value_y < FORWARD_MAX:
            self.action = self.ACTION_FORWARD
            self.speed = ((FORWARD_MAX - self.value_y) / FORWARD_MAX) * ESP_MAX_VALUE
        elif value_y > BACKWARD_MIN:
            self.action = self.ACTION_BACKWARD
            self.speed = ((self.value_y - BACKWARD_MIN) / (ESP_MAX_VALUE - BACKWARD_MIN)) * (ESP_MAX_VALUE * BACKWARD_SPEED_K)
        else:
            self.action = self.ACTION_STOP
            self.speed = 0

        self.speed = round(self.speed)

    def action_str(self):
        return self.actionsList[self.action]

    def to_string(self):
        return self.action_str() + ' ' + str(self.speed) + 'km/h (' + str(self.value_y) + ')'
