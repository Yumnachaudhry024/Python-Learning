#tuples are the collection like lists not square brakects but round braces
x=("Yumna", "Masood","Rukhshanada")
print(x[2])
print(max(x))

#or
x=(1,2,4)
print(max(x))
for iter in x:
    print(iter)
    
    
#Tuples are immuteable
#Things not to do with tuples:
#sort append etc
#Tuples are efficient


#Tuples and Assignments
(x,y)=(4,"friend")
print(y)                 #we ca put tuples on left side


#Tuples and Dictionaries:
d=dict()
d["Yumna"]=2
d["Laiba"]=3
for (k,v) in d.items():
    print(k,v)
    
    
#Tuples are comparable like string;
(0,1,2)<(5,6,7)
True



