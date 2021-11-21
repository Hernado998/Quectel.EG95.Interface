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
    def __init__(self,clientidx,broker,port):
        self.clientidx = clientidx
        self.broker = broker
        self.port=port
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
    Open a MQTT network to enable client-broker connexion
    '''
    def openNetwork_mqtt(self):
        args= self.clientidx+","+self.broker+","+self.port+"\r\n"
        Response = self.sendATCommand(OPEN_NETWORK_MQTT,args)
        return Response
    
    '''
    Close MQTT network
    '''
    def closeNetwork_mqtt(self):
        args = self.clientidx+"\r\n"
        Response = self.sendATCommand(CLOSE_NETWORK_MQTT,args)
        return Response
    
    '''
    Connect to MQTT broker
    '''
    def connect_mqtt(self,clientID,username,password):
        args = self.clientidx+","+clientID+"[,"+username+"[,"+password+"\r\n"
        Response = self.sendATCommand(CONNECT_MQTT,args)
        return Response
    
    '''
    Disconnect from the MQTT broker
    '''
    def disconnect_mqtt(self,clientID,username,password):
        args = self.clientidx+"\r\n"
        Response = self.sendATCommand(DISCONNECT_MQTT,args)
        return Response

    '''
    Subscribe to a specific topic and a QoS 0 or 1 or 2
    0: fire and forget
    1: send multiple pakages until one of them arrives 
    2: send one package at a time until we get an acknowledgment
    '''
    def subscribe_mqtt(self,msgID,topic,qos):
        args = self.clientidx+","+msgID+","+topic+","+str(qos)+"\r\n"
        Response = self.sendATCommand(SUBSCRIBE_MQTT,args)
        return Response
    
    '''
    Unsubscribe
    '''
    def unsebscribe_mqtt(self,msgID,topic):
        args = self.clientidx+","+msgID+","+topic+","+"\r\n"
        Response = self.sendATCommand(UNSUBSCRIBE_MQTT,args)
        return Response
    
    '''
    Publish a message under a topic with a specific QoS
    0: fire and forget
    1: send multiple pakages until one of them arrives 
    2: send one package at a time until we get an acknowledgment
    '''
    def publish_mqtt(self,msgID,qos,retain,topic,msg_len):
        args= str(self.clientidx)+','+str(msgID)+','+str(qos)+','+str(retain)+','+topic+','+str(msg_len)+'\r\n'
        Response = self.sendATCommand(PUBLISH_MQTT,args)
        return Response
    
    '''
    Read message comming from the broker
    '''
    def readMessage_mqtt(self):
        args=self.clientidx
        Response=self.sendATCommand(READ_MSG_MQTT,args)
        return Response






