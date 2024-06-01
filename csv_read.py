import csv
a=open("C:\\'Enter_ypur_path_here'\\'enter_file_name'.csv",'r')
b=csv.reader(a,delimiter=',')
for i in b:
    print(i)
