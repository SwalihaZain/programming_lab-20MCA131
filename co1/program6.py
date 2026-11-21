names = ['Anu', 'Akhil', 'Arun', 'Meera']
count = 0
for name in names:
    count = count + name.lower().count('a')
print("Count of a:", count)