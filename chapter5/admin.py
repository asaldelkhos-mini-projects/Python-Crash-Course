#exercise 5-8

names = ['admin', 'sahar', 'ehsan', 'nima', 'nazi']

#if we didn't have any user then first massage would print otherwaise second and third one prints.
if names == []:
    print('We need to find some users!')
else:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'\nHello {name.title()}, thank you for logging again.')
