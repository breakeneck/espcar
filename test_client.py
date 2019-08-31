from control import Control

# ESP32 pinouts
PIN_X = 35 # blue
PIN_Y = 34 # violet
PIN_SW = 22 # green

ctrl = Control()
ctrl.setup_joy(PIN_X, PIN_Y, PIN_SW)

while True:
    ctrl.read_joy()
    print(ctrl)
