#need to pip3 install libmagic
#pip3 install comment_parser
#for windows machines you must also download additional dll files
from comment_parser import comment_parser


#for files with c code
comment_parser.extract_comments('test.c' , mime='text/x-c')


#for files with .s extension
comment_parser.extract_comments('test2.s', mime='text/x-c')
