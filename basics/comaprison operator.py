name=input("What's your name: ")
if len(name)<3:
    print('Name must be at least 3 characters')
elif len(name)>50:
    print('Name must be under 50 characters')
else:
    print('You have lovely name')
