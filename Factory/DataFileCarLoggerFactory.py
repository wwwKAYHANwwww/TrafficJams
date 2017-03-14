import sys
sys.path.append("..") 
from Logger.DataFileCarLogger import DataFileCarLogger
from Factory.ILoggerFactory import ILoggerFactory

class DataFileCarLoggerFactory(ILoggerFactory):
    
    def __init__(self):
        pass;
    
    def getLogger(self):
        return DataFileCarLogger()