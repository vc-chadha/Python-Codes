def avg():
    a=[]
    f=int(input("Enter Total number of Elements : "))
    for i in range(f):
        b=int(input("Enter Elements : "))
        a.append(b)
    r=len(a)
    gh=sum(a)
    ta=gh/r
    print(ta)
avg()
