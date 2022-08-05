#exercise 7-4

prompt = "Hi dear customer, please choose your topping:"
prompt += "(when ever you finished enter 'quit')"
print(prompt)

active = True
while active:
    topping = input("topping:")

    if topping == 'quit':
        active = False
    else:
        print("we'll add that topping to your pizza.")
