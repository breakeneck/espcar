import machine
import net


button = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

try:
    wlan = net.connect_wifi(net.local_ssid, net.local_password, net.local_host)
    writeSocket = net.connect_host(net.local_host, net.port)

    while True:
        if net.read_click(button):
            writeSocket.send('Button pressed')

except Exception as e:
    print(e)
    # print("Oops!",sys.exc_info()[0],"occured.")

    # if (writeSocket):
    #     writeSocket.close()

    # wlan.disconnect()
    # wlan.active(False)

"""
import network
import socket
import time
import machine
# import sys

SSID = "Vrindavan"
PASSWORD = "harekrishna"
host = "192.168.2.222"
port = 10000

wlan = None
writeSocket = None
button = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)


def connectWifi(ssid, passwd):
    global wlan
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    wlan.connect(ssid, passwd)  # connect wifi
    while (wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return True
    print(wlan.ifconfig())


def clickRead():
    global button
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('button pressed')
        return True
    elif not first and second:
        print('Button released!')
        return False

    return False

# Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
    connectWifi(SSID, PASSWORD)
    connectToServer(host, port)

    while True:

        if clickRead():
            writeSocket.send('Button pressed')


        # data = writeSocket.recv(1024)  # Receive 1024 byte of data from the socket
        # if (len(data) == 0):  # if there is no data,close
        #     print("close socket")
        #     writeSocket.close()
        #     break
        # print(data)

            # print('Button pressed!')
        # elif not first and second:
        #     print('Button released!')
        # if not button.value():
        #     print('Button pressed!')
        #     writeSocket.send('Button pressed')  # send data

        # data = listenSocket.recv(1024)  # Receive 1024 byte of data from the socket
        # if (len(data) == 0):  # if there is no data,close
        #     print("close socket")
        #     listenSocket.close()
        #     break
        #
        # print(data)
except  Exception as e:
    print(e)
    # print("Oops!",sys.exc_info()[0],"occured.")

    if (writeSocket):
        writeSocket.close()

    wlan.disconnect()
    wlan.active(False)
"""
