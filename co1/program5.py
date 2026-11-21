a = list(map(int, input("Enter numbers:").split()))
b = ["over" if x > 100 else x for x in a]
print(b)