fname=input("Enter the number")
if len(fname)<1:
    fname="clown.txt"
hand=open(fname)
d=dict()
for lin in hand:
    
    lin=lin.rstrip()
    wds=lin.split()
    #print(wds)
    for w in wds:
        d[w]=d[w]+1
        print(w,"new",newcount)
        #if the key is not there the count is zero
        
        
        oldcount=d.get(w,0)
        print(w,"old",oldcount)
        newcount=oldcount+1
        d[w]=newcount
        print(w,"new",newcount)
        if w in d:
            d[w]=d[w]+1
            d[w]=d.get(w,0)+1
            
            
        else:
            d[w]=1
            
        print(d[w])
        
print(d)