#!/usr/bin/python
import sys
import subprocess
git_url = sys.argv[1]
print git_url
os.system("git init")
os.system("git fetch --tags --progress" "+refs/heads/*:refs/remotes/origin/*")
os.system("git config remote.origin.url https://github.com/larsenandtoubroinfotech/helloworld.git ")
os.system("git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/*")
result = subprocess.check_output(["cd","/home/shefali/test/git","&&","git","rev-parse","refs/remotes/origin/master^{commit}"])
print result

