#!/usr/bin/python


print("Content-type: text/html")
print()



import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
fileitem = form['ufile']
x=form.getvalue('osname')
if fileitem.filename:
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   cm='sudo docker exec {} mkdir /upload'.format(x)
   y=sp.getstatusoutput(cm)
   cmd='sudo docker cp /var/www/cgi-bin/hadoop/tmp/'+fn+' {}:/upload/'.format(x)
   z=sp.getstatusoutput(cmd)
   if z[0]==0:
         print("""\
            Content-Type: text/html\n
            <html>
            <body>
            <p>{}</p>
            </body>
            </html>
            """.format(message,))
else:
   print('No file was uploaded')
