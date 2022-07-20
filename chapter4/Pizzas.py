#exercise4-1

pizzas_list = ['pepperoni','napoletana', 'new york-style', 'quattro formaggi']

for pizza in pizzas_list:
    print(pizza)
print("\n")

#using for loop to print a sentence for each pizza

for pizza in pizzas_list:
    print(f"I like {pizza.title()} pizza")
print("\n")

print(f"I really like eating diffrent kind of pizzas, so I try many diffrent one and my number one fav is {pizzas_list[0]}.\nI really love pizza!")
