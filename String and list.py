#rstrip concept
friend=open("text.txt")
line="From:stephen.mat@gmail.com Sat Jan 5 09:14:16 2008"
words=line.split()
print(words)


for line in friend:
    line=line.rstrip()
    words=line.split()
    if not line.startswith("from"): continue
   
    print(words)
    
#Double split Pattern
words=line.split()
email=words[1]
places=email.split("@")
print(places[1])
