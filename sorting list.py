
#Sorting lists of Tuples
#1-Convert dict to list 
#2-Sort the list

d={"a":10,"b":1,"c":22}
t=sorted(d.items())
for k,v in sorted(d.items()):
    print(k,v)
    
    
#Sort by values not key
d={"a":10,"b":1,"c":22}
t=list()
for k,v in d.items():
    t.append((v,k))           #flip
print(t)
t=sorted(t,reverse=True)             #descending order
print(t)




