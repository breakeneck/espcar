import net
from control import Control

# ESP32 pinouts
PIN_X = 35  # blue
PIN_Y = 34  # violet
PIN_SW = 32  # green

wlan = net.connect_wifi()

ctrl = Control()
ctrl.setup_joy(PIN_X, PIN_Y, PIN_SW)

counter = 0

while True:
    print('Awaiting connection to socket')
    connection = net.connect_socket()
    if not connection:
        continue

    print('Socket connected, awaiting commands')

    while True:
        ctrl.read_joy()

        # print("Seding on server " + str(ctrl))
        response = net.send_command(connection, str(ctrl))
        if not response:
            print('No response or socket error')
            break

        print(response)
