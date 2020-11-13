#!/usr/bin/python3


print("content-type: text/html")
print()



import subprocess as sp
import cgi

form=cgi.FieldStorage()
nic=form.getvalue('nick')
image=form.getvalue('cont')

if image=='1':
    x='centos'

elif image=='2':
    x='ubuntu'

elif image=='3':
    x='alpine'

elif image=='4':
    x='debian'

elif image=='5':
    x='amazonlinux'

cmd = 'sudo docker run -d -i -t --name {} {}:latest'.format(nic,x)
print(cmd)
otput=sp.getstatusoutput(cmd)
print('<h1>your os launched</h1>')

