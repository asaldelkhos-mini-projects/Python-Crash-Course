filename = 'learning_python.txt'

with open(filename) as file_object:
    text = file_object.read()
print(text.rstrip())
