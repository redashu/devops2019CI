#!/usr/bin/python3

import  cgi,cgitb
cgitb.enable()
#  to recv  data from  web http protocol 


print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
#  only  looking  for  form  data and those variables  data as well

tech=html_data.getvalue('t')

if  tech  ==  "docker"  :
    print("<meta http-equiv='refresh'  content='0;url=http://54.91.107.242/docker.html'>")

else  :
    print("<meta http-equiv='refresh'  content='0;url=http://54.91.107.242/aws.html'>")

