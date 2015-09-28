#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ElementTree
import glob
import os
import sys

def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if iselementempty(classElement) :
			currentelement.remove(classElement)
		iteratetree(classElement)

def writechanges (tree,filename) :
	tree.write(filename)
	with open(filename, 'r+') as f:
		content = f.read()
		f.seek(0, 0)		#make sure you get to the start of the file
		f.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
		f.write('<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Composite//EN" "technicalContent/dtd/ditabase.dtd" [' + "\n")
		f.write('<!-- Begin Document Specific Declarations -->' + "\n")
		f.write('<!-- End Document Specific Declarations -->' + "\n")
		f.write(']>' + "\n")
		f.write(content)
		f.close()

def iselementempty(element) :
	return element.tag == 'li' and len(element.findall("*")) == 0 and element.text == None
		

xmlfiles = glob.glob('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/*.xml')
for xmlfile in xmlfiles :
	print xmlfile
	tree = ElementTree.parse(xmlfile)	#load the xml document
	root = tree.getroot()	#get the xml dom
	classElements = root.findall("*")
	for classElement in classElements :
		if iselementempty(classElement) :
			root.remove(classElement)
		iteratetree(classElement)
	writechanges(tree,xmlfile + 'new')

print "done"