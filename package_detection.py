#!/usr/bin/python
import sys
import subprocess
package_name = sys.argv[1]
print "package_name :: "+package_name
result = subprocess.check_output(["dpkg","-s",package_name])
if "Status: install ok installed" in result:
     print ""+package_name+" is installed"
else: 
     print ""+package_name+" is not installed"
