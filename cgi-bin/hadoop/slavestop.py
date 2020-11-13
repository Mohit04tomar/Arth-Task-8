#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue(osname)
cmd='sudo docker rm {}'.format(x)
co=sp.getstatusoutput(cmd)
if co[0]==0:
    print('<h1>Your System is Stopped and terminated</h1>')
else:
    print('Please Try Again')

