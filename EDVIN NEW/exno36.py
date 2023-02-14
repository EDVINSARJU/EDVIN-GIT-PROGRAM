class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
         return(2*(self.length+self.breadth))

length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
o=rectangle(length,breadth)
x=o.area()
y=o.perimeter()
print("the area is 1",x)
print("the perimeter is 1",y)

length=int(input("enter the length",))
breadth=int(input("enter the breadth",))
o1=rectangle(length,breadth)
z=o1.area()
p=o.perimeter()
print("the area is: ",z)
print("the perimeter is :",p)


if(x>z):
    print("the first recctangle is greater than second rectangle.")
else:
    print("the second rectangle is greater than first rectangle.")
