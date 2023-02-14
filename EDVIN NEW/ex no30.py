def longestLength(a):
    max1 = len(a[0])


    for i in a:
        if (len(i) > max1):
            max1 = len(i)

    print("length is ", max1)

a=[]
n =int(input("enter the num of words : "))
for j in range (0,n):
    i=input()
    a.append(i)
longestLength(a)