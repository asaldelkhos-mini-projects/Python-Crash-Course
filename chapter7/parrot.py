prompt = "\nYell me something, and I will repeat back to you"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
