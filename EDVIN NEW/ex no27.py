x= input("enter a string: ")
if (x[-3:]=="ing"):
    str=x.replace(x[-3:],"ly")
else:
    str=x+"ing"
print(str)