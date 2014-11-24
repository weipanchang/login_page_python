#!/usr/bin/env python

import cgi, os, string, sys
import hashlib

# Required header that tells the browser how to render the HTML.
print "Content-Type: text/html\n\n"
#sys.stdout.write("Content-type: text/html\n\n")

# Define function to generate HTML form.
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

    # Define function to test the password.
def test(id, passwd):
    passwd_file = open('passwords.txt', 'r')
    line = passwd_file.readline()
    passwd_file.close()
    combo = string.split(line, ":")
#    print combo[0], combo[1]

    encrypted_pw = hashlib.sha224(passwd).hexdigest()
#    print id, encrypted_pw

    if ((id == combo[0]) and ( encrypted_pw[0:30] == combo[1][0:30])): 
             return "passed"
    else:
             return "failed"

    # Define function display_page.
def display_page(result):
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Info Form</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    if (result == "passed"): 
             print "You entered the correct combo.\n"
    else:
             print "You entered the incorrect combo.\n"
    print "</BODY>\n"
    print "</HTML>\n"

    # Define main function.
def main():
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("username") \
    and form.has_key("password")):
             if (form["action"].value == "display"):
                result = test(form["username"].value, form["password"].value)
                display_page(result)
    else:
             generate_form()

    # Call main function.
main()