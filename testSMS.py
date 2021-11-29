# -*- coding: utf-8 -*-
'''
TEST Basic functions of EG9x Library
'''

from homefunc import QuectelEG95
from phonecall import QuectelEG95Call
from sms import QuectelEG95SMS
from mqttfunc import QuectelEG95Mqtt
from USBinit import usbInit
#from QuectelEG9x import QuectelEG9x

UARTinit = usbInit()
serial = UARTinit.get()
EG95=QuectelEG95(serial)
EG95Call = QuectelEG95Call(serial)
EG95SMS = QuectelEG95SMS(serial)
#EG95MQTT = QuectelEG95Mqtt()

while(1):
    
    #26162201
   
    #Request Manufacturer ID of the module
    print(EG95.requestManufacturerId())
    #Get Device ID of the mo26162201dule
    print(EG95.deviceModule())
    #Get firmeware of the module
    print(EG95.firmwareVersion())
    #Get Network Registration 
    print(EG95.networkRegistration())
    #Check GPRS Status
    print(EG95.grpsNetworkStatus())
    #Get list of Preferred Operators
    print(EG95.preferredOperator())
    #Get IMSI
    print(EG95.simCardIMSI())
    #Get ICCID
    print(EG95.simCardICCID())
    #Get SMS mode Txt or PDU ? 
    print(EG95SMS.GetSMSMode())
    #Set SMS mode Status to PDU
    print(EG95SMS.SetSMSMode("0"))
    #Get SMS mode Txt or PDU ? 
    print(EG95SMS.GetSMSMode())
    #Set SMS mode Status to TXT
    print(EG95SMS.SetSMSMode("1"))
    #Set SMS TE default Char : GSM 7 bit
    print(EG95SMS.SetSMSChar())
    #SEND SMS MESSAGE
    print(EG95SMS.SendSMS())
    #Get SMS Message Storage Area
    print(EG95SMS.GET_SMS_STORAGE_AREA())
    #Set SMS Message Storage Area
    print(EG95SMS.SET_SMS_STORAGE_AREA("“SM”,“SM”,“SM”"))
    #Read SMS Message LIST
    print(EG95SMS.READ_LIST_MESSAGE("ALL"))
    break

print("TEST : DONE")
print("===================================")