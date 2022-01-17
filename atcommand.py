"""
    AT Command class definition
    Authors : Iheb Omar Soula and Nadir Hermassi
    telecommunications Engineering Students @ SUPCOM [ HIGHER SCHOOL OF COMMUNICATIONS OF TUNIS]
    Project in Sup'Com with Comelit R&D company
    date: 12/10/2021
"""
class AT_COMMANDS:

    def __init__(self,atcommand):
        self.string=atcommand


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

        

''' 

AT Command list 

'''

TURN_OFF = AT_COMMANDS("AT+QPOWD\r\n")
NOTHING=AT_COMMANDS("\r\n")
MANIFACTURE_ID = AT_COMMANDS("AT+GMI\r\n")
OWN_NUMBER = AT_COMMANDS("AT+CSIM\r\n")
DEVICE_ID= AT_COMMANDS("AT+CGMM\r\n")
FIRMWARE_VS= AT_COMMANDS("AT+GMR\r\n")
REGISTRED_DEVICE_STATUS = AT_COMMANDS("AT+CGREG\r\n")
NETWORK_NAME=AT_COMMANDS("AT+QSPN\r\n")
PREFERED_OPERATORS_LIST = AT_COMMANDS("AT+CPON\r\n")
DELETE_SMS=AT_COMMANDS("AT+CMGD=\r\n")
SIM_CARD_IMSI= AT_COMMANDS("AT+CIMI\r\n")
SIM_CARD_ICCID=AT_COMMANDS("AT+QCCID\r\n")
SIM_CARD_INIT= AT_COMMANDS("AT+QINISTAT\r\n")
GET_SMS_MODE=AT_COMMANDS("AT+CMGF?\r\n")
SET_SMS_MODE=AT_COMMANDS("AT+CMGF=\r\n")
EXTENDED_CONF_SET=AT_COMMANDS("AT+QCFG\r\n")
SET_SMS_CHAR=AT_COMMANDS("AT+CSCS=\r\n")
SEND_SMS_NUMBER=AT_COMMANDS("AT+CMGS=\r\n")
GET_SMS_STORAGE_AREA=AT_COMMANDS("AT+CPMS?\r\n")
SET_SMS_STORAGE_AREA=AT_COMMANDS("AT+CPMS=\r\n")
READ_SMS_LIST=AT_COMMANDS("AT+CMGL=\r\n")
CALL_NUMBER=AT_COMMANDS("ATD\r\n")
DISCONNECT_NUMBER=AT_COMMANDS("ATH\r\n")
HUNG_UP_CALL=AT_COMMANDS("AT+CHUP\r\n")
CANCEL_CALL=AT_COMMANDS("ATH\r\n")
ANSWER_CALL=AT_COMMANDS("ATA\r\n")
CALL_RINGING=AT_COMMANDS("AT+CLCC\r\n")
AUTOMATIC_RINGS_BEFORE_ANSWER=AT_COMMANDS("ATSCALL_RINGING=\r\n")
VOICE_OVER_USB=AT_COMMANDS("AT+QPCMV=\r\n")
SWITH_DATA_MODE_TO_COMMAND_MODE=AT_COMMANDS("+++\r\n")
SWITH_COMMAND_MODE_TO_DATA_MODE=AT_COMMANDS("ATO\r\n")

SEVEN_BIT_ENCODING = AT_COMMANDS("AT+CSMP=17,167,2,0\r\n")
CONFIGURE_CERTIFICATE=AT_COMMANDS("AT+QSSLCFG\r\n")
STORE_CERTFICATE=AT_COMMANDS("AT+QFUPL\r\n")
CONFIGURE_RECEIVE_MODE=AT_COMMANDS("AT+QMTCFG\r\n")
OPEN_NETWORK_MQTT=AT_COMMANDS("AT+QMTOPEN\r\n")
CLOSE_NETWORK_MQTT=AT_COMMANDS("AT+QMTCLOSE=\r\n")
CONNECT_MQTT=AT_COMMANDS("AT+QMTCONN=\r\n")
DISCONNECT_MQTT=AT_COMMANDS("AT+QMTDISC=\r\n")
SUBSCRIBE_MQTT=AT_COMMANDS("AT+QMTSUB=\r\n")
UNSUBSCRIBE_MQTT=AT_COMMANDS("AT+QMTSUB=\r\n")
PUBLISH_MQTT=AT_COMMANDS("AT+QMTPUBX=\r\n")
READ_MSG_MQTT=AT_COMMANDS("AT+QMTRECV=\r\n")
SMS_EVT_RP_CONF=AT_COMMANDS("AT+CNMI=\r\n")


SET_PHONE_FUNCTIONALITY=AT_COMMANDS("AT+CFUN\r\n")
SIGNAL_QUALITY_REPORT_AND_QUERY=AT_COMMANDS("AT+QCSQ\r\n")
DEFINE_PDP_CONTEXT=AT_COMMANDS("AT+CGDCONT\r\n")
OPERATOR_SELECTION=AT_COMMANDS("AT+COPS\r\n")

CONFIGURE_PARAMETERS_TCP_IP_CONTEXT=AT_COMMANDS("AT+QICSGP\r\n")
ACTIVATE_PDP_CONTEXT=AT_COMMANDS("AT+QIACT\r\n")
DESACTIVATE_PDP_CONTEXT=AT_COMMANDS("AT+QIDEACT\r\n")
OPEN_SOCKET_SERVICE=AT_COMMANDS("AT+QIOPEN\r\n")
CLOSE_SOCKET_SERVICE=AT_COMMANDS("AT+QICLOSE\r\n")
QUERY_SOCKET_SERVICE_STATUS=AT_COMMANDS("AT+QISTATE\r\n")
PING = AT_COMMANDS("AT+QPING\r\n")