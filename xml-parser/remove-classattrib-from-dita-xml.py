#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmldom import getxmlroot
import glob
import os
import sys

def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if 'class' in classElement.attrib :
			del classElement.attrib['class']
			global changemade
			changemade = changemade + 1
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


xmlfiles = glob.glob('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/scripting/*.xml')
changemade = 0
for xmlfile in xmlfiles :
	print (xmlfile)
	root = getxmlroot(xmlfile)
	classElements = root.findall("*")
	for classElement in classElements :
		if 'class' in classElement.attrib :
			del classElement.attrib['class']
			changemade = changemade + 1
		iteratetree(classElement)
	try :
		if changemade > 0 :
			writechanges(tree,xmlfile)
	except:
		print (sys.exc_info()[0])

print ("done")