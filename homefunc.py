"""
    eg9x class definition
    EG9X class to control and manage the EG9x module 
    telecommunications Engineering Students @ SUPCOM [ HIGHER SCHOOL OF COMMUNICATIONS OF TUNIS]
    date: 12/10/2021
"""
from atcommand import *
import serial.tools.list_ports
import time


class eg9x:

    ''' 
    Connect the module through UART
    '''
    def __init__(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            ser=serial.Serial(port, 460800, timeout=5)
            if(ser.is_open):
                self.SerialPort=port
                break    
        self.serial=serial.Serial(self.SerialPort, 460800, timeout=0.3)
        
    '''
    Disconnect the module
    '''
    def disconnectQuectelEG95(self):
        self.serial.close()
        
        
    ''' 
    Check for the response from the Module
    @data : the returned data from the module
    '''
    def checkResponse(self,data):
        Status=""
        if(len(data)==0):
            Status="ERROR"
            return Status
        for character in range(len(data)):
            start=time.time()
            if data[character]=="O" and data[character+1]=="K":
                Status=data
                break

        return Status

    ''' 
    Send At Commands to the Module
    @command : the AT Command to Send
    @args    : Arguments if needed for the At Command
    '''
    def sendATCommand(self,command,args=None):
        command=AT_COMMANDS(command)
        to_send=""                          # Command to send
        if (len(command.get_string)!=0):
            to_send+=command.get_string()
        if(len(args)!=0):
            to_send+=args
        ser=self.serial                     
        ser.write(to_send)                  # Send the Command
        results=ser.readlines()
        status=self.checkResponse(results)
        if(status):
            return results
        return status
    '''
    Get Manufacturer ID of the module
    '''
    def requestManufacturerId(self):
        Response= self.sendATCommand(MANIFACTURE_ID)
        return Response
    '''
    Get Device ID of the module
    '''
    def deviceModule(self):
        Response= self.sendATCommand(DEVICE_ID)
        return Response
    '''
    Get firmeware of the module
    '''
    def firmwareVersion(self):
        Response=self.sendATCommand(FIRMWARE_VS)
        return Response
    
    '''
    Get Network Registration 
    '''   
    def networkRegistration(self,args="=?"):
        Response=self.sendATCommand(REGISTRED_DEVICE_STATUS,args)
        return Response
    '''
    Get GPRS Status 
    @args : the attached mode 
    '''       
    def grpsNetworkStatus(self,args="=gprsattach"):
        Response=self.sendATCommand(EXTENDED_CONF_SET,args)
        return Response
    '''
    Get list of Preferred Operators
    @args : test / read / write , default to Read
    '''    
    def preferredOperator(self,args="=?"):
        Response=self.sendATCommand(PREFERED_OPERATORS_LIST,args)
        return Response
    '''
    Get Request International Mobile Subscriber Identity (IMSI)
    '''     
    def simCardIMSI(self):
        Response=self.sendATCommand(SIM_CARD_IMSI)
        return Response
    '''
    Get Integrated Circuit Card Identifier
    '''         
    def simCardICCID(self):
        Response=self.sendATCommand(SIM_CARD_ICCID)
        return Response
