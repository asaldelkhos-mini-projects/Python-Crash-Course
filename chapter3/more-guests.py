#exercise3-6

guests = ['shakib', 'mah', 'sep', 'nafas', 'saba']

print(f"Hi {guests[0].title()}, I found a bigger table so i invite more friends.")

guests.insert(0, 'amirhossein')
guests.insert(3, 'sina')
guests.insert(7, 'pouya')

print(guests)
print("Hi, i have a dinner night, I would like if ur comiing\n")

#exercise3-7

print("Hi guys, unfortunatly I can invite two of u")

pouya = guests.pop(7)
print(f"hi {pouya}, sorry dinner is cansel.")

sina = guests.pop(3)
print(f"hi {sina}, sorry dinner is cansel.")

saba = guests.pop(5)
print(f"hi {saba}, sorry dinner is cansel.")

nafise = guests.pop(4)
print(f"hi {nafise}, sorry dinner is cansel.")

mah = guests.pop(2)
print(f"hi {mah}, sorry dinner is cansel.")

amir = guests.pop(0)
print(f"hi {amir}, sorry dinner is cansel.")

print(guests)
print(f"{guests[0]} and {guests[1]} see u.")
del guests[1]
del guests[0]
print(guests)
