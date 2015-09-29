#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import xml.etree.ElementTree as ET
import glob
import os
import sys

def checklink (xrefelement,root) :
	#now there can be three link destinations
	#1. external (scope = external) 
	#2.	internal within this xml
	#3.	internal in another xml but within this folder
	if 'scope' in xrefelement.attrib :	#1. external (scope = external) 
		pass
		#print xrefelement.attrib['href']
	else :
		parts = xrefelement.attrib['href'].split('#')
		if parts[0] == '' :	#within this file
			#print parts[1]
			#print "//topic[@id='" + parts[1] + "']"
			topics = root.findall(".//topic[@id='" + parts[1] + "']")
			if len(topics) == 0 :
				print 'broken link'
				print xrefelement.text
			elif len(topics) > 1 :
				print 'more than one topic with this id!!!'
		else :	#within this folder
			tree = ET.parse(foldername + parts[0])	#load the xml document
			otherroot = tree.getroot()	#get the xml dom
			topics = otherroot.findall(".//topic[@id='" + parts[1] + "']")
			if len(topics) == 0 :
				print 'broken link'
				print xrefelement.text
			elif len(topics) > 1 :
				print 'more than one topic with this id!!!'
			#print xrefelement.attrib['href']

def iteratetree (currentelement,root) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if classElement.tag == 'xref' :
			checklink(classElement,root)
		iteratetree(classElement,root)

		
foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/'
tree = ET.parse('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/rob_layouts_la.xml')	#load the xml document
root = tree.getroot()	#get the xml dom
classElements = root.findall("*")
for classElement in classElements :
	if classElement.tag == 'xref' :
		checklink(classElement)
	iteratetree(classElement,root)
		
		
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

print "done"