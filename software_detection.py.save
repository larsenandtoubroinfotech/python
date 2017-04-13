#!/usr/bin/python
from sys import argv
import 
from subprocess import call
import os
import commands
import sys
import subprocess, sys
print sys.argv
script_name , app_file = argv 
print app_file
file_extension = app_file.split(".")[1]
print file_extension
app_path = "/home/shefali/app"

#function
def java_application( app_file ):
  print app_file
  #os.system("echo "+app_file)
  #class_file = os.system("jar tf /home/shefali/app/"+app_file+ "| grep -F .class | head -1")
  #var = os.system(" echo hii")
  # call('echo `jar tf app_path/app_file | grep -F ".class" | head -1`')
  #print var
  #import commands
  status , class_file = commands.getstatusoutput("jar tf /home/shefali/app/"+app_file+ "| grep -F .class | head -1")
  print class_file
  #os.system(" cd /home/shefali/app/ && ls")
  #os.system("ls")
  status , sssss = commands.getstatusoutput(" cd /home/shefali/app/ && jar xvf"+app_file+" "+class_file+" ")
  status , major_version = commands.getstatusoutput("cd /home/shefali/app/ && javap -cp "+app_file+" -verbose " +class_file+ " | grep major")
  print major_version
  major_version_n = major_version.split(":")[1]
  print major_version_n
  major_version_n_n = major_version_n.split(" ")[1]
  print major_version_n_n
  string_var = open('/home/shefali/scripts/jdk_version').read()
  print string_var  
  if major_version_n_n in open('/home/shefali/scripts/jdk_version').read():
    print "true"
   
  if major_version_n_n in string_var:
    print "true"
  
  print major_version_n 
  #with open ('/home/shefali/scripts/jdk_version', 'rt') as jdk_version_file: # Open file lorem.txt for reading of text data.
  jdk_version_file = open('/home/shefali/scripts/jdk_version')
  for line in jdk_version_file: # Store each line in a string variable "line"
    if line.startswith(""+major_version_n_n+":"):
      print(line) # prints that line
      java_version = line.split(":")[1]
      print java_version

      temp = java_version.split(".")[1]
      print temp

      apache_tomcat="apache-tomcat-"+temp+""
      print apache_tomcat
      java_software="jdk-"+temp+""
      print java_software
          
     # import glob, os
      #os.chdir("/home/shefali/software")
      #for file in glob.glob("jdk-"+temp+"*"):
       # print(file)

 # with file = open('/home/shefali/docker/app_java_dockerfile', 'r') :
 # filedata = file.read()
 # filedata.replace('$java_software', '')
 # filedata.replace('$app_name', '')
 # filedata.replace('$tomcat_software', '')

if file_extension == "war":
  java_application( app_file )


apache_link="http://10.101.3.141/package_repository/debian/"
subprocess.call(['python' , 'phtn_test.py'] + "http://10.101.3.141/package_repository/debian/" + "apache_tomcat-7")

os.system("python phtn_test.py http://10.101.3.141/package_repository/debian/" +apache_tomcat+"")
os.system("python phtn_test.py http://10.101.3.141/package_repository/debian/" +java_software+"")



#jar tf $war


#javap -cp AngularJavaApp.war -verbose WEB-INF/classes/main/java/com/labyrinth/app/configuration/ApplicationContextConfig.class | grep major
