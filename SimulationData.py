import csv
import random
import time

# open the csv file

    # create a csv writer object
    
    
    # create 5 columns
    # currently all generated numbers are random between 0 to 99 
    
while(True):
                                                      #the program opens the csv file here
  with open('simul1.csv', 'a') as csvfile:
    
    
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([random.randint(0, 100),
                        random.randint(0, 100),
                        random.randint(0,100),
                        random.randint(0,100),
                        random.randint(0,100),
                        random.randint(0,100),
                        random.randint(0,100)
                        ])
    csvfile.close()                                  #we close the csv file to save the generated data properly
                                                     #so that other applicaions may access the data
    
  time.sleep(1)                                      # program sleeps for 1 second before generating new data