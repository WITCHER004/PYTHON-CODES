# SIMPLE CALCULATOR FOR TWO VARIABLES:
print('''1.ADDITION
         2.SUBTRACTION 
         3.DIVISION
         4.MULTIPLICATION
         5.SQUARING''')
n=eval(input("ENTER THE OPERATION YOU WANT EXECUTE:"))
if(n==1):
    a=eval(input("ENTER THE INTEGER :"))
    b=eval(input("ENTER THE INTEGER :"))
    c=a+b
    print("THE SUM IS",c)
elif(n==2):
    a=eval(input("ENTER THE INTEGER :"))
    b=eval(input("ENTER THE INTEGER :"))
    c=a-b
    print("THE DIFFERENCE IS",c)
elif (n ==3):
    a=eval(input("ENTER THE INTEGER :"))
    b=eval(input("ENTER THE INTEGER :"))
    if b != 0:
        result = a / b
        print("THE QUOTIENT IS",result)
    else:
        print("Division by zero is not allowed.")
   

elif(n==4):
    a=eval(input("ENTER THE INTEGER :"))
    b=eval(input("ENTER THE INTEGER :"))
    c=a*b
    print("THE PRODUCT IS",c)
elif(n==5):
    a=int(input("ENTER THE INTEGER :"))
    b=a**2
    print("THE SQUARE IS",b)
else:
    print("THE OPERATION SELECTED IS NOT PRESENT")