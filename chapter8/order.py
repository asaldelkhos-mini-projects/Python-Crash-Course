def sandwich_items(*items):
    for item in items:
        print(f"\n{item} added in your sandwich\n")

active = True
while active:
    item = input("choose your items:\n(when you are finished enter 'quit')")
    if item != 'quit':
        sandwich_items(item)
    else:
        active = False
        print("your sandwich is ready.")
