def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.")
    else:
        print(contents)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_file(filename)
