/* Program to test the EG9X Library with arduino  
 *  Developped by Iheb Omar Soula and Nadir Hermassi
 *  Telecommunications Enginnering Students @ Supcom
 *  Date: 16/10/2021
 */
void setup() {
  Serial.begin(115200);
    while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
}
}
String received;
String SendManfucturerID="AT+GMI\r\n";
String SendTurnOFF = "AT+QPOWD\r\n";
String SendDEVICE_ID="AT+CGMM\r\n";
String SendFIRMWARE_VS="AT+GMR\r\n";
String SendREGISTRED_DEVICE_STATUS="AT+CGREG?\r\n";
String SendNETWORK_NAME="AT+QSPN\r\n";
String SendPREFERED_OPERATORS_LIST="AT+CPOL?\r\n";
String SendSIM_CARD_IMSI="AT+CIMI\r\n";
String SendSIM_CARD_ICCID="AT+QCCID\r\n";
String SendSIM_CARD_INIT="AT+QINISTAT\r\n";
String Send_SMS_MODE="AT+CMGF?\r\n";
String SendSET_SMS_MODE_TXT="AT+CMGF=1\r\n";
String SendSET_SMS_MODE_PDU="AT+CMGF=0\r\n";
String SETSMS_CHAR_MODE="AT+CSCS=GSM\r\n";
String Send_SMS_NUMBER="AT+CMGS=";
String Send_SMS_STORAGE_AREA="AT+CPMS?\r\n";
String Send_SET_SMS_STORAGE_AREA="AT+CPMS=";
String Send_STORED_SMS="AT+CMGL=";
String SendCALL_NUMBER="ATD";
String SendDISCONNECT_NUMBER="ATH";
String SendHUNG_UP_CALL="AT+CHUP";
String SendEXTENDED_CONF_SET="AT+QCFG=gprsattach\r\n";
int sms_mode=1;
int send_sms=0;
void QuectelEG9xResponses()
{
  if(Serial.available()>0)
  {

    //received=Serial.readString();
  while (Serial.available()) {
    delay(2);  //delay to allow byte to arrive in input buffer
    char c = Serial.read();
    received += c;
  }



if (received.length() >0) {

    if(received==SendManfucturerID)
    {
    Serial.write("Quectel\nOK\n");  
    delay(200); 
    }
    else if(received==SendDEVICE_ID)
    {
      Serial.write("EG9x\nOK\n");
      delay(200);
    }
    else if(received==SendPREFERED_OPERATORS_LIST)
    {
      Serial.write("+CPOL: 1,2,'46008',0,0,0,1\n+CPOL: 3,2,'46002',0,0,0,1\n+CPOL: 4,2,'46007',0,0,0,1\n+CPOL: 2,2,'46000',0,0,0,1\nOK\n");
      delay(200);
    }
    else if(received==SendTurnOFF)
    {
      Serial.write("OK\nPOWERED DOWN\n");
      delay(200);
    }
    else if(received==SendFIRMWARE_VS)
    {
      Serial.write("Revision: BG96MAR02A07M1G\nOK");
      delay(200);
    }
    else if(received==SendREGISTRED_DEVICE_STATUS)
    {
      Serial.write("+CGREG: 0,0\nOK");
      delay(200);
    }
    else if(received==SendNETWORK_NAME)
    {
      Serial.write("+QSPN: 'CHN-UNICOM','UNICOM','',0,'46001'\nOK");
      delay(200);
    }
    else if(received==SendSIM_CARD_IMSI)
    {
      Serial.write("268069636139549\nOK\n");
      delay(200);
    }
    else if(received==SendSIM_CARD_ICCID)
    {
      Serial.write("+QCCID: 89351060000770861548\nOK\n");
      delay(200);
    }
    else if(received==SendSIM_CARD_INIT)
    {
      Serial.write("+QINISTAT: 1\nOK\n");
      delay(200);
    }
    else if(received==Send_SMS_MODE)
    {
      if(sms_mode)
      {
        Serial.write("SMS mode : TEXT \n OK\n");
      }
      else 
      {
         Serial.write("SMS mode : PDU \n OK\n");
      }
      delay(200);
    }
    else if(received==SendSET_SMS_MODE_TXT)
    {
      Serial.write("Set SMS to text mode \n OK\n");
      sms_mode=1;
      delay(200);
    }
    else if(received==SendSET_SMS_MODE_PDU)
    {
      Serial.write("Set SMS to PDU mode \n OK\n");
      sms_mode=0;
      delay(200);
    }
    else if(received==SendEXTENDED_CONF_SET)
    {
      Serial.write("GPRS: Registered\nOK\n");
      delay(200);
    }
    else if(received==SETSMS_CHAR_MODE)
    {
      Serial.write("GSM Mode Alphabet\nOK\n");
      delay(200);
    }
    else if(received.indexOf(Send_SMS_NUMBER)>=0)
    {
      send_sms+=1;
      if(send_sms==2)
      {
       Serial.write("+CMGS: 2\nOK\n");
       send_sms=0; 
      }
      delay(200);
    }
    else if(received==Send_SMS_STORAGE_AREA)
    {
      Serial.write("“ME”,0,255,“ME”,0,255,“ME”,0,255\nOK\n");
      delay(200);
    }
    else if(received.indexOf(Send_SET_SMS_STORAGE_AREA)>=0)
    {
      Serial.write("+CPMS: 0,50,0,50,0,50\nOK\n");
      delay(200);
    }
    else if(received.indexOf(Send_STORED_SMS)>=0)
    {
      Serial.write("+CMGL: 1,“STO UNSENT”,“”,,\n<This is a test from Quectel>\n+CMGL: 2,“STO UNSENT”,“”,,\n<This is a test from Quectel>\nOK\n");
      delay(200);
    }
  } 
 received="";
  }
  
}

void loop() {

  QuectelEG9xResponses();
  
}
