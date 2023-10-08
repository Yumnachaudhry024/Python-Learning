#application of Dictionaries is histogram
#ie we have many names (repeated ) and we have to find the most common name so its difficult
names=dict()
names ["cves"]=1
names["marque"]=1
print(names)
{"cves":1,"marque":1}
print(names)

#we can access the name by using for and if statement if name is not in the dict

#get method function :to reduce code
count=dict()
names={"cves","crves","yumna"}
for name in names:
    count[name]=count.get(name,0)+1
    print(count)
    
