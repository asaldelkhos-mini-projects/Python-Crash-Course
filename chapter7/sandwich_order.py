# exercixe 7-8

sandwich_orders = []
finished_orders = []

active = True
while active:
    order = input("Please enter your order:\n(When you are finish enter 'quit'.)")

    if order == 'quit':
        active = False
    else:
        sandwich_orders.append(order)
        finished_orders.append(order)

print("\nyour order is ready.")
