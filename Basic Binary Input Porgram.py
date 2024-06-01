import pickle

a=open("C:\\'Enter_your_address_here'\\'File_name_here'.dat","wb")
b=int(input("Enter Roll.No : "))
c=input("Enter Name : ")
d=int(input("Enter Class : "))
e=int(input("Enter Marks : "))
lst=[b,c,d,e]
pickle.dump(lst,a)    
f=int(input("Enter a Roll Number : "))
for i in lst:
    if i==f:       
        print("Roll No verified  ")
        break
        
    else:
        print("Not verfied ")
        break
        if i!=f:
            a=open("C:\\'Enter_your_address_here'\\'File_name_here'.dat","ab")
            pickle.dump(f,a)
            a.close()
            
            




