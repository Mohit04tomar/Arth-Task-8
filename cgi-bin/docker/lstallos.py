#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
cmd = 'sudo docker ps -a '
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print(out)
        print("out")
else:
        print("please try again")
