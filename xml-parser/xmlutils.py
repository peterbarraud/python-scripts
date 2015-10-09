#!c:/Python34/python.exe
import xml.etree.ElementTree as ET

def writexmlback (xmlfile,tree) :
	try :
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
	except PermissionError as permissionError:
		print (permissionError)

#use this function if you don't require to write the xml back to file
def getxmlroot(filename) :
	parser = ET.XMLParser()
	parser.entity['nbsp'] = u'\u00A0'	#handle &nsbp; in the source xml file
	tree = ET.parse(filename,parser)	#load the xml document
	return tree.getroot()	#get the xml dom

#use this function if you require to write the xml back to file
def getxmltree(filename) :
	parser = ET.XMLParser()
	parser.entity['nbsp'] = u'\u00A0'	#handle &nsbp; in the source xml file
	return ET.parse(filename,parser)	#load the xml document
