"""
    AT Command class definition
    Authors : Iheb Omar Soula and Nadir Hermassi
    telecommunications Engineering Students @ SUPCOM [ HIGHER SCHOOL OF COMMUNICATIONS OF TUNIS]
    date: 12/10/2021
"""
class AT_COMMANDS:

    def __init__(self,atcommand):
        self.atcommand=atcommand


    def __eq__(self,other):
        if (self.atcommand==other.atcommand):
            return True
        else:
            return False
    def __ne__(self,other):
        if(self.atcommand!=other.atcommand):
            return True
        else:
            return False

    def get_string(self):
        return self.atcommand

''' 

AT Command list 

'''

TURN_OFF = AT_COMMANDS("AT+QPOWD\r\n")
MANIFACTURE_ID = AT_COMMANDS("AT+GMI\r\n")
DEVICE_ID= AT_COMMANDS("AT+CGMM\r\n")
FIRMWARE_VS= AT_COMMANDS("AT+GMR\r\n")
REGISTRED_DEVICE_STATUS = AT_COMMANDS("AT+CGREG\r\n")
NETWORK_NAME=AT_COMMANDS("AT+QSPN\r\n")
PREFERED_OPERATORS_LIST = AT_COMMANDS("AT+CPOL\r\n")
SIM_CARD_IMSI= AT_COMMANDS("AT+CIMI\r\n")
SIM_CARD_ICCID=AT_COMMANDS("AT+QCCID\r\n")
SIM_CARD_INIT= AT_COMMANDS("AT+QINISTAT\r\n")
SET_SMS_MODE=AT_COMMANDS("AT+CMGF=")
SET_SMS_CHAR=AT_COMMANDS("AT+CSCS=")
SET_SMS_NUMBER=AT_COMMANDS("AT+CMGS=")
CALL_NUMBER=AT_COMMANDS("ATD")
DISCONNECT_NUMBER=AT_COMMANDS("ATH")
HUNG_UP_CALL=AT_COMMANDS("AT+CHUP")
OPEN_NETWORK_MQTT=AT_COMMANDS("AT+QMTOPEN=")
CLOSE_NETWORK_MQTT=AT_COMMANDS("AT+QMTCLOSE=")
CONNECT_MQTT=AT_COMMANDS("AT+QMTCONN=")
DISCONNECT_MQTT=AT_COMMANDS("AT+QMTDISC=")
SUBSCRIBE_MQTT=AT_COMMANDS("AT+QMTSUB=")
UNSUBSCRIBE_MQTT=AT_COMMANDS("AT+QMTSUB=")
PUBLISH_MQTT=AT_COMMANDS("AT+QMTPUBX=")
READ_MSG_MQTT=AT_COMMANDS("AT+QMTRECV=")
EXTENDED_CONF_SET=AT_COMMANDS("AT+QCFG")
