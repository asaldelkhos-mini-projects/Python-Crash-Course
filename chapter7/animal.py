animal = ['lion', 'giraffe', 'bear', 'lion', 'elephant']

for item in animal:
    print(item)
while 'lion' in animal:
    animal.remove('lion')

print('\n')
for item in animal:
    print(item)
