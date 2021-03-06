'''
Contains the classes: 
    - AverageYear
'''
import numpy as np
import Observer

class AverageYear(Observer):
    '''
    Has method: average_anomaly() which returns the average anomaly over the 5 years that are 
    provided by the reader class
    '''
    def __init__(self, reader):
        # pass it the reader object
        self.reader = reader

    
    def average_anomaly(self):
        pass

    def update(self):
        pass
