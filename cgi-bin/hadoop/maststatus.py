#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd='sudo docker exec --name {} bash -c "sudo hadoop dfsadmin -report " '.format(x)
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print(out)
else:
        print("Your Master is stopped")

