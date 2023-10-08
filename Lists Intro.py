#list are the the collection allows you to put many values in the variable (otherwisse variable store 1 value at a time)
#Data structures are the clever ways that do what data want to do
friends=["Fatima", "Muniba","Tehreem"]  # lists

print(friends[1])
#lists are mutabale (changeable) but the strings are not
numbers=[1,2,3,4,5]
numbers[2]=28
print(numbers)

#hw long is the list
#len func is used
friends=["Fatima", "Muniba","Tehreem"]  # lists

print(len(friends))

#using the range func returns the list of numbers
friends=["Fatima", "Muniba","Tehreem"]  # lists

print(range(len(friends)))

#tale of two loops
friends=["Fatima", "Muniba","Tehreem"]
for i in range(len(friends)):
    friend=friends[i]
    print("Happy new year", friend)
    
#cancetinating lists
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

#Slicing of list
a=[1,2,3,4,5,6]
print(a[1:3])


#List Method





