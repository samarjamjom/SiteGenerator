import os 
import re


def GenPages(page):
    template_html = open("../Deema/template.html").read()
    input_html = open(page).read()
    output_file = open("../Deema/" + page, "w")
    output_file.write( template_html.replace("SSG_CONTENTS", input_html))
    output_file.close()

def AddCurrent(list,CurrentPage):
    links = ""
    for x in list:
        links += "<li><a href="+x
        if(CurrentPage == x):
            links+=" class=current"  
        links+=">"+x+"</a></li>\n"
    input = open("../Deema/" + CurrentPage).read()
    output = open("../Deema/" + CurrentPage, "w")
    output.write(input.replace("Links_are_here", links))
    output.close()
    
pd =os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
d = os.path.join(pd,'content-pages')
os.chdir(d)
files=[]
for x in os.listdir(d):
    files.append(x)
    GenPages(x)

#print(files)

for x  in files:
    AddCurrent(files,x)




