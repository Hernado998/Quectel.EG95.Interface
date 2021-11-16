from atcommand import *
import serial.tools.list_ports
import time


class QuectelEG95SMS:
    ''' 
    Connect the module through UART
    '''
    def __init__(self, SMSHistory):
        self.SMSHistory = SMSHistory
        self.SMSHistory= {}
        ports = ["/dev/ttyACM0"]
        print(ports)
        if(len(ports)==0):
            
            print("Please Connect the module to USB Cable\n")
            while(len(ports)==0):
                ports = serial.tools.list_ports.comports()
                
        for port in ports:
            ser=serial.Serial(port, 115200, timeout=5)
            if(ser.is_open):
                self.SerialPort=port
                break    
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
    def SetSMSChar(self,args="GSM"):
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
            number=input("Enter Number\n")
            self.sendATCommand(SEND_SMS_NUMBER,number)
            message_text=input("Enter Message\n")
            Response=self.sendATCommand(SEND_SMS_NUMBER,message_text)
            self.SMSHistory.update({number+" :"+Response:message_text})
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
    def READ_LIST_MESSAGE(self,args="ALL"):
        mode=self.GetSMSMode()
        print(mode)
        if("PDU" in str(mode)):
            mode=0
        else:
            mode=1
        if((args in ["ALL","REC UNREAD","REC READ","STO UNSENT","STO SENT"]) and mode): #READ MESSAGE TEXT
            Response=self.sendATCommand(READ_SMS_LIST,args)
        elif((args in ["0","1","2","3","4"]) and not(mode)):                              #READ MESSAGE PDU
            Response=self.sendATCommand(READ_SMS_LIST,args)
        else:
            Response="+CMS ERROR: <err>"
        return Response