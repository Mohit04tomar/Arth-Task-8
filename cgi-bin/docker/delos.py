#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd = 'sudo docker rm {}  -f'.format(x)
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print(out)
        print("<h1> OS Removed </h1>")
else:
        print("please try again")
