#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd='sudo docker run -dit --name {} master:v3'.format(x)
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print("Your Hadoop system {} is configured".format(x))
else:
        print("please try again")


