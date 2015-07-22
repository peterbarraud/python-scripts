#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET
tree = ET.parse('test-file.xml')	#load the xml document
root = tree.getroot()	#get the xml dom

#print root
#let's xpath some stuff
#get all elements with the attrib "class" defined
classElements = root.findall(".//*[@class]")
for classElement in classElements :
	print classElement.tag	#tag name
	print classElement.attrib["class"]	#class attrib value
	#TODO: Remove attribues
	
#write back
tree.write("test-file-writeback.xml")

print "done"