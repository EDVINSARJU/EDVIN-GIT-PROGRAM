x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
gcd=1
for i in range(1,max(x,y)):
    if x%i==0 and y%i==0:
        gcd=i
print("gcd of",x,"and",y,"is",gcd)