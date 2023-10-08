#Regular Expression are not the base of Python but its is ditributed to python
#using re.search() like find()
hand=open("clown.txt")
for line in hand:
    line=line.rstrip()
    if line.find("From"):
        print(line)
import re
hand=open("clown.txt")
for line in hand:
    line=line.rstrip()
    if re.search("From:",line) :
        print(line)
        
#using re.search() like startwith()
hand=open("clown.txt")
for line in hand:
    line=line.rstrip()
    if line.startswith("From"):
        print(line)
        
import re
hand=open("clown.txt")
for line in hand:
    line=line.rstrip()
    if re.search("^From:",line) :
        print(line)


#Wild card Characters: dot character matches any character  x.*
#Fine tuning your match  ^X-\S+:

        