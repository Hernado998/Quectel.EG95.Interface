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
