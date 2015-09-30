#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmldom import getxmlroot
import glob
import os
import sys

def checklink (xrefelement,root) :
	#now there can be three link destinations
	#1. external (scope = external) 
	#2.	internal within this xml
	#3.	internal in another xml but within this folder
	if 'scope' in xrefelement.attrib :	#1. external (scope = external) 
		pass	#for now we are not checking for external links
	else :
		parts = xrefelement.attrib['href'].split('#')
		if parts[0] == '' :	#within this file
			topics = root.findall(".//topic[@id='" + parts[1] + "']")
			if len(topics) == 0 :
				print ('broken link')
				print (xrefelement.text)
			elif len(topics) > 1 :
				print ('more than one topic with this id!!!')
			elif len(topics) == 1:	#if links are fine, the check for sticky text
				title = topics[0].find('title')
				if xrefelement.text != title.text :
					print (xrefelement.text)
					print (title.text)
					print ('xxxxxxxxxxxxxxxxxxxx')
		else :	#within this folder
			otherroot = getxmlroot(foldername + parts[0])	#get the xml root
			topics = otherroot.findall(".//topic[@id='" + parts[1] + "']")
			if len(topics) == 0 :
				print ('broken link')
				print (xrefelement.text)
			elif len(topics) > 1 :
				print ('more than one topic with this id!!!')
			#print xrefelement.attrib['href']

def iteratetree (currentelement,root) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		if classElement.tag == 'xref' :
			checklink(classElement,root)
		iteratetree(classElement,root)

		
foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/user-guide/'		
		
xmlfiles = glob.glob(foldername + '*.xml')
for xmlfile in xmlfiles :
	print (xmlfile)
	root = getxmlroot(xmlfile)	#get the xml dom
	classElements = root.findall("*")
	for classElement in classElements :
		if classElement.tag == 'xref' :
			checklink(classElement)
		iteratetree(classElement,root)

print ("done")