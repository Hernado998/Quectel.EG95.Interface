from paho.mqtt import client as mqtt_client
from atcommand import *
import serial.tools.list_ports
import time
'''
Parameters for testing purposes
'''
broker = "10.42.0.219"
port = "1883"
topic = "test"
client_idx = "0"
clientID ="0"
msgID = "5000"
username = "admin"
password = "admin"

class QuectelEG95Mqtt:

    '''
    Initialize the brokers parameters and the client idx
    '''
    def __init__(self,serial):
        self.serial=serial
        
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
    CONFIGURE_RECEIVE_MODE
    '''
    def ConfigureReceiveMode(self,args):
        Response=self.sendATCommand(CONFIGURE_RECEIVE_MODE,args)
        return Response
    '''
    Store certificate
    '''
    def StoreCertificate(self,args):
        Response=self.sendATCommand(STORE_CERTFICATE,args)
        return Response
    '''
    Configure SSL certificate
    '''
    def ConfigureCertificate(self,args):
        Response=self.sendATCommand(CONFIGURE_CERTIFICATE,args)
        return Response
    '''
    Open a MQTT network to enable client-broker connexion
    '''
    def OpenNetworkMqtt(self,args):
        Response = self.sendATCommand(OPEN_NETWORK_MQTT,args)
        return Response
    
    '''
    Close MQTT network
    '''
    def CloseNetworkMqtt(self,args):
        Response = self.sendATCommand(CLOSE_NETWORK_MQTT,args)
        return Response
    
    '''
    Connect to MQTT broker
    '''
    def ConnectMqtt(self,args):
        Response = self.sendATCommand(CONNECT_MQTT,args)
        return Response
    
    '''
    Disconnect from the MQTT broker
    '''
    def DisconnectMqtt(self,args):
        Response = self.sendATCommand(DISCONNECT_MQTT,args)
        return Response

    '''
    Subscribe to a specific topic and a QoS 0 or 1 or 2
    0: fire and forget
    1: send multiple pakages until one of them arrives 
    2: send one package at a time until we get an acknowledgment
    '''
    def SubscribeMqtt(self,args):
        Response = self.sendATCommand(SUBSCRIBE_MQTT,args)
        return Response
    
    '''
    Unsubscribe
    '''
    def UnsebscribeMqtt(self,args):
        Response = self.sendATCommand(UNSUBSCRIBE_MQTT,args)
        return Response
    
    '''
    Publish a message under a topic with a specific QoS
    0: fire and forget
    1: send multiple pakages until one of them arrives 
    2: send one package at a time until we get an acknowledgment
    '''
    def PublishMqtt(self,args):
        Response = self.sendATCommand(PUBLISH_MQTT,args)
        return Response
    
    '''
    Read message comming from the broker
    '''
    def ReadMessageMqtt(self,args):
        Response=self.sendATCommand(READ_MSG_MQTT,args)
        return Response






