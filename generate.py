import pdfkit
print "Welcome to URL2PDF"
print "..............................."
file1 = "url.txt"
name = 0
file2 = open(file1,"r")
while file2.readline() :
	b = file2.readline()
	name = name + 1
	i = str(name)
	a = i + "file"
	file3 = open(a, "w")
	file3.write(b)
	file3.close()
file2.close()
print "%d"%name+"files Completed"
