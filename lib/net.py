import network
import socket
import time

BYTES = 16 # bytes to read for one time

ssid = "Vrindavan"
password = "harekrishna"
host = '192.168.2.222'
gateway = '192.168.2.1'

# ssid = 'WifiCar'
# password = 'harekrishna'
# host = '192.168.84.1'
# gateway = '192.168.84.1'

port = 10000

def create_wifi_ap(ssid, password):
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password)
    wlan.ifconfig((host, '255.255.255.0', host, host)) # ip, netmask, gateway, dns
    print(wlan.ifconfig())
    return wlan


def connect_wifi(static_ip = False, gateway = False):
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    if static_ip:
        wlan.ifconfig((static_ip, '255.255.255.0', gateway, gateway)) # add static IP
    wlan.connect(ssid, password)  # connect wifi
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

def accept_conections():
    listenSocket = socket.socket()  # create socket
    listenSocket.bind((host, port))  # bind ip and port
    listenSocket.listen(1)  # listen message
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('accepting.....')

    return listenSocket

def connect_host():
    writeSocket = socket.socket()  # create socket
    writeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set the value of the given socket option
    writeSocket.connect((host, port))  # send require for connect

    print('connected ' + host + ':' + str(port))
    writeSocket.send("hello DFRobot,I am TCP Client")  # send data
    print('Sent message to ' + host)

    return writeSocket




# def send_request(socket, host, port):
#     client = socket.socket()  # create socket
#     client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set the value of the given socket option
#     client.connect((host, port))  # send require for connect
#     print('connected ' + host + ':' + str(port))
#
#     client.send("hello DFRobot,I am TCP Client")  # send data
#     data = client.recv(1024)
#     print(data)
#
#     client.close()
#
# def receive_request(socket):
#     client, addr = socket.accept()
#     data = client.recv()
#     print(data)
#
#     client.send('OK')
#     client.close()


def listen():
    listenSocket = socket.socket()            #create socket
    listenSocket.bind((host, port))              #bind ip and port
    listenSocket.listen(1)                    #listen message
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #Set the value of the given socket option
    return listenSocket


def receive_command_per_socket(listenSocket):
    try:
        connection,addr = listenSocket.accept()
        data = connection.recv(1024)                #Receive 1024 byte of data from the socket
        # print('received ' + data + ' from ' + addr)
        connection.send('OK')                 #send data
        connection.close()
    except Exception as e:
        if (connection):
            connection.close()
            print('closed because ' + type(e).__name__)

    if (data):
        return data
    else:
        return 'NOOP'

def send_command_per_socket(request):
    sendSocket = socket.socket()                                   #create socket
    sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#Set the value of the given socket option
    sendSocket.connect((host, port))                                #send require for connect
    sendSocket.send(request)
    response = sendSocket.recv(1024)
    sendSocket.close()

    return response

def receive_command(connection):
    try:
        # connection,addr = listenSocket.accept()
        data = connection.recv(BYTES).decode('utf-8')                #Receive 1024 byte of data from the socket
        # print('received ' + data + ' from ' + addr)
        connection.send('OK')                 #send data

        if (str(data) == 'END'):
            print('End of program received')
            return False
    except Exception as e:
        print('closed because ' + type(e).__name__)
        return False

    if (data):
        return data
    else:
        return 'NOOP'


def connect_socket():
    try:
        sendSocket = socket.socket()                                   #create socket
        sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#Set the value of the given socket option
        sendSocket.connect((host, port))                                #send require for connect
        return sendSocket

    except Exception as e:
        if sendSocket:
            sendSocket.close()
        print('closed because ' + type(e).__name__)
        return False


def send_command(sendSocket, command):
    try:
        print('Sended ' + command)
        sendSocket.send(command)
        response = sendSocket.recv(BYTES)
        if len(response) == 0:
            return False
        # sendSocket.close()
    except Exception as e:
        print('closed because ' + type(e).__name__)
        return False

    return response
