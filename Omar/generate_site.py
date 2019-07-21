import os
import re
content_path="../content-pages"
#print(content_path)
pages=os.listdir(content_path)
my_string=""
for p in pages:
    my_string+="<li><a href="+p+">"+p[-len(p):-5]+"</a></li>\n"
template = open("template.html", "r").read()
template= template.replace("SSG_NAVIGAT",my_string)
open("template.html", "r").close()

for p in pages:
    content = open(content_path + "/" + p , "r").read()
    my_page_html =template.replace("SSG_CONTENTS",content) 
    my_string_new="<li><a href="+p+" class=\"current\">"+p[-len(p):-5]+"</a></li>\n"
    my_page_html=my_page_html.replace("<li><a href="+p+">"+p[-len(p):-5]+"</a></li>\n",my_string_new)
    generate_page = open(p,"w")
    print(my_page_html)
    generate_page.write(my_page_html)
    generate_page.close()