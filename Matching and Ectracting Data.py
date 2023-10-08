#we want all the list that match
#re.search() return true or false whether the string matches or not
#findall is used to extract those matches
import re
x="My 2 two fav no are 19 and 42 and 42 AEIOUT and B"
y=re.findall("[0-9]+",x)
print(y)

y= re.findall("AEIOU+",x)
print(y)


#Greedy Matching
#(+ *) these are repeate characters that pushes onward to both direction to match the largest possible string

import re
x="From: using the : charater"
y=re.findall("^F.+:",x)
print(y)


#Non Greedy Matching

import re
x="From: yumna.com.a using the : charater"
y=re.findall("^F.+?:",x)
print(y)

#Fine tuning string extraction
y=re.findall("\S+@\S+",x)
print(y)

