from atcommand import *
import serial.tools.list_ports
import time


class QuectelEG95Call:

    def __init__(self,serial):
        self.serial=serial
        self.CalledNumbers=[]

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
    Start Call
    @args : the attached mode 
    '''
    def Call(self):
        number=input("Enter Number\n")+";"
        Response= self.sendATCommand(CALL_NUMBER,number)
        self.CalledNumbers += [number]
        print(self.CalledNumbers)
        return Response
    '''
    Cancel Call
    '''
    def CancelCall(self):
        Response= self.sendATCommand(CANCEL_CALL)
        return Response
    '''
    Answer Call
    '''   
    def AnswerCall(self):
        Response= self.sendATCommand(ANSWER_CALL)
        return Response
    '''
    End Call
    '''
    def HungUpCall(self):
        Response= self.sendATCommand(HUNG_UP_CALL)
        return Response

    def Ringing(self):
        Response= self.sendATCommand(CALL_RINGING)
        return Response

    def AutomaticAnswerBeforeRings(self,number):
        Response=self.sendATCommand(VOICE_OVER_USB,str(number))
        return Response

    def VoiceOverUSB(self,args="1,0"):
        Response=self.sendATCommand(VOICE_OVER_USB,args)
        return Response 

    def SwithDataToCommand(self):
        time.sleep(1)
        Response=self.sendATCommand(SWITH_DATA_MODE_TO_COMMAND_MODE)
        time.sleep(1)
        return Response
    def SwitchCommandToData(self):
        time.sleep(1)
        Response=self.sendATCommand(SWITH_COMMAND_MODE_TO_DATA_MODE)
        time.sleep(1)
        return Response
    

    
