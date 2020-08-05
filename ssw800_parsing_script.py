#need to pip3 install libmagic
#pip3 install comment_parser
#pip3 
#for windows machines you must also download additional dll files
"""
Language	Mime String
C	text/x-c
C++/C#	text/x-c++
Go	text/x-go
HTML	text/html
Java	text/x-java-source
Javascript	application/javascript
Python	text/x-python
Ruby	text/x-ruby
Shell	text/x-shellscript
XML	text/xml
"""
from comment_parser import comment_parser

user_input = input("Which file would you like to process?\n")

#for files with c code
comments = comment_parser.extract_comments(user_input , mime='text/x-c')
F = rstrip
F = open(f"{user_input}.txt", "a")
for comment in comments:
    F.write(str(comment))
for comment in comments:
    print(str(comment))
F.close()

#For Multiple Files
for files in dirpath:
    comments = comment_parser.extract_comments(filename = document, mime='text/x-c')
        F = open(f"{filename}.txt", "a")
        for comment in comments:
            F.write(str(comment))
        for comment in comments:
            print(str(comment))
        F.close()


"""
#for files with c code
comments = comment_parser.extract_comments('rockbox.c', mime='text/x-c')
F = open("rockboxoutput.txt", "a")
for comment in comments:
    F.write(str(comment))
F.close()

#for files with c code
comments = comment_parser.extract_comments(filename = 'mdpnp.java', mime='text/x-java-source')
F = open(f"{filename}.txt", "a")
for comment in comments:
    F.write(str(comment))
F.close()
"""

