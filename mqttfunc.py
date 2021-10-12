from paho.mqtt import client as mqtt_client
import random as rnd
from InitiateCom import InitiateCom

broker = '10.42.0.219'
port = 1883
topic = "test"
client_idx = 0
clientID ="0"
msgID = 5000
username = "admin"
password = "admin"

serialPort = "/dev/ttyUSB0"

class QuectelEG95Mqtt:

    def __init__(self,clientidx,broker,port):
        self.clientidx = clientidx
        self.broker = broker
        self.port=port
        self.initiate=InitiateCom(serialPort)
        self.initiate.connectQuectelEG95()

    def openNetwork_mqtt(self):
        command = 'AT+QMTOPEN='+str(self.clientidx)+','+self.broker+','+str(self.port)+'\r'
        self.initiate.sendATCommand(command)
    
    def closeNetwork_mqtt(self):
        command = 'AT+QMTCLOSE='+str(self.clientidx)+'\r'
        self.initiate.sendATCommand(command)
    
    def connect_mqtt(self,clientID,username,password):
        command = 'AT+QMTCONN='+str(self.clientidx)+','+clientID+'[,'+username+'[,'+password+'\r'
        self.initiate.sendATCommand(command)

    def disconnect_mqtt(self,clientID,username,password):
        command = 'AT+QMTDISC='+str(self.clientidx)+'\r'
        self.initiate.sendATCommand(command)

    def subscribe_mqtt(self,msgID,topic,qos,):
        command = 'AT+QMTSUB='+str(self.clientidx)+','+str(msgID)+','+topic+','+str(qos)+'\r'
        self.initiate.sendATCommand(command)

    def unsebscribe_mqtt(self,msgID,topic):
        command = 'AT+QMTUNS='+str(self.clientidx)+','+str(msgID)+','+topic+','+'\r'
        self.initiate.sendATCommand(command)

    def publish_mqtt(self,msgID,qos,retain,topic,msg_len):
        command = 'AT+QMTPUBX='+str(self.clientidx)+','+str(msgID)+','+str(qos)+','+str(retain)+','+topic+','+str(msg_len)+'\r'
        self.initiate.sendATCommand(command)

    def readMessage_mqtt(self):
        command = 'AT+QMTRECV='+str(self.clientidx)+'\r'
        self.initiate.sendATCommand(command)
        return self.initiate.readData()






