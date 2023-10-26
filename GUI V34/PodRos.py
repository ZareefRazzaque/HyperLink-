import rclpy
from rclpy.node import Node

from std_msgs.msg import *



class DataPublisher(Node):
    def __init__(self):
        self.savedTopics = {}
        try :
            self.node = rclpy.create_node('data')
        except: pass
        
    def getNode(self):
        return self.node
        
        
    def getPublisher(self, dataName):
        
        try:
            publisher = self.savedTopics[dataName]
            
        except:
            publisher = self.node.create_publisher(Int32, dataName, 10)
            self.savedTopics[dataName] = publisher
        return publisher
    
    
    
    class DataListener(Node):
            
        def __init__(self):
            try :
                self.node = rclpy.create_node('data')
            except: pass
        
        def createSubscription(self, Topic):
            newSubscription = 
                
                    
                    
            
            
    
    
    
    
    
    
        

        
        
        
        
        