import os
import re

destinationDir = os.getcwd() + "\\ghaid"
contentDir = os.getcwd() + "\\content-pages"

def generateHeader(titles):
    header = ""
    for title in titles:
        header+= "<li><a href=\"" + title + "\">" + title + "</a></li>\n\t\t\t"
    return header


#I edited the template file and put a keyword "SSG_HEADER" to update the list easily
files = os.listdir("content-pages")
template = open(destinationDir + '\\' + "template.html").read()
newTemplate = open(destinationDir + '\\' + "newTemplate.html" , "w")
newTemplate.write(template.replace("SSG_HEADER", generateHeader(files)))
newTemplate.close()
#The newTemplate.html has the generated header.


for filename in os.listdir("content-pages"):
    template = open(destinationDir + '\\' + "newTemplate.html").read()
    file = open(contentDir + '\\' + filename, 'r')
    content = file.read()
    generated = open(destinationDir + '\\' + filename , "w")
    template = template.replace(str(filename), str(filename) + "\" class    =\"current", 1)
    generated.write(template.replace("SSG_CONTENTS", content))
    generated.close()
    
