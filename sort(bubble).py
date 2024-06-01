def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
    print(a)

user_input = input("Enter numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

bubble_sort(user_list)

    
