#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmlutils import getxmlroot
from xmlutils import getxmltree
from filewriter import FileWriter
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
	global NoOfErrors
	global NoOfLinkErrors
	global NoOfTextErrors
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
			#first we need to check if the destination file exists
			file_path = foldername + parts[0]
			if os.path.exists(file_path) :
				otherroot = getxmlroot(file_path)	#get the xml root
				topics = otherroot.findall(".//topic[@id='" + parts[1] + "']")
			else :
				logerrormessage('filenotfound',file_path,getxreftext(xrefelement))
		if topics != None :
			if len(topics) == 0 :
				logerrormessage('linkbreak',getxreftext(xrefelement),"Pointing to:\n" + parts[1])
			elif len(topics) > 1 :
				logerrormessage('mulitpleids',parts[1])
			elif len(topics) == 1:	#if links are fine, the check for sticky text
				title = topics[0].find('title')
				xreftext = getxreftext(xrefelement)
				titletext = cleanstring (title.text)
				if xreftext != titletext :
					logerrormessage('stickytext',"Link text\n" + xreftext, "Title text:\n" + titletext)

def getxreftext(xrefelement) :
	xreftext = None
	if xrefelement.tag == 'xref' :
		xreftext = cleanstring(xrefelement.text)
	elif xrefelement.tag == 'link' :
		linktext = xrefelement.find('linktext')
		xreftext = cleanstring(linktext.text)
	return xreftext


def logerrormessage(errtype,*othermessages) :
	global NoOfErrors
	global NoOfLinkErrors
	global NoOfTextErrors
	NoOfErrors = NoOfErrors + 1
	if errtype == 'linkbreak':
		logger.WriteLine('Link break')
		NoOfLinkErrors = NoOfLinkErrors + 1
	elif errtype == 'stickytext' :
		logger.WriteLine('Sticky text')
		NoOfTextErrors = NoOfTextErrors + 1
	elif errtype == 'filenotfound':
		logger.WriteLine('Destination file not found')
		NoOfLinkErrors = NoOfLinkErrors + 1
	elif errtype == 'mulitpleids':
		logger.WriteLine('more than one topic with this id!!!')
	for othermessage in othermessages :
		logger.WriteLine (othermessage)
	logger.LineSeparator()


def cleanstring (dirtystr):
	#first remove carriage returns from both string. but replace it with a space. just to make sure
	dirtystr = dirtystr.replace("\n",' ')
	#then remove any starting and trailing spaces or multiple spaces
	dirtystr = ' '.join(dirtystr.split())
	return dirtystr

def iteratetree (currentelement) :
	classElements = currentelement.findall("*")
	for classElement in classElements :
		checkhref(classElement)
		iteratetree(classElement)

foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/scripting/'

xmlfiles = glob.glob(foldername + '*.xml')
root = None
logger = FileWriter('dita-link-checker.log')
for xmlfile in xmlfiles :
	NoOfErrors = 0
	NoOfLinkErrors = 0
	NoOfTextErrors = 0
	print (xmlfile)
	logger.WriteLine ('Start: ' + xmlfile)
	root = getxmlroot(xmlfile)	#get the xml dom
	classElements = root.findall("*")
	for classElement in classElements :
		checkhref(classElement)
		iteratetree(classElement)
	#logger.WriteLine('Number of Errors: ' + str(NoOfErrors))
	logger.WriteLine('Number of Link Errors: ' + str(NoOfLinkErrors))
	logger.WriteLine('Number of Text Errors: ' + str(NoOfTextErrors))
	logger.WriteLine ('DONE: ' + xmlfile)
	logger.LineSeparator()
logger.Close()

print ("DONE. You can find the results in:\n" + logger.LogFileName())
