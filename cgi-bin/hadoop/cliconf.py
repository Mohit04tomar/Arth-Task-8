#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue(osname)
y=form.getvalue(iadd)
file1=open('core-site.xml','w')
cmd='<value>{}:9001</value>\n'.format(y)
lst=['<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n','<!-- Put site-specific property overrides in this file. -->\n\n','<configuration>\n','<property>\n','<name>fs.default.name</name>\n',cmd,'</property>\n','</configuration>\n']
file1.writelines(lst)
file1.close()
cmnd='sudo docker run -itd --name {} slave:v2'.format(x)
co=sp.getstatusoutput(cmnd)
if co[0]==0:
    cm='sudo docker cp /var/www/cgi-bin/hadoop/core-site.xml {}:/etc/hadoop/'.format(x)
    output=sp.getstatusoutput(cm)
    status=output[0]
    out=output[1]
    if status==0:
        print('<h1>You are connected to Master</h1>')
    else:
        print('Please Try Again')
else:
    print('Please Try Again')

