import sys
import glob
import serial
import time
import random
import io


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



def check_port():
    pass


def package_data(data):
    data_package = 's '
    for i in data:
        data_package = data_package + str(i) + ' '

    data_package = data_package + 'e'
    return data_package


def getValues(port, sig):
    if sig == '0':
        port.write(b'123 123 123\n')
    elif sig == '1':
        port.write(b'12')
    elif sig == '2':
        port.write(b's')
    elif sig == '3':
        port.write(b'e')
    guess_data = port.readline().decode('ascii')
    return guess_data


def translate_and_send_data(data_string, port):
    sub_data = data_string.split(' ')
    for i in sub_data:
        for j in i:
            if j == '0':
                port.write(b'0')
                print(0)
            elif j == '1':
                port.write(b'1')
                print(1)
            elif j == '2':
                port.write(b'2')
                print(2)
            elif j == '3':
                port.write(b'3')
                print(3)
            elif j == '4':
                port.write(b'4')
                print(4)
            elif j == '5':
                port.write(b'5')
                print(5)
            elif j == '6':
                port.write(b'6')
                print(6)
            elif j == '7':
                port.write(b'7')
                print(7)
            elif j == '8':
                port.write(b'8')
                print(8)
            elif j == '9':
                port.write(b'9')
                print(9)
            elif j == '\n':
                port.write(b'\n')
                print('end')
    # port.write(unicode(data_string))
    # port.flush()
    guess_data = port.readline().decode('ascii')
    return guess_data


def send_package_data(package):
    pass


def encode_data(raw_data):
    data_package = str(raw_data[0]) + " " + str(raw_data[1]) + "\n"
    return data_package





