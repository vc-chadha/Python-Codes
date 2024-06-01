myfile=open(r"C:\\'Enter_path_address_here'\\'Enter_file_name_here'.txt","r")
line_count=0
data=myfile.readlines()
for line in data:
    if line[0]=='T':
        line_count+=1
print(line_count)
myfile.close()


    
