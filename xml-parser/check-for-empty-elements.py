#!c:/Python34/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py
import glob
import os
import sys
from filewriter import FileWriter
from xmlutils import getxmltree

foldername = 'C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/fm/scripting/'

xmlfiles = glob.glob(foldername + '*.xml')
logger = FileWriter('check-for-empty-elements.log')

for xmlfile in xmlfiles :
	print (xmlfile)
	logger.WriteLine ('Start: ' + xmlfile)
	tree = getxmltree(xmlfile)	#get the xml dom
	root = tree.getroot()
	for element in tree.iter():
		if element.tag == 'body' or element.tag == 'li' or element.tag == '' :
			children = element.findall("*")
			if len(children) == 0 and (element.text == None or element.text == ''):
				logger.WriteLine (element.tag)
logger.Close()





print ("DONE. You can find the results in:\n" + logger.LogFileName())
