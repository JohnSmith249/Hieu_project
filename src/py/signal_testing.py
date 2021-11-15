import serial
import time
import data_accessing as da

available_ports = da.serial_ports()
online_flag = 0

try:
    port_connection = serial.Serial(available_ports[0], 9600, timeout=1)
    time.sleep(4)
    print('Connection establish at ' + str(available_ports[0]) + ' !!!')
    online_flag = 1
except:
    print('No Connection !!!')


if online_flag == 1:
    while(1):
        answer = input('get data ? ')
        if answer == 'y':
            port_connection.write(bytes('start\n', 'ascii'))
            Confirmation_sig = port_connection.readline().decode('ascii').replace('\r\n', "")
            print(Confirmation_sig)
            port_connection.write(bytes('123 123 123\n', 'ascii'))
            Confirmation_sig = port_connection.readline().decode('ascii').replace('\r\n', "")
            print(Confirmation_sig)
            port_connection.write(bytes('end\n', 'ascii'))
            Confirmation_sig = port_connection.readline().decode('ascii').replace('\r\n', "")
            print(Confirmation_sig)
            # if Confirmation_sig == '1':
            #     print('Package received !!!')
            # else:
            #     print('Package lost !!!')
        elif answer == 'n':
            print('Quitting !!!')
            break