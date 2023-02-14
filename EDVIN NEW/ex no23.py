dict={}
string=(input("enter the strings:"))
for n in string:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
        print(m,n)