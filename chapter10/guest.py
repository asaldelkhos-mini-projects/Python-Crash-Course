filename = 'guest.txt'

with open(filename, 'a') as file_object:
    guest_name = []
    active = True
    while active:
        name = input("What is your name? ")
        if name == 'Finish':
            active = False
        else:
            guest_name.append(name)
            print(guest_name)
            file_object.write(name)
            file_object.write("\n")
