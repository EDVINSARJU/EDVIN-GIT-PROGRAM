n=int(input("enter the list"))
print("enter the data")
list=[]
for i in range(0,n):
    ele=input()
    list.append(ele)
print(list)
count=0
for i in list:
    for j in i:
       if j=="a" or j=="A":
         count=count+1
print(count)
