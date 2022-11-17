str=(input("enter the word"))
a=str.split()
print(a)
dict={}
for n in a:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
       print(m,n)
