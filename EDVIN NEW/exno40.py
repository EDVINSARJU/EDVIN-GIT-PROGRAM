f=open("try.txt","r")
f1=open("demofun.txt","w")
content=f.readlines()
for i in range(0,len(content)):
  if(i%2!=0):
      f1.write(content[i])
  else:
      pass

f.close()
f1.close()
f=open("demofun.txt","r")
c=f.read()
print("odd lines are:",c)
f.close()