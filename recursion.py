def pr():
    recurring_element = input("Enter an Element: ")
    num = int(input("Enter Frequency of Recursion: "))
    i = 0
    while i < num:
        print(recurring_element, i + 1)
        i += 1

pr()
