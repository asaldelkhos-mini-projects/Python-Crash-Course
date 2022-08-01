#exercise 7-2

message = "Hi, welcome to our restaurant."
message += "How many people are in your dinner?"

num = input(message)
num = int(num)

if num > 8:
    print("Sorry, you should wait.\n\tWe don't have a empty table right now.")
else:
    print("You'r table is ready.\n\tEnjoy your dinner.")
