#BODY MASS INDEX CALCULATOR:-

n=input("ENTER YOUR NAME:")
h=eval(input("ENTER YOUR HEIGHT:"))
i=h * 0.348
w=eval(input("ENTER YOUR WEIGHT:"))
bmi=w/(i**2)
if(bmi >= 25):
  print("THE USER FALLS IN OBESITY RANGE")
elif(bmi >= 18 and bmi < 25):
  print("THE USER IS FIT ")
else:
  print("THE USER IS UNDERWEIGHT")
print("THE BODY MASS INDEX OF",n,"IS",bmi)
