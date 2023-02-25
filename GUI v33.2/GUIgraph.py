from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph


class GUIGraph():
    def __init__(self, name, view, recordnumber ):
        self.name = name  # name of the graph
        self.view = view # the graphics view the graph is held in 
        self.recordnumber = recordnumber # which record in the csv relates to this graph
        
        self.graph = pyqtgraph.PlotWidget(self.view)
        self.graph.setGeometry(QtCore.QRect(0, 0, self.view.width(), self.view.height()))
        self.graph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graph.setBackground('w')
        
    def plot(self,hour,temperature, pen):
        self.graph.plot(hour, temperature, pen=pen)