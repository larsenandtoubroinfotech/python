#!/usr/bin/python
from sys import argv
from subprocess import Popen,PIPE,STDOUT,call
import os
import commands
import sys
import subprocess, sys
#print sys.argv
#script_name , app_file = argv 
app_file = sys.argv[1]
print app_file
file_extension = app_file.split(".")[1]
print file_extension
service_name = app_file.split(".")[0]
print service_name
#function
def java_application( app_file ):
	status , class_file = commands.getstatusoutput("jar tf /home/shefali/app/"+app_file+"| grep -F .class | head -1")
	print class_file

        subprocess.Popen("cd /home/shefali/app/ && jar xvf "+app_file+" "+class_file+"",stdout=subprocess.PIPE,shell=True)
        print "cd /home/shefali/app/ && jar xvf "+app_file+" "+class_file+""
	status , major_version = commands.getstatusoutput("cd /home/shefali/app/ && javap -cp "+app_file+" -verbose " +class_file+ " | grep major")
        print "cd /home/shefali/app/ && javap -cp "+app_file+" -verbose " +class_file+ " | grep major"

        p = subprocess.Popen("cd /home/shefali/app/ && javap -cp "+app_file+" -verbose " +class_file+"", stdout=subprocess.PIPE, shell=True)
        for line in p.stdout: 
              if "major" in line:
                        major_version = line
                        print major_version


	print major_version
	major_version_n = major_version.split(":")[1]
	print major_version_n
	major_version_n_n = major_version_n.split(" ")[1]
	print major_version_n_n

##############################
        major_version_n_n = major_version_n_n.rstrip()
        print "ffffffff"+major_version_n_n

        print "----------------------------------------------------------------------------"

        jdk_version_file = open('/home/shefali/scripts/jdk_version')
	for line in jdk_version_file:
               print major_version_n_n
               print line
	#	if line.startswith(major_version_n_n+":"):
               if major_version_n_n in line:        
			print "Line ::",line
			java_version = line.split(":")[1]
			print "Java Version ::",java_version
			temp = java_version.split(".")[1]
			apache_tomcat="apache-tomcat-"+temp
			print "Apache Tomcat ::",apache_tomcat
			java_software="jdk-"+temp
			print "Java Software ::",java_software
                        ###################################
                        image_name=java_software+apache_tomcat
                        print "image_name ---",image_name
                        
                        #####temporary
                        image_name="jdk-7_apache-tomcat-7"
                         
                        ####################################
                        #for identifying the image is present in registry or not
                        result = subprocess.check_output(["curl", "-k", "https://citi.docker.com:5000/v2/_catalog"])
                        print "result", result
                        with open('some_file.txt', 'w') as f:
                             f.write(result)
                        with open('some_file.txt', 'r') as f:
                             for line in f:
                                print line
                                if image_name in line:
                                    print "Line :: ", line
                                    #image_status = "present"
                                    #os.system("python container_creation.py "+image_status+" "+service_name)
                                else:
                        ###################################
                        #for replacing @apavhe_package in the dockerfile
                        #getting tomcat package tar name from repository
                                    #image_status = "absent"
                                    proc = subprocess.Popen("python phtn_test.py http://10.101.3.141/package_repository/debian/ "+apache_tomcat,stdout=subprocess.PIPE,shell=True)
                                    print proc
                                    (out, err) = proc.communicate()
                                    outwithoutreturn = out.rstrip('\n')
                                    print "out ::", out
                                    print "outwithoutreturn ::", outwithoutreturn
                        #calling replace script   
                                    os.system("python replace_words.py "+outwithoutreturn+" @apache_package")                       
                        #for replacing @jdk_package in the dockerfile
                        #getting java package tar name from repository
                                    proc = subprocess.Popen("python phtn_test.py http://10.101.3.141/package_repository/debian/ "+java_software,stdout=subprocess.PIPE,shell=True)
                                    print proc
                                    (out, err) = proc.communicate()
                                    outwithoutreturn = out.rstrip('\n')
                                    print "out ::", out
                                    print "outwithoutreturn ::", outwithoutreturn
                        #calling replace script
                                    os.system("python replace_words.py "+outwithoutreturn+" @jdk_package")
                                    subprocess.Popen("docker build -f /home/shefali/docker/java_tomcat/dockerfile_base -t "+image_name+" /home/shefali/docker/java_tomcat",stdout=subprocess.PIPE,shell=True)
                        os.system("python replace_words.py "+app_file+" @war_name")
                        os.system("python container_creation.py "+service_name)              
if file_extension == "war":
	java_application( app_file )
