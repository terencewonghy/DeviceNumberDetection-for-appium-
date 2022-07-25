import os
import random



port_list = []
number_of_devices = ''
d_name = ''
port = ''
i = 0

def getNoOfDevice():
    global d_name
    os.system("cd C:\\Users\\username\\Desktop\\platform-tools")
    d_name = os.popen("adb devices").read()
    d_name = d_name.split('\n', 1)[-1]
    d_name = d_name.split()
    d_name = [x for x in d_name if x != 'device']

    #count number of devices
    global number_of_devices
    number_of_devices = len(d_name)
    return number_of_devices, d_name

def assignPort():

    global port
    port = random.randint(4700, 4900)
    port_list.append(port)
    return port, port_list

def check_port(port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    if result == 0:
        return True
    else:
        os.system("start cmd.exe /c appium --address localhost --port " + str(port))
        return False


def initiateServer():
    os.system("start cmd.exe /c appium --address localhost --port " + str(port))


getNoOfDevice(())
while i< number_of_devices:
    assignPort
    check_port(port)
    i += 1

