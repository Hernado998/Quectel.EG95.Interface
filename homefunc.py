import serial 
import time
from InitiateCom import InitiateCom


serialPort = "/dev/ttyUSB0"
class QuectelEG95Home:
    def __init__(self):
        self.initiate=InitiateCom(serialPort)
        self.initiate.connectQuectelEG95()
    def requestManufacturerId(self):
        command = 'AT+CGMI'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def deviceModule(self):
        command = 'AT+CGMM'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def firmwareVersion(self):
        command = 'AT+GMM'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def networkRegistration(self):
        command = 'AT+CREG?'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def grpsNetworkStatus(self,attachmode):
        command = 'AT+QCFG="gprsattach"[,'+str(attachmode)+']'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def preferredOperator(self):
        command = 'AT+CPOL'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def simCardIMSI(self):
        command = 'AT+CIMI'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()
    def simCardICCID(self):
        command = 'AT+QCCID'+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()



        
