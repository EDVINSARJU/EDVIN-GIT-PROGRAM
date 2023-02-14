import csv
c_col=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'EDVIN SARJU','Age':22},
           {'ID':2,'Name':'POOJA','Age':30},
           {'ID':3,'Name':'SAM','Age':21},
           {'ID':4,'Name':'SREE LASKMI','Age':23},
           {'ID':5,'Name':'EDWIN RAJU','Age':24},
           {'ID':6,'Name':'BENZ','Age':26},
           {'ID':7,'Name':'DESTISONA','Age':27},
           {'ID':8,'Name':'DEVIKA','Age':28},
           {'ID':9,'Name':'DIYA','Age':28},
           {'ID':10,'Name':'DILNA','Age':28}]
try:
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in d:
    print(i)




