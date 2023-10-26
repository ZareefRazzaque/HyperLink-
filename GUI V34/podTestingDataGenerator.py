import csv
import random
import time
from datetime import datetime
import rclpy
import PodRos

from std_msgs.msg import *

if __name__== '__main__':
  rclpy.init()
  datapublisher = PodRos.DataPublisher()

#these are the functions that create the simulation data for each sensor we are tracking
DataNode = datapublisher.getNode()
PodtempPublisher = datapublisher.getPublisher('PodTemp')
PRMSPublisher = datapublisher.getPublisher('PRMS')
IRMSPublisher = datapublisher.getPublisher('IRMS')
SpeedPublisher = datapublisher.getPublisher('Speed')
BatteryTempPublisher = datapublisher.getPublisher('BatteryTemp')
VoltagePublisher = datapublisher.getPublisher('Voltage')
DischargeRatePublisher = datapublisher.getPublisher('DischargeRate')

def generatePodTemp():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  PodtempPublisher.publish(msg)
  print(data)
  return data
  
  
def generatePRMS():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  PRMSPublisher.publish(msg)
  print(data)
  return data
  



def generateIRMS():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  IRMSPublisher.publish(msg)
  print(data)
  return data
    
  
  
  
def generateSpeed():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  SpeedPublisher.publish(msg)
  print(data)
  return data
  
  
  
  
def generateBatteryTemp():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  BatteryTempPublisher.publish(msg)
  print(data)
  return data

  
  
  
def generateVoltage():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  VoltagePublisher.publish(msg)
  print(data)
  return data
  
  

def generateDischargeRate():
  data = random.randint(0,100)
  msg = Int32()
  msg.data = data
  DischargeRatePublisher.publish(msg)
  print(data)
  return data
  









  ##########################################################################################################################################  
    
    # creates 5 columns
    # currently all generated numbers are random between 0 to 99 
    
with open('simul1.csv', 'w') as csvfile: #upon starting, the program creates a fresh csv file
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(["Pod Temperature",
                      "PRMS",
                      "IRMS",
                      "Speed",
                      "Battery Temperature",
                      "Voltage",
                      "Discharge Rate",
                      datetime.now()
                      ])
  csvfile.close() 
    
while(True):
                                                      #the program opens the csv file here
  with open('simul1.csv', 'a') as csvfile:
    
    
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([
                        generatePodTemp(),
                        generatePRMS(),
                        generateIRMS(),
                        generateSpeed(),
                        generateBatteryTemp(),
                        generateVoltage(),
                        generateDischargeRate()
                        ])
    csvfile.close()    
    #we close the csv file to save the generated data properly
                                                     #so that other applicaions may access the data
    
  time.sleep(1)                                      # program sleeps for 1 second before generating new data