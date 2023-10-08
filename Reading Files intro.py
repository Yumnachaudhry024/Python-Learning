#handling the file ( we can 
# open the file and can read it)
xfile=open ("mbox.txt")
for cheese in xfile:
    print(cheese)
    
    
#counting lines in a file
xfile=open ("mbox.txt")
count=0
for line in xfile:
    count=count+1
print("count", count)


#Reading the whole File
xfile=open("mbox.txt")
inp=xfile.read()
print(len(inp))


#Searching through file
xfile=open("mbox.txt")
for line in xfile:
    if line.startswith("From"):
        print(line)
        
        
        
#in above code there are two lines starts with from so output is two separte line to fix it 
xfile=open("mbox.txt")
for line in xfile:
    line=line.rstrip()                   #in this way the space bw two lines removed
    if line.startswith("From"):
        print(line)                 
        
#skipping through continue
xfile=open("mbox.txt")
for line in xfile:
    line=line.rstrip()                   #in this way the space bw two lines removed
    if not line.startswith("From"):
        continue
    print(line)                 
        
