import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class graph():
    def __init__(self, x, y):
        self.test = plt.subplot
        self.test.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
        self.test.axis([0, 6, 0, 20])
        self.test.show()
        
        self.test2 = plt
        self.test2.plot([1, 2, 3, 4], [2, 3, 4, 5], 'ro')
        self.test2.axis([0, 6, 0, 20])
        
        
        self.test.show()
        
#this is going to temperilly be a place to simulate data till we get the ROS TCP connections working 

import random
def graphsimulation():
    pass
    #return(random.randint(200),random.randint(200))

graph(3,5)

    