import machine
import time

DEFAULT_SPEED = 500

"""
PIN   1, 2, 3, 4, L,  R
GPIO  5, 4, 0, 2, 12, 14
8266 D1,D2,D3,D4, D6, D5
32  
"""


# order of pins on L298N
#
# PIN_ENABLE_A = 12 # white
# PIN_INPUT1 = 5 # orange
# PIN_INPUT2 = 4 # yellow
# PIN_INPUT3 = 0 # green
# PIN_INPUT4 = 2 # blue
# PIN_ENABLE_B = 14 # black
#
# GND violet

class Car:
    last_action_str = ...

    def __init__(self, pin_input1, pin_input2, pin_input3, pin_input4, pin_enable_a, pin_enable_b):
        self.p1 = machine.Pin(pin_input1, machine.Pin.OUT)
        self.p2 = machine.Pin(pin_input2, machine.Pin.OUT)
        self.p3 = machine.Pin(pin_input3, machine.Pin.OUT)
        self.p4 = machine.Pin(pin_input4, machine.Pin.OUT)

        self.p_left = machine.Pin(pin_enable_a)
        self.p_right = machine.Pin(pin_enable_b)

        self.pwm_left = machine.PWM(self.p_left)
        self.pwm_left.freq(500)

        self.pwm_right = machine.PWM(self.p_right)
        self.pwm_right.freq(500)

    def setPins(self, value1, value2, value3, value4, speed=DEFAULT_SPEED):
        self.p1.value(value1)
        self.p2.value(value2)
        self.p3.value(value3)
        self.p4.value(value4)

        self.pwm_left.duty(speed)
        self.pwm_right.duty(speed)

    """
    IN1	IN2	IN3	IN4	Direction
    0	0	0	0	Stop
    1	0	1	0	Forward
    0	1	0	1	Reverse
    1	0	0	1	Left
    0	1	1	0	Right
    """

    def forward(self, speed=DEFAULT_SPEED):
        self.setPins(1, 0, 1, 0, speed)

    def backward(self, speed=DEFAULT_SPEED):
        self.setPins(0, 1, 0, 1, speed)

    def left(self, speed=DEFAULT_SPEED):
        self.setPins(1, 0, 0, 1, speed)

    def right(self, speed=DEFAULT_SPEED):
        self.setPins(0, 1, 1, 0, speed)

    def stop(self, speed=0):
        self.setPins(0, 0, 0, 0, 0)

    def run_str_action(self, str_action, speed=DEFAULT_SPEED):
        def action_not_found():
            print('No Function ' + action + ' Found!')

        action = getattr(self, str_action, action_not_found)
        action(speed)

        self.last_action_str = str_action + ' ' + str(round(speed / 100)) + 'km/h'
        print(self.last_action_str)

    def run(self, engine_params):
        self.run_str_action(engine_params.action, engine_params.speed)
        # print(engine_params)

    """
    Accepts dict of timed actions, for example:
         
    """

    def route(self, timed_actions):
        for action_str, seconds in timed_actions.items():
            # print(action_str + ' - ' + str(seconds) + 'sec')
            self.run_str_action(action_str)
            time.sleep(seconds)
