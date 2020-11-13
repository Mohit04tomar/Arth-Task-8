#!/usr/bin/python3


print("content-type: text/html")
print()



import subprocess as sp
import cgi

form=cgi.FieldStorage()
cmd = 'sudo docker image ls '
output=sp.getstatusoutput(cmd)
stauts= output[0]
out=output[1]

if stauts==0:
        print("""<html>
                 <head>
                 <title>Docker Image</title>
                 </head>
                 <body>
                 <h2>{}</h2>
                 </body>
                 </html>""".format(out))
else:
        print("please try again")

