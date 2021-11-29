# -*- coding: utf-8 -*-
"""
    eg9x class definition to control and manage the EG9x module 
    Authors : Iheb Omar Soula and Nadir Hermassi
    telecommunications Engineering Students @ SUPCOM [ HIGHER SCHOOL OF COMMUNICATIONS OF TUNIS]
    Project in Sup'Com with Comelit R&D company
    date: 12/10/2021
"""
#from EG9x.atcommand import *
from atcommand import *
import serial.tools.list_ports
import time


class QuectelEG95:
    
    def __init__(self,serial):
        self.serial=serial    

    ''' 
    Check for the response from the Module
    @data : the returned data from the module
    '''
    def checkResponse(self,data):
        Status=bytes("", 'utf-8')
        if(len(data)==0):
            Status=bytes("ERROR", 'utf-8')
            return Status
        
        for string in data:
            for character in range(len(str(string))-1):
                ch=str(string)
                if ch[character]=="O" and ch[character+1]=="K":
                    for byte in data:
                        Status+=byte
                    break
        return Status

    ''' 
    Send At Commands to the Module
    @command : the AT Command to Send
    @args    : Arguments if needed for the At Command
    '''
    def sendATCommand(self,command,args=""):
        to_send=""                          # Command to send
        if (len(command.string)!=0):
            to_send+=command.string
        if(len(args)!=0):
            to_send=to_send[:-2]+args+str('\r\n')
        ser=self.serial  
        time.sleep(2)             
        ser.write(bytes(to_send, 'utf-8'))                  # Send the Command
        results=ser.readlines()  
        status=self.checkResponse(results)
        return status.decode("utf-8")

    '''
    Set phone functionality
    '''
    def setPhoneFunctionality(self,args):
        Response= self.sendATCommand(SET_PHONE_FUNCTIONALITY,args)
        return Response
    '''
    Signal Quality Report
    '''
    def siggnalQualityReportAndQuery(self,args):
        Response= self.sendATCommand(SIGNAL_QUALITY_REPORT_AND_QUERY,args)
        return Response
    '''
    Operator selection
    '''
    def operatorSelection(self,args):
        Response= self.sendATCommand(OPERATOR_SELECTION,args)
        return Response
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
    Configure parameters to TCP/IP context
    '''
    def configureParamTcpIPContext(self,args):
        Response=self.sendATCommand(CONFIGURE_PARAMETERS_TCP_IP_CONTEXT,args)
        return Response
    '''
    Activate PDP context
    '''
    def activatePdpContext(self,args):
        Response=self.sendATCommand(ACTIVATE_PDP_CONTEXT,args)
        return Response
    '''
    Desactivate PDP context
    '''
    def desactivatePdpContext(self,args):
        Response=self.sendATCommand(DESACTIVATE_PDP_CONTEXT,args)
        return Response
    '''
    Open socket service 
    '''
    def openSocketService(self,args):
        Response=self.sendATCommand(OPEN_SOCKET_SERVICE,args)
        return Response
    '''
    Close socket service 
    '''
    def closeSocketService(self,args):
        Response=self.sendATCommand(CLOSE_SOCKET_SERVICE,args)
        return Response
    '''
    Ping
    '''
    def ping(self,args):
        Response=self.sendATCommand(PING,args)
        return Response
    '''
    Query socket service status
    '''
    def socketServiceStatus(self,args):
        Response=self.sendATCommand(QUERY_SOCKET_SERVICE_STATUS,args)
        return Response
    '''
    Define PDP context, this function will let the module to connect to the internet
    '''
    def definePDPConntext(self,args):
        Response=self.sendATCommand(DEFINE_PDP_CONTEXT,args)
        return Response
    '''
    Get Network Registration 
    '''   
    def networkRegistration(self,args="?"):
        Response=self.sendATCommand(REGISTRED_DEVICE_STATUS,args)
        return Response
    '''
    Get Extended functions
    default to get GPRS Status 
    @args : the attached mode 
    '''       
    def grpsNetworkStatus(self,args="=gprsattach"):
        Response=self.sendATCommand(EXTENDED_CONF_SET,args)
        return Response
    '''
    Get list of Preferred Operators
    @args : test / read / write , default to Read
    '''    
    def preferredOperator(self,args="?"):
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

        
