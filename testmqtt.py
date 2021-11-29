# -*- coding: utf-8 -*-

from mqttfunc import QuectelEG95Mqtt
from USBinit import usbInit
from homefunc import QuectelEG95


UARTinit = usbInit()

serial = UARTinit.get()

EG95MQTT = QuectelEG95Mqtt(serial)
EG95 = QuectelEG95(serial)
#change to LTE use
print(EG95.grpsNetworkStatus("nwscanmode ,3"))
##print(EG95.grpsNetworkStatus("nwscanseq"))

#=0 sets the module to minimum functionality mode where 
#the SIM does not work. This is equivalent to resetting
#the module without turning off the power.
#To revert the SIM back to full functionality, use =1.
print(EG95.setPhoneFunctionality("=1"))
##print(EG95.setPhoneFunctionality("?"))

#PDP context identifier for TCP/IP transmission, Packet data protocol type,Access Point Name
print(EG95.definePDPConntext("=1,IP,internet.ooredoo.tn"))
##print(EG95.definePDPConntext("?"))

#Configuring paramaters to TCP/IP connexion
print("TCP/IP context: ")
print(EG95.configureParamTcpIPContext("=1,1,internet.ooredoo.tn, , ,1"))
print("PDP context: ")
print(EG95.activatePdpContext("=1"))
##print(EG95.activatePdpContext("?"))
print("Set up a TCP Client Connection and Enter into Buffer Access Mode ")
print(EG95.openSocketService("=1,0,TCP,220.180.239.212,8009,0,0"))
print("Query status")
print(EG95.socketServiceStatus("=1,0"))
#PING TEST
##print("Pinging Google")
##print(EG95.ping("=1,www.google.com"))

#See operators
print("Operators :")
print(EG95.operatorSelection("?"))
#Return Signal strenth and Query for our case with
#LTE /value1: lte_rssi/value2: lte_rsrp/value3: lte_sinr/value4: lte_rsrq
print(EG95.siggnalQualityReportAndQuery(""))

while(1):
    ch=[]
    while(ch !=['OK', '+QMTCONN:', '0,0,0']):
        #Disconnect MQTT server
        print(EG95MQTT.DisconnectMqtt("0"))
        #Configure receiving mode
        print(EG95MQTT.ConfigureReceiveMode("=recv/mode,0,0,1"))
        print(EG95MQTT.ConfigureReceiveMode("=aliauth ,0"))
        print(EG95MQTT.ConfigureReceiveMode("?"))
        #Configure MQTT session into SSL mode
        #print(EG95MQTT.ConfigureReceiveMode("ssl,0,1,2"))
        #Start MQTT SSL connection
        print(EG95MQTT.OpenNetworkMqtt("=0, broker.mqttdashboard.com , 1883"))
        print("Checking if network was opened successfully...\n")
        #Connect to MQTT server
        ch=EG95MQTT.ConnectMqtt("0, mosquitto").split()
        print(ch)
        
    print("Network opened successfully\n")
    print("Connection to server established\n")
    #Choose Publish/Subscribe
    inn=input("Press S to subscribe/ P to publish")
    if(inn=="S"):
        #args=client_idx,msgID,“topic”,qos
        #QoS=1: send multiple pakages until one of them arrives
        print(EG95MQTT.SubscribeMqtt("0,1, test008 ,1"))
        while(1):
            print(EG95MQTT.ReadMessageMqtt("0,0,test008"))
            if(UARTinit.readData()!=""):
                print(UARTinit.readData())
    if(inn=="P"):
        #args=client_idx,msgID,qos,retain,“topic”,msg_length 
        #QoS=1: send multiple pakages until one of them arrives
        print(EG95MQTT.PublishMqtt("0,0,0,0,test008,30"))
        print(UARTinit.readData())

    

    
UARTinit.closePort()