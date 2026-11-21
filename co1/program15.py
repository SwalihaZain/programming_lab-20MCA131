a=input("enter first list:").split(',')
b=input("enter second list:").split(',')
for color in a :
    if color not in b :
        print(color)
        
        