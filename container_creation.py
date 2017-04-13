#!/usr/bin/python
import commands
import subprocess
import sys
import subprocess, sys
from sys import argv
import os
service_name = sys.argv[1]
print service_name
service_name = service_name.lower()
image_name = "citi.docker.com:5000/"+service_name+""
print image_name
#subprocess.Popen("docker build -f /home/shefali/docker/java_tomcat/dockerfile -t "+image_name+" /home/shefali/docker/java_tomcat/", shell=True)
os.system("docker build -f /home/shefali/docker/java_tomcat/dockerfile -t "+image_name+" /home/shefali/docker/java_tomcat/")
#subprocess.Popen("docker push "+image_name+"", shell=True)
os.system("docker push "+image_name+"")
#subprocess.Popen("docker service create --network my_network --name "+service_name+" "+image_name+"", shell=True)
os.system("docker service create --network my_network -p $port:8080 --name "+service_name+" "+image_name+"")
print "done"  
