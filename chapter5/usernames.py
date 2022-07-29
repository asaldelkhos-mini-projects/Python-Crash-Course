#exercise 5-10

current_users = ['dua', 'ariana', 'selena', 'tylor', 'gaga']

new_users = ['harry', 'zayn', 'the weekend', 'seleNa', 'GaGa']

for name in new_users:
    if name.lower() in current_users[:]:
        print(f'please Enter a new Username, {name} is already exist.')
    else:
        print(f'{name} is avialable.')
