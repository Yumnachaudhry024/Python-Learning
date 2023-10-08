#Gross pay with defining a function
def computepay(x,y):
    #print("compute", x,y)
    if x>40:
        
        regular=x*y 
        overtime=(x-40.0)*(y*0.5)      #x*1.5*y
        
        gross_pay=regular+overtime
    else:
        gross_pay=x+y
    print("returning", gross_pay)    
    return gross_pay
        
        
    
x=float(input("hours:"))
y=float(input("rate per hour:"))

gross_pay=computepay(x,y)
print("gross",gross_pay)

    
