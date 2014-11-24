#!/usr/bin/env python

import cgi, os, sys

sys.stdout.write("Content-type: text/html\n\n")
 
#sys.stdout.write('<form method="post" action="test_form.py">')
#sys.stdout.write('<textarea name="comments" cols="40" rows="5">')
#sys.stdout.write("Enter comments here...")
#sys.stdout.write("</textarea>")
#sys.stdout.write("<br/>")
#sys.stdout.write('<input type="submit" value="Submit" >')
#sys.stdout.write("</form>")

def generate_form():
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Info Form</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Please, enter your username and password.</H3>\n"
    print "\t<TABLE BORDER = 0>\n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"cgi2.py\">\n"
    print "\t\t<TR><TH>Username:</TH><TD><INPUT TYPE = text \
    NAME = \"username\"></TD><TR>\n"
    print "\t\t<TR><TH>Password:</TH><TD><INPUT \
    TYPE = password NAME = \"password\"></TD></TR>\n"
    print "\t</TABLE>\n"
    print "\t<INPUT TYPE = hidden NAME = \"action\" VALUE = \
    \"display\">\n"
    print "\t<INPUT TYPE = submit VALUE = \"Enter\">\n"
    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

generate_form()