#!c:/Python27/python.exe

#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET
tree = ET.parse('test-file.xml')	#load the xml document
root = tree.getroot()	#get the xml dom
print root
