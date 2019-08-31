import net
from control import Control

wlan = net.connect_wifi(net.host, net.gateway) # static IP
print('connected')
listenSocket = net.listen()
print('Listening socket')

ctrl = Control()

while True:
    print('Accepting connections...')
    connection, addr = listenSocket.accept()
    print('Client connected', addr)

    while True:
        response = net.receive_command(connection)
        print(response)
        ctrl.load_str(response)
        print(ctrl.x, ctrl.y)
        # print(response)

        if not response:
            connection.close()
            break