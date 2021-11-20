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


class QuectelEG9x:

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
        print("Instanciation of Object : Done")
        
    '''
    Get SMS mode Status
    Default to TXT
    '''       
    def GetSMSMode(self):
        Response=self.sendATCommand(GET_SMS_MODE)
        return Response  
    '''
    Set SMS mode Status
    Default to TXT 
    @args : the attached mode 
    '''       
    def SetSMSMode(self,args="1"):
        Response=self.sendATCommand(SET_SMS_MODE,args)
        return Response         
    '''
    Set SMS TE default Char
    GSM 7 bit default alphabet
    @args : the attached mode 
    '''       
    def SetSMSChar(self,args='"GSM"'):
        Response=self.sendATCommand(SET_SMS_CHAR,args)
        return Response  


    '''
    Send SMS Message
    @args : the attached mode 
    '''       
    def SendSMS(self):
        mode=1
        if "PDU" in str(self.GetSMSMode()):
            mode=0
        if(mode):
            number='"'+str(input("Enter Number\n"))+'"'
            print(number)
            self.sendATCommand(SEND_SMS_NUMBER,number)
            message_text=input("Enter Message\n")
            self.sendATCommand(NOTHING,message_text)
            time.sleep(0.5)
            Response=self.sendATCommand(NOTHING,chr(26))
            return Response
        else:
            length=input("Enter Length\n")
            self.sendATCommand(SEND_SMS_NUMBER,length)
            try:
                message_Hex=input("Enter Hex Message\n")
                is_hex=int(message_Hex, 16)
                Response=self.sendATCommand(SEND_SMS_NUMBER,message_Hex)
                return Response
            except:
                print("Message should be HEX\n")
                return "ERROR\n"
            
    '''
    Get SMS Message Storage Area
    '''
    def GET_SMS_STORAGE_AREA(self):
        Response=self.sendATCommand(GET_SMS_STORAGE_AREA)
        return  Response
    '''
    Set SMS Message Storage Area
    @args : the attached Storage Area
    Default to SM : SIM CARD STORAGE 
    '''
    def SET_SMS_STORAGE_AREA(self,args="“SM”,“SM”,“SM”"):
        Response=self.sendATCommand(SET_SMS_STORAGE_AREA,args)
        return Response
    '''
    Read SMS Message LIST
    @args : the attached Storage Area
    Default : list ALL message in text mode 
    '''
    def READ_LIST_MESSAGE(self,args='"ALL"'):
        mode=self.GetSMSMode()
        if("PDU" in str(mode)):
            mode=0
        else:
            mode=1
        Response=self.sendATCommand(READ_SMS_LIST,args)
        return Response

    '''
    Delete SMS 
    @args : the attached Storage Area
    Default : SM
    '''   
    def DELETE_SMS(self,args="1,4"):
        Response=self.sendATCommand(DELETE_SMS,args)
    '''
    SMS EVENT REPORTING CONFIGURATION
    @args : the attached Storage Area
    Default : 1,2,0,1,0
    '''    
    def SMS_Event_Reporting_Conf(self,args="1,2,0,1,0"):
        self.SetSMSMode("1")
        self.SetSMSChar('"GSM"')
        Response=self.sendATCommand(SMS_EVT_RP_CONF,args)
