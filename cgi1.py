#!/usr/bin/env python

# Import the CGI module
import cgi, os, sys

# Required header that tells the browser how to render the HTML.
sys.stdout.write("Content-Type: text/html\n\n")

# Define function to generate HTML form.
def generate_form():
    sys.stdout.write("<HTML>\n")
    sys.stdout.write("<HEAD>\n")
    sys.stdout.write("\t<TITLE>Info Form</TITLE>\n")
    sys.stdout.write("</HEAD>\n")
    sys.stdout.write("<BODY BGCOLOR = white>\n")
    sys.stdout.write("\t<H3>Please, enter your name and age.</H3>\n")
    sys.stdout.write("\t<TABLE BORDER = 0>\n")
    sys.stdout.write('\t\t<FORM METHOD = post ACTION = "cgi1.py">\n')
    sys.stdout.write('\t\t<TR><TH>Name:</TH><TD><INPUT type = text name ="name"></TD><TR>\n')
    sys.stdout.write('\t\t<TR><TH>Age:</TH><TD><INPUT type = text name ="age"></TD></TR>\n')
    sys.stdout.write("\t</TABLE>\n")
    sys.stdout.write('\t<INPUT TYPE = hidden NAME = "action" VALUE = "display">\n')
    sys.stdout.write('\t<INPUT TYPE = submit VALUE = "Enter">\n')
    sys.stdout.write("\t</FORM>\n")
    sys.stdout.write("</BODY>\n")
    sys.stdout.write("</HTML>\n")

# Define function display data.
def display_data(name, age):
    sys.stdout.write("<HTML>\n")
    sys.stdout.write("<HEAD>\n")
    sys.stdout.write("\t<TITLE>Info Form</TITLE>\n")
    sys.stdout.write("</HEAD>\n")
    sys.stdout.write("<BODY BGCOLOR = white>\n")
    answer = name + ", you are " + age + " years old."
    sys.stdout.write(answer)
    sys.stdout.write("</BODY>\n")
    sys.stdout.write("</HTML>\n")

# Define main function.
def main():
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("name") \
    and form.has_key("age")):
             if (form["action"].value == "display"):
                display_data(form["name"].value, form["age"].value)
    else:
             generate_form()

    # Call main function.
main()