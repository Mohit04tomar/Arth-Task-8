#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
print(x)
cmd='sudo docker exec {} bash -c "sudo hadoop namenode format" '.format(x)
print(cmd)
output=sp.getstatusoutput(cmd)
print(output)
stauts= output[0]
out=output[1]

if stauts==0:
        z="<h1>Your Hadoop system {} is Formatted</h1>".format(x)
        print(z)
else:
        print("please try again")

