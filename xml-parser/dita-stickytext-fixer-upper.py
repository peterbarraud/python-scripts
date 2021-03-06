#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmlutils import getxmltree
from xmlutils import getxmlroot
from filewriter import FileWriter
from xmlutils import writexmlback
import glob
import os
import sys

def checkhref (hrefelement) :
	#since the href attribute can exist in any element, let's simply only for this attribute and not for any specific element
	if 'href' in hrefelement.attrib :
		if hrefelement.tag == 'image':
			pass
		elif hrefelement.tag == 'link' or hrefelement.tag == 'xref':
			checklink(hrefelement)
def checklink (xrefelement) :
	#since the href attribute can exist in any element, let's simply only for this attribute and not for any specific element

	#now there can be three link destinations
	#1. external (scope = external)
	#2.	internal within this xml
	#3.	internal in another xml but within this folder
	if 'scope' in xrefelement.attrib :	#1. external (scope = external)
		pass	#for now we are not checking for external links
	else :
		parts = xrefelement.attrib['href'].split('#')
		topics = None
		if parts[0] == '' :	#within this file
			topics = root.findall(".//topic[@id='" + parts[1] + "']")
		else :	#within this folder
			otherroot = getxmlroot(foldername + parts[0])	#get the xml root
			topics = otherroot.findall(".//topic[@id='" + parts[1] + "']")
		if len(topics) == 1:	#if links are fine, the check for sticky text
			title = topics[0].find('title')
			xreftext = None
			if xrefelement.tag == 'xref' :
				xreftext = xrefelement.text
			elif xrefelement.tag == 'link' :
				linktextelement = xrefelement.find('linktext')
				xreftext = linktextelement.text
			if xreftext != title.text :
				if xrefelement.tag == 'xref' :
					xrefelement.text = title.text
					xrefelement.attrib['outputclass'] = 'fm:'
					global changemade
					changemade = 1
				elif xrefelement.tag == 'link' :
					linktextelement = xrefelement.find('linktext')
					xrefelement.attrib['outputclass'] = 'fm:'
					linktextelement.text = title.text
					global changemade
					changemade = 1


def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		checkhref(classElement)
		iteratetree(classElement)


foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/'

xmlfiles = glob.glob(foldername + '*.xml')
root = None
logger = FileWriter('dita-stickytext-fixer-upper.log')
changemade = 0

for xmlfile in xmlfiles :
	print (xmlfile)
	logger.WriteLine ('Start: ' + xmlfile)
	root = getxmlroot(xmlfile)
	classElements = root.findall("*")
	for classElement in classElements :
		checkhref(classElement)
		iteratetree(classElement)
	if changemade == 1:
		writexmlback(xmlfile,tree)
	logger.WriteLine ('DONE: ' + xmlfile)
logger.Close()



print ("DONE. You can find the results in:\n" + logger.LogFileName())
