list1=["apple","orange","cherry"]
print(list1)
print(list1[0])
print(list1[2])
print(list1[1:2])
list1[1]="grapes"
print(list1)
for i in list1:
    print(i)
list1.insert(2,"orange")
print(list1)
list1.remove("orange")
print(list1)
list1.pop()
print(list1)
list1.clear()
print(list1)