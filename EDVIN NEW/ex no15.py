x=[3,6,9,12,15]
y=[2,4,6,8,10,12]
if(len(x)==len(y)):
    print("Both the list are of same lenght")
else:
    print("Not of same length")
if(sum(x)==sum(y)):
    print("Both the sum are same")
else:
    print("Both the sum of given list are not same")
print("common elements")
for i in x :
    for j in y :
        if(i==j):
            print(i)