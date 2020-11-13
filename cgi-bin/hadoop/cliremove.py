#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
y=form.getvalue('filename')
h="sudo hadoop fs -rm {}".format(y)
cmd='sudo docker exec {} bash -c\" {}  \"  '.format(h)
co=sp.getstatusoutput(cmd)
if co[0]==0:
    print('<h1>Your File is removed</h1>')
else:
    print('Please Try Again')

