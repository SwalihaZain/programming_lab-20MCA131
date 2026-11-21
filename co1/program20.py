a = list(map(int, input("Enter numbers:").split()))
b = [x for x in a if x % 2 != 0]
print(b)