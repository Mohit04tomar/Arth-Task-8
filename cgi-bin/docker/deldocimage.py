#!/usr/bin/python3

print("Content-type: text/html")
print()



import subprocess as sp
import cgi

form=cgi.FieldStorage()
image=form.getvalue("deldi")

if image=='1':
    cmd='sudo docker rmi centos:latest'

elif image=='2':
    cmd='sudo docker rmi ubuntu:latest'

elif image=='3':
    cmd='sudo docker rmi alpine:latest'

elif image=='4':
    cmd='sudo docker rmi debian:latest'

elif image=='5':
    cmd='sudo docker rmi amazonlinux:latest'

output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
    print("<h1> Your Image is Deleted  </h1>")
else:
    print("please try again")
