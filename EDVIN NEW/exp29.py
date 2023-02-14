
def even(i):
 if(i%2==0):
     for j in range(2,i):
         if(i/j==j):
            print(i)
x=int(input("Enter the starting 4 digit number"))
y=int(input("Enter the ending 4 digit number"))
for i in range (x,y):
    even(i)