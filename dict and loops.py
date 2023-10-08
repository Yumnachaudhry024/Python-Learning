count=dict()
line=input("ENTER TEXT")
words=line.split()

print("Words:",words)
print("counting...")

for word in words:
    count[word]=count.get(word,0)+1
print("Counts:",count)


#definte loop with dict
count={"name":23, "bool":21,"yumna":12}
for key in count:
    print(key,count[key])
    
    
#Retiving list of keys and values
#we can just take key or jus values through the dict
count={"name":23, "bool":21,"yumna":12}
print(count.keys())
print(count.values())
print(count.items())        #tuples  list but in list there are 2 tuples 0,1,2


#Two iteration variables:
count={"name":23, "bool":21,"yumna":12}
for aaa,bbb in count.items():
    print(aaa,bbb)
    
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])


    