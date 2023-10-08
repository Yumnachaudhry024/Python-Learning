#Taking a string as str
str="X-DSPAM-Confindence:0.8475"
atpos=str.find(":")      #to find the ":"

print(atpos)

#starting with position : to the end 
part=str[atpos+1:]         #+1 is because we want the part of str after ":"
print(part)
#convert into float
value=float(part)
print(value)               