import network
import socket
import time
import machine

SSID = "Vrindavan"
PASSWORD = "harekrishna"
host = "192.168.2.194"
port = 10000
wlan = None
s = None


def connectWifi(ssid, passwd):
    global wlan
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    wlan.connect(ssid, passwd)  # connect wifi
    while (wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return True


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


button = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

# while True:
#     if (read_click(button)):
#         print('clicked')

# """
# Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
    connectWifi(SSID, PASSWORD)
    ip = wlan.ifconfig()[0]  # get ip addr

    s = socket.socket()  # create socket
    s.setblocking(0)
    s.settimeout(3)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set the value of the given socket option
    s.connect((host, port))  # send require for connect
    s.send("hello DFRobot,I am TCP Client")  # send data

    while True:
        data = s.recv(1024)                               #Receive 1024 byte of data from the socket
        if(len(data) == 0):                               #if there is no data,close
          print("close socket")
          s.close()
          break
        print(data)
        if (read_click(button)):
            ret = s.send('Clicked')
except:
    if (s):
        s.close()
    wlan.disconnect()
    wlan.active(False)
# """
