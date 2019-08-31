# SERVER

import net
from control import Control

wlan = net.connect_wifi(net.host, net.gateway) # static IP
print('connected')
listenSocket = net.listen()
print('Listening socket')

control = Control()

while True:
    print('Accepting connections...')
    connection, addr = listenSocket.accept()
    print('Client connected', addr)

    while True:
        response = net.receive_command(connection)
        control.load(response)
        print(control.y_to_string(), control.x_to_string())
        # print(response)

        if not response:
            connection.close()
            break

# CLIENT
import net
import joy

wlan = net.connect_wifi()
counter = 0

while True:
    print('Awaiting connection to socket')
    connection = net.connect_socket()
    if not connection:
        continue

    print('Socket connected, awaiting commands')

    while True:
        joy.read()
        response = net.send_command(connection, joy.control.output())
        if not response:
            print('No response or socket error')
            break

        print(response)
        counter += 1


# JOY
from machine import Pin, ADC
from time import sleep
from control import Control

# ESP32 pinouts
PIN_X = 35 # blue
PIN_Y = 34 # violet
PIN_SW = 22 # green

dx = ADC(Pin(PIN_X))
dx.atten(ADC.ATTN_11DB)
dx.width(ADC.WIDTH_10BIT)

dy = ADC(Pin(PIN_Y))
dy.atten(ADC.ATTN_11DB)
dy.width(ADC.WIDTH_10BIT)

sw = Pin(PIN_SW, Pin.IN, Pin.PULL_UP)

control = Control()

def read():
    value_x = dx.read()
    value_y = dy.read()
    # sw_value = not sw.value()

    control.read(value_x, value_y)
    print(control.output())





# SERVER TESTING




    # command = net.receive_command(listenSocket)
    # print(command)


"""
SSID = "Vrindavan"
PASSWORD = "harekrishna"
host = '192.168.2.222'
ap_ssid = 'WifiCar'
ap_password = 'harekrishna'
ap_ip = '192.168.84.1'
port = 10000

wlan = None
listenSocket = None


def createWifiAP(ssid, password, ip):
    global wlan
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password)
    wlan.ifconfig((ip, '255.255.255.0', ip, ip)) # ip, netmask, gateway, dns
    print(wlan.ifconfig())

def connectWifi(ssid, passwd):
    global wlan
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    wlan.ifconfig((host, '255.255.255.0', '192.168.2.1', '192.168.2.1'))
    wlan.connect(ssid, passwd)  # connect wifi
    while wlan.ifconfig()[0] == '0.0.0.0':
        time.sleep(1)
    print(wlan.ifconfig())
    return True

# clients = []


def receive_data(client):
    data = client.recv(1024)  # Receive 1024 byte of data from the socket

    if (len(data) == 0):
        client.close()
        print('Received 0 bytes')
        return False

    print(data)
    ret = client.send('ACK')
    return True

def accept_conections():
    global  listenSocket
    listenSocket = socket.socket()  # create socket
    listenSocket.bind((host, port))  # bind ip and port
    listenSocket.listen(1)  # listen message
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('accepting.....')


"""


# while True:
#     client, addr = listenSocket.accept()
#     if addr:
#         print(addr, 'connected')
#
#     while True:
#         try:
#             data = client.recv(1024)  # Receive 1024 byte of data from the socket
#             print(data)
#             client.send('ACK')
#
#         except  Exception as e:
#             print(type(e).__name__)

    # wlan.disconnect()
    # wlan.active(False)



            # if (len(data) == 0):
            #     # client.close()
            #     print('Received 0 bytes')
            #     continue
