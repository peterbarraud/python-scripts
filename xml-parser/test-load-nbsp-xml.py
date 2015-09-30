#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET

def getxmlroot(filename) :
	parser = ET.XMLParser()
	parser.entity['nbsp'] = u'\u00A0'	#handle &nsbp; in the source xml file
	tree = ET.parse(filename,parser)	#load the xml document
	return tree.getroot()	#get the xml dom