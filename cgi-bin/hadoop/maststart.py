#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd='sudo docker exec {} bash -c "sudo hadoop-daemon.sh start namenode " '.format(x)
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print("Your Hadoop Master {} is Started".format(x))
        cm='sudo docker exec {} bash -c "sudo hadoop dfsadmin -report"  '.format(x)
        y=sp.getstatusoutput(cm)
        print(y[1])
else:
        print("please try again")

