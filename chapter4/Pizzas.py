#exercise4-1

pizzas_list = ['pepperoni','napoletana', 'new york-style', 'quattro formaggi']

#exercise4-11
friend_pizzas = pizzas_list[:]
pizzas_list.append('Iraninan pizza')
friend_pizzas.append('margarita')
print('My favorite pizzas are:')
for pizza in pizzas_list:
    print(pizza)
print("\n My friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
#for pizza in pizzas_list:
#    print(pizza)
#print("\n")

#using for loop to print a sentence for each pizza

#for pizza in pizzas_list:
#    print(f"I like {pizza.title()} pizza")
#print("\n")

#print(f"I really like eating diffrent kind of pizzas, so I try many diffrent one and my number one fav is {pizzas_list[0]}.\nI really love pizza!")
