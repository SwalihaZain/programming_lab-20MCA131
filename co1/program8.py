word = input("Enter a string: ")
result = word[0] + word[1:].replace(word[0], '$')
print(result)