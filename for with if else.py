#1-Code to find the larget number in list
x=1
print(x)

for list in [3,41,12,9,74,15]:
    if list>x:
        x=list
    else:
        print(x)
print("Largest Number", x)

#code to find smallest number:

x=-1
print("before",x)


for list in [3,-2,12,9,74,15]:
    if list<x:
        x=list
        print("smaallest",x)
    else:
        print(x)
print("Smallest", x)


#if we assign x=None in above code
x=None
print("before",x)


for value in [3,-2,12,9,74,15]:
    if x is None:
        x=value
        print("smaallest",x)
    elif value<x:
        x=value
    print(x,value)
print("Smallest", x)

#2-to count how many loops are executed we use counter variable like:
x=0
for thing in [3,4,2,7,9,14,44]:
    x=x+1
    print(x,thing)
print("After",x)


#3-summing the loops
x=0
print("before",x)
for thing in [3,4,5,7,9,14,44]:
    x=x+1
    print(x,thing)
print("After",x)


#4-Take an average of loops
count=0
sum=0
for value in [3,4,5,6,7,8]:
    count=count+1
    sum=sum +value
    print (sum,count,value)
print("after:",count,sum,sum/count)


#5-Filteriing the loops
#just like 1st code we can use if st in for loop (filtering)


#6-Search using a boolean variable
#like we say that if to find the value is there or not?
#code that check wheater 3 is present in list or not
number=False
print ("Before",number)
for value in [12,41,3,74,6,3]:
    if value==3:
        number=True
        print(number,value)
    else:
        number=False
print("After:", number)