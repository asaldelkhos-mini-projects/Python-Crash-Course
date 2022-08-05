#exercise 7-4

prompt = "Hi dear customer, please choose your topping:"
prompt += "(when ever you finished enter 'quit')"
print(prompt)

while True:
    topping = input("topping:")

    if topping == 'quit':
        break
    else:
        print("we'll add that topping to your pizza.")    
