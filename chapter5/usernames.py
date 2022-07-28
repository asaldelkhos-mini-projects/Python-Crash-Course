#exercise 5-10

current_users = ['dua', 'ariana', 'selena', 'tylor', 'gaga']

new_users = ['harry', 'zayn', 'the weekend', 'selena', 'gaga']
for value in range(0, 5):
    for user in new_users:
        if user.title() == current_users[value].title():
            print('please Enter a new Username, this one is already exist.')
        else:
            print('The username is avialable.')
