#!/usr/bin/python3

print("Content-type: text/html")
print()



import subprocess as sp
import cgi

form=cgi.FieldStorage()
x=form.getvalue('osname')
cmd = 'sudo docker start {} '.format(x)
op=sp.getstatusoutput(cmd)
if op[0]==0:
    y=form.getvalue('cmnd')
    cmdd='sudo docker exec {} {} '.format(x,y)
    z=sp.getstatusoutput(cmdd)
    if z[0]==0:
        print('<h1>{}<h1>'.format(z[1]))
        w=sp.getoutput('sudo docker stop {}'.format(x))
    else:
        print('PleaseTry Again')
else:
    print('Please Try Again')
    print('<h1><a href=/documentation/index.html>Click Here To get Back</a><h1>  ')
