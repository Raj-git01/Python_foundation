name =input('Enter your name? ')
while name =="":
    input("Enter your name? ")
age=int(input('What is your age? '))
while age<0:
    input('Enter your age - ')
print(f'Hello {name} , you are {age} years old')
