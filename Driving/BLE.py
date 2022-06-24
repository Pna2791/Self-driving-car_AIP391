import bluetooth
import time


class Car_BLE:
    available = False

    def __init__(self, name, port=1, address=None):
        if address is None:
            for add in bluetooth.discover_devices():
                if name == bluetooth.lookup_name(add):
                    address = add
                    break
        if address is not None:
            print('Found', address)
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((address, port))
            self.available = True
            print('Connected')
        else:
            print('Cannot found')

    def send(self, msg):
        if self.available:
            self.sock.send(msg + '\n')
        else:
            print('BLE not available')

    def close(self):
        if self.available:
            self.sock.close()
            self.available = False
        else:
            print('BLE not available')

    def action(self, act):
        if act == 0:
            self.sock.send('A-2\n')
        elif act == 1:
            self.sock.send('A0\n')
        elif act == 2:
            self.sock.send('A2\n')

    def speed(self, spd):
        if self.available:
            self.sock.send('S' + str(spd) + '\n')
            time.sleep(0.1)
        else:
            print('BLE not available')

    def delta(self, dlt):
        if self.available:
            self.sock.send('S' + str(dlt) + '\n')
            time.sleep(0.1)
        else:
            print('BLE not available')

    def pause(self):
        if self.available:
            self.sock.send('P\n')
        else:
            print('BLE not available')
