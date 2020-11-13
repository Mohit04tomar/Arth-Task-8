#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
cmd = 'sudo docker rm $(sudo docker container ls -a -q)'
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print("<h1>All Container Deleted</h2>")
else:
        print("please try again")
