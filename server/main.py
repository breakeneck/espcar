import net
from control import Control
from car import Car

wlan = net.connect_wifi(net.host, net.gateway)  # static IP
print('connected')
listenSocket = net.listen()
print('Listening socket')

"""
PIN   1, 2, 3, 4, L, R
GPIO  5, 4, 0, 2, 12,14
"""
PIN_INPUT1 = 13  # orange
PIN_INPUT2 = 12  # yellow
PIN_INPUT3 = 14  # green
PIN_INPUT4 = 27  # blue
PIN_ENABLE_A = 26  # white
PIN_ENABLE_B = 25  # black

ctrl = Control()
car = Car(PIN_INPUT1, PIN_INPUT2, PIN_INPUT3, PIN_INPUT4, PIN_ENABLE_A, PIN_ENABLE_B)

# car.route({'forward': 1, 'backward': 1, 'left': 1, 'right': 1})


while True:
    print('Accepting connections...')
    connection, addr = listenSocket.accept()

    print('Client connected', addr)
    car.route({'backward': 0.1, 'stop': 1})
    car.route({'backward': 0.1, 'stop': 1})

    while True:
        response = net.receive_command(connection)

        if not response:
            connection.close()
            break

        engine_params = ctrl.load_str(response)

        car.run(engine_params)

        # print(response)
        # print(ctrl.x, ctrl.y)
        # print(response)
