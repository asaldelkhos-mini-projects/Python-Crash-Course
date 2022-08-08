# testing sth for myself

def pet_info(name, type ='dog'):
    print(f"I have a {type}")
    print(f"my {type}'s name is {name}")

name_pet = input("What is your dog's name? ")
pet_info(type, name_pet)
