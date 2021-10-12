from paho.mqtt import client as mqtt_client
from atcommand import *

broker = "10.42.0.219"
port = "1883"
topic = "test"
client_idx = "0"
clientID ="0"
msgID = "5000"
username = "admin"
password = "admin"

class QuectelEG95Mqtt:

    def __init__(self,clientidx,broker,port):
        self.clientidx = clientidx
        self.broker = broker
        self.port=port

    def openNetwork_mqtt(self):
        args= self.clientidx+","+self.broker+","+self.port+"\r\n"
        Response = self.sendATCommand(OPEN_NETWORK_MQTT,args)
        return Response
    
    def closeNetwork_mqtt(self):
        args = self.clientidx+"\r\n"
        Response = self.sendATCommand(CLOSE_NETWORK_MQTT,args)
        return Response
    
    def connect_mqtt(self,clientID,username,password):
        args = self.clientidx+","+clientID+"[,"+username+"[,"+password+"\r\n"
        Response = self.sendATCommand(CONNECT_MQTT,args)
        return Response

    def disconnect_mqtt(self,clientID,username,password):
        args = self.clientidx+"\r\n"
        Response = self.sendATCommand(DISCONNECT_MQTT,args)
        return Response

    def subscribe_mqtt(self,msgID,topic,qos):
        args = self.clientidx+","+msgID+","+topic+","+str(qos)+"\r\n"
        Response = self.sendATCommand(SUBSCRIBE_MQTT,args)
        return Response

    def unsebscribe_mqtt(self,msgID,topic):
        args = self.clientidx+","+msgID+","+topic+","+"\r\n"
        Response = self.sendATCommand(UNSUBSCRIBE_MQTT,args)
        return Response
    def publish_mqtt(self,msgID,qos,retain,topic,msg_len):
        args= str(self.clientidx)+','+str(msgID)+','+str(qos)+','+str(retain)+','+topic+','+str(msg_len)+'\r\n'
        Response = self.sendATCommand(PUBLISH_MQTT,args)
        return Response

    def readMessage_mqtt(self):
        args=self.clientidx
        Response=self.sendATCommand(READ_MSG_MQTT,args)
        return Response






