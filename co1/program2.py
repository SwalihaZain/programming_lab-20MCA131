# 3(a) Generate positive numbers from a list

a = [-2, 3, -5, 6, 8, -1]
positive = [x for x in a if x > 0]
print("Positive numbers:", positive)


# 3(b) Square of N numbers

n = int(input("Enter Number: "))
square = [x*x for x in range(1, n+1)]
print("Squares:", square)


# 3(c) Select vowels from a word

word = input("Enter a word: ")
vowels = [x for x in word if x in "aeiouAEIOU"]
print("Vowels:", vowels)


# 3(d) Ordinal value of each character

word = input("Enter a word: ")
ordinal = [ord(x) for x in word]
print("Ordinal values:", ordinal)