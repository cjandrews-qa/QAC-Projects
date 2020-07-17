#! /usr/bin/python3
mark = int(input("What mark did you get mark?"))
#With elif
if mark >= 85:
    print('Distinction')
elif mark >= 65:
    print('Pass')
else:
    print('Fail')

#Without elif
if mark >= 85:
    print('Distinction')
else:
    if mark>= 65:
        print('Pass')
    else:
        print('Fail')
