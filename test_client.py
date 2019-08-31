from control import Control

# ESP32 pinouts
PIN_X = 35 # blue
PIN_Y = 34 # violet
PIN_SW = 32 # green

ctrl = Control()
ctrl.setup_joy(PIN_X, PIN_Y, PIN_SW)

while True:
    ctrl.read_joy()
    print(ctrl.x, ctrl.y, ctrl.is_click)
