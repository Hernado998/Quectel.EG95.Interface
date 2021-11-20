from atcommand import *
import serial.tools.list_ports
import time


class QuectelEG95Call:

    ''' 
    Connect the module through UART
    '''
    def __init__(self,CalledNumbers):
        self.CalledNumbers=CalledNumbers
        self.CalledNumbers=[]
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
        print(self.Called_Number)
        return Response
    '''
    Cancel Call
    '''
    def cancelCall(self):
        Response= self.sendATCommand(CANCEL_CALL)
        return Response
    '''
    Answer Call
    '''   
    def answer_call(self):
        Response= self.sendATCommand(ANSWER_CALL)
        return Response
    '''
    End Call
    '''
    def HungUpCall(self):
        Response= self.sendATCommand(HUNG_UP_CALL)
        return Response

    

    
