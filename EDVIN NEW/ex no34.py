class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return (2*(self.l+self.b))


l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
o=rectangle(l,b)
li=int(input("Enter the length"))
bi=int(input("Enter the breadth"))
o1=rectangle(li,bi)
z=o1.area()
q=o1.perimeter()
x=o.area()
y=o.perimeter()
print("Area of first rectangle : ",x)
print("Perimeter of first rectangle : ",y)
print("Area of second rectangle : ",z)
print("Perimeter of second rectangle : ",q)
if (x>z):
    print("The first rectangle is greater than second rectangle")
elif(z>x):
    print("The second rectangle is greater than first rectangle")
else:
    print("rectangle same area")
