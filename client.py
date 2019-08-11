import machine
import net

button = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

wlan = net.connect_wifi()
# response = net.send_command('Yohoho')
counter = 0

while True:
    print('Awaiting connection to socket')
    connection = net.connect_socket()
    if not connection:
        continue

    print('Socket connected, awaiting commands')

    while True:
        response = net.send_command(connection, 'Button Click ' + str(counter))
        if not response:
            print('No response or socket error')
            break

        print(response)
        counter += 1
        # try:
        #     if net.read_click(button):
        #         response = net.send_command(connection, 'Button Click')
        #         print(response)
        #     else:
        #         respone = net.send_command(connection, 'NoOperation')
        #         print(response)
        # except:
        #     connection.close()
