l=[]

def stack07():
    while True:
        inp1=input("Enter Command Push/Pop/Read Here : ")
        if inp1=='Push':
            inp2=input("Enter Stack Value : ")
            l.append(inp2)
            print(l)
        elif inp1=='Pop':
            l.pop()
            print(l)
        elif inp1=='Read':
            print(l)
        else:
            print("Wrong Command ")
            return stack07()
        d=input("Do you Wish to run this Program again (Yes/No) ? ")
        if d=='No'or d=='no' :
            break
        elif d=='Yes' or d=='yes' :
            continue
        else:
            print("Code Invalid")
            return stack07

stack07()

