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

#for files with c code
comments = comment_parser.extract_comments('openwrt.c' , mime='text/x-c')
F = open("openwrtoutput.txt", "a")
for comment in comments:
    F.write(str(comment))
F.close()

#for files with c code
comments = comment_parser.extract_comments('rockbox.c', mime='text/x-c')
F = open("rockboxoutput.txt", "a")
for comment in comments:
    F.write(str(comment))
F.close()

#for files with c code
comments = comment_parser.extract_comments('mdpnp.java', mime='text/x-java-source')
F = open("mdpnpoutput.txt", "a")
for comment in comments:
    F.write(str(comment))
F.close()


