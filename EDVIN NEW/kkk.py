f=open("demofun.txt", "a")
f.write("this content have to be added to the demo file")
f=open("demofun.txt", "r")
print(f.read())
f.close()