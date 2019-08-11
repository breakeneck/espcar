from machine import Pin, ADC
from time import sleep
from control import Control

# ESP32 pinouts
PIN_X = 35 # blue
PIN_Y = 34 # violet
PIN_SW = 22 # green

dx = ADC(Pin(PIN_X))
dx.atten(ADC.ATTN_11DB)
dx.width(ADC.WIDTH_10BIT)

dy = ADC(Pin(PIN_Y))
dy.atten(ADC.ATTN_11DB)
dy.width(ADC.WIDTH_10BIT)

sw = Pin(PIN_SW, Pin.IN, Pin.PULL_UP)

control = Control()

def read():
    value_x = dx.read()
    value_y = dy.read()
    # sw_value = not sw.value()

    control.decrypt(value_x, value_y)



while True:
    read()
    print(control.y_to_string(), control.x_to_string())

    sleep(0.1)
