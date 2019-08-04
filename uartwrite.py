import machine
print("hello world")

adc = machine.ADC(0)


uart = machine.UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters


value_x = adc.read()
uart.write('hello\r\n')
