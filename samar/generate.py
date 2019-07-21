import os

os.chdir("..")
cwd=os.getcwd()
print("Current working directory: " + cwd)

filenames = os.listdir(os.path.join(cwd,"content-pages"))
print("content pages: " + ", ".join(filenames))
template_html=open(os.path.join(cwd,"samar","template.html")).read()

for fn in filenames:
	content_file = os.path.join(cwd, "content-pages", fn)
	content = open(content_file, "r").read()
	content = template_html.replace("SSG_CONTENTS", content)
	output_file = open(os.path.join(cwd, "samar", fn), "w")
	output_file.write(content)
	output_file.close()


def Html_file(filenames, Current_File):
	s=""
	for fn in filenames:
		s+="<li><a href="+fn
		if (fn==Current_File):
			s+=" class=current"
		s+=">"+fn+"</a></li>"+"\n"+"\t\t\t"
	content_file = open(os.path.join(cwd, "samar", Current_File), "r").read()
	output_file = open(os.path.join(cwd, "samar", Current_File), "w")
	output_file.write(content_file.replace("SAMAR", s))
	output_file.close()

for fn in filenames:
	Html_file(filenames, fn)





