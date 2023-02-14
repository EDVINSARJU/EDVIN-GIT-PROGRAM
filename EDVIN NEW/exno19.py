n=int(input("enter the size of list:"))
print("enter the element:")
list=[]
for i in range(0,n):
    ele=int(input())
    if (ele%2==0):
        list.append(0)
        list.remove(0)
    else:
         list.append(ele)
print(list)
