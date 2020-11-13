#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd='sudo docker rm --name {} '.format(x)
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print("Your Master is stopped and terminated".format(x))
else:
        print("please try again")

