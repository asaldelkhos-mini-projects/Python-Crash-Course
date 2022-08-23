filename = 'learning_python.txt'

with open(filename) as file_object:
    text = file_object.readlines()

for line in text:
    print(line.rstrip())
