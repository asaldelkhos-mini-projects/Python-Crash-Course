filename = 'guest.txt'

with open(filename, 'a') as file_object:
    guest_name = []
    active = True
    while active:
        name = input("What is your name? ")
        if name == Finish:
            active = False
        else:
            guest_name.append(name)
    file_object.write(guest_name)
