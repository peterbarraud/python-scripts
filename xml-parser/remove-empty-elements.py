#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

from xmlutils import getxmltree
from xmlutils import writexmlback
from filewriter import FileWriter
import glob
import os
import sys

def removeelement(parent,element) :
	if element.tag in elementstoremove :
		children = element.findall("*")
		if len(children) == 0 and (element.text == None or element.text == '') :
			filewriter.WriteLine(element.tag)
			parent.remove(element)
			global changemade
			changemade = 1


def iteratetree (currentelement) :
	elements = currentelement.findall("*")
	for element in elements :
		removeelement(currentelement,element)
		iteratetree(element)

foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/scripting/'

xmlfiles = glob.glob(foldername + '*.xml')
changemade = 0
filewriter = FileWriter('remove-empty-elements.log')
# elementstoremove = ['body','li','dd','ol','note']
elementstoremove = ['body']
for xmlfile in xmlfiles :
	print (xmlfile)
	filewriter.WriteLine(xmlfile)
	changemade = 0
	tree = getxmltree(xmlfile)	#load the xml document
	root = tree.getroot()	#get the xml dom
	elements = root.findall("*")
	for element in elements :
		removeelement(root,element)
		iteratetree(element)
	writexmlback(xmlfile,tree)

filewriter.Close()
print ("done")
