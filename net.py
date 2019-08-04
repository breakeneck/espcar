import network
import socket
import time

# ssid = "Vrindavan"
# password = "harekrishna"
# host = '192.168.2.222'

ssid = 'WifiCar'
password = 'harekrishna'
host = '192.168.84.1'

port = 10000

def create_wifi_ap(ssid, password, ip):
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password)
    wlan.ifconfig((ip, '255.255.255.0', ip, ip)) # ip, netmask, gateway, dns
    print(wlan.ifconfig())
    return wlan

def connect_wifi(ssid, passwd, host):
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    wlan.ifconfig((host, '255.255.255.0', '192.168.2.1', '192.168.2.1'))
    wlan.connect(ssid, passwd)  # connect wifi
    while wlan.ifconfig()[0] == '0.0.0.0':
        time.sleep(1)
    print(wlan.ifconfig())
    return wlan


def receive_data(client):
    data = client.recv(1024)  # Receive 1024 byte of data from the socket

    if (len(data) == 0):
        client.close()
        print('Received 0 bytes')
        return False

    print(data)
    ret = client.send('ACK')
    return True

def accept_conections(host, port):
    listenSocket = socket.socket()  # create socket
    listenSocket.bind((host, port))  # bind ip and port
    listenSocket.listen(1)  # listen message
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('accepting.....')

    return listenSocket

def connect_host(host, port):
    writeSocket = socket.socket()  # create socket
    writeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set the value of the given socket option
    writeSocket.connect((host, port))  # send require for connect

    print('connected ' + host + ':' + str(port))
    writeSocket.send("hello DFRobot,I am TCP Client")  # send data
    print('Sent message to ' + host)

    return writeSocket


def read_click(button):
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
