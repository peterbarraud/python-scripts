#!c:/Python27/python.exe
import httplib
from HTMLParser import HTMLParser
from urlparse import urljoin
import urllib2
import urllib
from urlparse import urlparse

def test_link() :
	#get the page response
	response = urllib2.urlopen(page_link)
	#get the page HTML
	html = response.read()
	#set the HTML parser callback
	parser = MyHTMLParser()
	parser.feed(html)

class MyHTMLParser(HTMLParser):	
	def handle_starttag(self, tag, attrs):
		if tag == "a" :
			global bad_link
			bad_link = 0
			for attr in attrs :
				if attr[0] == 'href' :
					#urljoin to join and create absolute links out of relative page links
					link_to_test = urljoin(page_link,attr[1])
					#we've seen that hitting pages behind a password (eg ftp) throw errors
					#let's not exclude these. let's log them
					print "Checking: " + link_to_test
					try :
						if urllib.urlopen(link_to_test).getcode() != 200 :
							bad_link = 1
							bad_link_counter += 1
					except IOError as err:
						print "I/O error({0}): {1}".format(err.errno, err.strerror)
					except :
						print "Unexpected error:", sys.exc_info()[0]
		else :
			bad_link = 0
	def handle_data(self, data):
		if bad_link == 1 :
			print "Link: " + data + " is broken"
		
	
# instantiate the parser and feed it some HTML
bad_link = 0;
bad_link_counter = 0
page_link = 'https://helpx.adobe.com/indesign/using/files-templates.html'
test_link()
print "{0} bad links were found.".format(bad_link_counter)
print "done"