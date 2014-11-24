#!/usr/bin/env python

import cgi, os, sys

 
form = cgi.FieldStorage()
 
val1 = form.getvalue('comments')
 
sys.stdout.write("Content-type: text/html\n\n")
sys.stdout.write("") 
sys.stdout.write("The form input is below...<br/>")
sys.stdout.write (val1)