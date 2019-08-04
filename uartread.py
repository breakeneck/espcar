import machine
import time


uart = machine.UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters


adc = machine.ADC(0)

inc = 0
while True:
    try:
        # value_y = adc.read()
        value_x = uart.readline()

        print('x = ' + value_x)# + 'y = ' + value_y)
    except:
        print('cant read'  + str(inc))

    inc = inc + 1
    time.sleep_ms(500)

