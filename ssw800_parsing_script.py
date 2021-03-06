#pip3 install libmagic
#pip3 install comment_parser
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
import os
dirName_mdpnp = r"C:\Users\Edward\Documents\GitHub\mdpnp"
dirName_openwrt = r"C:\Users\Edward\Documents\GitHub\openwrt"
dirName_rockbox = r"C:\Users\Edward\Documents\GitHub\rockbox"
##First task is getting all files in the folder
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles
mdpnpFiles = getListOfFiles(dirName_mdpnp)
openwrtFiles = getListOfFiles(dirName_openwrt)
rockboxFiles = getListOfFiles(dirName_rockbox)




output_directory = r"C:\Users\Edward\Documents\GitHub\SYS800\OUTPUT_FILES\\"
##Second Task: We need to extract all the extensions for each file
#For Multiple C-Files
def parse_project(project, allFiles):
    for fyle in allFiles:
        if fyle.endswith(".java"):
            comments = comment_parser.extract_comments(fyle, mime="text/x-java-source")
            name = fyle.replace("\\", ".").replace(
                "C:.Users.Edward.Documents.GitHub.", "")
            output = output_directory + project + "\\" + name[:-5] + ".txt"
            F = open(output, "a")
            for comment in comments:
                F.write(str(comment))
            F.close()
        ##F = open(f"{dirpath}-{fyle}.txt", "a")
        ##F.close()
        if fyle.endswith(".c"):
            try:
                comments = comment_parser.extract_comments(fyle, mime="text/x-c")
                name = fyle.replace("\\", ".").replace(
                    "C:.Users.Edward.Documents.GitHub.", "")
                output = output_directory + project + "\\" + name[:-2] + ".txt"
                F = open(output, "a")
                for comment in comments:
                    F.write(str(comment))
                F.close()
            except UnicodeDecodeError:
                print("Bad characters in files!" + fyle)
            except ValueError:
                print("The file is empty!")
print("MDPNP # of Files" + "= " + str(len(mdpnpFiles)))
print("OpenWRT # of Files" + "= " + str(len(openwrtFiles)))
print("Rockbox # of Files" + "= " + str(len(rockboxFiles)))
mdpnp_comments = parse_project("MDPNP", mdpnpFiles)
#parse_project("OpenWRT", openwrtFiles)
#parse_project("Rockbox", rockboxFiles)


