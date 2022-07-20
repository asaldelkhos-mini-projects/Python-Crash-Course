#exercise4-1

pizzas_list = ['pepperoni','napoletana', 'new york-style', 'quattro formaggi']

for pizza in pizzas_list:
    print(pizza)
print("\n")

#using for loop to print a sentense for each pizza

for pizza in pizzas_list:
    print(f"I like {pizza.title()} pizza")
