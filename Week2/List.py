#had no way to test this answer because something is wrong my python?
july = ["chris", "chris", "wasim", "arselan", "dom", "cliff", "josh", "tobi", "sam", "jason", "k", "mowafak", "t", "bon", "jack", "ed", "brad", "steven", "jacob", "ryan", "javis"]


july.append("luke")
print(f'Proof that luke has been added using july[-1]: {july[-1]}')

name5 = july[4]
print(f'Name number 5 in the list was: {name5}')


from collections import Counter 

c = Counter(july)

for name, count in c.items():
    if count != 1:
        print(f'{name} appears {count} times in the list')
    else:
        
