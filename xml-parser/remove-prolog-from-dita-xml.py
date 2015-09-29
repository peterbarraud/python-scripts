#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET
import glob
import os
import sys

def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if classElement.tag == 'prolog' :
			currentelement.remove(classElement)
			#print classElement.tag	#tag name
		iteratetree(classElement)

def writechanges (tree,filename) :
	tree.write(xmlfile)
	with open(xmlfile, 'r+') as f:
		content = f.read()
		f.seek(0, 0)		#make sure you get to the start of the file
		f.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
		f.write('<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Composite//EN" "technicalContent/dtd/ditabase.dtd" [' + "\n")
		f.write('<!-- Begin Document Specific Declarations -->' + "\n")
		f.write('<!-- End Document Specific Declarations -->' + "\n")
		f.write(']>' + "\n")
		f.write(content)
		f.close()			



xmlfiles = glob.glob('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/scripting/*.xml')
for xmlfile in xmlfiles :
	print xmlfile
	tree = ET.parse(xmlfile)	#load the xml document
	root = tree.getroot()	#get the xml dom
	classElements = root.findall("*")
	for classElement in classElements :
		if classElement.tag == 'prolog' :
			root.remove(classElement)
		iteratetree(classElement)
	try :
		writechanges(tree,xmlfile)
	except:
		print sys.exc_info()[0]
		

print "done"