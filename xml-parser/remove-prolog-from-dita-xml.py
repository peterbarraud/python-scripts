#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET
tree = ET.parse('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/rob_editformat_ed.xml')	#load the xml document
root = tree.getroot()	#get the xml dom

def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if classElement.tag == 'prolog' :
			currentelement.remove(classElement)
			#print classElement.tag	#tag name
		iteratetree(classElement)



#print root
#let's xpath some stuff
#get all elements with the attrib "class" defined
classElements = root.findall("*")
for classElement in classElements :
	if classElement.tag == 'prolog' :
		root.remove(classElement)
		#print classElement.tag	#tag name
	iteratetree(classElement)
	
#write back
tree.write("test-file-writeback.xml")

print "done"