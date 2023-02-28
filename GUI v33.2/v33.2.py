# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v33.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as graph
import GUIgraph 
import time
import threading 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        #this sets the app full screen
        screen = app.desktop().screenGeometry()
        screenwidth = int(screen.width())
        screenheight = int(screen.height())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screenwidth, screenheight)
        print("screen resolution: ", int(screenwidth), int(screenheight))
        
        #creates the border which everything will sit inside
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(
            int((10/1920)*screenwidth), 
            int((20/1080)*screenheight), 
            int(screenwidth - int((20/1920)*screenwidth)), 
            int(screenheight - int((40/1080)*screenheight)) 
            ))        
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        
        #keeps the three sections equally spaced
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(
            int((20/1920)*screenwidth), 
            int((50/1080)*screenheight),
            screenwidth,
            int(screenheight -(110/1080)*screenheight)
            ))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(
            0,
            0,
            0,
            0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #the leftmost column of the system
        self.leftframe = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.leftframe.setFrameShape(QtWidgets.QFrame.Box)
        self.leftframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftframe.setMidLineWidth(2)
        self.leftframe.setObjectName("leftframe")
        self.LeftLabel = QtWidgets.QLabel(self.leftframe)
        self.LeftLabel.setGeometry(QtCore.QRect(
            int(250/1920*screenwidth),
            int(10/1080*screenheight),
            int(161/1920*screenwidth),
            int(61/1080*screenheight)))
        
        #the label for motor
        font = QtGui.QFont()
        font.setPointSize(28)
        self.LeftLabel.setFont(font)
        self.LeftLabel.setObjectName("LeftLabel")
        
        
        ##########################################################################################
        #code for the slipbox
        #frame for slip
        self.slipbox = QtWidgets.QFrame(self.leftframe)
        self.slipbox.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(80/1080*screenheight),
            int(550/1920*screenwidth),
            int(121/1080*screenheight)))
        self.slipbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slipbox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.slipbox.setObjectName("slipbox")
        
        #slider for slip
        self.slipSlider = QtWidgets.QSlider(self.slipbox)
        self.slipSlider.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(60/1080*screenheight),
            int(500/1920*screenwidth),
            int(22/1080*screenheight)))
        self.slipSlider.setOrientation(QtCore.Qt.Horizontal)
        self.slipSlider.setObjectName("slipSlider")
        
        #the +1 label for the slip slider 
        self.label_2 = QtWidgets.QLabel(self.slipbox)
        self.label_2.setGeometry(QtCore.QRect(
            int(500/1920*screenwidth), 
            int(90/1080*screenheight),
            int(31/1920*screenwidth),
            int(16/1080*screenheight)))
        self.label_2.setObjectName("label_2")
        
        #the -1 for the slip slider 
        self.label = QtWidgets.QLabel(self.slipbox)
        self.label.setGeometry(QtCore.QRect(
            int(30/1920*screenwidth),
            int(90/1080*screenheight), 
            int(16/1980*screenwidth), 
            int(16/1080*screenheight)))
        self.label.setObjectName("label")
        
        #label saying slip 
        self.sliplabel = QtWidgets.QLabel(self.slipbox)
        self.sliplabel.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(10/1080*screenheight),
            int(61/1920*screenwidth),
            int(31/1080*screenheight)))
        self.sliplabel.setObjectName("sliplabel")
        
        # the manual input for slip
        self.slipInput = QtWidgets.QLineEdit(self.slipbox)
        self.slipInput.setGeometry(QtCore.QRect(
            int(120/1920*screenwidth),
            int(20/1080*screenheight),
            int(71/1920*screenwidth),
            int(20/1080*screenheight)))
        self.slipInput.setObjectName("slipInput")
        
        
        ############################################################################################
        #code for the temperature section  
        #the frame holding the temperature graphs of the system
        self.temperatureWidget = QtWidgets.QWidget(self.leftframe)
        self.temperatureWidget.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth), 
            int(290/1080*screenheight), 
            int(610/1920*screenwidth),
            int(400/1080*screenheight)))
        self.temperatureWidget.setObjectName("temperatureWidget")
        
        #placeholder for the tempreture graph
        self.temperatureGraphic = QtWidgets.QGraphicsView(self.temperatureWidget)
        self.temperatureGraphic.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(70/1080*screenheight),
            int(570/1920*screenwidth),
            int(300/1080*screenheight)))
        self.temperatureGraphic.setObjectName("temperatureGraphic")
        
        #label stating temperature
        self.temperatureLabel = QtWidgets.QLabel(self.temperatureWidget)
        self.temperatureLabel.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(20/1080*screenheight),
            int(201/1920*screenwidth),
            int(41/1080*screenheight)))
        self.temperatureLabel.setObjectName("temperatureLabel")
        
        ####################################################################################
        #code for the ERPM section (the label and the input)
        self.ERPMBox = QtWidgets.QWidget(self.leftframe)
        self.ERPMBox.setGeometry(QtCore.QRect(
            int(240/1920*screenwidth),
            int(230/1080*screenheight),
            int(111/1920*screenwidth),
            int(80/1080*screenheight)))
        self.ERPMBox.setObjectName("ERPMBox")
        
        #label stating ERPM
        self.ERPMLabel = QtWidgets.QLabel(self.ERPMBox)
        self.ERPMLabel.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(10/1080*screenheight),
            int(81/1920*screenwidth),
            int(31/1080*screenheight)))
        self.ERPMLabel.setObjectName("ERPMLabel")
        
        #input for ERPM
        self.ERPMInput = QtWidgets.QLineEdit(self.ERPMBox)
        self.ERPMInput.setGeometry(QtCore.QRect(
            int(0/1920*screenwidth),
            int(40/1080*screenheight),
            int(111/1920*screenwidth),
            int(21/1080*screenheight)))
        self.ERPMInput.setObjectName("ERPMInput")
        
        ############################################################################################
        #code for the rms graphics
        
        #p rms graph
        self.PRMSGraphic = QtWidgets.QGraphicsView(self.leftframe)
        self.PRMSGraphic.setGeometry(QtCore.QRect(
            int(30/1920*screenwidth),
            int(700/1080*screenheight),
            int(280/1920*screenwidth),
            int(241/1080*screenheight)))
        self.PRMSGraphic.setObjectName("PRMSGraphic")
        
        #i rms graph
        self.IRMSGraphic = QtWidgets.QGraphicsView(self.leftframe)
        self.IRMSGraphic.setGeometry(QtCore.QRect(
            int(330/1920*screenwidth),
            int(700/1080*screenheight),
            int(280/1920*screenwidth),
            int(241/1080*screenheight)))
        self.IRMSGraphic.setObjectName("IRMSGraphic")
        
        #p rms label
        self.PRMSLabel = QtWidgets.QLabel(self.leftframe)
        self.PRMSLabel.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(660/1080*screenheight),
            int(121/1920*screenwidth),
            int(31/1080*screenheight)))
        self.PRMSLabel.setObjectName("PRMSLabel")
        
        #i rms label
        self.IRMSLabel = QtWidgets.QLabel(self.leftframe)
        self.IRMSLabel.setGeometry(QtCore.QRect(
            int(330/1920*screenwidth),
            int(660/1080*screenheight),
            int(101/1920*screenwidth),
            int(31/1080*screenheight)))
        self.IRMSLabel.setObjectName("IRMSLabel")
        
        ###############################################################################################

        #adds the left frame to the horizontal layout widget
        self.horizontalLayout.addWidget(self.leftframe)
        
        ################################################################################################
        #creates the middle section of the gui
        self.midframe = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.midframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.midframe.setObjectName("midframe")
        
        #################################################################################################
        #section on speed
        
        #label for speed
        self.speedLabel = QtWidgets.QLabel(self.midframe)
        self.speedLabel.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(30/1080*screenheight),
            int(181/1920*screenwidth),
            int(41/1080*screenheight)))
        self.speedLabel.setObjectName("speedLabel")
        
        #the horizontal slider for speed
        self.SelectSpeed = QtWidgets.QSlider(self.midframe)
        self.SelectSpeed.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(90/1080*screenheight),
            int(600/1920*screenwidth),
            int(22/1080*screenheight)))
        self.SelectSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.SelectSpeed.setObjectName("SelectSpeed")
        
        #the minimal value for speed (0)
        self.label_8 = QtWidgets.QLabel(self.midframe)
        self.label_8.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(110/1080*screenheight),
            int(16/1920*screenwidth),
            int(31/1080*screenheight)))
        self.label_8.setObjectName("label_8")
        
        #the maximum value for speed
        self.label_9 = QtWidgets.QLabel(self.midframe)
        self.label_9.setGeometry(QtCore.QRect(
            int(600/1920*screenwidth),
            int(110/1080*screenheight),
            int(61/1920*screenwidth),
            int(31/1080*screenheight)))
        self.label_9.setObjectName("label_9")
        
        #the graph view for speed
        self.SpeedGraphic = QtWidgets.QGraphicsView(self.midframe)
        self.SpeedGraphic.setGeometry(QtCore.QRect(
            int(20/1920*screenwidth),
            int(150/1080*screenheight),
            int(600/1920*screenwidth),
            int(200/1080*screenheight)))
        self.SpeedGraphic.setObjectName("SpeedGraphic")
        ##########################################################################
        #section on power
        
        #the label for Power
        self.powerLabel  = QtWidgets.QLabel(self.midframe)
        self.powerLabel .setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(390/1080*screenheight),
            int(111/1920*screenwidth),
            int(31/1080*screenheight)))
        self.powerLabel .setObjectName("powerLabel ")
        
        #the slider for power
        self.powerSelect = QtWidgets.QSlider(self.midframe)
        self.powerSelect.setGeometry(QtCore.QRect(
            int(30/1920*screenwidth),
            int(440/1080*screenheight),
            int(251/1080*screenwidth),
            int(21/1080*screenheight)))
        self.powerSelect.setOrientation(QtCore.Qt.Horizontal)
        self.powerSelect.setObjectName("powerSelect")
        
        #the image for power  (probably a traffic light )
        self.powergraphic = QtWidgets.QGraphicsView(self.midframe)
        self.powergraphic.setGeometry(QtCore.QRect(
            int(500/1920*screenwidth),
            int(420/1080*screenheight),
            int(91/1920*screenwidth),
            int(51/1080*screenheight)))
        self.powergraphic.setObjectName("powergraphic")
        
        #############################################################################
        #section on statuses
        
        #the label saying status
        self.statusLabel = QtWidgets.QLabel(self.midframe)
        self.statusLabel.setGeometry(QtCore.QRect(
            int(280/1920*screenwidth),
            int(480/1080*screenheight),
            int(101/1920*screenwidth),
            int(41/1080*screenheight)))
        self.statusLabel.setObjectName("statusLabel")
        
        #where we will hold the list of statuses and how they are
        self.listView = QtWidgets.QListView(self.midframe)
        self.listView.setGeometry(QtCore.QRect(
            int(50/1920*screenwidth),
            int(520/1080*screenheight),
            int(550/1920*screenwidth),
            int(400/1080*screenheight)))
        self.listView.setObjectName("listView")
        ####################################################################################
        
        #adding the middle section to the GUI
        self.horizontalLayout.addWidget(self.midframe)
        
        
        ##################################################################################
        
        #this is the rightside section of the gui 
        self.rightframe = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.rightframe.setObjectName("rightframe")

        #####################################################################################
        #this keeps the right side equally spaced
        self.verticalLayoutWidget = QtWidgets.QWidget(self.rightframe)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(
            int(0/1920*screenwidth),
            int(0/1080*screenheight),
            int(550/1920*screenwidth),
            int(731/1080*screenwidth)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(
            0,
            0, 
            0, 
            0)
        self.verticalLayout.setObjectName("verticalLayout")
    
    
        self.ManualModeLayout_2 = QtWidgets.QVBoxLayout()
        self.ManualModeLayout_2.setObjectName("ManualModeLayout_2")
        
        #################################################################################
        #the box on the right side of the screen above the CMD section 
        self.rightbox = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.rightbox.setMinimumSize(QtCore.QSize(
            0, 
            int(575/1080*screenheight)))
        self.rightbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rightbox.setFrameShape(QtWidgets.QFrame.Box)
        self.rightbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightbox.setMidLineWidth(2)
        self.rightbox.setObjectName("rightbox")
        
        #label saying battery
        self.batteryLabel = QtWidgets.QLabel(self.rightbox)
        self.batteryLabel.setGeometry(QtCore.QRect(
            int(220/1920*screenwidth),
            int(10/1080*screenheight),
            int(161/1920*screenwidth),
            int(61/1080*screenheight)))
        self.batteryLabel.setObjectName("batteryLabel")
        
        #label saying temperature
        self.batteryTemperatureLabel = QtWidgets.QLabel(self.rightbox)
        self.batteryTemperatureLabel.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(80/1080*screenheight),
            int(201/1920*screenwidth),
            int(31/1080*screenheight)))
        self.batteryTemperatureLabel.setObjectName("batteryTemperatureLabel")
        
        #should show current data for temperature on the right 
        self.batteryData = QtWidgets.QGraphicsView(self.rightbox)
        self.batteryData.setGeometry(QtCore.QRect(
            int(200/1920*screenwidth),
            int(83/1080*screenheight),
            int(81/1980*screenwidth),
            int(21/1080*screenheight)))
        self.batteryData.setObjectName("batteryData")
        
        #graph for temperature
        self.batteryTemperatureGrahpicsView = QtWidgets.QGraphicsView(self.rightbox)
        self.batteryTemperatureGrahpicsView.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(120/1080*screenheight),
            int(480/1920*screenwidth),
            int(100/1080*screenheight)))
        self.batteryTemperatureGrahpicsView.setObjectName("textBrowser")
       
       #label saying voltage
        self.voltageLabel = QtWidgets.QLabel(self.rightbox)
        self.voltageLabel.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(250/1080*screenheight),
            int(91/1920*screenwidth),
            int(41/1080*screenheight)))
        self.voltageLabel.setObjectName("voltageLabel")
        
        #should show current data for voltage
        self.voltageData = QtWidgets.QGraphicsView(self.rightbox)
        self.voltageData.setGeometry(QtCore.QRect(
            int(200/1920*screenwidth),
            int(240/1080*screenheight),
            int(81/1920*screenwidth),
            int(21/1080*screenheight)))
        self.voltageData.setObjectName("voltageData")
        
        #the graph for voltage
        self.voltageGraphic = QtWidgets.QGraphicsView(self.rightbox)
        self.voltageGraphic.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(280/1080*screenheight),
            int(480/1920*screenwidth),
            int(100/1080*screenheight)))
        self.voltageGraphic.setObjectName("voltageGraphic")
        
        #label saying discharge rate
        self.dischargeLabel = QtWidgets.QLabel(self.rightbox)
        self.dischargeLabel.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(420/1080*screenheight),
            int(211/1920*screenwidth),
            int(31/1080*screenheight)))
        self.dischargeLabel.setObjectName("dischargeLabel")
        
        #should show current data for discharge
        self.dischargeData = QtWidgets.QGraphicsView(self.rightbox)
        self.dischargeData.setGeometry(QtCore.QRect(
            int(200/1920*screenwidth),
            int(430/1080*screenheight),
            int(81/1920*screenwidth),
            int(21/1080*screenheight)))
        self.dischargeData.setObjectName("dischargeData")
        
        #graph for discharge
        self.dischargeGraphic = QtWidgets.QGraphicsView(self.rightbox)
        self.dischargeGraphic.setGeometry(QtCore.QRect(
            int(40/1920*screenwidth),
            int(460/1080*screenheight),
            int(480/1920*screenwidth),
            int(131/1080*screenheight)))
        self.dischargeGraphic.setObjectName("dischargeGraphic")
        
        ##############################################################################################
        
        #adding the top right box to the 
        self.ManualModeLayout_2.addWidget(self.rightbox)
        
        
        self.ManualModeTop_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.ManualModeTop_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ManualModeTop_2.setObjectName("ManualModeTop_2")

        #the first input for the CMD
        self.ManualModeLineEdit_3 = QtWidgets.QLineEdit(self.ManualModeTop_2)
        self.ManualModeLineEdit_3.setGeometry(QtCore.QRect(
            int(10/1920*screenwidth),
            int(20/1080*screenheight),
            int(400/1920*screenwidth),
            int(20/1080*screenheight)))
        self.ManualModeLineEdit_3.setObjectName("ManualModeLineEdit_3")

        #the button for the CMD
        self.SendCMDButton_3 = QtWidgets.QPushButton(self.ManualModeTop_2)
        self.SendCMDButton_3.setGeometry(QtCore.QRect(
            int(450/1920*screenwidth),
            int(20/1080*screenheight),
            int(75/1920*screenwidth), 
            int(23/1080*screenheight)))
        self.SendCMDButton_3.setObjectName("SendCMDButton_3")

        self.ManualModeLayout_2.addWidget(self.ManualModeTop_2)
        
        #the secondary input for the CMD
        self.ManualModeTextBoxslipbox = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.ManualModeTextBoxslipbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ManualModeTextBoxslipbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ManualModeTextBoxslipbox.setLineWidth(1)
        self.ManualModeTextBoxslipbox.setObjectName("ManualModeTextBoxslipbox")
        self.ManualModeTextEdit_2 = QtWidgets.QTextEdit(self.ManualModeTextBoxslipbox)
        self.ManualModeTextEdit_2.setGeometry(QtCore.QRect(
            int(13/1920*screenwidth),
            int(0),
            int(530/1920*screenwidth),
            int(280/1080*screenheight)))
        self.ManualModeTextEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.ManualModeTextEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ManualModeTextEdit_2.setObjectName("ManualModeTextEdit_2")

        self.ManualModeLayout_2.addWidget(self.ManualModeTextBoxslipbox)
        self.verticalLayout.addLayout(self.ManualModeLayout_2)
        self.horizontalLayout.addWidget(self.rightframe)
        self.DashBoardTitle = QtWidgets.QLabel(self.frame)
        self.DashBoardTitle.setGeometry(QtCore.QRect(
            40,
            20,
            100,
            31))

        self.DashBoardTitle.setObjectName("DashBoardTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        ########################################################################
        #some graphing code
        
        #tempoary graphing data, for testing purposes
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        
        
        #graph for temperature
        
        self.temperatureGraph = GUIgraph.GUIGraph("temperatureGraph", self.temperatureGraphic,0)
        self.temperatureGraph.plot(hour, temperature)
        
        
        
        
        
        
        #graph for prms
        self.PRMSGraph = GUIgraph.GUIGraph("PRMSGraph", self.PRMSGraphic,1)
        self.PRMSGraph.plot(hour, temperature)
        
        
        
        
        
        #graph for rrms
        self.RRMSGraph = GUIgraph.GUIGraph("RRMSGraph", self.IRMSGraphic,2)
        self.RRMSGraph.plot(hour, temperature)
        
        
        
        
        
        #graph for speed
        self.speedGraph = GUIgraph.GUIGraph("speedGraph", self.SpeedGraphic,3)
        self.speedGraph.plot(hour, temperature)
        
        
        
        
        
        #graph for battery temperature
        self.batterytemperature = GUIgraph.GUIGraph("batteryTemperatureGraph", self.batteryTemperatureGrahpicsView,4)
        self.batterytemperature.plot(hour, temperature)
        
        
        
        
        
        
        #graph for Voltages
        self.voltageGraph = GUIgraph.GUIGraph("voltageGraph", self.voltageGraphic,5)
        self.voltageGraph.plot(hour, temperature)
        
        
        
        
        
        #graph for discharge rate
        self.dischargeGraph = GUIgraph.GUIGraph("dischargeGraph", self.dischargeGraphic,6)
        self.dischargeGraph.plot(hour, temperature)
        
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LeftLabel.setText(_translate("MainWindow", "Motors"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">+1</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">-1</span></p></body></html>"))
        self.sliplabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Slip.</span></p></body></html>"))
        self.slipInput.setText(_translate("MainWindow", "Manual Input"))
        self.temperatureLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Temperature</span></p></body></html>"))
        self.ERPMLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">ERPM</span></p></body></html>"))
        self.PRMSLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">P (RMS)</span></p></body></html>"))
        self.IRMSLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">I (RMS)</span></p></body></html>"))
        self.speedLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Speed (KM/H)</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">200</span></p></body></html>"))
        self.powerLabel .setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Power</span></p></body></html>"))
        self.statusLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Status</span></p></body></html>"))
        self.batteryLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Battery</span></p></body></html>"))
        self.batteryTemperatureLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Temperature:</span></p><p><br/></p></body></html>"))
        self.voltageLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Voltage:</span><br/></p></body></html>"))
        self.dischargeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Discharge Rate:</span></p></body></html>"))
        self.SendCMDButton_3.setText(_translate("MainWindow", "Send CMD"))
        self.DashBoardTitle.setText(_translate("MainWindow", "DashBoard"))
        
    def updateGraphs(self):
        self.speedGraph.clear()
        self.speedGraph.plot([1,2,3,4,5],[1,2,34,5,6])
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.showFullScreen()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.updateGraphs()
    MainWindow.show()
    
    sys.exit(app.exec_())
