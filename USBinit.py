# -*- coding: utf-8 -*-
import serial.tools.list_ports

class usbInit():
    ''' 
    Connect the module through UART
    '''
    def __init__(self):
        ports = serial.tools.list_ports.comports()
        self.SerialPort=ports[-1][0]
        if(len(ports)==0):
            print("Please Connect the module to USB Cable\n")
            while(len(ports)==0):
                ports = serial.tools.list_ports.comports()
        for port,desc, hwid in ports:
            try:
                self.serial=serial.Serial(port, 115200, timeout=1)
                if(not(self.serial.open())):
                    continue
                response=self.requestManufacturerId()
                print(port)
                print(response)
                if "Quectel" in str(response):
                    self.SerialPort=port
                    break
                else:
                    continue
            except:
                continue   
        self.serial=serial.Serial(self.SerialPort, 115200, timeout=5)   
        print("USB communication initialized ! ")

    def readData(self):
        return self.serial.readline().decode("utf-8") 

    def closePort(self):
        self.serial.close()
        print("\nUSB communication closed !")

    def get(self):
        return self.serial
