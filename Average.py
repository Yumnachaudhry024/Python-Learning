# Take some numbers and find the average (Basically to elaborate the concept of loop in list)

#Take an empty list
numberlist=list()
while True:
    inp=input("Enter the number: ")
    if inp=="done": break
    Value=float(inp)
    numberlist.append(Value)
average= sum(numberlist)/len(numberlist)
print("Average:", average)
    