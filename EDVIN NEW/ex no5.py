x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
z=int(input("Enter the 3rd number:"))
if(x>y) and (x>z):
    largest=x
elif(y>x) and (y>z):
    largest=y
else:
    largest=z
print("The largest number:",largest)