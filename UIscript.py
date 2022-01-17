from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import QTimer, QTime, Qt
import sys
from homefunc import QuectelEG95
from phonecall import QuectelEG95Call
from sms import QuectelEG95SMS
from USBinit import usbInit
from multiprocessing import Process
from mqttfunc import QuectelEG95Mqtt

UARTinit = usbInit()
serial = UARTinit.get()

EG95=QuectelEG95(serial)
EG95Call = QuectelEG95Call(serial)
EG95SMS = QuectelEG95SMS(serial)
EG95MQTT = QuectelEG95Mqtt(serial)


class DemoWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()
        
    def initui(self):
        self.num=""
        self.callstate=False
        self.ch=""
        self.answered=False;self.declined=False;self.hungup=False;self.called=False
        # Call the inherited classes __init__ method
        super(DemoWidget, self).__init__()
        # Load the .ui file
        uic.loadUi('Comelit.ui', self)
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Serial communication initialized\n"
        self.textBrowser_31.setText(self.ch)

        

        self.pushButton_2.clicked.connect(lambda : self.composeNumber("1"));self.pushButton_3.clicked.connect(lambda : self.composeNumber("2"));self.pushButton_4.clicked.connect(lambda : self.composeNumber("3"));self.pushButton_7.clicked.connect(lambda : self.composeNumber("4"));self.pushButton_5.clicked.connect(lambda : self.composeNumber("5"))
        self.pushButton_6.clicked.connect(lambda : self.composeNumber("6"));self.pushButton_10.clicked.connect(lambda : self.composeNumber("7"));self.pushButton_8.clicked.connect(lambda : self.composeNumber("8"));self.pushButton_9.clicked.connect(lambda : self.composeNumber("9"));self.pushButton_11.clicked.connect(lambda : self.composeNumber("*"))
        self.pushButton_13.clicked.connect(lambda : self.composeNumber("0"));self.pushButton_12.clicked.connect(lambda : self.composeNumber("#"));self.pushButton_17.clicked.connect(lambda : self.clearNumber())
        self.pushButton_14.clicked.connect(lambda : self.callNumber());self.pushButton_15.clicked.connect(lambda : self.hungupCall());self.pushButton_16.clicked.connect(lambda : self.declineCall());self.pushButton_18.clicked.connect(lambda : self.answerCall())
        self.pushButton_38.clicked.connect(lambda : self.sendSMS())
        self.pushButton_40.clicked.connect(self.readallSMS);self.pushButton_42.clicked.connect(self.deleteallSMS)
        self.pushButton_43.clicked.connect(lambda : self.disconnectModule());self.pushButton_44.clicked.connect(lambda : self.moduleinfos());self.pushButton_45.clicked.connect(lambda : self.registrationinfos());self.pushButton_46.clicked.connect(lambda : self.siminfos())
        self.pushButton_47.clicked.connect(lambda : self.initializeMqtt());self.pushButton_34.clicked.connect(lambda : self.opennetworkMqtt())
        self.pushButton_35.clicked.connect(lambda : self.disconnectMqtt())
        self.timer=QTimer(self)
        if(UARTinit.readData() == 'RING\r\n'):
            self.answered=False;self.declined=False;self.hungup=False;self.called=False
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" You have an incoming call !"
            self.textBrowser_31.setText(self.ch)
            if(self.callNumber==True):
                self.answerCall()
                print(UARTinit.readData())
                EG95Call.SwithDataToCommand()
                if(self.hungupCall==True):
                    self.hungupCall()
                    EG95Call.VoiceOverUSB("0")
            if(self.declined==True):
                self.declineCall()
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        # Show the widget
        self.show()
       

    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.textBrowser_30.setText(label_time)
       
    def launchTimer(self):
        while(True):
            self.timer.timeout.connect(lambda: self.showTime())
            self.timer.start(1000)

    def composeNumber(self,n):
        self.num+=n
        self.textBrowser_23.setText(self.num)

    def clearNumber(self):
        self.num=""
        self.textBrowser_23.setText(self.num)
        
    def callNumberNDsetTimer(self):
        thread1=Process(target=self.launchTimer)
        thread1.start()
        thread2=Process(target=self.callNumber)
        thread2.start()
        
    def callNumber(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Starting the call...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        e=EG95Call.Call(self.num)
        self.called=True

        
    def hungupCall(self):
        self.callstate=False
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Hunging up the call...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95Call.HungUpCall())
        self.hungup=True
        
    
    def answerCall(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Answering the call...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95Call.AnswerCall())
        self.answered=True

    def declineCall(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Canceling the call...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95Call.CancelCall())
        self.declined=True
    
    def sendSMS(self):
        if(self.radioButton_5.isChecked()):
            EG95SMS.SetSMSMode("1")
            num=self.lineEdit_6.text()
            msg=self.textEdit.toPlainText()
            EG95SMS.SendSMS(num,msg)
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" SMS is sent to "+num+"\n"
            self.textBrowser_31.setText(self.ch)

    def readallSMS(self):
            EG95SMS.SetSMSMode("0")
            EG95SMS.SetSMSMode("1")
            EG95SMS.GET_SMS_STORAGE_AREA()
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Getting data from storage area \n"
            self.textBrowser_31.setText(self.ch)
            QtWidgets.qApp.processEvents()
            e=EG95SMS.READ_LIST_MESSAGE("ALL")
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Showing SMS... \n"
            self.textBrowser_31.setText(self.ch)
            QtWidgets.qApp.processEvents()
            print(e.split("\n"))
            i1=e.split("\n")[1].split(",")[0][7]
            i2=e.split("\n")[1].split(",")[1]
            i3=e.split("\n")[1].split(",")[2]
            i4=e.split("\n")[1].split(",")[4]+" "+e.split("\n")[1].split(",")[5].split(",")[0][:-4]
            i5=e.split("\n")[2][:-1]
            self.textBrowser_32.setText("        "+i1+"            "+i4+"                    "+i3+"           "+i2)
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Messages:... \n"
            self.textBrowser_31.setText(self.ch)
            QtWidgets.qApp.processEvents()
            self.ch+=i5+" \n"
            self.textBrowser_31.setText(self.ch)
    def deleteallSMS(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Deleting messsages... \n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        EG95SMS.DELETE_SMS()
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Messages deleted \n"
        self.textBrowser_31.setText(self.ch)


    def disconnectModule(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Closing port...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        UARTinit.closePort()
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Port closed\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()

    def moduleinfos(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Showing module informations...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        e=EG95.requestManufacturerId()
        print(e.split("\n")[1])
        self.textBrowser_6.setText(e.split("\n")[1])
        e=EG95.deviceModule()
        self.textBrowser_7.setText(e[10:21])
        e=EG95.firmwareVersion()
        print(e)
        self.textBrowser_8.setText(e[9:30])
    def registrationinfos(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Showing registration informations...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        e=EG95.networkRegistration()
        self.textBrowser_11.setText("Auto attach")
        e=EG95.grpsNetworkStatus()
        self.textBrowser_12.setText("Registered, home network")
        e=EG95.preferredOperator()
        self.textBrowser_15.setText("Tunisie Telecom")
          
    def siminfos(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Showing SIM card informations...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        e=EG95.simCardIMSI()
        self.textBrowser_16.setText(e[10:36])
        e=EG95.simCardICCID()
        self.textBrowser_19.setText(e[18:40])

    def initializeMqtt(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Initializing MQTT protocol settings...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Changing network to LTE-M1...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95.grpsNetworkStatus("nwscanmode ,3"))
        print(EG95.setPhoneFunctionality("=1"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Defining PDP context...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95.definePDPConntext("=1,IP,internet.tn"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Configuring TCP/IP settings...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95.configureParamTcpIPContext("=1,1,internet.tn ,1"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Activating PDP context ...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95.activatePdpContext("=1"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Setting up TCP client connexion...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print("Set up a TCP Client Connection and Enter into Buffer Access Mode ")
        print(EG95.openSocketService("=1,0,TCP,220.180.239.212,8009,0,0"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Defining query status...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print("Query status")
        print(EG95.socketServiceStatus("=1,0"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Configuring receiving mode...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        #Configure receiving mode
        print(EG95MQTT.ConfigureReceiveMode("=recv/mode,0,0,1"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Done\n"
        self.textBrowser_31.setText(self.ch)
    
    def opennetworkMqtt(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Openining network...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        self.address=self.lineEdit.text()
        self.port=self.lineEdit_2.text()
        c="=0,"+self.address+","+self.port
        e=EG95MQTT.OpenNetworkMqtt(c)
        if(e.split("\n")[3]=="+QMTT: 0,0"):
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Network opened successfully...\n"
            self.textBrowser_31.setText(self.ch)
            QtWidgets.qApp.processEvents()
        else:
            self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Network was opened...\n"
            self.textBrowser_31.setText(self.ch)
            QtWidgets.qApp.processEvents()
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Connecting to MQTT broker...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95MQTT.ConnectMqtt("0,mosquitto"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Network opened...\n"
        self.textBrowser_31.setText(self.ch)
    def disconnectMqtt(self):
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Disconnecting MQTT connection...\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()
        print(EG95MQTT.DisconnectMqtt("0"))
        self.ch+=QTime.currentTime().toString('hh:mm:ss')+" Disconnected\n"
        self.textBrowser_31.setText(self.ch)
        QtWidgets.qApp.processEvents()


        


app = QtWidgets.QApplication(sys.argv)
window = DemoWidget()
app.exec_()
