def sandwich_items(*item):
    items.append(item)
    print(f"{item} added in your sandwich")

items = []
item = ''
while item != 'quit':
    item = input("choose your items:\n(when you are finished enter 'quit')")
    if item != 'quit':
        sandwich_items(item)
    else:
        print("your sandwich is ready.")
        print(items)
