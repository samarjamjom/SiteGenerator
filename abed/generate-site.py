import subprocess
import os
TemplateFile = open("abed\\template.html", "r")  
TemplateHTML= TemplateFile.read()
#recreate the list
TraineesWebPages=""
for directory in os.listdir(os.getcwd()):
    if (directory.find(".")<0 and not directory=="content-pages" and  not directory=="images" and not directory=="style"  and not directory =="current-directory_" ):
        TraineesWebPages+='<li><a href="'+directory+'/generated-site/index.html" class ="current">'+directory+'</a></li>\n'
TemplateHTML=TemplateHTML.replace("SSG_LIST",TraineesWebPages)
TemplateFile.close()
os.chdir("content-pages")

for HTMLfile in os.listdir(os.getcwd()):
    file=open(HTMLfile, "r")
    FileContent= file.read()
    file.close()
    newHTMLfile="..\\abed\\"+HTMLfile
    file = open(newHTMLfile, "w") 
    file.write( TemplateHTML.replace("SSG_CONTENTS",FileContent))
    file.close()




