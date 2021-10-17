'''
TEST Basic functions of EG9x Library
'''
#from EG9x import QuectelEG9x
from QuectelEG9x import QuectelEG9x

EG95=QuectelEG9x()

while(1):
    #Request Manufacturer ID of the module
    print(EG95.requestManufacturerId())
    #Get Device ID of the module
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
    print(EG95.GetSMSMode())
    #Set SMS mode Status to PDU
    print(EG95.SetSMSMode("0"))
    #Get SMS mode Txt or PDU ? 
    print(EG95.GetSMSMode())
    #Set SMS mode Status to TXT
    print(EG95.SetSMSMode("1"))
    #Set SMS TE default Char : GSM 7 bit
    print(EG95.SetSMSChar("GSM"))
    #SEND SMS MESSAGE
    print(EG95.SendSMS())
    #Get SMS Message Storage Area
    print(EG95.GET_SMS_STORAGE_AREA())
    #Set SMS Message Storage Area
    print(EG95.SET_SMS_STORAGE_AREA("“SM”,“SM”,“SM”"))
    #Read SMS Message LIST
    print(EG95.READ_LIST_MESSAGE("ALL"))
    break

print("TEST : DONE")
print("===================================")
