from machine import Pin, ADC
from time import sleep

dx = ADC(Pin(35))
dx.atten(ADC.ATTN_11DB)
dx.width(ADC.WIDTH_10BIT)

dy = ADC(Pin(34))
dy.atten(ADC.ATTN_11DB)
dy.width(ADC.WIDTH_10BIT)

sw = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
  x_value = dx.read()
  y_value = dy.read()
  sw_value = not sw.value()

  print(x_value, y_value, sw_value)

  sleep(0.1)
