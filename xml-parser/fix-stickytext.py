#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmldom import getxmlroot
import glob
import os
import sys

	

def writechanges (xmlfile) :
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

def check_and_fix_stickytext(xrefelement) :
	if 'scope' in xrefelement.attrib:
		return;
	parts = xrefelement.attrib['href'].split('#')
	topics = None
	if parts[0] == '' :	#within this file
		topics = root.findall(".//topic[@id='" + parts[1] + "']")
	else :
		otherroot = getxmlroot(foldername + parts[0])
		topics = otherroot.findall(".//topic[@id='" + parts[1] + "']")
	if len(topics) == 1:	#link is fine so lets check the sticky text
		title = topics[0].find('title')
		if title.text != xrefelement.text :
			print (title.text)
			print (xrefelement.text)
			print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
			xrefelement.text = title.text
			global changemade
			changemade = changemade + 1
def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if classElement.tag == 'xref' :
			check_and_fix_stickytext(classElement)
		iteratetree(classElement)

		
foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/'
changemade = 0
xmlfile = foldername + 'rob_layouts_la.xml'
root = getxmlroot(xmlfile)
classElements = root.findall("*")
for classElement in classElements :
	if classElement.tag == 'xref' :
		check_and_fix_stickytext(classElement)
	iteratetree(classElement)
if changemade > 0 :
	writechanges(xmlfile)

#xmlfiles = glob.glob(foldername + '*.xml')
#for xmlfile in xmlfiles :
#	print xmlfile
#	tree = ET.parse(xmlfile)	#load the xml document
#	root = tree.getroot()	#get the xml dom
#	classElements = root.findall("*")
#	for classElement in classElements :
#		if classElement.tag == 'xref' :
#			checklink(classElement)
#		iteratetree(classElement,root)

print ("done")