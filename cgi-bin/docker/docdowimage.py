#!/usr/bin/python3

print("Content-type: text/html")
print()



import subprocess as sp
import cgi

form=cgi.FieldStorage()
image=form.getvalue("ddi")

if image=='1':
    cmd='sudo docker pull centos'

elif image=='2':
    cmd='sudo docker pull ubuntu'

elif image=='3':
    cmd='sudo docker pull alpine'

elif image=='4':
    cmd='sudo docker pull debian'

elif image=='5':
    cmd='sudo docker pull amazonlinux'

output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
    print("<h1> Your Image is Downloaded  </h1>")
else:
    print("please try again")
