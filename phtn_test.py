#!/usr/bin/python
#from sys import argv
from subprocess import call
import os
import commands
import re
import sys
from HTMLParser import HTMLParser

#print 'Number of arguments:', sys.argv, 'arguments.'
file_to_be_search=sys.argv[1]
#print file_to_be_search
search_word=sys.argv[2]
#print search_word


#result = os.popen("curl http://10.101.3.141/package_repository/debian/").read()
result = os.popen("curl -s "+ file_to_be_search).read()
#subprocess.check_output(["curl", "-k", "-s" ,  '--data-binary' ,etree.tostring(root) ,file_to_be_search],stderr=subprocess.STDOUT)

#print result
temp = []
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   #print name, "=", value
		   temp.append(value)
	   		#print str(temp)


parser = MyHTMLParser()
parser.feed(result)

for idx, word in enumerate(temp):
    #print idx, word
	if search_word in word:
		print word
