from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph



class GUIGraph():
    def __init__(self, name, view, recordnumber ):
        
        self.name = name  # name of the graph
        self.view = view # the graphics view the graph is held in 
        self.recordnumber = recordnumber # which record in the csv relates to this graph
        
        self.datashown = [0 for i in range(0,15)] # this is set to read the last 15 pieces of data
        self.pointer = 0
        
        self.pen = pyqtgraph.mkPen(color=(255, 0, 0))
        self.graph = pyqtgraph.PlotWidget(self.view)
        self.graph.setGeometry(QtCore.QRect(0, 0, self.view.width(), self.view.height()))
        self.graph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graph.setBackground('w')
        self.graph.plot(  [0 for i in range(0,len(self.datashown))],   self.datashown,   pen= self.pen)
        

        
        
    ############################################################################################################
    #functions 
    
    def pointernext(self):
        self.pointer += 1 
        if self.pointer == len(self.datashown):
            self.pointer = 0
    
    def plot(self, data):
        self.clear
        self.graph.plot([i for i in range(len(data))], data, pen = self.pen)
        self.datashown = data
        self.pointer = 0            
                #how the plot function works is through through drawing a line
                #the first array details the x axis of the lines points beiing drawn
                #whist the second line is the y asis of hte lines points 
    

        
    def clear(self):
        self.graph.clear()
        self.pointer = 0
        self.datashown = [0 for i in range(len(self.datashown))]
    
    def update(self, data):
        self.datashown[self.pointer] = data
        self.pointernext()
        self.graph.clear()
        
        for i in range (len(self.datashown)):
            
            self.graph.plot( 
                            [i for i in range(0,len(self.datashown))],
                            self.datashown[self.pointer:]+self.datashown[:self.pointer],
                            pen = self.pen
                            )
        
    def dataUpdate(self):
        print("testing")
        with open('simul1.csv', 'r') as csvfile:
            data = csvfile.readlines()
            print(data[self.recordnumber])
            csvfile.close()
            
        
    

        
    
    