#!c:/Python27/python.exe
#execute this file on the bash prompt with: chmod +x first-parse.py && first-parse.py

import glob

xmlfiles = glob.glob('C:/aaWork/p4v_ws/theoden/depot/EN/Docs/TechComm Suite/2015/rh/user-guide/*.xml')
for xmlfile in xmlfiles :
	print xmlfile
