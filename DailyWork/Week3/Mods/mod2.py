import mod1

def roll2():
    one = mod1.dice()
    two = mod1.dice()
    throw = (f'Dice 1 = {one} \nDice 2 = {two}\nValue of Dice = {one+two}')
    return throw

print(roll2())