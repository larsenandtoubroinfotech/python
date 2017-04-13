#!/usr/bin/python
from sys import argv
from subprocess import call
import os
import commands
import sys
import subprocess, sys

script_name , textToReplace , textToSearch = argv
print script_name
print textToSearch
print textToReplace

# Read in the file
filedata = None
with open('/home/shefali/docker/java_tomcat/dockerfile_base', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(textToSearch, textToReplace)

# Write the file out again
with open('/home/shefali/docker/java_tomcat/dockerfile_base', 'w') as file:
  file.write(filedata)
