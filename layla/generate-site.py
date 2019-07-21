import os
import re

print("Clearing the screen")
os.system("cls")

print("Current working directory (before changing it): " + os.getcwd())
print("Script file: " + __file__ )
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir) 
print("Current working directory: " + os.getcwd())
contentPath ="../content-pages"
contentPages = os.listdir(contentPath)

print( ", ".join(contentPages))
#print(contentPages)
readyPath = "readyPages"
if not os.path.isdir(readyPath):
    os.makedirs(readyPath)

#TODO another loop to do the list items and update the next one to have current class
listItems = ""
for page in contentPages:
    listItems+="<li><a href="+page+">"+page+"</a></li>\n"

#print(listItems+"\n")
templatefile = open("template.html", "r")
template = templatefile.read()
template= template.replace("SSG_NAVBAR",listItems)
#templatefile.write(template)
templatefile.close()

for page in contentPages:
    print("Page: " + page)
    full_path = contentPath + "/" + page
    content = open(full_path, "r").read()
    if not os.path.isfile(full_path):
        print(full_path + " does not exist!")
    generated_html =template.replace("SSG_CONTENTS",content) 

    anchor = "<li><a href="+page
    print("anchor is:"+ anchor)
    pos = generated_html.find(anchor)+len(anchor)
    print("position is "+str(pos))
   # scoreAnchor = report.find("%" , pos)
   #line[:index] + 'Fu ' + line[index:]
    result = generated_html[:pos]+" class = 'current'"+generated_html[pos:]
    output_path = readyPath + "/" + page
    print(os.getcwd() + "/" + output_path)
    generatedPage = open(output_path,"w")
    generatedPage.write(result)
    generatedPage.close()
