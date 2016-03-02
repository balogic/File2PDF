import pdfkit
print "Welcome to URL2PDF"
print "..............................."
file1 = "url.txt"
name = 0
file2 = open(file1,"r")
g = file2.readlines()
for h in g:
	name = name + 1
	i = str(name)
	a = i + ".pdf"
	pdfkit.from_url(h,a)
file2.close()
print "%d"%name+"files Completed"
