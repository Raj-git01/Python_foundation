weight=int(input('Enter body weight : '))
unit=input('(L)bs or (K)g: ')
if unit.upper()=="L":
    convert=weight*0.45
    print(f'You are {convert}kgs')
else:
    convert=weight/0.45
    print(f'You are {convert} lbs')
