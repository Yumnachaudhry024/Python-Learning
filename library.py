#string has builtin capabilities/libraries (built in funcs used by anyone )
name="HELLO g"
name1=name.lower()  #lower all the letters
print(name1)         #upper() is used to capatilize all letters

#another way
print("There,".lower())



#replace
name="HELLO g"
name1=name.replace("g","jane")  
print(name1) 

#white spaces (to remove strip func is used)

name="          HELLo g"
name1=name.strip()  
print(name1) 

#Prifixes:
line="nefdnvdhnfv"
print(line.startswith("Please"))

#parsing and extracting:

data="from you class I ll be there"
atpos=data.find("a")      #find the letter or word
print(atpos)                #atpos: at what postition is a or letter 

