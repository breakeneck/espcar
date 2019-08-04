import machine
import time

import control
from control import Control
from car import Car

# from machine import UART
#
# uart = UART(1, 9600)                         # init with given baudrate
# uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters


adc = machine.ADC(0)

# control = Control()
# car = Car()

# car.route({car.FORWARD: 2, car.BACKWARD: 2, car.LEFT: 2, car.RIGHT: 2, car.STOP: 0})

while True:
    value_y = adc.read()

    print('x = ' + value_x + 'y = ' + value_y)
    # control.read_action(value_y)
    #
    # if (prev_action == control)
    # print(control.to_string())
    #
    # prev_action = control.action

    # car.run(control)
    # print(car.last_action_str)

    time.sleep_ms(100)
