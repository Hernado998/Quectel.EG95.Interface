# -*- coding: utf-8 -*-
'''
TEST Basic functions of EG9x Library
'''
import time
import keyboard
from homefunc import QuectelEG95
from phonecall import QuectelEG95Call
from sms import QuectelEG95SMS
from mqttfunc import QuectelEG95Mqtt
from USBinit import usbInit
#from QuectelEG9x import QuectelEG9x

UARTinit = usbInit()

serial = UARTinit.get()

EG95Call = QuectelEG95Call(serial)
#EG95SMS = QuectelEG95SMS(serial)
#EG95MQTT = QuectelEG95Mqtt()
EG95Call.VoiceOverUSB("1,0")

while(1):
    if(UARTinit.readData() == 'RING\r\n'):
        print("You have an incoming call !")
        inn = input("Press a to answer or d to decline\n")
        if(inn=="a"):
            EG95Call.AnswerCall()
            print(UARTinit.readData())
            print("Answered")
            EG95Call.SwithDataToCommand()
            inn1=input("If you like to hang up press h !\n")
            if(inn1=="h"):
                EG95Call.HungUpCall()
                EG95Call.VoiceOverUSB("0")
                print("Call hanged up")
            if(inn=="d"):
                EG95Call.CancelCall()
                print("Cancelled")
    


print("TEST : DONE")
print("===================================")