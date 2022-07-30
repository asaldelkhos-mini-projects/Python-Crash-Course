#exercise 6-1 |dictionary

person = {
    'first_name' : 'Amir',
    'last_name' : 'mine',
    'age' : 21,
    'city' : 'mashhad'
    }

# access to values
for info in person.values():
    print(info)

# access to everything in a dictionary
for info, value in person.items():
    print(f"\n{info}:")
    print(value)
print("\n")

#access to keys
for info in person.keys():
    print(info)
