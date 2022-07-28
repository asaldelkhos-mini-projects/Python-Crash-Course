#exercise 5-8

names = ['admin', 'sahar', 'ehsan', 'nima', 'nazi']

for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'\nHello {name.title()}, thank you for logging again.')
