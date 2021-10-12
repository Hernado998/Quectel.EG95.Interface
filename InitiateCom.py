import serial 
import time

class InitiateCom:
    def __init__(self,serialPort):
        self.serialPort= serialPort

    def setSerialPort(self, port):
        self.serialPort= port

    def connectQuectelEG95(self):
        self.ser = serial.Serial(self.serialPort, 460800, timeout=5)
        time.sleep(1)

    def sendATCommand(self,command):
        self.ser.write(command)
        time.sleep(1)

    def readData(self):
        data=self.ser.readline()
        print(data)
        return data

    def disconnectQuectelEG95(self):
        self.ser.close()

