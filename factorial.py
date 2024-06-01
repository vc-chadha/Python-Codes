n=int(input("Enter Number  "))
def recur(n):
    if n==0:
        return 1
    return n*recur(n-1)
print(recur(n))
    
