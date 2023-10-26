


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as graph 
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
        self.listView.setGeometry(QtCore.QRect(int((20/1290)*screenwidth), int((400/891)*screenheight), int((391/1290)*screenwidth), int((440/981)*screenheight)))
        self.listView.setObjectName("listView")
        self.checkBox = QtWidgets.QCheckBox(self.midframe)
        self.checkBox.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(410/891*screenheight), 170, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_2.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(490/891*screenheight), 170, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_3.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(470/891*screenheight), 300, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_4.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(450/891*screenheight), 200, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_5.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(430/891*screenheight), 200, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.midframe)
        self.pushButton.setGeometry(QtCore.QRect(int(250/1290*screenwidth), int(540/891*screenheight), 170, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.midframe)
        self.pushButton_2.setGeometry(QtCore.QRect(int(250/1290*screenwidth), int(610/891*screenheight), 170, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.midframe)
        self.pushButton_3.setGeometry(QtCore.QRect(int(250/1290*screenwidth), int(680/891*screenheight), 170, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_6 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_6.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(510/891*screenheight), 170, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_7.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(530/891*screenheight), 250, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_8.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(550/891*screenheight), 170, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_9.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(570/891*screenheight), 170, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_10.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(590/891*screenheight), 170, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_11.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(630/891*screenheight), 170, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_12.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(610/891*screenheight), 220, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_13.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(650/891*screenheight), 170, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_14.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(670/891*screenheight), 170, 17))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_15.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(690/891*screenheight), 250, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_16.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(730/891*screenheight), 251, 17))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_17.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(750/891*screenheight), 250, 17))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_18.setGeometry(QtCore.QRect(int(30/1290*screenwidth), int(710/891*screenheight), 281, 17))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_19.setGeometry(QtCore.QRect(int(240/1290*screenwidth), int(410/891*screenheight), 171, 16))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_20.setGeometry(QtCore.QRect(int(240/1290*screenwidth), int(430/891*screenheight), 171, 16))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.midframe)
        self.checkBox_21.setGeometry(QtCore.QRect(int(240/1290*screenwidth), int(450/891*screenheight), 171, 16))
        self.checkBox_21.setObjectName("checkBox_21")
        self.label_16 = QtWidgets.QLabel(self.midframe)
        self.label_16.setGeometry(QtCore.QRect(int(240/1290*screenwidth), int(500/891*1080), 170, 16))
        self.label_16.setObjectName("label_16")

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
        pen = graph.mkPen(color=(255, 0, 0))
        
        #graph for temperature
        self.temperatureGraph = graph.PlotWidget(self.temperatureGraphic)
        self.temperatureGraph.setGeometry(QtCore.QRect(0, 0, self.temperatureGraphic.width(), self.temperatureGraphic.height()))
        self.temperatureGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.temperatureGraph.setBackground('w')
        self.temperatureGraph.plot(hour, temperature, pen=pen)
        
        
        
        
        
        #graph for prms
        self.PRMSGraph = graph.PlotWidget(self.PRMSGraphic)
        self.PRMSGraph.setGeometry(QtCore.QRect(0, 0, self.PRMSGraphic.width(), self.PRMSGraphic.height()))
        self.PRMSGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.PRMSGraph.setBackground('w')
        self.PRMSGraph.plot(hour, temperature, pen=pen)
        
        
        
        
        
        #graph for rrms
        self.RRMSGraph = graph.PlotWidget(self.IRMSGraphic)
        self.RRMSGraph.setGeometry(QtCore.QRect(0, 0, self.IRMSGraphic.width(), self.IRMSGraphic.height()))
        self.RRMSGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.RRMSGraph.setBackground('w')
        self.RRMSGraph.plot(hour, temperature, pen=pen)
        
        
        
        
        
        #graph for speed
        self.speedGraph = graph.PlotWidget(self.SpeedGraphic)
        self.speedGraph.setGeometry(QtCore.QRect(0, 0, self.SpeedGraphic.width(), self.SpeedGraphic.height()))
        self.speedGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.speedGraph.setBackground('w')
        self.speedGraph.plot(hour, temperature, pen=pen)
        
        
        
        
        
        #graph for battery temperature
        self.batterytemperature = graph.PlotWidget(self.batteryTemperatureGrahpicsView)
        self.batterytemperature.setGeometry(QtCore.QRect(0, 0, self.batteryTemperatureGrahpicsView.width(), self.batteryTemperatureGrahpicsView.height()))
        self.batterytemperature.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.batterytemperature.setBackground('w')
        self.batterytemperature.plot(hour, temperature, pen=pen)
        
        
        
        
        
        
        #graph for Voltages
        self.voltageGraph = graph.PlotWidget(self.voltageGraphic)
        self.voltageGraph.setGeometry(QtCore.QRect(0, 0, self.voltageGraphic.width(), self.voltageGraphic.height()))
        self.voltageGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.voltageGraph.setBackground('w')
        self.voltageGraph.plot(hour, temperature, pen=pen)
        
        
        
        
        
        #graph for discharge rate
        self.DischargeGraph = graph.PlotWidget(self.dischargeGraphic)
        self.DischargeGraph.setGeometry(QtCore.QRect(0, 0, self.dischargeGraphic.width(), self.dischargeGraphic.height()))
        self.DischargeGraph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.DischargeGraph.setBackground('w')
        self.DischargeGraph.plot(hour, temperature, pen=pen)
        
        
        
        

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
        self.checkBox.setText(_translate("MainWindow", "Live LED Off"))
        self.checkBox_2.setText(_translate("MainWindow", "LV Switch Closed"))
        self.checkBox_3.setText(_translate("MainWindow", "Emergancy Stop Closed"))
        self.checkBox_4.setText(_translate("MainWindow", "Motor Live LED Off"))
        self.checkBox_5.setText(_translate("MainWindow", "Brake Live LED Off"))
        self.pushButton.setText(_translate("MainWindow", "Arm Pod"))
        self.pushButton_2.setText(_translate("MainWindow", "Abort Pod"))
        self.pushButton_2.setStyleSheet("background-color : red")
        self.pushButton_3.setText(_translate("MainWindow", "Launch Pod"))
        self.checkBox_6.setText(_translate("MainWindow", "LV Live LED On"))
        self.checkBox_7.setText(_translate("MainWindow", "On Borad Electronics Active"))
        self.checkBox_8.setText(_translate("MainWindow", "Relay R2 Closed"))
        self.checkBox_9.setText(_translate("MainWindow", "Relay R3 Closed"))
        self.checkBox_10.setText(_translate("MainWindow", "Relay R4 Closed"))
        self.checkBox_11.setText(_translate("MainWindow", "Relay R4 Closed"))
        self.checkBox_12.setText(_translate("MainWindow", "HVR1 and HVR2 Closed"))
        self.checkBox_13.setText(_translate("MainWindow", "HV Live LED On"))
        self.checkBox_14.setText(_translate("MainWindow", "Brake Live LED On"))
        self.checkBox_15.setText(_translate("MainWindow", "Open, Close: R2, R3, R4"))
        self.checkBox_16.setText(_translate("MainWindow", "Open, Close: HVR1, HVR2"))
        self.checkBox_17.setText(_translate("MainWindow", "Break Live LED Off"))
        self.checkBox_18.setText(_translate("MainWindow", "Did Break and Motor Live Turn off"))
        self.checkBox_19.setText(_translate("MainWindow", "Disengage Manual Brake Locks"))
        self.checkBox_20.setText(_translate("MainWindow", "R5 Closed"))
        self.checkBox_21.setText(_translate("MainWindow", "Motor Live LED Active"))
        self.label_16.setText(_translate("MainWindow", "Automatic Checks:"))
        
    def updateGraphs(self):
        self.DischargeGraph.clear()
        self.DischargeGraph.plot([1,2,3,4,5,6,7,8,9,10],[50,12,35,66,33,22,21,32,35,45], pen=graph.mkPen(color=(255, 0, 0)) )
            


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
