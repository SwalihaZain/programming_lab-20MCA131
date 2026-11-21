start = int(input("Enter starting range:"))
end = int(input("Enter ending range:"))
result = []
for i in range(start, end+1):
    if 1000 <= i <= 9999:
        if int(i**0.5) ** 2 == i:
            if all(int(d) % 2 == 0 for d in str(i)):
                result.append(i)
print(result)