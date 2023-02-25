import csv
import random
import time
from datetime import datetime


#these are the functions that create the simulation data for each sensor we are tracking 

def generatePodTemperature():
  return random.randint(0,100)
  
  
  
def generatePRMS():
  return random.randint(0,100)



def generateIRMS():
  return random.randint(0,100)
  
  
  
def generateSpeed():
  return random.randint(0,100)
  
  
  
def generateBatteryTemp():
  return random.randint(0,100)
  
  
  
def generateVoltage():
  return random.randint(0,100)
  
  

def generateDischargeRate():
  return random.randint(0,100)









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
                        generatePodTemperature(),
                        generatePRMS(),
                        generateIRMS(),
                        generateSpeed(),
                        generateBatteryTemp(),
                        generateVoltage(),
                        generateDischargeRate()
                        ])
    csvfile.close()                                  #we close the csv file to save the generated data properly
                                                     #so that other applicaions may access the data
    
  time.sleep(1)                                      # program sleeps for 1 second before generating new data