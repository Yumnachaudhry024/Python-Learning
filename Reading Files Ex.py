#Write a program to read through file and print the contents of the file (line by line ) all the upper case 


xfile=open("mbox.txt")
print(xfile)
for line in xfile:
    line=line.rstrip()
    print(line.upper())