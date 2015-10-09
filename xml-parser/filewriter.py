#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py
import os

class FileWriter:
    def __init__(self,filename=''):
        if filename == '' :
            filename = os.path.basename(__file__) + '.log'
        self.filename = filename
        self.target = open(filename, 'w')
    def Close(self):
        self.target.close()
    def Write(self,content):
        self.target.write(content)
    def WriteLine(self,content):
        self.target.write (content + "\n")
    def LineSeparator (self):
        self.WriteLine('================================================')
    def LogFileName(self):
        return self.filename
